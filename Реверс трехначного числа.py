num = int(input('Введите трехначное число чтобы сделать  реверс этого числа  '))
a100 = (num%100)%10
b10 = (num%100)//10
c1 = num//100
print(c1+b10*10+a100*100)