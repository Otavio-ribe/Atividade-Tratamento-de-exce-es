class Erro0(Exception):
    pass

try:
    numero = int(input("Digite um número inteiro:" ))
    
    resultado = numero/10
    if numero == 0:
        raise Erro0 (f"O numero {numero} não é permitido")
        

except Erro0 as e:
    print(f"Erro: {e}")
except ValueError:
    print("O número inserido é invalido")

else:
    print(F"O seu numero é {numero}, a divisão por 10 é igual a: {resultado}")
