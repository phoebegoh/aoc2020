with open('input','r') as f:
    data = f.read().splitlines()

# create an array of op,arg
#[ [op,arg], [op,arg] ]
instructions = []
instructions = [line.split() for line in data]
completed = [0 for x in range(len(instructions))]

# 
def do_wop(arr):
    action = arr[0]
    ctr = arr[1]
    print("Running",action,ctr)
    if action == "nop":
        index += 1
    if action == "jmp":
        index += ctr
    if action == "acc":
        acc += ctr
        index += ctr

# Return True if the last command in a program was run
def is_complete():
    if completed[-1] == 1:
        return True
    return False

# Return True if this command was already run
def already_run(index):
    if completed[index] == 1:
        return True
    return False

index = 0
acc = 0
while not is_complete():

    if already_run(index):
        print("Already run step at position",index)
        break

    action = instructions[index][0]
    ctr = int(instructions[index][1])

    print("Running index",index,'-',action,ctr)
    completed[index] = 1
    if action == "nop":
        index += 1
    if action == "jmp":
        index += ctr
    if action == "acc":
        acc += ctr
        index += 1
    
    print(" Acc:",acc)

print("Part 1:",acc)