"""
=========================================================
Professional Port Scanner V3
Author : Daksh Kumawat

Version : 3.0

Features Added in Part 1
------------------------
✔ Multi-threaded scanning
✔ Service detection
✔ Banner grabbing
✔ Domain/IP support
=========================================================
"""

import socket
import concurrent.futures
import time
import csv

# =====================================================
# Common Services Database
# =====================================================

SERVICES = {
    20: "FTP-DATA",
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    6379: "Redis",
    8080: "HTTP-ALT"
}

# Stores open ports
open_ports = []

# =====================================================
# Banner Grabbing
# =====================================================

def grab_banner(ip, port):
    """
    Attempts to grab the banner
    of an open service.
    """

    try:

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.settimeout(1)

        sock.connect((ip, port))

        banner = sock.recv(1024).decode(errors="ignore").strip()

        sock.close()

        if banner:
            return banner

    except:
        pass

    return "Unknown"

# =====================================================
# Scan Single Port
# =====================================================

def scan_port(ip, port):

    try:

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.settimeout(0.5)

        result = sock.connect_ex((ip, port))

        if result == 0:

            service = SERVICES.get(port, "Unknown")

            banner = grab_banner(ip, port)

            if len(banner) > 45:
                banner = banner[:45] + "..."

            open_ports.append(
                (port, service, banner)
            )

            print(
                f"{port:<8}"
                f"{'OPEN':<10}"
                f"{service:<15}"
                f"{banner}"
            )

        sock.close()

    except:
        pass

# =====================================================
# Scan Multiple Ports
# =====================================================

def scan_ports(ip, start_port, end_port):

    with concurrent.futures.ThreadPoolExecutor(
        max_workers=100
    ) as executor:

        executor.map(
            lambda port: scan_port(ip, port),
            range(start_port, end_port + 1)
        )
# =====================================================
# Save TXT Report
# =====================================================

def save_txt_report(target, ip, start_port, end_port, duration):

    with open("scan_report.txt", "w") as file:

        file.write("=" * 60 + "\n")
        file.write("           PROFESSIONAL PORT SCAN REPORT\n")
        file.write("=" * 60 + "\n\n")

        file.write(f"Target           : {target}\n")
        file.write(f"Resolved IP      : {ip}\n")
        file.write(f"Port Range       : {start_port}-{end_port}\n")
        file.write(f"Ports Scanned    : {end_port - start_port + 1}\n")
        file.write(f"Open Ports       : {len(open_ports)}\n")
        file.write(f"Scan Duration    : {duration:.2f} seconds\n\n")

        file.write("-" * 60 + "\n")
        file.write(f"{'PORT':<8}{'SERVICE':<15}BANNER\n")
        file.write("-" * 60 + "\n")

        for port, service, banner in open_ports:
            file.write(f"{port:<8}{service:<15}{banner}\n")


# =====================================================
# Save CSV Report
# =====================================================

def save_csv_report():

    with open("scan_report.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(["Port", "Service", "Banner"])

        for port, service, banner in open_ports:
            writer.writerow([port, service, banner])


# =====================================================
# Print Scan Summary
# =====================================================

def print_summary(target, ip, start_port, end_port, duration):

    print("\n")
    print("=" * 60)
    print("                 SCAN SUMMARY")
    print("=" * 60)

    print(f"Target           : {target}")
    print(f"Resolved IP      : {ip}")
    print(f"Port Range       : {start_port}-{end_port}")
    print(f"Ports Scanned    : {end_port - start_port + 1}")
    print(f"Open Ports       : {len(open_ports)}")
    print(f"Scan Duration    : {duration:.2f} seconds")

    print("=" * 60)

    print("\nReports Generated")
    print("✔ scan_report.txt")
    print("✔ scan_report.csv")


# =====================================================
# Print Table Header
# =====================================================

def print_table():

    print("\n")
    print("=" * 75)
    print(f"{'PORT':<8}{'STATUS':<10}{'SERVICE':<15}BANNER")
    print("=" * 75)
# =====================================================
# Main Program
# =====================================================

def main():

    print("=" * 60)
    print("        PROFESSIONAL PORT SCANNER V3")
    print("=" * 60)

    while True:

        print("\nMENU")
        print("1. Scan Target")
        print("2. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            open_ports.clear()

            target = input("\nEnter IP Address or Domain: ").strip()

            try:
                ip = socket.gethostbyname(target)

            except socket.gaierror:
                print("\n❌ Invalid IP address or domain.")
                continue

            try:

                start_port = int(input("Start Port : "))
                end_port = int(input("End Port   : "))

            except ValueError:

                print("\n❌ Please enter valid port numbers.")
                continue

            if start_port < 1 or end_port > 65535:

                print("\n❌ Ports must be between 1 and 65535.")
                continue

            if start_port > end_port:

                print("\n❌ Start Port cannot be greater than End Port.")
                continue

            print(f"\nResolved IP : {ip}")

            print("\nScanning...")

            print_table()

            start_time = time.time()

            scan_ports(ip, start_port, end_port)

            end_time = time.time()

            duration = end_time - start_time

            print_summary(
                target,
                ip,
                start_port,
                end_port,
                duration
            )

            save_txt_report(
                target,
                ip,
                start_port,
                end_port,
                duration
            )

            save_csv_report()

        elif choice == "2":

            print("\nThank you for using Professional Port Scanner!")

            break

        else:

            print("\n❌ Invalid Choice.")


# =====================================================
# Program Starts Here
# =====================================================

if __name__ == "__main__":
    main()
