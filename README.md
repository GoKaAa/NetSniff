# 🕵️ NetSniff

**NetSniff** is an advanced, multithreaded IP and port scanner built with Python.  
It supports scanning **individual IPs, domains, full port ranges, IP ranges, and CIDR blocks**, with **banner grabbing** and customizable settings.

> ⚡️ Blazing fast. ✨ Powerful features. 💻 Made for professionals.

---

![NetSniff Banner](https://img.shields.io/badge/Made%20with-Python-blue?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-orange?style=for-the-badge)

---

## 🚀 Features

- ✅ Scan any IP, domain, IP range, or CIDR block
- ✅ Customizable port ranges (`1-65535`)
- ✅ Multithreaded scanning for maximum performance
- ✅ Banner grabbing to detect services
- ✅ Optional timeout setting
- ✅ Smart DNS resolution
- ✅ Beautiful console output using `rich`
- ✅ Graceful interruption handling

---

## 📦 Installation

```bash
git clone https://github.com/mvaipp/NetSniff.git
cd NetSniff
pip install rich
```

---

## 🧠 Usage

```bash
python netsniff.py -i <target> [options]
```

### 🔧 Examples

| Target Type     | Command Example |
|------------------|------------------|
| Domain           | `python netsniff.py -i example.com` |
| Single IP        | `python netsniff.py -i 192.168.1.1` |
| CIDR block       | `python netsniff.py -i 192.168.1.0/24` |
| IP Range         | `python netsniff.py -i 192.168.1.10-192.168.1.20` |
| Custom Ports     | `-p 21,22,80,443,8080` |
| Full Port Range  | `-p 1-65535` |
| Set Timeout      | `--timeout 2.5` |
| Custom Threads   | `-t 200` |

### 🧪 Sample Run

```bash
python netsniff.py -i 192.168.1.1 -p 1-100 -t 100 --timeout 1.5
```

---

## 🛠 Arguments

| Flag | Description |
|------|-------------|
| `-i`, `--ip` | Target IP/domain/IP range/CIDR (**required**) |
| `-p`, `--ports` | Port(s) to scan (e.g., `22,80` or `1-65535`) |
| `-t`, `--threads` | Number of threads (default: 100) |
| `--timeout` | Timeout per port in seconds (default: 1.0) |

---

## 💡 Output Example

```bash
Scanning 192.168.1.1 on ports 20 to 25 with 100 threads.
[green]Open[/green] → [bold cyan]192.168.1.1:22[/bold cyan] | [dim]SSH-2.0-OpenSSH_7.6[/dim]
[green]Open[/green] → [bold cyan]192.168.1.1:80[/bold cyan] | [dim]Apache httpd[/dim]
```

---

## 📁 File Structure

```
NetSniff/
├── netsniff.py       # Main scanner script
└── README.md         # This file
```

---

## ✅ To-Do (Coming Soon)

- [ ] Export results to JSON / CSV
- [ ] OS fingerprinting using TTL values
- [ ] Web UI using Flask
- [ ] Auto IP detection
- [ ] Nmap integration

---

## 📄 License

**MIT License** — Use freely for personal and commercial use.

---

## 🤝 Contributions

Contributions, feature suggestions, and pull requests are welcome!  
Feel free to [open an issue](https://github.com/mvaipp/NetSniff/issues) or fork and enhance it.

---

## 📬 Contact

Made with ❤️ by [Ankush Sheoran](https://github.com/mvaipp)  

---
