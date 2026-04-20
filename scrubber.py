import hashlib
import pandas as pd
import socket
import socket
from logger import log_event

def secure_remote_hash(data_string):
    """Internal helper to talk to the C++ server."""
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('127.0.0.1', 5555))
        client.send(data_string.encode())
        response = client.recv(1024).decode()
        client.close()
        return response
    except ConnectionRefusedError:
        return None

def run_network_scrub():
    """This is the function main.py is looking for!"""
    print("\n[+] Contacting C++ Security Vault...")
    
    # We'll simulate scrubbing a batch of names
    test_names = ["Patient_A", "Patient_B"]
    for name in test_names:
        result = secure_remote_hash(name)
        if result:
            print(f"    [OK] Protected ID for {name}: {result}")
            log_event("Security", f"Data scrubbed for {name} via C++ Server.")
        else:
            print(f"    [!] Error: C++ Server is offline.")
            log_event("Error", "C++ Security Server connection failed.")
            break

def anonymize_name(name):
    return hashlib.sha256(name.encode()).hexdigest()

def process_health_data(input_file, output_file):
    df = pd.read_csv(input_file)
    print("--- SECURE PROCESSING STARTED ---")
    df['Full_Name'] = df['Full_Name'].apply(anonymize_name)
    df = df.drop(columns=['PatientID'])
    df.to_csv(output_file, index=False)
    print(f"SUCCESS: Data scrubbed and PatientID removed.")
    print(f"FILE SAVED AS: {output_file}")
    return output_file

# Run the engine
#process_health_data('patients.csv')