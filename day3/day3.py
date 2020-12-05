# https://adventofcode.com/2020/day/3
# Starting at the top-left corner of your map
# following a slope of right 3 and down 1, 
# how many trees would you encounter?


with open('input') as f:
    treemap = [line.split() for line in f]


def count_trees(inc_across,inc_down):
    trees = 0
    i = 0
    rowcount = 0
    for rows in treemap:
        if (rowcount % inc_down == 0):
            for row in rows:
                #print("row: {}, col: {} is {}".format(row,i,row[i]))
                if(row[i] == "#"):
                    trees += 1
                i += inc_across
            if (i > len(row)-1):
                i -= len(row)
        rowcount += 1
    return trees

track = count_trees(1,1) * count_trees(3,1) * count_trees(5,1) * count_trees(7,1) * count_trees(7,2)
print(track)
print(count_trees(1,1))
print(count_trees(3,1))
print(count_trees(5,1))
print(count_trees(7,1))
print(count_trees(7,2))