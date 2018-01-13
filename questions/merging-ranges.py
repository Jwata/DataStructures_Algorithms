#!/usr/bin/env python

def merge_meetings(meetings):

    # O(n log(n))
    sorted_meetings = sorted(meetings)

    merged_meetings = [sorted_meetings[0]]
    for current_start, current_end in sorted_meetings[1:]:

        previous_start, previous_end = merged_meetings[-1]

        if previous_end >= current_start:
            # merge
            merged_meeting = (previous_start, max(previous_end, current_end))
            merged_meetings[-1] = merged_meeting
        else:
            # append
            merged_meetings.append((current_start, current_end))

    return merged_meetings


meetings = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
merged = merge_meetings(meetings)
print(merged) # should be [(0, 1), (3, 8), (9, 12)]

meetings = [(1, 2), (2, 3)]
merged = merge_meetings(meetings)
print(merged) # should be [(1, 3)]

meetings = [(1, 5), (2, 3)]
merged = merge_meetings(meetings)
print(merged) # should be [(1, 5)]

meetings = [(1, 10), (2, 6), (3, 5), (7, 9)]
merged = merge_meetings(meetings)
print(merged) # should be [(1, 10)]
