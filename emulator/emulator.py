import random
import time
import requests

BACKEND_URL = "http://backend:5000/api/telemetry"
REQUEST_TIMEOUT_SECONDS = 2
RETRY_DELAY_SECONDS = 1

def main():
    while True:
        value = random.randint(1, 500)
        data = {
            "value": value
        }
        try:
            response = requests.post(
                BACKEND_URL,
                json=data,
                timeout=REQUEST_TIMEOUT_SECONDS,
            )
            response.raise_for_status()
        except requests.RequestException as error:
            print(f"Telemetry send failed: {error}")
            time.sleep(RETRY_DELAY_SECONDS)
            continue
        time.sleep(1)

if __name__ == "__main__":
    main()
