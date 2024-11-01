def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
            arr[min_index], arr[i] = arr[i], arr[min_index]

    return arr




def bubbleSort(arr):
    for i in range (len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        
    return arr




def insertion_Sort(arr):
    n = len(arr)
    for i in range(1, n):
        itemToInsert = arr[i]
        position = i
        while position > 0 and arr[position - 1] > itemToInsert:
            arr[position] = arr[position - 1]
            position -= 1
            
        arr[position] = itemToInsert

    return arr


def main():
    arr = [2, 1, 3, 0]
    print("Unsorted arr is", arr)
    sorted_Arr = selectionSort(arr)
    print("Sorted array is:", sorted_Arr)

main()





