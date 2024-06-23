year = int(input())
temp = year
while(1):
    temp+=1
    year = temp    
    a = year%10
    year = (year // 10)
    b = year%10
    year = (year // 10)
    c = year%10
    year = (year // 10)
    d = year%10
    year = (year // 10)
    
    if (a!=b and a!=c  and a != d and b!=c and b!=d and c!=d):
        break
    
    
print(temp)
    