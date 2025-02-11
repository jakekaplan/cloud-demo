from prefect import flow

@flow
def hello_world():
    print("hello world!")
