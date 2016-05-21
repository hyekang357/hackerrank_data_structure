#!/bin/python

import sys


arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)

# arr.append([1,1,1,0,0,0])
# arr.append([0,1,0,0,0,0])
# arr.append([1,1,1,0,0,0])
# arr.append([0,0,2,4,4,0])
# arr.append([0,0,0,2,0,0])
# arr.append([0,0,1,2,4,0])

largest_sum = -1000

for row in range(1,5):
	for col in range(1,5):

		top_left = arr[row-1][col-1]
		top_center = arr[row-1][col]
		top_right = arr[row-1][col+1]
		center = arr[row][col]
		bottom_left = arr[row+1][col-1]
		bottom_center = arr[row+1][col]
		bottom_right = arr[row+1][col+1]

		hour_glass_sum = top_left + top_center + top_right + center + bottom_left + bottom_center + bottom_right

		if hour_glass_sum > largest_sum:
			largest_sum = hour_glass_sum


print largest_sum



