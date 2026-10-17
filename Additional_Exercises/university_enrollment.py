
# Exercise 2: University Enrollment Records

LAST_NAME = "Aldovino"
STUDENT_ID = "TUMP-26-4168"
SEED_DIGIT = 8
ID_SUM = 27
NAME_LENGTH = 8
ARTIST_LENGTH = 11
ARTIST_SUM = 168

# Generate two ascending enrollment datasets
dataset_a = sorted([
    (SEED_DIGIT * 100 + ID_SUM * 3 + i * 11) % 1000
    for i in range(10)
])

dataset_b = sorted([
    (ARTIST_LENGTH * 20 + NAME_LENGTH * 5 + i * 13) % 1000
    for i in range(10)
])

def merge_sorted(a, b):
    i = 0
    j = 0
    merged = []
    comparisons = 0

    while i < len(a) and j < len(b):
        comparisons += 1

        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1

    # Append remaining records
    merged.extend(a[i:])
    merged.extend(b[j:])

    return merged, comparisons

consolidated, comparisons = merge_sorted(dataset_a, dataset_b)

print("=== University Enrollment Records ===")
print("Last Name:", LAST_NAME)
print("Student ID:", STUDENT_ID)
print("Dataset A:", dataset_a)
print("Dataset B:", dataset_b)
print("Consolidated Dataset:", consolidated)
print("Records in Dataset A:", len(dataset_a))
print("Records in Dataset B:", len(dataset_b))
print("Records After Consolidation:", len(consolidated))
print("Comparisons:", comparisons)
print("Sorted Correctly:", consolidated == sorted(consolidated))
print("Record Count Verified:",
      len(consolidated) == len(dataset_a) + len(dataset_b))
print("Time Complexity: O(n + m)")
print("Auxiliary Space Complexity: O(n + m)")
