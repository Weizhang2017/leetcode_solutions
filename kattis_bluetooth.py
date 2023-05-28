import time
n = int(input())
start = time.time()
teeth = [[0,0], [0,0]]
blue = [0, 0]
for i in range(n):
	side, type_ = input().split()
	if side[1] in '-+':
		if type_ == 'b':
			blue[0] = 1
		if side[1] == '+':
			teeth[0][0] += 1
		else:
			teeth[0][1] += 1
	else:
		if type_ == 'b':
			blue[1] = 1
		if side[0] == '+':
			teeth[1][0] += 1
		else:
			teeth[1][1] += 1

if blue[0] and blue[1]:
	print(2)
else:
	if teeth[0][0] < 8 and teeth[0][1] < 8 and blue[0] != 1:
		print(1)
	elif teeth[1][0] < 8 and teeth[1][1] < 8 and blue[1] != 1:
		print(0)
	else:
		print(2)
print('time:', time.time() - start)
