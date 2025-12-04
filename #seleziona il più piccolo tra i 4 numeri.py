#seleziona il più piccolo tra i quattro numeri

a = float(input("inserisci a: "))
b = float(input("inserisci b: "))
c = float(input("inserisci c: "))
d = float(input("inserisci d: "))
if a>b:
    if b>c:
        if c>d:
         min = d
        else:
         min = c
    else:
         if b>d:
          min = d
         else: 
          min = b
else:
    if a>c:
         if c>d:
          min = d
         else:
          min = c
    else:
         if a>d:
           min = d
         else:
            min = a


print ("tra ",a,",",b," , ",c," e ",d," il minore è ",min) 
