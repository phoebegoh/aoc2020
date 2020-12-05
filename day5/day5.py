# Total rows on plane: 128
# Total columns on plane: 8
import math
allids = []

# The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane (numbered 0 through 127)
def get_row(line):
    minval = 0
    maxval = 127

    for char in line[0:7]: # first 7 characters
        median = (minval + maxval)/2
        #print("min: {} max: {} char: {} median: {}".format(minval,maxval,char,median))
        
        if char == "F":
            maxval = math.floor(median)
            median = math.floor(median)
        if char == "B":
            minval = math.ceil(median)
            median = math.ceil(median) #is there a nicer way to do this?
    
    return median

def get_col(line):
    minval = 0
    maxval = 7
    median = 0

    for char in line[7:]: # rest of string
        median = (minval + maxval)/2
        #print("min: {} max: {} char: {} median: {}".format(minval,maxval,char,median))
        
        if char == "L":
            maxval = math.floor(median)
            median = math.floor(median)
        if char == "R":
            minval = math.ceil(median)
            median = math.ceil(median) #is there a nicer way to do this?
    
    return int(median)

def get_seat_id(row,col):
    return (row*8)+col


# Goal: What is the highest seat ID on a boarding pass?
def part1():
    maxid = 0
    with open('input', 'r') as f:
        for line in f:
            seat = get_seat_id(get_row(line),get_col(line))
            allids.append(seat)
            #print("{}:{}".format(line,seat))
            maxid = seat if seat > maxid else maxid
    return maxid



# Goal: What is the ID of your seat?
# some of the seats at the very front and back of the plane don't exist on this aircraft, so they'll be missing from your list as well.
def part2():

    allids.sort() # we now have a list of all the boarding passes included
    for i in range(len(allids)-2):
        seat1 = allids[i]
        seat2 = allids[i+1]
        #print("Comparing {} and {}".format(seat1,seat2))
        if seat2 - seat1 == 2:
            #print("Found a gap between {} and {}".format(seat1,seat2))
            return seat2 - 1
        

part1()
part2()
print(part1())
print(part2())


# BFFFBBFRRR: row 70, column 7, seat ID 567.
#FFFBBBFRRR: row 14, column 7, seat ID 119.
#BBFFBBFRLL: row 102, column 4, seat ID 820.
# tests = ["FBFBBFFRLR","BFFFBBFRRR","FFFBBBFRRR","BBFFBBFRLL"]
# for test in tests:
#     #print("row: {} col: {}".format(get_row(test),get_col(test)))
#     print(get_seat_id(get_row(test),get_col(test)))