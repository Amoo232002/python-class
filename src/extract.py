import pandas as pd
import os   
import requests
import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(message)s")


def read_csv():
    try:    
        df = pd.read_csv(r"C:\\Users\\marv\\OneDrive\\Desktop\\python-class-quantum\\doc\\Sample Test Movielens.csv")
        print(df.head())
        return df
    except Exception as e:
        print(e)

app_id = os.getenv("app_id")
app_key = os.getenv("app_key")

if __name__ == "__main__":
    read_csv()