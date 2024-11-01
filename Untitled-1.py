def bubbleSort(arr):
    for i in range (len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j + 1] = arr[j]
        
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
    sorted_Arr = insertion_Sort(arr)
    print("Sorted array is:", sorted_Arr)

main()





