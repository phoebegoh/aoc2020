# https://adventofcode.com/2020/day/2
# input format
# password policy: password
# policy - lowest, highest number of times a letter must appear
# 1-3 a means at least 1 a, at most 3 'a's.
# Goal: check the input 

valid = 0
with open('input') as f:
    for line in f:
        policy, letters, password = line.split()
        #print(policy, letters, password)
        atLeast,atMost = policy.split("-")
        #print("{} {}".format(min,max))
        letter = letters[0]
        #print("Checking {} for minimum {} and maximum {} occurences of: {}".format(password,min,max,letter))
        count = password.count(letter)
        if ((count >= int(atLeast)) and (count <= int(atMost))):
            valid += 1
            #print("{} occurs {} times in {} (min: {}, max: {})".format(letter,count,password,atLeast,atMost))
print(valid)

#bonus
valid = 0
with open('input') as f:
    for line in f:
        policy, letters, password = line.split()
        a, b = policy.split('-')
        letter = letters[0]
        #print("{} {} {}".format(password,password[int(a)-1],password[int(b)-1]))

        if ((password[int(a)-1] == letter) and (password[int(b)-1] != letter)) or ((password[int(b)-1] == letter) and (password[int(a)-1] != letter)):
            print("{}, {}: {} {}".format(password,letter,password[int(a)-1],password[int(b)-1]))
            valid +=1

print(valid)