import random, time


def quick_sort(array): 
    if len(array) <= 1: return array

    pivot = array[0]
    less, equal, greater = [], [], []
    for item in array:  # for items less then pivot 
        if item < pivot: less.append(item)
    for item in array:  # for items equal pivot 
        if item == pivot: equal.append(item)
    for item in array:  # for items greater then pivot 
        if item > pivot: greater.append(item)
    return quick_sort(greater) + equal + quick_sort(less) 
  

MIN, MAX, N = 0, 10, 10  # min and  max of integers, number of integers
random_ints = [random.randint(MIN, MAX + 1) for i in range(N)]
print('Before: {}'.format(random_ints))

start = time.perf_counter()
sorted_array_1 = quick_sort(random_ints)
sort_time_1 = time.perf_counter() - start
print('After (own function = {0:.7f}): {1}'.format(sort_time_1, sorted_array_1))

start = time.perf_counter()
sorted_array_2 = sorted(random_ints, reverse=True)
sort_time_2 = time.perf_counter() - start
print('After (build-in function = {0:.7f}): {1}'.format(sort_time_2, sorted_array_2))
