class Solution:
    # @param s : A string
    # @return : A string
    def reverseWords(self, s):
        # write your code here
        if len(s) == 0 or len(s) == 1:
            return s
        s = s.strip()   # important ,delete leading or trailing spaces in a string
        s = s.split(' ')
        if len(s) == 1:
            return s[0]
        if s[0] == ' ' or s[len(s) - 1] == ' ':
            print s
        i, j = 0, len(s) - 1
        while i < j:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i = i + 1
            j = j - 1
        s = ' '.join(s)
        return s