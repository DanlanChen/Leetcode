def find_target_in_2sum(arr, target):
    arr = sorted(arr)
    if len(arr) == 0:
        return 1
    i = 0 
    j = len(arr) - 1
    rst = 1
    while i<j:
        print(i, j)
        if arr[i] + arr[j] > target:
            j = j -1
        if arr[i] + arr[j] <= target:
            rst += j - i
            i += 1
    return rst
arr = [1, 2, 3]
target = 6
two_sum = find_target_in_2sum(arr, target)

print(two_sum)

