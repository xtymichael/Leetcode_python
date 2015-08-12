# Python Note Taking

```python
#zip example
>>> x = [1, 2, 3]
>>> y = [4, 5, 6]
>>> zipped = zip(x, y)
>>> zipped
[(1, 4), (2, 5), (3, 6)]
>>> x2, y2 = zip(*zipped)
>>> x == list(x2) and y == list(y2)
True
```


```python
#map example
result = map(lambda x: x * x, [1, 2, 3])
reuslt = [1, 4, 9]

#filter example
result = filter(lambda x: x > 0, [-2, -1, 0, 1, 2])
reuslt = [1, 2]

#reduce example
result = reduce(lambda x, y: x + y, [1, 2, 3, 4])
result = 10
```

```python
a = [1, 2, 3, 4]
print a[::-1]

b = [[1,2],[3,4]]
print b[::-1]
>> [4, 3, 2, 1]
```

```python
maxInt = 2 ** 31 -1
minInt = -2 ** 31
```


