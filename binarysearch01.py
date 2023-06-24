import random
import time

# Implementation of Binary Search

# It is remarkably faster than the Linear Search Method


# First, lets define what a "naive search" or Linear Search is. 
# Is it the process of scanning through an entire list(for example) and ask if its equal to the target
# If it is, return the index. If it is not, return False.
def naive_search(l, target):

    for i in range(len(l)):
        if l[i] == target:
            return i
    
    return print("Target does not exist in the list")

# ----------------------------------------------------------------------------------------#
# Here is a BINARY SEARCH
# Binary search uses divide and conquer!
# We need to take advantage of the fact that the list provided to us is sorted
# Return -1 if the target doesn't exist in the list

def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if high < low:
        return -1

    # Example l = [1, 3, 5, 10, 12]  
    midpoint = (low + high) // 2

    if l[midpoint] == target:
        return midpoint    
    elif target < l[midpoint]:
        return binary_search(l, target, low=low, high= midpoint-1)    
    else: 
        # target > l[midpoint]
        return binary_search(l, target, low= midpoint+1, high=high)


# Testing both the methods. Both return index 3 as they should.
if __name__ == '__main__':
    l =[1, 3, 5, 10, 12]
    target = 10
    print(naive_search(l, target))
    print(binary_search(l, target))

    # Testing time complexity

    length = 10000
    # Building a sorted list of length 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-5*length, 5*length))
    sorted_list = sorted(list(sorted_list))

    # Testing time for each iteration of naive_search (Linear Search)
    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)        
    end = time.time()
    print(f"Naive search time: {(end-start)/length} seconds")

    # Testing time for each iteration of BINARY SEARCH
    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)        
    end = time.time()
    print(f"Binary search time: {(end-start)/length} seconds")

    # Output:
    #   Naive search time: 0.00012140653133392333 seconds 
    #   Binary search time: 1.9008398056030273e-06 seconds

    # Lesson learnt: If you ever have to search a huge sorted list,  
    # NEVER search every single item!
