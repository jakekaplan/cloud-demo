import os
import pandas


def hello_pandas():
    print("hi panda!")
    print(f"pandas version: {pandas.__version__}")
    print(f"{os.environ.get('PANDA')}")
