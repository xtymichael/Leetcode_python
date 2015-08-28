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
>> [4, 3, 2, 1]

b = [[1,2],[3,4]]
print b[::-1]
>> [[3, 4], [1, 2]]
```

```python
maxInt = 2 ** 31 -1
minInt = -2 ** 31
```

```python
d = dict()
d.pop(somekey, None) #remove key from dict

d.keys() # [key1, key2, ...] all keys of a dict
```

```python
(set(range(11)) - set(range(10))).pop()

>> 10
```
[More about sets](https://docs.python.org/2/library/sets.html)


```python
num = ['99', '200','93']
num.sort(lambda x, y: cmp(y+x, x+y))

>> num = ['99', '93', '200']
>> ''.join(num).lstrip('0') or '0'
# join ---->  9993200
# lstrip ----> get rid of all 00000 prefix  (avoid ['0', '0'])
# or '0'  -----> '' or '0' = '0'
```

```python
>>> mylist = ['a', 'b', 'c', 'd']
>>> [item for item in enumerate(mylist)]
[(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]
```

### Stacks & Queue
Stacks: LIFO: Last in, first out
Queue: FIFO: First in, first out
### Stacks
Push: add item to top of the stacks 
Pop: remove item from top of the stacks
peek: return top item without removing
### Queue
enqueue:add item to the back of the queue
dequeue:remove item from front of the queue
peek: return front item
### Linked List
next prev
singly linked — omit the prev
insert in the head
### Binary Search Tree
left sub smaller or eq
right sub bigger