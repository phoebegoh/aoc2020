with open('input','r') as f:
    data = f.read().splitlines()
#ops = [0 for i in range(len(data)-1)]
#[ [op,arg], [op,arg] ]

# create an array of op,arg
instructions = []
instructions = [line.split() for line in data]
completed = [0 for x in range(len(instructions))]

print(instructions)

# acc increases accumulator
# jmp changes instruction
# nop does nothing

def do_op(op,index):
    acc = 0
    action = op[0]
    step = op[1]
    next_index = index

    print("Before: index:",index,"next index:",next_index,"value:",instructions[index],"action:",action,"step:",step,"state:",completed[index])
    
    if completed[index] == 1:
        print("I've run this before! acc:", acc)
    else:
        
        # If this is a nop, do the next instruction
        if action == 'nop':
            print("This is a nop")
            next_index += 1

        # If this is an acc, increase acc, then do next instruction
        elif action == 'acc':
            
            if (step[0] == '+'):
                acc += int(step[1:])
            elif (step[0] == '-'):
                acc -= int(step[1:])
        
            next_index += 1

        # otherwise, must be a jmp. Do the specified instruction
        else:
            if (step[0] == '+'):
                next_index += int(step[1:])
            elif (step[0] == '-'):
                next_index -= int(step[1:])

        completed[index] = 1
        print("After: acc:",acc,"index:",index,"next_index:",next_index)
        print("After: action:",action,"step:",step)
        print("---")

        return acc + do_op(instructions[next_index],next_index)

    return 0

print(do_op(instructions[0],0))