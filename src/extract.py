import pandas as pd
import os   
import requests
from requests.exceptions import HTTPError
import logging
from dotenv import load_dotenv
import json

load_dotenv()

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(message)s")

filename = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "doc", "Sample Test Movielens.csv")

base_url = "https://api.adzuna.com/v1/api/jobs"
country = "br"
page = 5
results_per_page = 10
id = os.getenv("app_id")
key = os.getenv("app_key")
params = {"app_id":id,
          "app_key":key}
headers = {"Accept":"application/json"}

def read_csv():
    try:    
        df = pd.read_csv(filename)
        print(df.head())
        logging.info("read succesful")
        return df
    except Exception as e:
        logging.error(e)

def read_api():
    try:
        response = requests.get(url=f"{base_url}/{country}/search/{page}?results_per_page={results_per_page}&what=Data%20Engineer", params=params,headers=headers)  
        response.raise_for_status()
        logging.info("api data downloaded successfully")
        data = response.json()
        path = os.path.join("doc/jobs.json")
        with open(path, "w") as file:
            json.dump(data, file)
        logging.info("json file copied successfully")
    except HTTPError as e:
        logging.error(f"error getting data from adzuna {e}")

def parse_json():
    path = os.path.join("doc/jobs.json")
    with open(path, "r") as file:
        data = json.load(file)
    job_list = []
    result = data.get("results",[])
    for jobs in result:
        job_list.append({
        "id" : jobs.get("id",""),
        "location" : jobs.get("location",""),
        "salary" : jobs.get("salary_is_predicted",""),
        "company" : jobs.get("company",""),
        "category" : jobs.get("category",""),
        "date" : jobs.get("created",""),
        "title" : jobs.get("title",""),
        "job_url" : jobs.get("redirect_url",""),
        "description" : jobs.get("description","")})

    df = pd.DataFrame(job_list)
    print(df.head())

if __name__ == "__main__":
    print(filename)
    read_csv()
    read_api()
    parse_json()