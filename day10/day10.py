# find the next joltage that has a difference of 1, 2, or 3
# j = current joltage
def next_joltage(j,remaining):
  #print("calling next_joltage,",j)
  
  for r in remaining:
    difference = r - j
    for i in 1,3:
      if difference == i:
        remaining.remove(r)
        return (r,i,remaining) # return the difference, and new array
  return -1
  
def part1(data):
  device = max(data) + 3
  data.append(device)
  data.sort()
  
  diffs = [0 for i in range(3)]
  joltage = 0
  while len(data) > 0:
      #print("\n###\nloop, length of list:",len(data))
      #print("diffs = ",diffs)
      #print("data = ",data)
      #print("joltage = ",joltage)  
      (joltage, d, data) = next_joltage(joltage,data)
      #print("new joltage:",joltage,"\ndifference:", d, "\nnew list:", data)
      diffs[d-1] += 1
  
  #print(diffs)
  print("Part 1:",diffs[0]*diffs[2])
  return diffs
  
# find how many arrangements of data starting at 0 and ending in device
def get_arrangements(joltage,data):
  lookup = [0]*len(data)
  lookup[0] = 1
  
  print(data)
  # iterate over all adapters. if remainder is <= 3, add to the total
  for i in range(0,len(data)):
    total = 0
    for j in range(1, 4):
      if i - j < 0:
        continue
      if data[i] - data[i-j] <= 3:
        total += lookup[i-j]
        lookup[i] = total

  return lookup[-1]
  
def part2(data):
  
  device = max(data) + 3
  data += [0,device]
  data.sort()
  joltage = 0

  arrangements = get_arrangements(joltage,data)
    
  print("Part 2:",arrangements)

data = []
with open('input','r') as f:
  data = [int(x) for x in f] # a more efficient way to read integers!

#part1(data)

part2(data)
