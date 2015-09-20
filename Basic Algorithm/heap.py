# HEAP

def max_heapify(alist, i, end):
	# parent = (i - 1) / 2
	left = i * 2 + 1
	right = i * 2 + 2
	if (left <= end and alist[left] > alist[i]):
		largest = left
	else:
		largest = i
	if (right <= end and alist[right] > alist[largest]):
		largest = right

	if largest != i:
		alist[i], alist[largest] = alist[largest], alist[i]
		max_heapify(alist, largest, end)


def build_max_heap(alist):
	for i in range(len(alist)/2 - 1, -1, -1):
		max_heapify(alist, i, len(alist) - 1)


def heap_sort(alist):
	build_max_heap(alist)
	end = len(alist) - 1
	for i in range(len(alist) - 1, 0, -1):
		alist[0], alist[i] = alist[i], alist[0]
		end -= 1
		max_heapify(alist, 0, end)


def heap_extract_max(alist):
    if len(alist) < 1:
    	exit  # 'list has no item'
    maxItem = alist[0]
    alist[0] = alist[len(alist) - 1]
    max_heapify(alist, 0, len(alist) - 1)
    alist.pop()

def heap_increase_key(alist, key, index):
	if key <= alist[index]:
		exit  # new key is not larger
	alist[index] = key
	while index > 0 and alist[(index - 1) / 2] < alist[index]:
		alist[index], alist[(index - 1) / 2] = alist[(index - 1) / 2], alist[index]
		index = (index - 1) / 2


def max_heap_insert(alist, key):
	alist.append(float('-Infinity'))
	heap_increase_key(alist, key, len(alist) - 1)


sample = [54,26,93,17,77,31,44,55,20]
print sample
build_max_heap(sample)
print sample
max_heap_insert(sample, 80)
print sample



