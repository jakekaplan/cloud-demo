import pandas
import os

def hello_world():
    print("Hello world!")

def hello_pandas(name: str):
    print(f"hello {name}!")
    print("pandas version", pandas.__version__)
    print(os.environ.get("CLOUD_ENV"))
    
