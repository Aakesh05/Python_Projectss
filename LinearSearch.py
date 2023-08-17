
def linearSearch(array, n, x):
 
    for i in range(0, n):
        if (array[i] == x):
            return i
    return -1
 
 
array = [24, 41, 31, 11, 9]
x = 9
n = len(array)
result = linearSearch(array, n, x)
if(result == -1):
    print("Element not found")
else:
    print("Element is Present at Index: ", result)