# 🌐 Professional Port Scanner

A professional multi-threaded TCP Port Scanner built with Python for network reconnaissance and cybersecurity learning. This tool scans a target host, identifies open ports, performs basic banner grabbing, and generates a scan report.

---

## 🚀 Features

* 🔍 Scan IP addresses or domain names
* ⚡ Multi-threaded scanning for faster performance
* 🌐 Automatic DNS resolution
* 📡 Banner grabbing for open services
* 🎯 Custom port range selection
* 📝 Automatic scan report generation
* ⏱ Scan execution time measurement
* 🛡 Robust exception handling
* 💻 Interactive command-line interface

---

## 🛠 Technologies Used

* Python 3
* Socket Programming
* Concurrent Futures (ThreadPoolExecutor)
* DNS Resolution
* File Handling
* TCP Networking

---

## 📂 Project Structure

```text
port-scanner/
│
├── port_scanner.py
├── scan_report.txt
├── README.md
└── .gitignore
```

---

## ⚙ Installation

Clone the repository:

```bash
git clone https://github.com/dakshkumawat07/Port-Scanner.git
```

Navigate to the project folder:

```bash
cd Port-Scanner
```

Run the program:

```bash
python3 port_scanner.py
```

---

## 📋 Usage

1. Enter a target IP address or domain.
2. Specify the starting port.
3. Specify the ending port.
4. The scanner identifies open ports.
5. Results are displayed on the terminal.
6. A report is automatically saved as `scan_report.txt`.

---

## 📊 Example Output

```text
=========================================
      PROFESSIONAL PORT SCANNER
=========================================

Target : scanme.nmap.org

Resolved IP : 45.xxx.xxx.xxx

Scanning...

[OPEN] Port 22  | SSH
[OPEN] Port 80  | HTTP

=========================================

SCAN COMPLETED

Open Ports : 2

Time Taken : 1.24 seconds

Report saved as scan_report.txt
```

---

## 🎯 Learning Outcomes

Through this project, I learned:

* TCP/IP networking fundamentals
* Socket programming in Python
* DNS resolution
* Multi-threading using ThreadPoolExecutor
* Banner grabbing
* Network reconnaissance techniques
* File handling
* Exception handling

---

## 🔮 Future Improvements

* Service detection
* CIDR subnet scanning
* CSV report export
* GUI using Tkinter
* Scan history
* Progress bar
* Operating system fingerprinting
* IPv6 support

---

## ⚠ Disclaimer

This project is intended for educational purposes only.

Use this scanner only on systems and networks that you own or have explicit permission to test. Unauthorized scanning may violate laws or network policies.

---

## 👨‍💻 Author

**Daksh Kumawat**

GitHub: https://github.com/dakshkumawat07

