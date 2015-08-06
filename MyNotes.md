# Python Note Taking:


## Rotate Image Different Solutions:
[Link](https://leetcode.com/discuss/38426/seven-short-solutions-1-to-7-lines)

```python
class Solution:
    def rotate(self, A):
        A[:] = zip(*A[::-1])
```