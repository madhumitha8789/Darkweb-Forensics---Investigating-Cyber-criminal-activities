import socket
import socks
import time
import sys

def test_tor_with_pysocks():
    print("PySocks Direct Test: Configuring SOCKS5 proxy at 127.0.0.1:9050...")
    
    # Save original socket for cleanup
    original_socket = socket.socket
    
    try:
        # Configure PySocks to use Tor
        socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
        socket.socket = socks.socksocket
        
        print("PySocks Direct Test: Attempting to connect to httpbin.org:80...")
        
        # Try a simple HTTP connection
        start_time = time.time()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(20)  # 20 second timeout
        
        try:
            s.connect(("httpbin.org", 80))
            connected = True
            print(f"PySocks Direct Test: SUCCESS! Connected to httpbin.org in {time.time() - start_time:.2f} seconds")
            
            # Send a simple HTTP request to get IP
            http_request = b"GET /ip HTTP/1.1\r\nHost: httpbin.org\r\nConnection: close\r\n\r\n"
            s.sendall(http_request)
            
            # Receive the response
            response = b""
            while True:
                data = s.recv(4096)
                if not data:
                    break
                response += data
            
            # Try to extract the IP from the response
            response_str = response.decode('utf-8', errors='ignore')
            print("\nResponse from httpbin.org/ip:")
            print("===========================")
            print(response_str)
            
        except socket.timeout:
            print(f"PySocks Direct Test: FAILED with timeout after {time.time() - start_time:.2f} seconds")
        except socket.error as e:
            print(f"PySocks Direct Test: FAILED with socket error: {e}")
        finally:
            s.close()
            
    except Exception as e:
        print(f"PySocks Direct Test: General error: {e}")
    finally:
        # Always restore the original socket
        socket.socket = original_socket
        print("PySocks Direct Test: Socket restored to original state")


# Also try with alternate port 9150 if the first test fails
def test_alternate_port():
    print("\n\nTrying alternate Tor Browser port (9150)...")
    
    # Save original socket for cleanup
    original_socket = socket.socket
    
    try:
        # Configure PySocks to use Tor on alternate port
        socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9150)
        socket.socket = socks.socksocket
        
        print("PySocks Direct Test: Attempting to connect to httpbin.org:80 via port 9150...")
        
        # Try a simple HTTP connection
        start_time = time.time()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(20)  # 20 second timeout
        
        try:
            s.connect(("httpbin.org", 80))
            print(f"PySocks Direct Test: SUCCESS with port 9150! Connected in {time.time() - start_time:.2f} seconds")
            
            # Send a simple HTTP request to get IP
            http_request = b"GET /ip HTTP/1.1\r\nHost: httpbin.org\r\nConnection: close\r\n\r\n"
            s.sendall(http_request)
            
            # Receive the response
            response = b""
            while True:
                data = s.recv(4096)
                if not data:
                    break
                response += data
            
            # Try to extract the IP from the response
            response_str = response.decode('utf-8', errors='ignore')
            print("\nResponse from httpbin.org/ip via port 9150:")
            print("===========================")
            print(response_str)
            
        except socket.timeout:
            print(f"PySocks Direct Test (port 9150): FAILED with timeout after {time.time() - start_time:.2f} seconds")
        except socket.error as e:
            print(f"PySocks Direct Test (port 9150): FAILED with socket error: {e}")
        finally:
            s.close()
            
    except Exception as e:
        print(f"PySocks Direct Test (port 9150): General error: {e}")
    finally:
        # Always restore the original socket
        socket.socket = original_socket
        print("PySocks Direct Test: Socket restored to original state")


if __name__ == "__main__":
    print("Make sure Tor Browser is running before this test.")
    print("Testing connection to httpbin.org through Tor using PySocks directly.\n")
    
    # Run the standard port test
    test_tor_with_pysocks()
    
    # Run the alternate port test
    test_alternate_port() 