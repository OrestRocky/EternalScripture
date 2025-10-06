# test_ipfs_connection.py
import requests

IPFS_GATEWAY = "https://ipfs.io/ipfs/"

def check_ipfs_connection(cid="bafybeigdyrztp5b2n6g7q7w7sdp6d73f5s7tovodt5ddsqmgxemvyy6lpa"):
    """Simple check to see if IPFS gateway is reachable and content exists."""
    url = f"{IPFS_GATEWAY}{cid}"
    try:
        response = requests.head(url, timeout=5)
        if response.status_code == 200:
            print(f"✅ IPFS reachable: {url}")
        else:
            print(f"⚠️ Gateway responded with {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Connection error: {e}")

if __name__ == "__main__":
    check_ipfs_connection()
Add IPFS test script for connectivity check
