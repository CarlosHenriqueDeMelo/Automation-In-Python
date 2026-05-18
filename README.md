# 🤖 Python Automation Projects

This repository contains Python automation projects developed to practice process automation, data handling, and workflow optimization using Python.

---

## 🚀 Technologies Used

- Python 3
- PyAutoGUI
- Pandas
- CSV
- Automation Scripts

---

# 📦 ProjectPy01 – Product Registration Automation

A Python automation project that automatically logs into a website and registers products from a CSV file using GUI automation.

## 📌 Features

- Automatically opens Google Chrome
- Accesses a login page
- Performs automatic login
- Reads product data from a CSV file
- Registers products automatically in the system
- Handles optional observations field

## 🛠️ Technologies

- **PyAutoGUI** → GUI automation and mouse/keyboard control
- **Pandas** → CSV data processing
- **Time** → Execution timing and delays

## 📂 Project Structure

```bash
ProjectPy01/
│── auxiliar.py
│── codigo.py
│── produtos.csv
```

## 📊 Dataset

The `produtos.csv` file contains:

- Product code
- Brand
- Product type
- Category
- Unit price
- Cost
- Additional observations

Example:

| Code | Brand | Type | Price |
|-------|--------|------|--------|
| MOLO000251 | Logitech | Mouse | 25.95 |

## ▶️ How to Run

Install dependencies:

```bash
pip install pyautogui pandas
```

Run the automation:

```bash
python codigo.py
```

⚠️ **Important:** Screen coordinates are configured for a specific monitor resolution. You may need to adjust the mouse positions in the code using `auxiliar.py`.

---

# 📊 ProjectPy02 – Customer Churn Data Analysis

A data analysis project focused on customer cancellation behavior (churn) using Python, Pandas, and Plotly.

## Features

- Data cleaning
- Exploratory Data Analysis (EDA)
- Customer churn analysis
- Interactive visualizations
- Pattern identification

## Technologies

- Python
- Pandas
- Plotly
- Jupyter Notebook

## Files

```bash
ProjectPy02/
│── inicial.ipynb
│── gabarito (1).ipynb
│── cancelamentos.csv
```

---

## 📄 License

This repository is intended for educational and portfolio purposes.
