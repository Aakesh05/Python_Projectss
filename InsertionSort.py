def insertionSort(arr):
    for i in range (1, len(arr)):

        key = arr[i]

        j = i-1
        while j >= 0 and key < arr[i]:
                arr[j + 1] = arr[i]
                j -= 1
        arr[j + 1] = key


arr = [12, 2, 34, 22, 78, 54]
insertionSort(arr)
for i in range (len(arr)):
     print ("% d" % arr[i])