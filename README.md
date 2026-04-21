# 🏥 SentiHealth Navigator
### *Advanced Clinical Intelligence & Security Platform*

---

## 🌍 Impact Statement: Strengthening SA Healthcare
In many South African clinical settings—particularly rural clinics—data security and reliable analytics are hampered by limited local infrastructure. **SentiHealth Navigator** addresses this by providing a high-speed, local-first C++ security layer that protects patient PII (Personally Identifiable Information) even in offline environments. The Python-based intelligence engine enables resource-constrained facilities to predict patient recovery and manage bed availability effectively, balancing **POPIA compliance** with high-performance clinical insights.

---

## 🖥️ System Preview

### **1. Full System Pipeline**
Demonstrating the **Distributed Handshake** between the Python navigator and the C++ Security Server, followed by an automated SQL analytical sweep and AI training.

![Full Pipeline Scan](Full%20Pipeline%20Scan.png)
![Complete Scan](Complete%20Scan.png)

### **2. Clinical Intelligence Dashboard**
Converting relational SQL data into actionable metrics to track disease prevalence and recovery benchmarks.

![BI Dashboard (Chart)](BI%20Dashboard%28Chart%29.png)

---

## 🏗️ Technical Architecture & Workflow

### **User-Centric Workflows**
| User Role | Workflow | Primary Benefit |
| :--- | :--- | :--- |
| **Hospital Admin** | Monitors the BI Dashboard for regional trends. | **Resource Allocation:** Smarter bed/staff management. |
| **Clinical Staff** | Inputs anonymized vitals into the Navigator. | **Risk Assessment:** Using AI to predict recovery needs. |
| **IT/SecOps** | Audits the C++ Security Vault and local logs. | **Compliance:** Ensures 100% adherence to POPIA/GDPR. |

### **The "Vault & Engine" Model**
* **Security Vault (C++ Backend):** A standalone server using **Winsock2 TCP/IP Sockets**. It hashes sensitive data in an isolated memory space before it ever touches the database.
* **Intelligence Engine (Python):** Orchestrates the **SQLite** relational database, **Pandas** analytics, and the predictive model.

---

## 🚀 Key Technical Features

### **1. AI Recovery Predictor (Random Forest Ensemble)**
Upgraded from a basic decision tree to a **Random Forest Regressor** (100+ trees). This ensemble method provides higher predictive accuracy and stability by "voting" across multiple models to determine patient recovery outcomes.

### **2. SQL-Driven Data Integrity**
Utilizes a **Synthetic Clinical Dataset** modeled after anonymized benchmarks (inspired by MIMIC-III). The schema is optimized for portable SQLite execution but is fully compatible with enterprise RDBMS like **PostgreSQL**.

### **3. Forensic Audit Trail**
Maintains an immutable `audit_log.txt` that captures every user interaction and system handshake, ensuring a clear chain of custody for all clinical data.

---

## 🧠 Key Learning Outcomes
* **Cross-Language Interoperability:** Mastered socket communication between C++ and Python.
* **Ensemble ML:** Learned to implement and tune Random Forest models for clinical regression.
* **DevOps Mindset:** Integrated **Docker** containerization logic for microservice deployment.
* **Regulatory Engineering:** Applied practical POPIA security principles to software design.

---

## 🛠️ Tech Stack & Deployment
* **Languages:** Python 3.11, C++ (MinGW-w64)
* **Libraries:** Pandas, Scikit-Learn (Ensemble), Matplotlib, Seaborn
* **Cloud Ready:** Designed for **Azure Health Data Services** or **AWS HealthLake**.
* **Containerization:** Includes a `Dockerfile` for standardized microservice deployment.

---

## 📋 Quick Start
1.  **Run Security Server:** `g++ security_server.cpp -o security_server -lws2_32 && ./security_server`
2.  **Launch Navigator:** `pip install pandas scikit-learn matplotlib seaborn && python main.py`

---
*Developed as a showcase of Systems Engineering and Data Science proficiency.*