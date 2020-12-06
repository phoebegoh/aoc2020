# Create a list of all possible answers
# Create a running total
questions = "abcdefghijklmnopqrstuvwxyz"
total = 0

# get all groups
with open('input','r') as f:
    groups = f.read().split("\n\n")
    
for group in groups:
    answers = ""
    
    chars = group.replace('\n','')

    for c in chars:
        #print("eval ",c)
        if c not in answers:
            answers += c

    # count is the length of the list of total answers from this group
    count = len(set(questions) & set(answers))
    #print("group:",chars)
    #print("answers:",answers)
    #print("count:",count)
    # print("---")
    total += count

print("part 1 answer:",total)

total = 0
for group in groups:
    x = 0
    answers = set()

    people = group.splitlines()
    result = set(set(people[0]).intersection(*people)) 
    # I learned something new. This is the intersection of ALL the lists in people.
    # https://www.semicolonworld.com/question/53496/python-intersection-of-multiple-lists


    #print("answers:",people)
    #print("intersect:",result)
    #print("---")
    total += len(result)

print("part 2 answer:",total)