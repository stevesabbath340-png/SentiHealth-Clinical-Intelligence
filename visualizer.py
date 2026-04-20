import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

# Suppress minor styling warnings
warnings.filterwarnings('ignore')

def generate_dashboard():
    print("\n--- GENERATING BI DASHBOARD ---")
    print("[+] Connecting to SQL Database...")
    
    try:
        # 1. Pull data directly from your SQL Database
        conn = sqlite3.connect('sentihealth.db')
        query = "SELECT Region, Condition, Recovery_Days FROM patients"
        df = pd.read_sql_query(query, conn)
        conn.close()
        
        if df.empty:
            print("[-] Error: Database is empty. Please run the scrubber/migration first.")
            return

        print("[+] Rendering Visualizations...")

        # 2. Set up a professional "Dashboard" layout (1 row, 2 columns)
        sns.set_theme(style="whitegrid")
        fig, axes = plt.subplots(1, 2, figsize=(12, 5))
        fig.suptitle('SentiHealth Clinical Analytics Dashboard', fontsize=16, fontweight='bold')

        # Chart 1: Average Recovery Days per Condition (Bar Chart)
        sns.barplot(
            data=df, 
            x='Condition', 
            y='Recovery_Days', 
            ax=axes[0], 
            palette='Blues_d',
            errorbar=None
        )
        axes[0].set_title('Average Recovery Time by Condition')
        axes[0].set_ylabel('Days')
        axes[0].set_xlabel('Medical Condition')

        # Chart 2: Case Distribution by Region (Pie Chart)
        region_counts = df['Region'].value_counts()
        axes[1].pie(
            region_counts, 
            labels=region_counts.index, 
            autopct='%1.1f%%', 
            colors=sns.color_palette('pastel')
        )
        axes[1].set_title('Patient Distribution by Region')

        # 3. Display the Dashboard
        plt.tight_layout()
        print("[+] Dashboard rendered successfully. Close the window to continue.")
        plt.show()

    except sqlite3.OperationalError:
        print("[-] Error: Database not found. Run Option 1 or 4 to initialize the DB.")