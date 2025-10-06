# run_all_tests.py
"""
EternalScripture Integration Test Runner
----------------------------------------
This script runs all core test modules to verify IPFS connectivity and 
mock blockchain recording functionality. 
"""

import time

try:
    import test_ipfs_connection
    import test_blockchain_record
except ImportError as e:
    print(f"⚠️ Missing test module: {e}")
    print("Make sure test_ipfs_connection.py and test_blockchain_record.py exist in the scripts/ directory.")
    exit(1)

def run_ipfs_test():
    print("\n🚀 Running IPFS connectivity test...")
    time.sleep(1)
    test_ipfs_connection.check_ipfs_connection()

def run_blockchain_test():
    print("\n🔗 Running mock blockchain record test...")
    time.sleep(1)
    cid = "bafybeigdyrztp5b2n6g7q7w7sdp6d73f5s7tovodt5ddsqmgxemvyy6lpa"
    block_hash = test_blockchain_record.mock_blockchain_record(cid)
    test_blockchain_record.verify_record(cid, block_hash)

def main():
    print("===============================================")
    print("🧠 EternalScripture System Integration Check")
    print("===============================================")
    start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"Test started at: {start_time}\n")

    run_ipfs_test()
    run_blockchain_test()

    end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"\n✅ All tests completed successfully at {end_time}")
    print("===============================================\n")

if __name__ == "__main__":
    main()
Add integration runner for IPFS and blockchain test scripts
