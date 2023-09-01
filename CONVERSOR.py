#se que lo estoy subiendo un dia tarde pero es que subi el archivo en pdf porque no entendi la instruccion y apenas me di cuenta que era en .py
#CONVERSOR DECIMAL-BINARIO ASIGNANDO VALORES

decimal = 100
binario = ""
cociente = decimal

While cociente != 1:
    residuo = cociente % 2
    cociente = cociente // 2
    binario = binario + str(residuo)
    
binario = binario + str(cociente)
binario = binario[::-1]
print (binario)

#CONVERSOR DECIMAL-BINARIO CON PETICION AL USUARIO
decimal=int(input())
binario=""
cociente= decimal 
while cociente !=1:
  
    residuo= cociente  %2
    cociente = cociente //2
    binario =binario+ str (residuo)

binario = binario + str(cociente)
binario=binario[::-1]
print (binario)

#CONVERSOR BUNARIO-DECIMAL CON VALORES ASIGNADOS

binario = "1100100"
decimal = 0
base = 1

for bit in binario[::-1]:
    if bit == '1':
        decimal += base
    base *= 2

print(decimal)




