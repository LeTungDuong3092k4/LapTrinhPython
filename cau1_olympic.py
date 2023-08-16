#cau1_Đọc dãy số cho file, sau đó sắp xếp tăng dần, tính thời gian chạy của chương trình
import time

def read_array():
    with open("dayso.txt", "r") as f:
        array = f.read().split()
    array = list(map(int, array))
    return array

def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result+=left[i:]
    result+=right[j:]
    return result

def calculate_time(define, array):
    start = time.time()
    define(array)
    end = time.time()
    return end - start

dayso = read_array()
print("Day so sau khi sap xep:", merge_sort(dayso))
print(f"Chay het {calculate_time(merge_sort, dayso)} giay")