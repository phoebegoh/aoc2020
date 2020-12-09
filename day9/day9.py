numbers = []
current = []
preamble = 25 # length of preamble
input = 'input'
#preamble = 5
#input = 'test'

# returns False if i is the sum of 2 of the numbers starting from data[start]
def is_valid(n,start):
  array = current[start:start+preamble]
  array.sort()
  #print("Searching array:",array,"for 2 numbers adding to:",n)
  l = 0
  h = len(array)-1
  while (l < h):
    #print(array[l],'+',array[h],'=',array[l]+array[h])
    if array[l] + array[h] == n:
      return True
    elif array[l] + array[h] < n:
      l += 1
    elif array[l] + array[h] > n:
      h -= 1
  return False

# return the contiguous list of numbers that adds up to n
def get_contiguous_set(n):

  array = []
  for i in range(2,len(numbers)-1): # for each possible set size
    for j in range(0,len(numbers)-1):
      count = sum(numbers[j:j+i])
      if count == n:
        print("I found {} numbers that sum to {}".format(i,n))
        return i,j
#    array = [numbers[j:j+i] for j in range(0,len(numbers)-1)]
  return -1,-1
  
with open(input,'r') as f:
  numbers = f.read().splitlines()

numbers = list(map(int,numbers))
current = numbers[:preamble] # start with the preamble

#print("Input:",numbers)
check = 0
for n in numbers[preamble:]:
  #print("Current:",current)
  if not is_valid(n,check):
    #print("Found invalid number:",n)
    break
  check += 1
  current.append(n)

print("Part 1:",n)

(size,index) = get_contiguous_set(n)
contiguous_set = numbers[index:index+size]
contiguous_set.sort()
print("Part 2:",contiguous_set[0]+contiguous_set[-1])
