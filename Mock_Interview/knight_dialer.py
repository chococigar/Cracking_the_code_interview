pos_dic = {0:[4, 6], 1: [6, 8], 2:[7, 9], 3:[4,8], 4:[3, 9, 0], 5:[], 6:[1, 7, 0], 7:[2, 6], 8:[1, 3], 9:[2, 4]}

def count_num(len_num, start_num):
	if len_num <= 1:
		return len_num

	cur_branches = [0 for x in range(10)]
	prev_branches = [0 for x in range(10)]

	cur_branches[start_num] = 1

	for i in range(len_num):
		
		for ind in range(0, 10):
			for neighbor in pos_dic[ind]: # rather than length of things.
				cur_branches[ind] += prev_branches[neighbor]

		if i == len_num-1:
			break

		prev_branches = cur_branches
		cur_branches = [0 for x in range(10)]

	return sum(cur_branches)

print(count_num(4, 0))
