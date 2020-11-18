#https://www.youtube.com/watch?v=3IFxpozBs2I

from typing import List

def get_prefix_table(pattern:List[str]):
    n = len(pattern)
    prefix = [0] * n
    i = 1
    len_i = 0
    while i < n:
        if pattern[i] == pattern[len_i]:
            len_i += 1
            prefix[i] = len_i
            i += 1

        else:
            if len_i > 0 :
                len_i = prefix[len_i-1]
            else:
                prefix[i] = len_i
                i += 1
    return prefix

def move_prefix_table(prefix):
    n = len(prefix)
    i = n - 1
    while i >0:
        prefix[i] = prefix[i-1]
        i -= 1

    prefix[0] = -1
    return prefix

def kmp_search(text:List[str], pattern:List[str]):
    prefix = get_prefix_table(pattern)
    print(prefix)

    prefix = move_prefix_table(prefix)
    print(prefix)
    n = len(pattern)
    m = len(text)
    i = 0
    j = 0
    rst = []
    # text[i], len(text) = m
    # pattern[j] , len(pattern) = n
    while i < m:

        if (j == n -1)  and (text[i] == pattern[j]):
            print(i, j)
            rst.append(i-j)
            j = prefix[j]
        if text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            j = prefix[j]
            if j == -1:
                j += 1
                i += 1
    return rst

pattern = "ABABCABAA"
text = "ABABABCABAABABABABABCABAACA"
rst = kmp_search(text, pattern)
print(rst)

