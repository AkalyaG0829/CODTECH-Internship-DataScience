import pandas as pd
import os

def load_data():
    # Always resolve relative to project root
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    data_path = os.path.join(project_root, "data")

    demand = pd.read_csv(os.path.join(data_path, "demand.csv"))
    capacity = pd.read_csv(os.path.join(data_path, "capacity.csv"))
    costs = pd.read_csv(os.path.join(data_path, "costs.csv"))
    return demand, capacity, costs

def to_dict(df, key_col, val_col):
    return dict(zip(df[key_col], df[val_col]))