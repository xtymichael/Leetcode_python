class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        period = 2 * (numRows - 1)
        lines = ['' for i in range(numRows)]
        for i in range((len(s) - 1) / period + 1):
            for j in range(period):
                cur = i * period + j
                if cur <= len(s) - 1:
                    reminder = cur % period
                    if reminder >= numRows:
                        reminder = period - reminder
                    lines[reminder] += s[cur]
        return ''.join(lines)




##########################################################
def convert(self, s, nRows):
    if nRows==1:
        return s
    period= 2*(nRows -1)
    lines=["" for i in range(nRows)]
    d={} # dict remainder:line
    for i in xrange(period):
        if i<nRows:
            d[i]=i
        else:
            d[i]=period-i

    for i in xrange(len(s)):
        lines[ d[i%period] ] +=s[i]

    return "".join(lines)