class Solution:
    def strStr(self, source, target):
        # write your code here
        if  source is not None and target is not None:
            if len(source) >= len(target) :
                if len(target) == 0:
                    return 0
                for i in range(len(source)):
                #   print source[i : i +len(target)]
                  if source[i: i + len(target)] == target:
                       return i
        return -1