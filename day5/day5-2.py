# Trying this again probably the way you're meant to do it :)

# FBFBBFFRLR: row 44, column 5, seat ID 357
# BFFFBBFRRR: row 70, column 7, seat ID 567.
# FFFBBBFRRR: row 14, column 7, seat ID 119.
# BBFFBBFRLL: row 102, column 4, seat ID 820.
tests = ["FBFBBFFRLR","BFFFBBFRRR","FFFBBBFRRR","BBFFBBFRLL"]

with open('input') as f:
    data = f.read().splitlines()
    
# part 1:
# to find the seat ID, multiply column by 8 and add col.
# i learnt that this is actually shifting left by 3 (ha ha.. 2^3)
# so therefore, seat id = (row << 3) + col

# first 7 characters are "B" or "F". If "B" it's the bottom half. If "F" it's the top half.
# last 3 characters are "R" or "L". If "L" it's the bottom half. If "R" it's the top half.
# so 'BFFFBBFRRR' = 0111001111
rc="BFRL"
binary="1010"
t = rc.maketrans(rc,binary) # Make a translation table from rc to binary
#print(t)
ids = []
for line in data:
    translated = line.translate(t)
    row = int(translated[:7],2)
    col = int(translated[7:],2)
    #seat = (row << 3) + col
    #print(line,translated,row,col,seat)
    ids.append((row << 3)+col)

ids.sort()
print(ids[-1])

# part 2:
# you can find the difference between an array that is "complete" (all seats in the range) vs the list we've just created (i.e. all seats except mine)
# and i also found that set(list1) - set(list2) returns the set of elements in list1 not in list2.
# obviously, this wouldn't work if there were more than 1 missing seat.
# this would also not work if we were in the 1st or the last seat, but it was noted that you were not in either of these seats.
allids = list(range(ids[0],ids[-1]))
print(set(allids) - set(ids)) # find the difference between allids and ids