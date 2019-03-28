import pandas as pd
from sklearn.model_selection import train_test_split
import os

def load(data_dir, seed=2):
    train = pd.read_csv(os.path.join("data", data_dir, "train.csv"))
    train, val = train_test_split( train, random_state=seed )
    test = pd.read_csv(os.path.join("data", data_dir, "test.csv"))
    return train, val, test

def load_train(data_dir):
    return pd.read_csv(os.path.join("data", data_dir, "train.csv"))

def load_file(filename):
    return pd.read_csv(filename)
