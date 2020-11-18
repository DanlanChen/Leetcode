#pinterest

def find_target_in_2sum(arr, target):
    arr = sorted(arr)
    if len(arr) == 0:
        return 1
    two_sum = set()
    for i in range(len(arr) - 1):
        for j in range(i, len(arr)):
            two_sum.add(arr[i] + arr[j])
    two_sum = sorted(list(two_sum), reverse=True)
    for i in range(len(two_sum)):
        if two_sum[i] <= target:
            return i+1
        else:
            continue
    return len(two_sum) + 1
arr = [1, 3, 3]
target = 1
two_sum = find_target_in_2sum(arr, target)

print(two_sum)

