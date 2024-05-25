import os
import pandas as pd
from sqlalchemy import create_engine

# Database connection settings
DB_HOST = 'db'
DB_PORT = '5433'
DB_NAME = 'nyc_taxi'
DB_USER = 'admin'
DB_PASS = 'admin'

def load_data(file_path):
    try:
        engine = create_engine(f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
        df = pd.read_csv(file_path)
        df.to_sql('taxi_data', engine, if_exists='append', index=False)
        print(f'Data from {file_path} loaded successfully!')
    except Exception as e:
        print(f'Error loading data from {file_path}: {e}')

if __name__ == '__main__':
    data_dir = './data'
    for file in os.listdir(data_dir):
        if file.endswith('.csv'):
            load_data(os.path.join(data_dir, file))
