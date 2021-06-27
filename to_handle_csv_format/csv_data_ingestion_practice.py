import pandas as pd

def load_csv_to_pandas(file_path):
    dataframe = pd.read_csv(file_path, parse_dates = ['tpep_pickup_datetime', 'tpep_dropoff_datetime'])
    return dataframe

if __name__ == '__main__':
    df = load_csv_to_pandas(file_path)
    print(df.dtypes)
    print(df.head())
    
# in linux terminal: cd to wherever the file located then python3 thefilename.py
# be mindful with typo mistakes


