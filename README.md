# 🌐 Professional Port Scanner V3

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Version-3.0-orange)

A professional multi-threaded TCP Port Scanner built using Python. This project performs fast port scanning, detects common network services, grabs service banners, and generates professional scan reports in TXT and CSV formats.

---

## ✨ Features

- ⚡ Multi-threaded TCP Port Scanning
- 🌍 Scan IP Addresses and Domain Names
- 🔍 Automatic DNS Resolution
- 📡 Service Detection (HTTP, SSH, FTP, HTTPS, MySQL, etc.)
- 🏷 Banner Grabbing
- 📄 Professional TXT Report Generation
- 📊 CSV Report Export
- 📈 Scan Statistics
- 🧾 Clean Command-Line Interface
- 🛡 Input Validation & Error Handling
- 💻 Cross-Platform Support

---

## 📂 Project Structure

```
Port-Scanner/
│── port_scanner.py
│── README.md
│── scan_report.txt
│── scan_report.csv
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Port-Scanner.git
```

Go into the project folder

```bash
cd Port-Scanner
```

Run the scanner

```bash
python port_scanner.py
```

---

## 🖥 Example

```
============================================================
        PROFESSIONAL PORT SCANNER V3
============================================================

MENU
1. Scan Target
2. Exit

Enter your choice: 1

Enter IP Address or Domain:
scanme.nmap.org

Resolved IP : 45.33.32.156

Scanning...

PORT     STATUS     SERVICE         BANNER

22       OPEN       SSH             OpenSSH
80       OPEN       HTTP            Unknown

============================================================
SCAN SUMMARY
============================================================

Target           : scanme.nmap.org
Resolved IP      : 45.33.32.156
Ports Scanned    : 81
Open Ports       : 2
Scan Duration    : 1.84 seconds
```

---

## 📄 Generated Reports

### TXT Report

- Professional scan summary
- Open ports
- Detected services
- Banner information
- Scan duration

### CSV Report

Export results directly into Excel or Google Sheets.

| Port | Service | Banner |
|------|---------|---------|
|22|SSH|OpenSSH|
|80|HTTP|Unknown|

---

## 🛠 Technologies Used

- Python 3
- Socket Programming
- Concurrent Futures (Multi-threading)
- CSV Module
- Time Module

---

## 📚 Concepts Practiced

- Socket Programming
- TCP Networking
- DNS Resolution
- Multi-threading
- Banner Grabbing
- Service Detection
- File Handling
- CSV Export
- Exception Handling
- Input Validation

---

## 🎯 Future Improvements

- GUI Version (Tkinter)
- PDF Report Export
- Scan History
- Custom Thread Configuration
- Nmap-style Output
- Automatic Service Detection using `socket.getservbyport()`
- Colorized Terminal Output
- Progress Indicator

---

## ⚠ Disclaimer

This project is developed for educational purposes and authorized security testing only. Do not scan systems without proper permission.

---

## 👨‍💻 Author

**Daksh Kumawat**

If you found this project useful, consider giving it a ⭐ on GitHub!
