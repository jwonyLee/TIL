prime = [None for _ in range(100)]
check = [False for _ in range(101)]
pn = 0
num = 100

for i in range(2, num+1):
    if not check[i]:
        prime[pn] = i
        pn += 1
    
    j = i*i
    while j <= num:
        check[j] = True
        j += i

prime = [p for p in prime if p]
print(prime)