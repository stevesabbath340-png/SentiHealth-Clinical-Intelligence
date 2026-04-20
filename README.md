# 🏥 SentiHealth: Clinical Intelligence & Security Platform
### *Subtitle: SentiHealth Insights — Advanced Data Analytics & Predictive Care*

**SentiHealth** is an enterprise-grade informatics platform bridging the gap between low-level systems security (**C++**) and high-level predictive health analytics (**Python**). This project demonstrates a robust, decoupled architecture designed for secure clinical decision support.

---

## 🖥️ System Preview

### **1. Full System Pipeline**
The following capture shows the **Distributed Handshake** between the Python client and the C++ Security Server, followed by the automated SQL analytical sweep.

![Full Pipeline Scan](images/Full%20Pipeline%20Scan.png)

### **2. Clinical Intelligence Dashboard**
Our visualization layer converts relational data into actionable metrics, providing health officials with real-time geographic and condition-based trends.

![BI Dashboard](images/BI%20Dashboard(Chart).png)

---

## 🏗️ Technical Architecture

### **1. Security Vault (C++ Backend)**
* **Technology:** Winsock2 TCP/IP Sockets.
* **Function:** Acts as a standalone "Data Scrubber" to hash sensitive Patient PII (Personally Identifiable Information) in an isolated memory space before database insertion.

### **2. AI Intelligence Engine (Python - Upgraded)**
* **Model:** **Random Forest Ensemble Regressor.**
* **Why it matters:** Unlike standard decision trees, this model utilizes an **Ensemble Method** (100 individual trees) to prevent overfitting. It provides higher predictive accuracy for patient recovery times through multi-model voting.

### **3. Data Persistence & Analytics**
* **Database:** SQLite3 (Schema optimized for future PostgreSQL migration).
* **Analytics:** Leverages **Pandas** for high-performance data manipulation and **Seaborn** for clinical-grade visualization.

---

## 🚀 Key Features
* **Forensic Audit Logging:** Every system event is captured in `audit_log.txt` to ensure compliance with **POPIA/GDPR** accountability standards.
* **Ensemble Prediction:** Clinical-grade recovery forecasting based on age, regional environmental factors, and condition severity.
* **Distributed Processing:** Separation of concerns between the security layer (C++) and the application layer (Python).

---

## 🛠️ Tech Stack
| Tier | Technology |
| :--- | :--- |
| **Security/Network** | C++ (MinGW-w64), Winsock2 |
| **Predictive AI** | Python (Scikit-Learn Ensemble Methods) |
| **Data Science** | Pandas, NumPy |
| **Relational DB** | SQLite3 |
| **Visual BI** | Matplotlib, Seaborn |

---

## 📋 Installation & Execution

### **1. Launch Security Server**
```bash
g++ security_server.cpp -o security_server -lws2_32
./security_server

2. Launch Clinical Dashboard
Bash
pip install pandas scikit-learn matplotlib seaborn
python main.py

🎓 Author's Note
This project was developed to demonstrate proficiency in Systems Engineering and Data Science. While SQLite was utilized for portable demonstration, the architecture is designed to scale to enterprise RDBMS like PostgreSQL for population-scale health informatics.