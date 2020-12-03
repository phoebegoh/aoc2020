# Find two entries that sum to 2020 and then multiply those numbers together
input = []
with open('input') as f:
    for line in f:
        input.append(int(line))

print(input)

for i in range(0,len(input)-1):
    num1 = input[i];
    for j in range(1, len(input)-1):
        if(num1 + input[j] == 2020):
              num2 = input[j]
              break
    else:
        continue
    break

print("eureka! " + str(num1) + " + " + str(num2) + " = 2020")


print(str(num1 * num2))

# bonus: Find three entries that sum to 2020 and then multiply those numbers together

for i in range(0,len(input)-1):
    num1 = input[i]
    for j in range(1, len(input)-1):
        num2 = input[j]
        for k in range(2, len(input)-1):
            if (num1 + num2 + input[k] == 2020):
                num3 = input[k]
                print("Eureka! {} + {} + {} = 2020".format(num1, num2, num3))
                break
        else:
            continue
        break
    else:
        continue
    break

print(str(num1 * num2 * num3))