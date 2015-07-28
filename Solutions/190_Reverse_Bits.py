class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
    	result = 0
    	r = [0] * 32
    	j = 31

    	# n to binary ---> r
        while n >= 1:
        	r[j] = n % 2
        	n /= 2
        	j -= 1

        # r binary to decimal ----> result
        for i in range(32):
        	result += r[i] * (2 ** i)

        	
        return result
