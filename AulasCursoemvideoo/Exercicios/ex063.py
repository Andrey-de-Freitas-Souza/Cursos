n = int(input("""Digite quantos elementos da sequência de 
fibonacci ,você quer que eu mostre:"""))
a = 0
s = 1
x = 0
while n > 0:
    n -= 1
    x = x + a
    print(x, end=", ")
    a = x
    x = s
    s = a