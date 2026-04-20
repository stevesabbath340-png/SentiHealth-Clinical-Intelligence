import datetime

def log_event(event_type, description):
    # Generates a high-precision timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] | {event_type.upper()} | {description}\n"
    
    # Appends to the file so previous logs are never overwritten
    with open("audit_log.txt", "a") as log_file:
        log_file.write(log_entry)

def view_logs():
    print("\n--- SYSTEM AUDIT TRAIL ---")
    try:
        with open("audit_log.txt", "r") as log_file:
            lines = log_file.readlines()
            for line in lines[-15:]:
                print(line.strip())
    except FileNotFoundError:
        print("[-] No audit logs found. System initialize pending.")
    print("--------------------------")