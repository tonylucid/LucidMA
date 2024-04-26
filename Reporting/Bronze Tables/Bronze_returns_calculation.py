from functools import reduce

import numpy as np
import pandas as pd

from Utils.Common import print_df, get_file_path
from Utils.Constants import roll_schedule_mapping
from Utils.Hash import hash_string



# Read the data from the Excel file
input_excel_path = get_file_path(r"S:/Users/THoang/Data/series_returns_2021_2024.xlsx")
df = pd.read_excel(input_excel_path)

# Select the required columns
df = df[['Start_date', 'End_date', 'PoolDescription', 'InvestorDescription', 'Revised Beginning Cap Balance',
         'Withdrawal - BOP',
         'Contribution', 'Revised Ending Cap Acct Balance', 'Returns']]

# Convert 'Start_date' and 'End_date' to datetime
df['Start_date'] = pd.to_datetime(df['Start_date'])
df['End_date'] = pd.to_datetime(df['End_date'])

# Add 'Returns' column to df_grouped
df['Returns'] = 1 + df['Returns']
df = df.sort_values('Start_date')
df['Returns'] = df['Returns'].astype(float)

# Initialize an empty DataFrame to store the result
df_result = pd.DataFrame(
    columns=['Return_ID', 'Pool_name', 'Start_date', 'End_date', 'Day_counts', 'Pool_name', 'Investor_name',
             'Relevant_returns', 'Calculated_returns'])
# List to hold data before concatenating to the dataframe


from datetime import datetime
import time

# Modifying the script to return a DataFrame instead of a dictionary

data_to_append = []
# Convert dates in data to datetime objects for comparison
df['Start_date'] = pd.to_datetime(df['Start_date'])

# Iterate through each unique pool description
for pool in df['PoolDescription'].unique():
    pool_data = df[df['PoolDescription'] == pool]

    # For each date range, calculate the cumulative return
    for start_period, end_period in roll_schedule_mapping[pool]:
        start_period_dt = datetime.strptime(start_period, '%Y-%m-%d')
        end_period_dt = datetime.strptime(end_period, '%Y-%m-%d')

        # Filter 1: Filter rows based on the date range
        period_data = pool_data[
            (pool_data['Start_date'] > start_period_dt) & (pool_data['Start_date'] < end_period_dt)]

        # Filter 2: Exclude capital account that has intra-period contributions or withdrawals
        # (timings that are at the beginning of the evaluation period)
        exclusion_df = period_data[(period_data['Start_date'] > start_period_dt + pd.Timedelta(days=1)) & (
                (abs(period_data['Withdrawal - BOP']) >= 1000) | (abs(period_data['Contribution']) >= 1000))]
        excluded_investors = exclusion_df['InvestorDescription'].unique()
        period_data = period_data[~period_data['InvestorDescription'].isin(excluded_investors)]

        # Group by 'InvestorDescription' and aggregate 'Returns' into a list
        grouped = period_data.groupby('InvestorDescription')['Returns'].apply(list).reset_index()

        for _, group_row in grouped.iterrows():
            investor_name = group_row['InvestorDescription']
            relevant_returns = group_row['Returns']
            # Check if relevant_returns is not empty
            if relevant_returns and not any(np.isnan(x) for x in relevant_returns):
                # Calculate the product of all elements in the 'Relevant returns' list, minus 1, then adjust for the day
                # count
                product_of_returns = reduce((lambda x, y: x * y), relevant_returns) - 1
                day_counts = (end_period_dt - start_period_dt).days
                calculated_returns = (product_of_returns * 360) / day_counts
                return_id = hash_string(f"{pool}{start_period}{end_period}{time.time()}")
                # Prepare the data to be appended
                data_to_append.append({
                    'Return_ID': return_id,
                    'Pool_name': pool,
                    'Start_date': start_period_dt,
                    'End_date': end_period_dt,
                    'Day_counts': day_counts,
                    'Investor_name': investor_name,
                    'Relevant_returns': relevant_returns,
                    'Calculated_returns': calculated_returns
                })
                # Append the data to the result DataFrame
cumulative_returns_df = pd.DataFrame(data_to_append)

# Drop the 'Relevant returns' column from df_result
cumulative_returns_df = cumulative_returns_df.drop(columns=['Relevant_returns'])

# Calculate 'Calculated_Starting_Balance'
def calculate_starting_balance(row):
    mask = (df['Start_date'] == row['Start_date'] + pd.Timedelta(days=1)) & (
            df['InvestorDescription'] == row['Investor_name']) & (df['PoolDescription'] == row['Pool_name'])
    starting_balance = df.loc[mask, 'Revised Beginning Cap Balance']
    if starting_balance.empty:
        return 0  # or any other default value
    else:
        return starting_balance.iloc[0]  # return the first value


cumulative_returns_df['Calculated_Starting_Balance'] = cumulative_returns_df.apply(calculate_starting_balance, axis=1)


# Calculate 'Calculated_Ending_Balance'
def calculate_ending_balance(row):
    mask = (df['End_date'] == row['End_date']) & (df['InvestorDescription'] == row['Investor_name']) & (df['PoolDescription'] == row['Pool_name'])
    ending_balance_df = df.loc[mask, 'Revised Ending Cap Acct Balance']
    if ending_balance_df.empty:
        return 0  # or any other default value
    else:
        return ending_balance_df.iloc[0]


cumulative_returns_df['Calculated_Ending_Balance'] = cumulative_returns_df.apply(calculate_ending_balance, axis=1)

file_path = get_file_path("S:/Users/THoang/Data/all_funds_master_returns_comparison_by_account.xlsx")
cumulative_returns_df.to_excel(file_path, engine="openpyxl")
# file_path = r"S:\Users\THoang\Data\master_returns_comparison_prime_by_account.xlsx"
# df_result.to_excel(file_path, engine="openpyxl")

# PIVOT 2
# Group by 'Start_date' and 'End_date' and aggregate the specified columns
df_grouped = cumulative_returns_df.groupby(['Pool_name', 'Start_date', 'End_date']).agg({
    'Calculated_Starting_Balance': 'sum',
    'Calculated_Ending_Balance': 'sum',
    'Day_counts': 'median'
}).reset_index()

# Convert 'Start_date' and 'End_date' to 'mmmm-yy-dd' format
df_grouped['Start_date'] = df_grouped['Start_date'].dt.strftime('%Y-%m-%d')
df_grouped['End_date'] = df_grouped['End_date'].dt.strftime('%Y-%m-%d')

df_grouped['Annualized Returns - 360'] = ((df_grouped['Calculated_Ending_Balance'] - df_grouped[
    'Calculated_Starting_Balance']) / df_grouped['Calculated_Starting_Balance'] * 360 / df_grouped[
                                              'Day_counts']).round(4)

file_path = get_file_path("S:/Users/THoang/Data/all_funds_master_returns_comparison.xlsx")
df_grouped.to_excel(file_path, engine="openpyxl")

