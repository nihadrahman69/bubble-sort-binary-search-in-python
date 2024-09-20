def printarray(array, x):
    for i in range(x):
        print(arr[i], end="\t")


def swapped(x, y, array):
    temp = array[x]
    array[x] = array[y]
    array[y] = temp


def bubblesort(array, x):
    for i in range(x):
        swap = 0
        for j in range(x-i-1):
            if array[j] > array[j+1]:
                swap = 1
                swapped(j, j+1, array)
        if swap == 0:
            break


def binsearch(array, low, high, a):
    while low <= high:
        mid = low+(high-low)//2
        if array[mid] == a:
            return mid
        if array[mid] > a:
            high = mid - 1
        else:
            low = mid + 1
    return -1


arr = [5, 8, 2, 7, 4, 9, 1, 3, 6]
n = len(arr)

print("Enter array elements: ")
printarray(arr, n)
print()

print("Sorted array: ")
bubblesort(arr, n)
printarray(arr, n)
print()

x = int(input("Enter the element you want to find: "))
result = binsearch(arr, 0, n-1, x)

if result == -1:
    print("Value not found.")
else:
    print(f"Value found at index {result}!")


