A=set()
B=set()
C=set()
A1=set()
B1=set()
C1=set()

i=1
while i<=200:
    if i%4==0:
        A.add(i)
    if i%3==0:
        B.add(i)
    if i%5==0:
        C.add(i)
    i=i+1

D=A|B|C

for i in D:
    if i%12==0:
        A1.add(i)
    if i%20==0 and i%3!=0:
        B1.add(i)
    if i%15==0 and i%4!=0:
        C1.add(i)
    
print("Множина А: ",A)
print("Множина В: ",B)
print("Множина С: ",C)
print("Множина D: ",D)
print("Числа, які діляться на 12: ",A1)
print("Числа, які діляться на 20 і не діляться на 3: ",B1)
print("Числа, які діляться на 15 і не діляться на 4: ",C1)