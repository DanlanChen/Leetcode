class Solution:
    # @param s: a list of char
    # @param offset: an integer 
    # @return: nothing
    def rotateString(self, s, offset):
	    # write you code here
        if len(s) == 0 or len(s) == 1:
            return s
        offset = offset % len(s)
        self.reverse(s, 0, len(s) - offset -1)
        self.reverse(s, len(s) - offset, len(s) - 1)
        self.reverse(s, 0, len(s) - 1)
    def reverse(self, s, start, end):
        i = start
        j = end
        while i < j:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i = i + 1
            j = j - 1
        # print s
        return s