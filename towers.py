n,k = map(lambda x: int(x), raw_input().split(' '))
initial = map(lambda x: int(x), raw_input().split(' '))
final = map(lambda x: int(x), raw_input().split(' '))

stacks = [[] for x in range(k)]

for i in range(n):
	stacks[ initial[i] - 1].append(i+1)

for i in range(k):
	stacks[i].reverse() 

def moveToBottom(disk, src, dst, moves):	
	if stacks[src].index(disk) == len(stacks[src])-1 and (len(stacks[dst]) ==0 or disk < stacks[dst(-1)]):
		moves.append((src, dst))
		stacks[dst].append(stacks[src].pop())	
		return moves	
	else:
		if len(stacks[dst]) == 0: 
			nextIndex = stacks[src].index(disk) + 1
			nextNum = stacks[src][nextIndex]
			destinations = list(set(range(k)) - set([src, dst]))
			moves = moveToBottom(nextNum, src, destinations[0], moves)
		 
			moves = moveToBottom(disk, src, dst, moves)
			return moves

		else:	 
			raise Exception( "Can't move %s %s %s index: %s" % (disk, src, dst, stacks[src].index(disk)))

print stacks
print moveToBottom(disk = 2, src = 0, dst = 2, moves = [])
print stacks 
