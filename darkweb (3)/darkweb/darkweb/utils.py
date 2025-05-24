import requests

def get_tor_session():
    session = requests.session()
    session.proxies = {
        'http': 'socks5h://127.0.0.1:9150',
        'https': 'socks5h://127.0.0.1:9150'
    }
    return session

def get_apparent_ip_through_tor():
    """Attempts to get the current external IP address through the Tor session."""
    session = get_tor_session()
    try:
        # Using httpbin which is an HTTP service; HTTPS can be more complex with proxies
        response = session.get('http://httpbin.org/ip', timeout=20) # 20s timeout for IP check
        response.raise_for_status() # Raise an exception for bad status codes
        ip_data = response.json()
        return ip_data.get('origin')
    except requests.exceptions.RequestException as e:
        print(f"Error checking IP via Tor: {e}")
        return f"Error fetching IP: {e}"
    except Exception as e_gen:
        print(f"Generic error checking IP via Tor: {e_gen}")
        return f"Generic error fetching IP: {e_gen}" 