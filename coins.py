n=int(input("введите число монет: "))
mas=[i for i in range(5)]
sum=0
for i in range(n):
    mas[i]=int(input("введите сторону монеты(1 - орел или 0 - решка): "))
    if mas[i]==0:
        sum=sum+1
if sum<n-sum:
    print(sum)
else:
    print(n-sum)
