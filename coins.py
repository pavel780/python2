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

##

s=int(input("введите сумму "))
p=int(input("введите произведение "))

for i in range(s):
    if i*(s-i)==p:
        print(f'первое число ="{i}",второе число ="{s-i}"')
        break

##
x=1
n=int(input("введите n "))
while x<=n:
    print(x)
    x=x*2
