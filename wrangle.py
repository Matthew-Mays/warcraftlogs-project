import pandas as pd

# This function will acquire and prepare the data for exploration
def get_wrangle_bgs_data():
    
    # Acquire the data
    df = pd.read_csv('archive/wowbgs.csv')
    
    # Fill categorically negative nulls with a value of 0
    df = df.fillna(0)
    
    # Setting all columns to lower case for convenience
    df.columns = [column.lower() for column in df.columns]

    # Lowercase all string rows for convenience
    df['battleground'] = df['battleground'].str.lower()
    df['code'] = df['code'].str.lower()
    df['faction'] = df['faction'].str.lower()
    df['class'] = df['class'].str.lower()
    
    return df