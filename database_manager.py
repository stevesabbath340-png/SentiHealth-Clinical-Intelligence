import sqlite3
import pandas as pd

def initialize_database():
    # Connect to (or create) the database file
    conn = sqlite3.connect('sentihealth.db')
    cursor = conn.cursor()

    print("[+] Initializing SQL Database...")

    # 1. Create the Table using SQL syntax
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            PatientID TEXT,
            Full_Name TEXT,
            Age INTEGER,
            Gender TEXT,
            Region TEXT,
            Condition TEXT,
            Recovery_Days INTEGER
        )
    ''')
    
    # 2. Migration: Load CSV data into SQL (if the table is empty)
    cursor.execute("SELECT count(*) FROM patients")
    if cursor.fetchone()[0] == 0:
        df = pd.read_csv('patients.csv')
        df.to_sql('patients', conn, if_exists='append', index=False)
        print("[+] Migration Complete: CSV data moved to Relational SQL Table.")
    
    conn.commit()
    conn.close()

def query_secure_data():
    """Example of a professional SQL query"""
    conn = sqlite3.connect('sentihealth.db')
    # We only pull the data the analyst is allowed to see
    query = "SELECT Condition, Region, Recovery_Days FROM patients"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df