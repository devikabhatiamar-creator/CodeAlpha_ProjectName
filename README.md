# 🚀 CodeAlpha - Data Redundancy Removal System

## 📌 Project Description
This project is a cloud-based system designed to detect and remove duplicate data efficiently. It ensures that only unique and verified data is stored in the database, improving data accuracy and system performance.

---

## 🎯 Objective
- Identify duplicate data entries  
- Prevent redundant storage  
- Maintain a clean and optimized database  

---

## 🚀 Features
- 🔍 Detects duplicate data entries  
- 🚫 Prevents redundant data storage  
- ✅ Validates new data before insertion  
- 🗄️ Maintains database accuracy  
- ⚡ Improves overall system efficiency  

---

## 🛠️ Technologies Used
- Python  
- SQLite (`data.db`)  
- Streamlit  

---

## ▶️ How to Run

1. Download or clone this repository  
2. Open the project folder  
Run the app:
streamlit run app.py
Open in browser:
http://localhost:8501
📂 Project Structure
app.py         # Main application logic  
database.py    # Database operations  
utils.py       # Helper functions  
data.db        # SQLite database  
README.md      # Project documentation  
🧠 How It Works
User inputs data
System compares it with existing database records
If duplicate → rejected
If unique → stored successfully
📸 Screenshots

🎯 Internship Task

This project is submitted as part of the CodeAlpha Cloud Computing Internship
Task 1: Data Redundancy Removal System
3. Install dependencies:
```bash
pip install streamlit
