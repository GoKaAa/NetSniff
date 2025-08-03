import socket
import threading
import ipaddress
import argparse
import re
from queue import Queue
from rich.console import Console
from rich.table import Table

console = Console()
print_lock = threading.Lock()
queue = Queue()

def parse_ip_range(ip_input):
    try:
        if '-' in ip_input:
            start_ip, end_ip = ip_input.split('-')
            return [str(ip) for ip in ip_range(start_ip.strip(), end_ip.strip())]
        elif '/' in ip_input:
            return [str(ip) for ip in ipaddress.ip_network(ip_input, strict=False)]
        else:
            # If it's a domain, resolve it
            try:
                ip = socket.gethostbyname(ip_input)
                return [ip]
            except socket.gaierror:
                console.print(f"[red]Invalid domain or IP: {ip_input}[/red]")
                return []
    except Exception as e:
        console.print(f"[red]Error parsing IP range: {e}[/red]")
        return []

def ip_range(start_ip, end_ip):
    start = int(ipaddress.IPv4Address(start_ip))
    end = int(ipaddress.IPv4Address(end_ip))
    return (ipaddress.IPv4Address(ip) for ip in range(start, end + 1))

def banner_grab(ip, port, timeout):
    try:
        s = socket.socket()
        s.settimeout(timeout)
        s.connect((ip, port))
        banner = s.recv(1024).decode(errors="ignore").strip()
        s.close()
        return banner if banner else "No banner"
    except:
        return "No banner"

def scan_port(ip, port, timeout):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            s.connect((ip, port))
            with print_lock:
                banner = banner_grab(ip, port, timeout)
                console.print(f"[green]Open[/green] → [bold cyan]{ip}:{port}[/bold cyan] [dim]| {banner}[/dim]")
    except:
        pass

def threader(ip, timeout):
    while True:
        port = queue.get()
        scan_port(ip, port, timeout)
        queue.task_done()

def scan_ip(ip, ports, timeout, threads):
    console.print(f"\n[bold yellow]Scanning {ip}[/bold yellow] on ports {min(ports)} to {max(ports)} with {threads} threads.")
    for _ in range(threads):
        t = threading.Thread(target=threader, args=(ip, timeout))
        t.daemon = True
        t.start()
    for port in ports:
        queue.put(port)
    queue.join()

def main():
    parser = argparse.ArgumentParser(description="NetSniff - Advanced IP & Port Scanner")
    parser.add_argument("-i", "--ip", required=True, help="Target IP / domain / CIDR / IP range")
    parser.add_argument("-p", "--ports", default="1-1024", help="Ports to scan, e.g. 22,80,443 or 1-65535")
    parser.add_argument("-t", "--threads", type=int, default=100, help="Number of threads")
    parser.add_argument("--timeout", type=float, default=1.0, help="Timeout per port in seconds")

    args = parser.parse_args()

    ips = parse_ip_range(args.ip)

    port_input = args.ports.replace(" ", "")
    ports = set()
    for part in port_input.split(','):
        if '-' in part:
            start, end = part.split('-')
            ports.update(range(int(start), int(end)+1))
        else:
            ports.add(int(part))

    if not ips:
        return

    try:
        for ip in ips:
            scan_ip(ip, sorted(ports), args.timeout, args.threads)
    except KeyboardInterrupt:
        console.print("\n[red]Scan interrupted by user.[/red]")

if __name__ == "__main__":
    main()
