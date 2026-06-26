import socket
import concurrent.futures
import time

open_ports = []


def grab_banner(ip, port):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((ip, port))
        banner = s.recv(1024).decode(errors="ignore").strip()
        s.close()

        if banner:
            return banner

    except:
        pass

    return "Unknown"


def scan_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

        result = s.connect_ex((ip, port))

        if result == 0:
            banner = grab_banner(ip, port)

            print(f"[OPEN] Port {port:<5} | {banner}")

            open_ports.append((port, banner))

        s.close()

    except:
        pass


def save_report(target, ip):
    with open("scan_report.txt", "w") as file:

        file.write("=" * 45 + "\n")
        file.write("PORT SCAN REPORT\n")
        file.write("=" * 45 + "\n\n")

        file.write(f"Target : {target}\n")
        file.write(f"IP     : {ip}\n\n")

        if open_ports:

            file.write("Open Ports\n")
            file.write("-" * 30 + "\n")

            for port, banner in open_ports:
                file.write(f"{port:<6} {banner}\n")

        else:
            file.write("No open ports found.\n")


def main():

    print("=" * 45)
    print("      PROFESSIONAL PORT SCANNER")
    print("=" * 45)

    target = input("\nEnter IP or Domain: ")

    try:
        ip = socket.gethostbyname(target)

    except socket.gaierror:
        print("\nInvalid Host.")
        return

    print(f"\nResolved IP : {ip}")

    start_port = int(input("Start Port : "))
    end_port = int(input("End Port   : "))

    print("\nScanning...\n")

    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:

        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, ip, port)

    end_time = time.time()

    print("\n" + "=" * 45)

    print("SCAN COMPLETED")

    print(f"Open Ports : {len(open_ports)}")

    print(f"Time Taken : {end_time - start_time:.2f} seconds")

    save_report(target, ip)

    print("\nReport saved as scan_report.txt")


if __name__ == "__main__":
    main()
