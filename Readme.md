# 🗂️ Consolidating Excel Sheets with Python
This Python script reads all sheets from a `.xlsx` Excel file and merges them into a single spreadsheet.


## 📌 What the script does:
- Loads **all sheets** from an Excel file
- Adds a column named `__source_sheet` with the original sheet name
- Concatenates all sheets into a single DataFrame
- Saves the result to a new file: `all_sheets_combined.xlsx`

## ▶️ How to use
1. Clone this repository:
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo

2. Create and activate a virtual environment:
python -m venv venv
venv\Scripts\activate  # on Windows

3. Install the required dependencies:
pip install pandas openpyxl

4. Add your .xlsx file inside the project folder

5. Run the script
python main.py


## 📦 Requirements
- Python 3.7+
- pandas
- openpyxl
