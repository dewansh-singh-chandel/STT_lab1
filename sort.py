"""
Module Name: sort.py
Description: A module to demonstrate a simple sorting algorithm.
"""

# Original array to sort
arr = [1, 3, 2, 0, 7, 8, 6]


def sort_array(input_arr):
    """
    Sorts an array in ascending order using a simple sorting algorithm.

    Args:
        input_arr (list): The list of integers to sort.

    Returns:
        list: A sorted copy of the input list.
    """
    s_arr = input_arr.copy()
    for i, _ in enumerate(s_arr):
        for j in range(i + 1, len(s_arr)):
            if s_arr[i] > s_arr[j]:
                s_arr[i], s_arr[j] = s_arr[j], s_arr[i]
    return s_arr


if __name__ == "__main__":
    sorted_arr = sort_array(arr)

    print("Original array:", arr)
    print("Sorted array:", sorted_arr)
