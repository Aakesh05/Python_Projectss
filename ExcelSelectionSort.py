import pandas as pd

import openpyxl

import time
def selection_sort(arr):

    # Selection sort implementation

    n = len(arr)

    for i in range(n):

        min_idx = i

        for j in range(i+1, n):

            if arr[j] < arr[min_idx]:

                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def read_excel_file(file_path):

    try:

        # Read the Excel file using pandas

        df = pd.read_excel(file_path)

 
        column_e = df["Price"]
        column_e = column_e.apply(pd.to_numeric, errors='coerce').dropna()
         
        
        list_column_e = column_e.tolist()
        start_time = time.time()
        selection_sort(list_column_e)
        end_time = time.time()
 
        print("Data in Column E:")
        for value in list_column_e:
             print(value)    

        print(f"Time Taken to Sort data: {end_time - start_time: .6f} seconds.")



    except FileNotFoundError:

        print(f"File not found at path: {file_path}")

    except pd.errors.ParserError:

        print(f"Error parsing the file at path: {file_path}")

 

if __name__ == "__main__":

    file_path = r"C:\Users\schoo\Documents\TECHTORIUM !!!\2023\Term 3\Advanced Python\.vscode\DiamondValues(10000).xlsx"

    read_excel_file(file_path)