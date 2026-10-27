
seat_numbers = [100, 105, 112, 120, 125, 130, 135, 142, 150]
input("List: " + str(seat_numbers) + f" n={len(seat_numbers)} Press Enter")

target = 130

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    steps = 0
    while low <= high:
        mid = (low + high) // 2  
        steps += 1
        print("round", steps, "-> checked", arr[mid])
        if arr[mid] == target:
            return mid, steps
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, steps

def recursive_binary_search(arr, target, low, high, steps=0):
    if low > high:
        return -1, steps
    
    mid = (low + high) // 2
    steps += 1
    print("round", steps, "-> checked", arr[mid])
    if arr[mid] == target:
        return mid, steps
    elif arr[mid] < target:
        return recursive_binary_search(arr, target, mid + 1, high, steps)
    else:
        return recursive_binary_search(arr, target, low, mid - 1, steps)

print(f"\n--- Testing Iterative Binary Search for Target: {target} ---")
idx, total_steps = binary_search(seat_numbers, target)
print("found", target, "at position", idx + 1, "in", total_steps, "steps -> O(log n)")

print("Iterative binary search takes O(log n) time and O(1) space because it uses a fixed number of variables.")
input("Press Enter to continue...")



