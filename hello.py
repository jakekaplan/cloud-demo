import prefect
import pandas
import os

@flow
def hello_world():
    print("Hello world!")

@flow
def hello_pandas(name: str):
    print(f"hello {name}!")
    print("pandas version", pandas.__version)
    print(os.environ.get("CLOUD_ENV"))
    
