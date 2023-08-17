import pandas as pd
import time
import matplotlib.pyplot as plt

def read_scenario_data(scenario, data):
    print(f"===== {scenario} Scenario =====")
    print(f"Data for {scenario} Scenario:")
    for value in data:
        print(value)
    print(f"Number of data points: {len(data)}")
    print("\n")

    # Create a line chart using Matplotlib
    plt.plot(data)
    plt.xlabel('Index')
    plt.ylabel('BirthWeight')
    plt.title(f'{scenario} Scenario: Baby Weight Data')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
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
        "Sorted": sorted(list_column_f)
    }
    
    scenario = "Sorted"
    data = scenarios[scenario]
    start_time = time.time()
    read_scenario_data(scenario, data)
    end_time = time.time()
    print(f"Time taken for {scenario} scenario: {end_time - start_time:.6f} seconds")
