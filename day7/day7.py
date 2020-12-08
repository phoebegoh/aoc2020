import re

bags = {}
count = []
  
def has_bag(color):
  #print('Color: ',color)
  for key,contents in bags.items():             # search every possible bag
    for c in contents:                          # for each bag IN that container
      if color in c:                            # if the bag matches the color
        #print(color,"found")
        count.append(key)                       # append the bag to the array
        has_bag(key)                            # run has_bag on the new bag
  return 0

def total_bags(color):
  x = 0
  
  #print("Looking for:",color)
  for key,contents in bags.items():
    #print("Checking",key,"for",color)
    if color in key:                              # If this is the color of the bag
      for c in contents:                         # Go through the contents of bag
        m = re.search(r'(\d+|no) (.*) bags?',c)   # Get the count of each internal bag
        
        if m is not None:
          
          if (m.group(1) == 'no'):
            continue
          
          n = int(m.group(1))                   # e.g. 2
          newcolor = m.group(2)                 # e.g. shiny teal
          
          #print(n,newcolor)
          x += n + (n * total_bags(newcolor))
  return x

with open('input','r') as f:
  for line in f.read().splitlines():
    (bag,contents) = line.split(' bags contain ')
    bags[bag] = contents.split(', ')

has_bag('shiny gold')

print("Part 1:",len(set(count)))

total = total_bags('shiny gold')

print("Part 2:",total)
