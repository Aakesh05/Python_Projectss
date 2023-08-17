import pandas as pd
import time
import pytest

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def read_scenario_data(scenario, data):
    print(f"===== {scenario} Scenario =====")
    print(f"Data for {scenario} Scenario:")
    for value in data:
        print(value)
    print(f"Number of data points: {len(data)}")
    print("\n")

@pytest.mark.parametrize("scenario", ["Unsorted", "Sorted", "Reversed", "Blank", "Duplicate"])
def test_bubble_sort(scenario):
    file_path = r"C:\Users\schoo\Documents\TECHTORIUM !!!\2023\Term 3\TERM 3 ASSESSMENTS\BirthWeight.xlsx"
    
    # Read the Excel file using pandas
    df = pd.read_excel(file_path)

    # Extract the "BirthWeight" column and convert it to numeric
    column_f = df["BirthWeight"]
    column_f = column_f.apply(pd.to_numeric, errors='coerce').dropna()
    
    # Convert the numeric data to a list
    list_column_f = column_f.tolist()

    scenarios = {
        "Unsorted": list_column_f,
        "Sorted": sorted(list_column_f),
        "Reversed": sorted(list_column_f, reverse=True),
        "Blank": [],
        "Duplicate": list_column_f + list_column_f
    }
    
    data = scenarios[scenario]
    bubbleSort(data)
    read_scenario_data(scenario, data)

if __name__ == "__main__":
    for scenario in ["Unsorted", "Sorted", "Reversed", "Blank", "Duplicate"]:
        test_bubble_sort(scenario)
