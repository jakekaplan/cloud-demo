import prefect
from prefect import flow

@flow(log_prints=True)
def hello_world():
    print("hello world!")
    print(prefect.__version__)
