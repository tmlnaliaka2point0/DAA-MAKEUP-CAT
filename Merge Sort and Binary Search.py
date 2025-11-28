import time
import random
import sys

# Increase recursion limit for deep recursion, necessary for large N in Merge Sort
sys.setrecursionlimit(2000) 

# MERGE SORT IMPLEMENTATION 
def merge_sort(arr):
    """Sorts an array using the Merge Sort algorithm (Divide and Conquer)."""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Recursive calls
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge step
    merged = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# BINARY SEARCH IMPLEMENTATION
def binary_search(sorted_arr, target):
    """Searches for a target in a sorted array using Binary Search."""
    low = 0
    high = len(sorted_arr) - 1
    
    while low <= high:
        # Use integer division for the midpoint index
        mid = (low + high) // 2
        
        if sorted_arr[mid] == target:
            return mid  # Target found, return index
        elif sorted_arr[mid] < target:
            low = mid + 1  # Search in the right half
        else:
            high = mid - 1 # Search in the left half
            
    return -1 # Target not found

# PERFORMANCE MEASUREMENT AND MAIN EXECUTION 
def measure_performance(n, target):
    """Generates an array of size n, measures sort/search time, and returns data."""
    # Generate random data (house numbers between 1 and 5000)
    data = [random.randint(1, 5000) for _ in range(n)]
    
    # 1. Measure Sorting Time
    start_time_sort = time.perf_counter()
    sorted_data = merge_sort(data.copy()) # Use a copy for clean measurement
    end_time_sort = time.perf_counter()
    sort_time = end_time_sort - start_time_sort
    
    # 2. Measure Searching Time
    # Ensure the target exists in the array for the most consistent measurement
    if target not in sorted_data:
        # If target isn't in the random list, replace a random element with the target
        sorted_data[random.randint(0, n - 1)] = target
        
    start_time_search = time.perf_counter()
    search_index = binary_search(sorted_data, target)
    end_time_search = time.perf_counter()
    search_time = end_time_search - start_time_search
    
    return data, sorted_data, search_index, sort_time, search_time

def main_demonstration():
    # Input Sample (at least 10 delivery points)
    INITIAL_ROUTE = [150, 42, 301, 5, 88, 205, 12, 99, 110, 350, 50, 420]
    TARGET_HOUSE = 110
    
    print("2. Coding & Implementation Demonstration")
    print(f"Input Route (n={len(INITIAL_ROUTE)}): {INITIAL_ROUTE}")
    print(f"Target House Number: {TARGET_HOUSE}")
    
    # Execute the sort and search on the sample data
    sorted_route = merge_sort(INITIAL_ROUTE.copy())
    search_index = binary_search(sorted_route, TARGET_HOUSE)
    
    print("\n[Output Snippets/Screenshots]")
    print(f"Sorted Route: {sorted_route}")
    
    if search_index != -1:
        print(f"Result: Target {TARGET_HOUSE} found at index {search_index}.")
    else:
        print(f"Result: Target {TARGET_HOUSE} not found.")

if __name__ == "__main__":
    main_demonstration()