🏥 SentiHealth: Clinical Intelligence & Security Platform

SentiHealth is a multi-tier, distributed informatics system designed for secure patient data management, predictive analytics, and regulatory compliance. The platform demonstrates the integration of low-level systems programming (C++) with high-level data science and machine learning (Python).

## 📸 Screenshots

### Full Pipeline Scan
![Full Pipeline Scan](images/Full%20Pipeline%20Scan.png)
*Complete end-to-end view of the secure data ingestion, anonymization, processing, and predictive analytics pipeline.*

### BI Dashboard (Chart)
![BI Dashboard (Chart)](images/BI%20Dashboard(Chart).png)
*Interactive Business Intelligence dashboard showing real-time patient population trends, recovery predictions, and regional analytics.*

🏗️ System Architecture

Unlike standard monolithic applications, SentiHealth utilizes a Distributed Client-Server Model:

* **Security Vault (C++ Backend)**: A hardened server built using Winsock (TCP/IP). It handles cryptographic data anonymization to ensure PII (Personally Identifiable Information) is never stored in its raw form.
* **Intelligence Engine (Python Frontend)**: The primary orchestration layer that manages the user interface, relational database operations, and predictive modeling.
* **Relational Storage (SQLite)**: An industry-standard SQL backend ensuring data integrity and relational mapping between patient demographics and clinical outcomes.

🚀 Key Features

1. **Distributed Security Engine (C++/Winsock)**
   * Implements raw socket programming to communicate between processes via Port 5555.
   * Performs high-speed data scrubbing and hashing in a memory-safe environment.

2. **AI Recovery Predictor (Machine Learning)**
   * Utilizes a Decision Tree Regressor to analyze patient age, condition, and region.
   * Predicts expected recovery durations to assist in hospital resource allocation.

3. **SQL-Driven Population Analytics**
   * Executes complex queries via Pandas and SQLAlchemy to generate real-time health reports.
   * Tracks disease prevalence and regional recovery benchmarks.

4. **Business Intelligence (BI) Dashboard**
   * Generates interactive visualizations using Matplotlib and Seaborn.
   * Provides clinical staff with "at-a-glance" insights into patient population trends.

5. **Forensic Audit Logging (Compliance)**
   * Implements an immutable audit trail (`audit_log.txt`) that records every system transaction.
   * Ensures adherence to international data standards such as POPIA and GDPR.

🛠️ Technical Stack

| Component       | Technology                                      |
|-----------------|-------------------------------------------------|
| Languages       | Python 3.11+, C++ (MinGW/GCC)                   |
| Networking      | Winsock2 (Windows Sockets), TCP/IP              |
| Data Science    | Pandas, NumPy                                   |
| Machine Learning| Scikit-Learn (Linear/Tree Regression)           |
| Database        | SQLite3                                         |
| Visualization   | Matplotlib, Seaborn                             |

📦 Installation & Execution

**Prerequisites**
* Python 3.x
* G++ Compiler (MinGW-w64)
* Required Libraries: `pip install pandas scikit-learn matplotlib seaborn`

### 1. Launch the Security Server (C++)
Open a terminal and compile + run the server:

```bash
g++ security_server.cpp -o security_server -lws2_32
./security_server

2. Launch the Application (Python)
Open a second terminal and run:
Bashpython - main.py

📋 Compliance Note
This system was built with Security-by-Design principles. By isolating the data-scrubbing logic into a standalone C++ server, we reduce the attack surface of the main application and ensure that sensitive medical data is processed in an isolated memory space.

Author
Developed as a showcase of Systems Engineering and Data Science proficiency.