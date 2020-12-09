with open('input','r') as f:
    data = f.read().splitlines()

# create an array of op,arg
#[ [op,arg], [op,arg] ]
instructions = []
instructions = [line.split() for line in data]
completed = [0 for x in range(len(instructions))]
start = 0
acc = 0

# Return True if the last command in a program was run
def is_complete():
    if completed[-1] == 1:
        return True
    return False

# Return True if this command was already run
def is_infinite(index):
    if completed[index] == 1:
        return True
    return False

# Iterate over the instructions array starting at index
# If you find a jmp, flip it to nop (and vice versa) and then return
def flip_jmpnop(index):

    for i in range(index,len(instructions)-1):

        if instructions[i][0] == 'jmp':
            #print("Flipped",i,"to nop")
            instructions[i][0] = 'nop'
            return
        elif instructions[i][0] == 'nop':
            #print("Flipped",i,"to jmp")
            instructions[i][0] = 'jmp'
            return
        else:
            pass
    return

def run_program(index):
    global acc

    while not is_complete():

        if is_infinite(index):
            print("Breaking on infinite loop",index)
            return False

        action = instructions[index][0]
        ctr = int(instructions[index][1])

        #print("Running index",index,'-',action,ctr)
        completed[index] = 1
        if action == "nop":
            index += 1
        if action == "jmp":
            index += ctr
        if action == "acc":
            acc += ctr
            index += 1

    return True

checked = 0
while not run_program(0):
    acc = 0
    flip_jmpnop(checked)
    completed = [0 for x in range(len(instructions))]
    run_program(0)
    flip_jmpnop(checked)
    checked += 1
    
#print("Part 1:",acc)
print("Part 2",acc)