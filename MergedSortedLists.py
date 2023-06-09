lists = [[1,4,5],[1,3,4],[2,6]]
flat = []
for list in lists:
    for i in list:
        flat.append(i)
flat.sort()
print(flat)

# 2) Mergek Sorted Lists
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.

# Example1:
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output:[1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6

# Example2:
# Input: lists= []
# Output: []

# Example3:
# Input: lists = [[]]
# Output: []


# Constraints:
# k == lists.length
# 0 <= k <= 104
# 0 <= lists[i].length <= 500
# -104 <= lists[i][j] <= 104
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 104.