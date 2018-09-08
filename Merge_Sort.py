'''
Implementation Of Merge Sort in Python
Purpose : Sorting elements in ascending order
Author  : Utkarsh Srivastava
Date    : 4/09/2018
'''


def Merge_Sort(array):
    if len(array) <= 1:
        return array

    half = len(array)//2
    L = Merge_Sort(array[:half])
    R = Merge_Sort(array[half:])

    return Merge(L, R)


def Merge(L, R):
    merged_array = []
    i = j = 0
    while (i < len(L) and j < len(R)):
        if (L[i] <= R[j]):
            merged_array.append(L[i])
            i += 1

        else:
            merged_array.append(R[j])
            j += 1

    merged_array += L[i:]
    merged_array += R[j:]

    return merged_array


def main():
    unsorted_array = [int(x)
                      for x in input("Enter Array to be Sorted ").split()]
    sorted_array = Merge_Sort(unsorted_array)
    print ("Sorted array is : ", sorted_array)


main()
