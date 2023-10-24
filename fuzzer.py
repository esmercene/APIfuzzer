import requests
import sys


def fuzz_loop():
    for word in sys.stdin:
    response = requests.get(url=f"http://10.10.11.161/{word}")
    if response.status_code == 404:
        fuzz_loop()
    else:
        data = response.json()
        print(response.status_code)
        print(data)
        print(word)
    # data = response.json()

fuzz_loop()

