import os
import sys
import pandas as pd
from pathlib import PurePath, Path

input_data_path = sys.argv[1]
output_data_path = sys.argv[2]


def split_train_test(input_data_path, output_data_path):
    '''
    This function picks csv file from input_data_path as pandas dataframe
    This function splits the csv file in training and test datasets
    This function saves the training and test datasets in output_data_path
    '''
    csv_data = pd.read_csv(input_data_path)
    X_train, X_test = csv_data.iloc[:60000, :-1], csv_data.iloc[60000:, :-1]
    y_train, y_test = csv_data.iloc[:60000, -1], csv_data.iloc[60000:, -1]

    X_train.to_csv(output_data_path+"X_train.csv", index=False)
    X_test.to_csv(output_data_path+"X_test.csv", index=False)
    y_train.to_csv(output_data_path+"y_train.csv", index=False)
    y_test.to_csv(output_data_path+"y_test.csv", index=False)

    return print("The Dataset has been split into Training and Test Datasets; and save in {}".format(output_data_path))

print("Spliting Dataset into Training and Test Datasets; and saving as Processed Datasets")
split_train_test(input_data_path, output_data_path)
