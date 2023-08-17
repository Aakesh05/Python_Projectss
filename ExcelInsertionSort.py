import pandas as pd
import matplotlib.pyplot as plt
import time
import openpyxl

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def read_excel_file(file_path):
    try:
        # Read the Excel file using pandas
        df = pd.read_excel(file_path)

        # Extract the "Price" column and convert it to numeric
        column_f = df["BirthWeight"]
        column_f = column_f.apply(pd.to_numeric, errors='coerce').dropna()
        
        # Convert the numeric data to a list
        list_column_f = list_column_f.tolist()

        # Measure the time taken to sort the data using insertion sort
        start_time = time.time()
        insertionSort(list_column_f)
        end_time = time.time()

        # Print the sorted data
        print("Data in Column F (Sorted):")
        for value in list_column_f:
            print(value)

        print(f"Time Taken to Sort data: {end_time - start_time:.6f} seconds.")

        # Create a line chart using Matplotlib
        plt.plot(list_column_f)
        plt.xlabel('Index')
        plt.ylabel('Price')
        plt.title('Sorted Price Data')
        plt.grid(True)
        plt.show()

    except FileNotFoundError:
        print(f"File not found at path: {file_path}")

    except pd.errors.ParserError:
        print(f"Error parsing the file at path: {file_path}")

if __name__ == "__main__":

    file_path = r"C:\Users\schoo\Documents\TECHTORIUM !!!\2023\Term 3\TERM 3 ASSESSMENTS\BirthWeight.xlsx"
    
    read_excel_file(file_path)
