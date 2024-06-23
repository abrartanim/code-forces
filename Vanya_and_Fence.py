count = int(input())
fence_height = int(input())

total = 0

for i in range(count):
    inp = int(input())
    if (inp > fence_height):
        total = total + 2
    else:
        total = total + 1
        
print(total)