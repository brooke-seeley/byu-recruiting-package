import pandas as pd

## Load and prepare high school dataset

def load_hs_data(path):

    data = pd.read_excel(path, sheet_name='247Data')

    data = data[[
        '247Top', 'Position', 'Utah', 'Distance', 'Height', 'Weight',
        'Score', 'LDS', 'Alumni', 'Poly', 'BYU'
    ]]

    categorical_cols = ['247Top', 'Position', 'Utah', 'LDS', 'Alumni', 'Poly']

    for col in categorical_cols:
        data[col] = data[col].astype('category')

    data['BYU'] = data['BYU'].map({'N': 0, 'Y': 1})

    X = data.drop(columns=['BYU'])
    y = data['BYU']

    return X, y, categorical_cols

## Load and prepare transfer/JC dataset

def load_transfer_data(path):
    
    data = pd.read_excel(path, sheet_name='Transfers')

    data = data[[
        'Years', '247Top', 'Position', 'Distance', 'Conf', 'Height', 'Weight',
        'Score', 'LDS', 'Alumni', 'Prev', 'Poly', 'BYU'
    ]]

    categorical_cols = ['247Top', 'Position', 'Conf', 'LDS', 'Alumni', 'Prev', 'Poly']

    for col in categorical_cols:
        data[col] = data[col].astype('category')

    data['BYU'] = data['BYU'].map({'N': 0, 'Y': 1})

    X = data.drop(columns=['BYU'])
    y = data['BYU']

    return X, y, categorical_cols