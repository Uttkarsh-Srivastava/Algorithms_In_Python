''' 
Implementation Of Insertion Sort in Python
Purpose : Sorting elements in ascending order
Author  : Utkarsh Srivastava
Date    : 4/09/2018
'''


def Sort(array):
    for i in range(0, len(array)):
        for j in range(i - 1, -1, -1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

    return array


def main():
    unsorted_array = [int(x)
                      for x in input("Enter Array to be Sorted ").split()]
    sorted_array = Sort(unsorted_array)
    print ("Sorted array is : ", sorted_array)


main()
