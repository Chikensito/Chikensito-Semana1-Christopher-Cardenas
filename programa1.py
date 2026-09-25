entrada1=input("Ingrese el numero 1:")
num1=int(entrada1)
entrada2=input("Ingrese el numero 2:")
num2=int(entrada2)
sum=num1+num2
rest=num1-num2
multi=num1*num2
print(f"el resultado de la suma es:{sum}")
print(f"el resultado de la resta es:{rest}")
print(f"el resultado de la multiplicacion es:{multi}")
if num2==0 or num1==0:
    print("No es posible realizar la operacion")
else:
    div=num1/num2
    print(f"el resultado de la division es:{div}")
