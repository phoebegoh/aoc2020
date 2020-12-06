# Create a set of all possible answers
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

    count = len(set(questions) & set(answers))
    #print("group:",chars)
    #print("answers:",answers)
    #print("count:",count)
    #print("---")
    total += count

print("part 1 answer:",total)

total = 0
for group in groups:
    x = 0
    answers = set()
    people = group.splitlines()
    print("answers:",people)
    result = set(set(people[0]).intersection(*people))
    print("intersect:",result)
    print("---")
    total += len(result)

print("part 2 answer:",total)