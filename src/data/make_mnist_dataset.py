import os
import sys
import pandas as pd
from pathlib import PurePath, Path
from sklearn.datasets import fetch_openml

DATA_PATH = sys.argv[1]
# DATA_PATH = os.path.abspath("data/external/")

def fetch_mnist_dataset():
    '''
    This function fetches MNIST Dataset
    mnist_784 contains images with 28x28(=784) pixels
    It returns Pandas Dataframe with 784 features and one target column
    '''
    mnist = fetch_openml('mnist_784', version=1, parser='liac-arff')

    df_mnist = pd.DataFrame(mnist['data'])
    df_mnist['target'] = mnist['target']
    return df_mnist


def save_mnist_dataset(str: DATA_PATH):
    '''
    This function saves MNIST dataset in desired folder
    '''
    df = fetch_mnist_dataset()
    filename = "MNIST_784.csv"
    filepath = PurePath(DATA_PATH, filename)
    df.to_csv(filepath)
    return print("MNIST Dataset has been saved to {} location".format(filepath))


save_mnist_dataset(DATA_PATH)
