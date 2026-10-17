
# Exercise 3: E-Commerce Order Processing

import time

LAST_NAME = "Aldovino"
STUDENT_ID = "TUMP-26-4168"
SEED_DIGIT = 8
ID_SUM = 27
NAME_LENGTH = 8
ARTIST_LENGTH = 11
ARTIST_SUM = 168

SIZE = 20

# Generate the same order numbers for all input conditions
base_orders = [
    (ID_SUM * 10 + ARTIST_SUM + i * SEED_DIGIT) % 997
    for i in range(SIZE)
]

# Ensure unique order numbers
base_orders = sorted(set(base_orders))

sorted_orders = base_orders.copy()
reverse_orders = base_orders[::-1]

random_orders = base_orders.copy()
random_orders.sort(
    key=lambda x: (x * SEED_DIGIT + ARTIST_SUM) % 997
)

def bubble_sort(data):
    arr = data.copy()
    comparisons = 0
    movements = 0

    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            comparisons += 1

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                movements += 3

    return arr, comparisons, movements

def selection_sort(data):
    arr = data.copy()
    comparisons = 0
    movements = 0

    for i in range(len(arr)):
        min_index = i

        for j in range(i + 1, len(arr)):
            comparisons += 1

            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            movements += 3

    return arr, comparisons, movements

def insertion_sort(data):
    arr = data.copy()
    comparisons = 0
    movements = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0:
            comparisons += 1

            if arr[j] > key:
                arr[j + 1] = arr[j]
                movements += 1
                j -= 1
            else:
                break

        arr[j + 1] = key
        movements += 1

    return arr, comparisons, movements

algorithms = [
    ("Bubble Sort", bubble_sort),
    ("Selection Sort", selection_sort),
    ("Insertion Sort", insertion_sort)
]

conditions = [
    ("Sorted", sorted_orders),
    ("Reverse", reverse_orders),
    ("Random", random_orders)
]

print("=== E-Commerce Order Processing ===")
print("Last Name:", LAST_NAME)
print("Student ID:", STUDENT_ID)
print("Dataset Size:", len(base_orders))

for condition_name, orders in conditions:
    print(f"\n--- {condition_name} Input ---")
    print("Input Orders:", orders)

    for name, algorithm in algorithms:
        start = time.perf_counter()
        result, comparisons, movements = algorithm(orders)
        elapsed = time.perf_counter() - start

        print(f"\n{name}")
        print("Sorted Output:", result)
        print("Comparisons:", comparisons)
        print("Movements:", movements)
        print(f"Execution Time: {elapsed:.8f} s")
        print("Sorting Verified:", result == sorted(orders))

print("\nBig O Analysis:")
print("Bubble Sort: Best O(n) with optimization; otherwise O(n^2)")
print("Selection Sort: Best, Average, Worst O(n^2)")
print("Insertion Sort: Best O(n); Average and Worst O(n^2)")
print("Auxiliary Space: O(1) for all three algorithms")
