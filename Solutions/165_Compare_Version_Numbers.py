class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
	    f1 = map(lambda x: int(x) ,version1.split('.'))
	    f2 = map(lambda x: int(x) ,version2.split('.'))
	    f1 += [0]*(len(f2)-len(f1))
	    f2 += [0]*(len(f1)-len(f2))
	    return 1 if f1 > f2 else (-1 if f1 < f2 else 0)