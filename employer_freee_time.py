from typing import List
def free_time(intervals:List[List[List]]) ->List[List]:
    intervals = get_flat_interval(intervals)
    intervals = sorted(intervals, key = lambda interval:interval[0])
    # merged_intervals = merge(intervals)
    free_time = get_free_time(intervals)
    return free_time

def get_flat_interval(intervals):
    new_intervals = []
    for interval in intervals:
        new_intervals += interval
    return new_intervals

# def merge(intervals):
#     curr_interval = intervals[0]
#     merged = []
#     for i in range(1, len(intervals)):
#         interval = intervals[i]
#         # print(interval)
#         if interval[0] > curr_interval[1]:
#             merged.append(curr_interval)
#             curr_interval = interval
#         else:
#             # print(curr_interval)
#             curr_interval[1] = max(curr_interval[1], interval[1])
#     merged.append(curr_interval)
#     return merged

# def get_free_time(intervals):
#     free_time = []
#     for i in range(len(intervals) - 1):
#         start = intervals[i][1]
#         end = intervals[i + 1][0]
#         free_time.append([start, end])
#     return free_time

def get_free_time(intervals):
    curr_interval = intervals[0]
    rst = []
    for i in range(1, len(intervals)):
        interval = intervals[i]
        if curr_interval[1] < interval[0]:
            rst.append([curr_interval[1], interval[0]])
            curr_interval = interval
        else:
            curr_interval[1] = max(curr_interval[1], interval[1])
    return rst

schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
print(free_time(schedule))

schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
print(free_time(schedule))
