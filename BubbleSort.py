def bubblesort(elements):
	swapped = False
	for n in range(len(elements)-1, 0, -1):
		for i in range(n):
			if elements[i] > elements[i + 1]:
				swapped = True
				elements[i], elements[i + 1] = elements[i + 1], elements[i]
				if not swapped:
					return
				
elements = [132, 34, 6, 343, 85, 974, 2, 32, 11, 10, 47, 102]

print("Unsorted List is: ")
print(elements)
bubblesort(elements)
print("Sorted List is: ")
print(elements)
bubblesort(elements)
				
				

