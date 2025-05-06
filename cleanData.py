import pandas as pd

def load_cleaned_data(filename='cleanCSVData.csv'):
    df = pd.read_csv(filename)
    return df
