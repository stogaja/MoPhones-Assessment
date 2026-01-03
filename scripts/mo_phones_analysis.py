import pandas as pd
import os
import glob
import numpy as np
from datetime import datetime

# Settings
base_dir = r"c:\Users\HP\Desktop\Personal Projects\MoPhones"
credit_dir = os.path.join(base_dir, "data", "raw", "Credit Data")
sales_path = os.path.join(base_dir, "data", "raw", "Sales and Customer Data.xlsx")
nps_path = os.path.join(base_dir, "data", "raw", "NPS Data.xlsx")
report_path = os.path.join(base_dir, "docs", "analysis_report.md")

def load_credit_data():
    print("Loading Credit Data...")
    all_files = glob.glob(os.path.join(credit_dir, "Credit Data - *.csv"))
    df_list = []
    for filename in all_files:
        df = pd.read_csv(filename)
        # Ensure DATE is datetime
        df['DATE'] = pd.to_datetime(df['DATE'], dayfirst=True) # DD/MM/YYYY example on 01-01-2025
        df_list.append(df)
    
    credit_df = pd.concat(df_list, ignore_index=True)
    print(f"Loaded {len(credit_df)} rows of credit data.")
    return credit_df

def load_customer_data():
    print("Loading Customer Data...")
    xl = pd.ExcelFile(sales_path)
    
    # Load sheets
    # gender_df = pd.read_excel(xl, 'Gender') 
    dob_df = pd.read_excel(xl, 'DOB')
    income_df = pd.read_excel(xl, 'Income Level')
    
    # Clean column names (strip whitespace)
    dob_df.columns = dob_df.columns.str.strip()
    income_df.columns = income_df.columns.str.strip()
    
    # Normalize keys
    dob_df.rename(columns={'Loan Id': 'LOAN_ID', 'date_of_birth': 'DOB'}, inplace=True)
    income_df.rename(columns={'Loan Id': 'LOAN_ID'}, inplace=True)
    
    # print(f"DOB Sheet Columns: {dob_df.columns.tolist()}") 
    
    return dob_df, income_df

def load_nps_data():
    print("Loading NPS Data...")
    # Inspect first to find the right sheet/columns
    xl = pd.ExcelFile(nps_path)
    # Assuming first sheet
    nps_df = pd.read_excel(xl, sheet_name=0)
    # Identify LOAN_ID column matches
    # Usually 'Loan Id'
    if 'Loan Id' in nps_df.columns:
        nps_df.rename(columns={'Loan Id': 'LOAN_ID'}, inplace=True)
    
    return nps_df

def calculate_age_group(age):
    if pd.isna(age): return 'Unknown'
    if 18 <= age <= 25: return '18-25'
    if 26 <= age <= 35: return '26-35'
    if 36 <= age <= 45: return '36-45'
    if 46 <= age <= 55: return '46-55'
    if age > 55: return 'Above 55'
    return 'Under 18'

def calculate_income_group(income):
    if pd.isna(income): return 'Unknown'
    if income < 5000: return 'Below 5,000'
    if 5000 <= income <= 9999: return '5,000–9,999'
    if 10000 <= income <= 19999: return '10,000–19,999'
    if 20000 <= income <= 29999: return '20,000–29,999'
    if 30000 <= income <= 49999: return '30,000–49,999'
    if 50000 <= income <= 99999: return '50,000–99,999'
    if 100000 <= income <= 149999: return '100,000–149,999'
    if income >= 150000: return '150,000 and above'
    return 'Unknown'

