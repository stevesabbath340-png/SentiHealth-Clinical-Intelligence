import sqlite3
import pandas as pd
from logger import log_event

def run_health_analytics():
    # Audit hook
    log_event("Analytics", "User accessed Population Health SQL Dashboard.")
    
    print("\n--- SQL-DRIVEN POPULATION ANALYTICS ---")
    
    try:
        # 1. Connect and pull data
        conn = sqlite3.connect('sentihealth.db')
        df = pd.read_sql_query("SELECT * FROM patients", conn)
        conn.close()

        if df.empty:
            print("[-] No data found in SQL database.")
            return

        print(f"\nTotal Patients Records: {len(df)}")
        
        # 2. Executive Breakdown by Condition
        print("\n[+] Cases by Condition:")
        counts = df['Condition'].value_counts()
        for condition, total in counts.items():
            print(f"    - {condition:15} | {total} cases")

        print("-" * 40)

        # 3. Executive Recovery Stats by Region
        print("[+] Avg Recovery Days by Region:")
        avg_recovery = df.groupby('Region')['Recovery_Days'].mean()
        for region, days in avg_recovery.items():
            print(f"    - Region: {region:10} | Avg Recovery: {days:.1f} days")

    except Exception as e:
        # THIS WAS THE MISSING PART!
        print(f"[-] Analytics Error: {e}")
        log_event("Error", f"Analytics failed: {str(e)}")