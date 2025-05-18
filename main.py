import pandas as pd

# Path to your original Excel File
excel_file = "vagas_e_candidaturas.xlsx"

# Load all sheets (using xlrd for .xls files)
xls = pd.ExcelFile(excel_file, engine='openpyxl')

# List to store dataframes from each sheet
all_dfs = []

#Loop through all sheets
for sheet_name in xls.sheet_names:
    df = pd.read_excel(xls, sheet_name=sheet_name, engine='openpyxl')
    df['__source_sheet'] = sheet_name # (optional) add a column with the original sheet name
    all_dfs.append(df)

 # Concatenate all DataFrames, aligning columns by name
final_df = pd.concat(all_dfs, ignore_index= True)

#Save to a new Excel file
final_df.to_excel('all_sheets_combined.xlsx', index=False)