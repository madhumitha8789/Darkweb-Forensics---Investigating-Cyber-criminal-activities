import requests

def check_ip_via_tor():
    proxies = {
        'http': 'socks5h://127.0.0.1:9150',
        'https': 'socks5h://127.0.0.1:9150'
    }
    try:
        print("Minimal test: Attempting to connect to http://httpbin.org/ip via Tor SOCKS proxy (port 9150)...")
        response = requests.get('http://httpbin.org/ip', proxies=proxies, timeout=30) # 30 sec timeout
        response.raise_for_status()
        ip_data = response.json()
        print(f"Minimal test: Success! Apparent IP: {ip_data.get('origin')}")
    except requests.exceptions.Timeout as e_timeout:
        print(f"Minimal test: FAILED with Timeout! {e_timeout}")
    except requests.exceptions.RequestException as e_req:
        print(f"Minimal test: FAILED with RequestException! {e_req}")
    except Exception as e_gen:
        print(f"Minimal test: FAILED with a general exception! {e_gen}")

if __name__ == "__main__":
    print("Ensure Tor Browser is running and connected before running this test.")
    check_ip_via_tor() 