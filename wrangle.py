import pandas as pd
from sklearn.model_selection import train_test_split

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
    
    # Set categorical variable in win column to int (1 = True, 0 = False)
    df['win'] = df['win'].astype(int)
    
    # Changing column name 'class' because that is a reserved word. Will change it to 'c_class' (character_class)
    df = df.rename(columns={'class': 'c_class'})

    # Adding a column that contains the categorical variable for whether or not the faction is horde
    df['is_horde'] = [1 if faction == 'horde' else 0 for faction in df.faction]
    
    # Adding a seperator to the code column for game #s at 10+ for a certain battleground, this will be useful later for exploration.
    for bg in df.code:
        if len(str(bg)) == 4:
            df.loc[(df['code'] == bg), 'code'] = f'{bg[0:2]}_{bg[2:]}'

    train_validate, test = train_test_split(df, test_size=.25)
    train, validate = train_test_split(train_validate, test_size=.35)
    return train, validate, test