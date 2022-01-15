"""
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

 

Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explanation: 
- index 0 --> the greatest element to the right of index 0 is index 1 (18).
- index 1 --> the greatest element to the right of index 1 is index 4 (6).
- index 2 --> the greatest element to the right of index 2 is index 4 (6).
- index 3 --> the greatest element to the right of index 3 is index 4 (6).
- index 4 --> the greatest element to the right of index 4 is index 5 (1).
- index 5 --> there are no elements to the right of index 5, so we put -1.
Example 2:

Input: arr = [400]
Output: [-1]
Explanation: There are no elements to the right of index 0.

"""

from typing import List

# bruteforce
# t = O(n^2)
# s = O(n)

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)+1):
            remaining_array = arr[i:] # slice array to remain with other elements from the current index element
            new_array = remaining_array[1:] # slice the elements to remove the first one to avoid returning current element in max
            max_num = 0
            
            if new_array:
                max_num = max(new_array)
            if i == len(arr): # if we've reached end of list...
                arr[len(arr)-1] = -1 # replace last element with -1
            else:
                arr[i] = max_num # replace other elements with the maximum number
        
        return arr

# optimal solution
# t = O(n)
# s = O(n)

class Solution2:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right_max = -1

        for i in range(len(arr) - 1, -1, -1): # loop in reverse from the last element
            new_max = max(arr[i], right_max)
            arr[i] = right_max
            right_max = new_max

        return arr


arr = [400]
solution = Solution2()
print(solution.replaceElements(arr))

