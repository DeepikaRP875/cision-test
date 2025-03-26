# 7.	Intersection of Sorted Arrays
# Write a function in a Object Orientated Programming language of your choice that takes two sorted arrays of integers as input and returns an array containing numbers common to both arrays without duplicates.

#This code defines a class ArrayIntersection with a method find_intersection that finds the intersection of two sorted arrays using a two-pointer technique to ensure the result contains unique common elements.

class ArrayIntersection:
    def find_intersection(self, arr1, arr2):
        if not arr1 or not arr2:
            return []

        result = []
        i = 0
        j = 0

        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                i += 1
            elif arr1[i] > arr2[j]:
                j += 1
            else:
                if not result or result[-1] != arr1[i]:
                    result.append(arr1[i])
                i += 1
                j += 1

        return result
    

#This function get_sorted_array_input prompts the user to enter a comma-separated list of sorted integers, validates the input to ensure it is sorted, and returns the array if valid, otherwise it prompts the user again.

def get_sorted_array_input():

    while True:
        try:
            input_str = input("Enter a comma-separated list of sorted integers: ")
            arr = [int(x.strip()) for x in input_str.split(",")]
            if all(arr[i] <= arr[i+1] for i in range(len(arr) - 1)) or len(arr) <= 1:
                return arr
            else:
                print("Array is not sorted. Please enter a sorted array.")
        except ValueError:
            print("Invalid input. Please enter integers only, separated by commas.")
        except IndexError:
            return []
        

#The user should input two arrays of integers,  Each array must be sorted, either in ascending or descending order, Both arrays should have the same number of elements.

if __name__ == "__main__":
    intersection_finder = ArrayIntersection()

    print("Enter the first sorted array:")
    arr1 = get_sorted_array_input()

    print("Enter the second sorted array:")
    arr2 = get_sorted_array_input()

    intersection = intersection_finder.find_intersection(arr1, arr2)
    print(f"Intersection: {intersection}")