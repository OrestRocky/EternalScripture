# test_blockchain_record.py
import hashlib
import time

def mock_blockchain_record(cid):
    """Simulates recording a CID into a blockchain-like structure."""
    timestamp = int(time.time())
    record = f"{cid}-{timestamp}"
    mock_hash = hashlib.sha256(record.encode()).hexdigest()
    print(f"🧱 Recorded mock block:\nCID: {cid}\nTimestamp: {timestamp}\nHash: {mock_hash}")
    return mock_hash

def verify_record(cid, expected_hash):
    """Verifies that the same CID produces the same hash."""
    timestamp = int(time.time())  # just for simulation
    test_hash = hashlib.sha256(f"{cid}-{timestamp}".encode()).hexdigest()
    print(f"Verifying record for CID {cid}")
    if test_hash == expected_hash:
        print("✅ Record verified successfully.")
    else:
        print("⚠️ Hash mismatch (expected simulation only).")

if __name__ == "__main__":
    cid = "bafybeigdyrztp5b2n6g7q7w7sdp6d73f5s7tovodt5ddsqmgxemvyy6lpa"
    block_hash = mock_blockchain_record(cid)
    verify_record(cid, block_hash)
