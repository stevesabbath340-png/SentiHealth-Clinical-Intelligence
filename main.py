import os
import sys
from scrubber import process_health_data, run_network_scrub
from database_manager import initialize_database
from analytics import run_health_analytics
from predictor import run_ai_prediction
from visualizer import generate_dashboard
from logger import log_event, view_logs

def run_cpp_scrubber():
    log_event("Security", "C++ Engine triggered.")
    print("Launching C++ Security Engine...")
    # Use the .exe extension and Windows-style pathing
    os.system("security_server.exe")

def main():
    initialize_database()

def main():
    print("========================================")
    print("1. Run Privacy Scrubber (C++ Engine)")
    print("2. Run Population Analytics (SQL & Pandas)")
    print("3. Run AI Recovery Predictor (Machine Learning)")
    print("4. View BI Dashboard (Data Visualization)")
    print("5. Run Full System Pipeline")
    print("6. View Audit Logs")
    print("7. Exit")
    

    choice = input("\nSelect an option (1-7): ")

    raw_data = 'patients.csv'
    clean_data = 'processed_health_data.csv'

    if choice == '1':
            # Option 1: Calls the socket client in scrubber.py
            run_network_scrub()

    elif choice == '2':
            # Option 2: No arguments needed - it pulls directly from SQL
            run_health_analytics()

    elif choice == '3':
            # Option 3: Logic handled in predictor.py
            run_ai_prediction()

    elif choice == '4':
            # Option 4: Generates the Matplotlib charts
            generate_dashboard()

    elif choice == '5':
            # Option 5: The "Bursary Flex" - runs everything in sequence
            print("\n--- EXECUTING FULL SYSTEM PIPELINE ---")
            run_network_scrub()
            run_health_analytics()
            generate_dashboard()
            run_ai_prediction()
            log_event("SYSTEM", "Full end-to-end pipeline executed successfully.")

    elif choice == '6':
            # Option 6: Reads the audit_log.txt file
            view_logs()

    elif choice == '7':
            print("[+] Shutting down SentiHealth. Stay secure.")
            log_event("SYSTEM", "User exited application.")
            sys.exit()

    else:
            print("[!] Invalid selection. Please try again.")

if __name__ == "__main__":
    main()