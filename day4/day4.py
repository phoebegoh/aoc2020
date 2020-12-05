# https://adventofcode.com/2020/day/4
# Each passport is represented as a sequence of key:value pairs separated by spaces or newlines. Passports are separated by blank lines.
# Missing cid is fine, but missing any other field is not
# possible entries:
# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID) -- you can ignore this because it doesn't make the passport valid
import re

entries = ["byr:","iyr:","eyr:","hgt:","hcl:","ecl:","pid:"]
ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

 # array of passports with correct entries
valid_pp = [] 

with open('input', 'r') as f:
    lines = f.read().strip()

def part1():
    count = 0
    for line in lines.split("\n\n"):
        #print(line) # this is a passport
        valid = [entry for entry in entries if entry in line]
        if len(valid) == len(entries):
            count += 1
            valid_pp.append(line)
    return count # this is the number of valid passports

def part2():
    valid = 0

    for pp in valid_pp: # iterate through the valid entries from above
        track = 0
        #print(pp.strip().split())
        d = dict(item.split(":") for item in pp.split()) 
        for k,v in d.items():
            #print("Checking {}:{}".format(k,v))
            if k == "byr":
                if (int(v) >= 1920) and (int(v) <= 2002): # at least 1920, at most 2002
                    track += 1
                    continue
                else:
                    print("{} failed byr".format(v))
            if k == "iyr":
                if (int(v) >= 2010) and (int(v) <= 2020): # at least 2010, at most 2020
                    track += 1
                    continue
                else:
                    print("{} failed iyr".format(v))
            if k == "eyr":
                if (int(v) >= 2020) and (int(v) <= 2030): # at least 2020, at most 2030
                    track += 1 
                    continue
                else:
                    print("{} failed eyr".format(v))                
            if k == "hgt":
                m = re.search('(\d+)cm$',v) # check for cm
                if m:
                    val = int(m.group(1))
                    if (val >= 150) and (val <= 193): # at least 150cm, at most 193cm
                        track += 1
                        continue
                m = re.search('(\d+)in$',v) # check for in 
                if m:
                    val = int(m.group(1))
                    if (val >= 59) and (val <= 76): # must be at least 59 and at most 76.
                        track += 1
                        continue
            if k == "hcl" and re.search('^#[0-9a-f]{6}$',v):  # a # followed by exactly six characters 0-9 or a-f.
                track += 1
                continue
            else:
                print("{} failed hcl".format(v))
            if k == "ecl" and v in ecl: # ecl must be in the list of valid colours (ecl)
                track += 1
                continue
            else:
                print("{} failed ecl".format(v))
            if k == "pid" and re.search('^[\d]{9}$',v): # 9 digit number
                track += 1
                continue
            else:
                print("{} failed pid".format(v))
#        print("")
        if (track == len(entries)):
            print("All {} criteria met".format(len(entries)))
            valid += 1

    print ("There are {} valid entries".format(valid))
    return valid

    # for pp in valid_pp:
    #     pp.strip().split(maxsplit=1)
    #     #print(pp.strip().split())
    #     for item in pp:
    #         print(item)
    #         print("---")
        #d = {k: v for item in pp for (k,v) in [item.split(maxsplit=1)]}
    #for k, v in d.items():
    #    print(k, v)   
       #print(pp.split()) # this is each passport


   # d = dict (passport.split(":") for passport in line.split()) #this is the key:val pair
    #for k, v in d.items():
    #    print(k, v)
   # for entry in entries:
    #    if entry in d:
     #       print(entry + " found")
      #  else:
       #     print(entry + " not found")

part1()
part2()

print("The Answer to part 1 is: {}".format(part1()))
print("The Answer to part 2 is: {}".format(part2()))