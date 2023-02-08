"""Combine Data Files."""
import pandas as pd
import os


def read_data(filename=str):
    """Read single data file."""
    data = pd.read_table(filename, delimiter="\t", header=None)
    return data


total_data = []
with os.scandir(
    "HW3/Diabetes-Data/"  # grab all the filenames in the folder that I want to read
) as filenames:
    for file in filenames:
        single_file = read_data(f"HW3/Diabetes-Data/{file.name}")
        total_data.append(single_file)
    appended_data_concat = pd.concat(total_data)  # rbind all the dataframes
    appended_data_concat.to_csv("HW3/combined_data.csv")
    # export data to csv file in current directory
