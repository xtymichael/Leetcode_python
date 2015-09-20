# three-way quicksort
def quicksort(alist, left, right):
	if left < right:
		lo, hi = partition(alist, left, right)
		quicksort(alist, left, lo - 1)
		quicksort(alist, hi + 1, right)


def partition(alist, left, right):
	pivot = alist[left]
	i = l = left
	r = right
	while i <= r:
		if alist[i] < pivot:
			l += 1
			i += 1
			alist[i], alist[l] = alist[l], alist[i]
		elif alist[i] > pivot:
			r -= 1
			alist[i], alist[r] = alist[r], alist[i]
		else:
			i += 1
	return l, r



sample = [54,26,93,17,77,31,44,55,20]
quicksort(sample, 0, len(sample))
print sample



# # quick sort, in-place 3-way partition
# # David Eppstein, UCI, 17 Jan 2002

# import random
# R = random.Random(42)

# def qsort(L):
# 	quicksort(L,0,len(L))

# def quicksort(L,start,stop):
# 	if stop - start < 2: return
# 	key = L[R.randrange(start,stop)]
# 	e = u = start
# 	g = stop
# 	while u < g:
# 		if L[u] < key:
# 			swap(L,u,e)
# 			e = e + 1
# 			u = u + 1
# 		elif L[u] == key:
# 			u = u + 1
# 		else:
# 			g = g - 1
# 			swap(L,u,g)
# 	quicksort(L,start,e)
# 	quicksort(L,g,stop)

# def swap(A,i,j):
# 	temp = A[i]
# 	A[i] = A[j]
# 	A[j] = temp

# L = [3,1,4,1,5,9,2,6,5,3,5,8,9,7,9]
# qsort(L)
# print Lb