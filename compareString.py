class Solution:
    """
    @param A : A string includes Upper Case letters
    @param B : A string includes Upper Case letters
    @return :  if string A contains all of the characters in B return True else return False
    """
    def compareStrings(self, A, B):
        cnt = dict()
        for i in A:
            if i in cnt.keys():
                cnt[i] += 1
            else:
                cnt[i] = 1
        for j in B:
            if j in cnt.keys():
                cnt[j] -= 1
            else:
                cnt[j] = -1
            if cnt[j] < 0:
                return False
        return True