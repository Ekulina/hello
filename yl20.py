code = input("Sisesta esimesed 11 numbrit: ")

a = ((eval("+".join(code[i] for i in range(0,len(code),2)))*3)+eval("+".join(code[i] for i in range(1,len(code),2))))%10

print(code+str(a if a==0 else 10-a))