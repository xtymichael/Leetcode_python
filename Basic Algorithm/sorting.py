# Sorting Algorithm 

# Insertion Sort
# Time: O(n^2)
# Space: O(1)
# pick each item insert to the right place
def insertionSort(alist):
    for i in range(1,len(alist)):
        cur = alist[i]
        pos = i
        while pos > 0 and alist[pos - 1] > cur:
            alist[pos] = alist[pos - 1]
            pos -= 1
        alist[pos] = cur
    return alist


# Bubble Sort
# Time: O(n^2)
# Space: O(1)
# exachange btw every two items
def BubbleSort(alist):
    for i in range(len(alist) - 1, 0, -1):
        for j in range(i):
            if alist[j] > alist[j + 1]:
                temp = alist[j]
                alist[j] = alist[j + 1]
                alist[j + 1] = temp
    return alist
    

# Selection Sort
# Time: O(n^2)
# Space: O(1)
# select the largest to put it in the last
def selectionSort(alist):
    for i in range(len(alist) - 1, 0, -1):
        maxIndex = 0
        for j in range(i + 1):
            if alist[j] > alist[maxIndex]:
                maxIndex = j
        alist[i], alist[maxIndex] = alist[maxIndex], alist[i]
    return alist


# Merge Sort
# Time: O(nlogn)
# Space: O(n)
# select the largest to put it in the last
def mergeSort(alist):
    if len(alist) < 2:
        return alist

    mid = len(alist) / 2

    left = alist[:mid]
    right = alist[mid:]

    mergeSort(left)
    mergeSort(right)

    l = r = 0
    for i in range(len(alist)):

        lval = left[l] if l < len(left) else None
        rval = right[r] if r < len(right) else None

        if (lval and rval and lval < rval) or rval is None:
            alist[i] = lval
            l += 1
        elif (lval and rval and lval >= rval) or lval is None:
            alist[i] = rval
            r += 1
    return alist


# Quick Sort
# Time: O(nlogn)
# Space: O(log(n))
# https://www.youtube.com/watch?v=MZaf_9IZCrc
def quickSort(alist, left, right):
    if left < right:
        q = partition(alist, left, right)
        quickSort(alist, left, q - 1)
        quickSort(alist, q + 1, right)
    return alist

def partition(alist, left, right):
    pivot = alist[right]
    i = left - 1
    for j in range(left, right):
        if alist[j] < pivot:
            i += 1
            alist[i], alist[j] = alist[j], alist[i]
    alist[i + 1], alist[right] = alist[right], alist[i + 1]
    return i + 1



sample = [54,26,93,17,77,31,44,55,20]
#print insertionSort(sample)
#print BubbleSort(sample)
#print selectionSort(sample)
#print mergeSort(sample)
print quickSort(sample, 0, len(sample) - 1)
