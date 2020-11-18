from typing import List

def count_inconsecutive_number(arr:List[int]):
	if len(arr) <= 2:
		return 0
	rst = 0
	diff = arr[1]-arr[0]
	for i in range(1, len(arr) - 1):
		new_diff = arr[i+1] - arr[i]
		if new_diff == 0:
			continue
		if new_diff*diff < 0:
			rst += 1
		diff = new_diff
	return rst

if __name__ == '__main__':
	arr=[0, 1, 1, 0]
	arr2 =[0, 1, 0]
	arr3 = [1,1,1,2,1,3]
	print(count_inconsecutive_number(arr3))
