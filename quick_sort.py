import pandas as pd
import time

def quickSort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)

def read_excel_file(file_path):
    try:
        # Read the Excel file using pandas
        df = pd.read_excel(file_path)

        # Extract the "BirthWeight" column and convert it to numeric
        column_f = df["BirthWeight"]
        column_f = column_f.apply(pd.to_numeric, errors='coerce').dropna()

        # Convert the numeric data to a list
        list_column_f = column_f.tolist()

        # Measure the time taken to sort the data using Quick Sort
        start_time = time.time()
        sorted_list = quicksort(list_column_f)
        end_time = time.time()

        # Print the sorted data
        print("Sorted BirthWeight Values:")
        for value in sorted_list:
            print(value)

        print(f"Time Taken to Sort data: {end_time - start_time:.6f} seconds.")

    except FileNotFoundError:
        print(f"File not found at path: {file_path}")

    except pd.errors.ParserError:
        print(f"Error parsing the file at path: {file_path}")

if __name__ == "__main__":
    file_path = r"C:\Users\schoo\Documents\TECHTORIUM !!!\2023\Term 3\TERM 3 ASSESSMENTS\BirthWeight.xlsx"
    read_excel_file(file_path)