def main():
    # 1. Load Data
    credit_df = load_credit_data()
    dob_df, income_df = load_customer_data()
    nps_df = load_nps_data()
    
    # 2. Add Age
    # Merge DOB to credit_df
    # DOB sheet cols: Loan Id, DOB
    dob_df['DOB'] = pd.to_datetime(dob_df['DOB'], errors='coerce')
    
    # Check if we lost data
    # print(dob_df.head())
    
    joined_df = credit_df.merge(dob_df, on='LOAN_ID', how='left')
    
    print("\nJoined Data Info:")
    print(joined_df[['DATE', 'DOB']].dtypes)
    print(joined_df[['DATE', 'DOB']].head())

    # Ensure datetime again 
    joined_df['DATE'] = pd.to_datetime(joined_df['DATE'], errors='coerce')
    joined_df['DOB'] = pd.to_datetime(joined_df['DOB'], errors='coerce')

    # Calculate Age
    # Age = (Report Date - DOB) / 365.25
    joined_df['calculated_age'] = (joined_df['DATE'] - joined_df['DOB']).dt.days / 365.25
    joined_df['Age Group'] = joined_df['calculated_age'].apply(calculate_age_group)
    
    # 3. Add Income
    # Income sheet cols: Loan Id, Duration, Received, Banks Received, Paybills Received Others
    # Sum columns
    income_cols = ['Received', 'Banks Received', 'Paybills Received Others']
    # Ensure numeric
    for col in income_cols:
        if col in income_df.columns:
            income_df[col] = pd.to_numeric(income_df[col], errors='coerce').fillna(0)
    
    income_df['Total_Income'] = income_df[income_cols].sum(axis=1)
    
    # Average Income = Total / Duration
    # Handle duration 0 or NaN
    income_df['Duration'] = pd.to_numeric(income_df['Duration'], errors='coerce').fillna(1)
    income_df['Average_Income'] = income_df['Total_Income'] / income_df['Duration']
    
    income_df['Income Group'] = income_df['Average_Income'].apply(calculate_income_group)
    
    # Merge to main
    final_df = joined_df.merge(income_df[['LOAN_ID', 'Average_Income', 'Income Group']], on='LOAN_ID', how='left')
    
    print("\nData Preparation Complete.")
    print(final_df[['LOAN_ID', 'DATE', 'Age Group', 'Income Group']].head())
    
    # Prepare Report
    with open(report_path, 'w') as f:
        f.write("# MoPhones Data Analysis Report\n\n")
        
        # --- Analysis Q1: Portfolio Performance ---
        f.write("## 1. Portfolio Performance Over Time\n")
        # Group by Snapshot Date
        perf = final_df.groupby('DATE').agg({
            'LOAN_ID': 'count',
            'TOTAL_PAID': 'sum',
            'ARREARS': 'sum',
            'DAYS_PAST_DUE': 'mean'
        }).reset_index()
        f.write(perf.to_string(index=False))
        f.write("\n\n")
        
        # Breakdown by Status
        status_breakdown = final_df.groupby(['DATE', 'ACCOUNT_STATUS_L1']).size().unstack(fill_value=0)
        f.write("### Account Status Breakdown (Count)\n")
        f.write(status_breakdown.to_string())
        f.write("\n\n")
        
        # --- Analysis Q2: Risk Indicators ---
        f.write("## 2. Risk Indicators (Arrears by Age/Income)\n")
        # Latest snapshot for current risk profile
        latest_date = final_df['DATE'].max()
        latest_df = final_df[final_df['DATE'] == latest_date]
        
        risk_by_age = latest_df.groupby('Age Group')['ARREARS'].mean().sort_values()
        f.write("### Average Arrears by Age Group (Latest Snapshot)\n")
        f.write(risk_by_age.to_string())
        f.write("\n\n")
        
        risk_by_income = latest_df.groupby('Income Group')['ARREARS'].mean().sort_values()
        f.write("### Average Arrears by Income Group (Latest Snapshot)\n")
        f.write(risk_by_income.to_string())
        f.write("\n\n")
        
        # --- Analysis Q3: NPS vs Credit ---
        f.write("## 3. NPS vs Credit Outcomes\n")
        nps_merged = latest_df.merge(nps_df, on='LOAN_ID', how='inner')
        
        # Identify Score column
        score_col = [c for c in nps_merged.columns if 'score' in c.lower() or 'nps' in c.lower() or 'recommend' in c.lower()]
        if score_col:
            col = score_col[0] # Take first likely column
            f.write(f"Using NPS Column: {col}\n")
            
            # NPS by Status
            nps_by_status = nps_merged.groupby('ACCOUNT_STATUS_L1')[col].mean()
            f.write("### Average NPS by Account Status\n")
            f.write(nps_by_status.to_string())
            f.write("\n\n")
            
            # NPS by Arrears (Binning Arrears?)
            nps_merged['Has_Arrears'] = nps_merged['ARREARS'] > 0
            nps_by_arrears = nps_merged.groupby('Has_Arrears')[col].mean()
            f.write("### Average NPS by Arrears Existence\n")
            f.write(nps_by_arrears.to_string())
            f.write("\n\n")
        else:
            f.write("Could not identify NPS Score column.\n")
            f.write(f"NPS Columns: {nps_df.columns.tolist()}\n")

    print(f"Analysis complete. Report written to {report_path}")

if __name__ == "__main__":
    main()
