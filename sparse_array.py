
import sys

N = int(raw_input())

arr_str = []
for arr_i in xrange(N):
    arr_str.append(raw_input().strip())

Q = int(raw_input())
for query_i in xrange(Q):

	counter = 0
	query = raw_input().strip()
	for each_str in arr_str:
		if query == each_str:
			counter += 1

	print counter