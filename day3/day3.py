# Starting at the top-left corner of your map
# following a slope of right 3 and down 1, 
# how many trees would you encounter?


track = 1

with open('input') as f:
    treemap = [line.split() for line in f]

trees = 0
i = 0
for rows in treemap:
    for row in rows:
        print("row: {}, col: {} is {}".format(row,i,row[i]))
        if(row[i] == "#"):
            trees += 1
        i += 3
        if (i > len(row)-1):
            i -= len(row)

track *= trees
print("trees: {}, total: {}".format(trees,track))

trees = 0
i = 0
for rows in treemap:
    for row in rows:
        #print("row: {}, col: {} is {}".format(row,i,row[i]))
        if(row[i] == "#"):
            trees += 1
        i += 1
        if (i > len(row)-1):
            i -= len(row)

track *= trees
print("trees: {}, total: {}".format(trees,track))

trees = 0
i = 0
for rows in treemap:
    for row in rows:
        #print("row: {}, col: {} is {}".format(row,i,row[i]))
        if(row[i] == "#"):
            trees += 1
        i += 5
        if (i > len(row)-1):
            i -= len(row)

track *= trees
print("trees: {}, total: {}".format(trees,track))

trees = 0
i = 0
for rows in treemap:
    for row in rows:
        #print("row: {}, col: {} is {}".format(row,i,row[i]))
        if(row[i] == "#"):
            trees += 1
        i += 7
        if (i > len(row)-1):
            i -= len(row)

track *= trees
print("trees: {}, total: {}".format(trees,track))

trees = 0
i = 0
countrow = 0
for rows in treemap:
    if (countrow % 2 == 0):
        for row in rows:
            #print("checking row: "+ str(countrow))
            print("row: {}, col: {} is {}".format(row,i,row[i]))
            if(row[i] == "#"):
                trees += 1
            i += 1
            if (i > len(row)-1):
                i -= len(row)
    countrow += 1

track *= trees
print("trees: {}, total: {}".format(trees,track))