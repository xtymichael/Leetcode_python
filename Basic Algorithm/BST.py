# BINARY SEARCH TREE


# Binary Search
# Interrative 
def binarySearch(alist, target):
	first = 0
	last = len(alist) - 1
	while first <= last:
		mid = (first + last) / 2
		if alist[mid] == target:
			return mid
		elif alist[mid] > target:
			last = mid - 1
		else:
			first = mid + 1
	return None

# Recursive
def binarySearch_recrsion(alist, target, first, last):
	if len(alist) == 0:
		return None
	mid = (first + last) / 2
	if alist[mid] == target:
		return mid
	elif alist[mid] > target:
		return binarySearch_recrsion(alist, target, first, mid - 1)
	else:
		return binarySearch_recrsion(alist, target, mid + 1, last)




sample = [17, 20, 26, 31, 44, 54, 55, 77, 93]
print binarySearch(sample, 54)
print binarySearch_recrsion(sample, 93, 0, len(sample))




