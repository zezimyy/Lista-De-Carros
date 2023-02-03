listaCarros = ["aaa0001"]
addCarro = ""
remCarro = ""
verCarro = ""
fazer = ""
Loop = True

def menu():
  print("-="*15)
  print("Adicionar carro (A)")
  print("Remover carro (R)")
  print("Verificar carro (V)")
  print("-="*15)

while Loop == True:
  menu()
  print()
  fazer = str(input("Oque deseja fazer: "))

  if fazer == "a" or fazer == "A":
    addCarro = input("Qual a placa do carro a ser adicionada?: ")
    listaCarros.append(addCarro)

  if fazer == "r" or fazer == "R":
    remCarro = input("Qual a placa do carro deseja remover?: ")
    listaCarros.remove(remCarro)

  if fazer == "v" or fazer == "V":
    verCarro = input("Qual a placa do carro a ser verificada?: ")
    print(verCarro in listaCarros)