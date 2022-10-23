T=tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
lit = input("Введіть велику літеру англійского алфавіту: ")
N = int(input("Введіть кількість послідовних літер, N= "))
print("Кортеж: ",T)

if lit in T: 
    num = T.index(lit)
    for i in range(4):
        T2 = T[num:num+N]
        print("Сторона квадрата",i+1," ",T2)
        num=num+N
else:
    print("невірна літера")
