
# Exercise 1: Emergency Dispatch Record Search

LAST_NAME = "Aldovino"
STUDENT_ID = "TUMP-26-4168"
FAVORITE_ARTIST = "Taylor Swift"

SEED_DIGIT = 8
ID_SUM = 27
NAME_LENGTH = 8
ARTIST_LENGTH = 11
ARTIST_SUM = 168

# Generate unique incident records
size = 10
original = sorted({
    (ID_SUM * 10 + i * 7 + ARTIST_SUM) % 997
    for i in range(size)
})

# Rotate records using the seed digit
rotation = SEED_DIGIT % len(original)
rotated = original[rotation:] + original[:rotation]

# Target incident generated from student-specific inputs
target = (ID_SUM * 10 + ARTIST_SUM) % 997

def linear_search(data, target):
    comparisons = 0

    for i, value in enumerate(data):
        comparisons += 1
        if value == target:
            return i, comparisons

    return -1, comparisons

def rotated_binary_search(data, target):
    left = 0
    right = len(data) - 1
    comparisons = 0

    while left <= right:
        mid = (left + right) // 2
        comparisons += 1

        if data[mid] == target:
            return mid, comparisons

        if data[left] <= data[mid]:
            if data[left] <= target < data[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if data[mid] < target <= data[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1, comparisons

linear_index, linear_count = linear_search(rotated, target)
search_index, search_count = rotated_binary_search(rotated, target)

print("=== Emergency Dispatch Record Search ===")
print("Last Name:", LAST_NAME)
print("Student ID:", STUDENT_ID)
print("Seed Digit:", SEED_DIGIT)
print("ID Sum:", ID_SUM)
print("Artist Sum:", ARTIST_SUM)
print("Original Dataset:", original)
print("Rotated Dataset:", rotated)
print("Target Incident:", target)
print("Rotated Search Index:", search_index)
print("Rotated Search Comparisons:", search_count)
print("Linear Search Index:", linear_index)
print("Linear Search Comparisons:", linear_count)
print("Time Complexity: O(log n) average, O(n) worst case")
print("Auxiliary Space Complexity: O(1)")