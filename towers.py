n,k = map(lambda x: int(x), raw_input().split(' '))
initial = map(lambda x: int(x), raw_input().split(' '))
final = map(lambda x: int(x), raw_input().split(' '))

stacks = [[] for x in range(k)]

for i in range(n):
	stacks[ initial[i] - 1].append(i+1)

for i in range(k):
	stacks[i].reverse() 

def moveToBottom(disk, src, dst):
	if stacks[src].index(disk) == len(stacks[src])-1 and len(stacks[dst]) ==0:
		stacks[dst].append(stacks[src].pop())
	else:
		if len(stacks[dst]) == 0: 
			nextIndex = stacks[src].index(disk) + 1
			nextNum = stacks[src][nextIndex]
			destinations = list(set(range(k)) - set([src, dst]))
			moveToBottom(nextNum, src, destinations[0])

			moveToBottom(disk, src, dst)

		else:	 
			raise Exception( "Can't move %s %s %s index: %s" % (disk, src, dst, stacks[src].index(disk)))

print stacks
moveToBottom(disk = 2, src = 0, dst = 2)
print stacks 