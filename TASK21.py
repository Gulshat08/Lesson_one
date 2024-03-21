n = 10
maxsub = 0
sp = [int(x) for x in input().split()]
for i in range(len(sp)-1):
    if (abs(sp[i+1]-sp[i])) > maxsub:
        maxsub = abs(sp[i+1]-sp[i])
    print(maxsub*100)