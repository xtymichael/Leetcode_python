
#Python program to print all permutations of a given string
#Below are the permutations of string ABC.
#ABC, ACB, BAC, BCA, CAB, CBA


def swap(a, i, j):
    a[i], a[j] = a[j], a[i]

def permute(a, i, n):
    if i == n:
        return a
    else:
        for j in range(i, n+1):
            swap(a, i, j)
            [a].append(permute(a, i+1, n))
            swap(a, i, j)  # backtrack

print permute(list('ABC'), 0, 2)
