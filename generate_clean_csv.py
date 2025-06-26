# =============================================================================
# AITHON V2: FINAL CLEANED DATA AS CSV GENERATOR (WITH ENHANCED FEATURES)
# =============================================================================

import pandas as pd
import numpy as np
import sys

# --- 1. CONFIGURATION AND CONSTANTS ---
try:
    FILE_PATH = './survey.csv'
    df_raw = pd.read_csv(FILE_PATH)
except FileNotFoundError:
    print("ERROR: survey.csv not found.", file=sys.stderr)
    sys.exit(1)

# V2: Expanded feature list for a more accurate model
FEATURE_COLS = [
    'Age', 'Gender', 'no_employees', 'tech_company', 'remote_work', 'family_history',
    'benefits', 'care_options', 'wellness_program', 'seek_help', 'anonymity', 'leave',
    'mental_health_consequence', 'phys_health_consequence', 'coworkers', 'supervisor', 'mental_vs_physical'
]
TARGET_COL = 'treatment'

# V2: Added new mappings
EMPLOYEE_MAP = {'1-5': 0, '6-25': 1, '26-100': 2, '100-500': 3, '500-1000': 4, 'More than 1000': 5}
CONSEQUENCE_MAP = {'No': 0, 'Maybe': 1, 'Yes': 2}
LEAVE_MAP = {'Very difficult': -2, 'Somewhat difficult': -1, "Don't know": 0, 'Somewhat easy': 1, 'Very easy': 2}
YES_NO_MAP = {'Yes': 1, 'No': 0}
RESPONSE_MAP = {'Yes': 1, 'No': 0, "Don't know": -1}
SOCIAL_MAP = {'Yes': 1, 'No': -1, 'Some of them': 0}

# --- 2. DATA PROCESSING PIPELINE ---

def run_cleaning_pipeline(df):
    df_work = df[FEATURE_COLS + [TARGET_COL]].copy()

    # Clean Age
    df_work['Age'] = pd.to_numeric(df_work['Age'], errors='coerce')
    df_work.dropna(subset=['Age'], inplace=True)
    df_work = df_work[(df_work['Age'] >= 18) & (df_work['Age'] <= 80)].copy()
    df_work['Age'] = df_work['Age'].astype(int)

    # Clean Gender
    df_work['Gender'] = df_work['Gender'].str.lower()
    male_list = ['male', 'm', 'male (cis)', 'man']
    female_list = ['female', 'f', 'woman', 'female (cis)']
    df_work.loc[df_work['Gender'].isin(male_list), 'Gender'] = 'male'
    df_work.loc[df_work['Gender'].isin(female_list), 'Gender'] = 'female'
    df_work.loc[~df_work['Gender'].isin(['male', 'female']), 'Gender'] = 'other'

    # Map all categorical columns
    cols_to_map = {
        'benefits': RESPONSE_MAP, 'care_options': RESPONSE_MAP, 'wellness_program': RESPONSE_MAP,
        'seek_help': RESPONSE_MAP, 'anonymity': RESPONSE_MAP, 'treatment': RESPONSE_MAP,
        'mental_vs_physical': RESPONSE_MAP, 'remote_work': YES_NO_MAP, 'family_history': YES_NO_MAP,
        'tech_company': YES_NO_MAP, 'no_employees': EMPLOYEE_MAP, 'mental_health_consequence': CONSEQUENCE_MAP,
        'phys_health_consequence': CONSEQUENCE_MAP, 'leave': LEAVE_MAP, 'coworkers': SOCIAL_MAP, 'supervisor': SOCIAL_MAP
    }
    for col, mapping in cols_to_map.items():
        if col in df_work.columns:
            df_work[col] = df_work[col].map(mapping)
    
    # Fill remaining NaNs using the recommended syntax
    for col in df_work.columns:
        if df_work[col].isnull().any():
            df_work.loc[:, col] = df_work[col].fillna(df_work[col].mode()[0])
            
    # One-Hot Encode Gender
    df_clean = pd.get_dummies(df_work, columns=['Gender'], drop_first=True, dtype=int)
    return df_clean

# --- 3. MAIN EXECUTION ---
if __name__ == '__main__':
    final_df = run_cleaning_pipeline(df_raw)
    csv_output_string = final_df.to_csv(index=False)
    print(csv_output_string)