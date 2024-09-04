menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
saldo = 0
limite = 500
limite_saque = 3
numero_saque = 0
extrato =""

while True :
    
    opcao = input(menu)

    if opcao == "d" :  
       valor = float(input("Qual o valor do depósito ?"))

       if valor > 0 :
          saldo += valor
          extrato += f"\nDepósito: R$ {valor:.2f}\n"
       else : 
        print("Operação Falhou!!! Número tem que ser maior que R$ 0")

    elif opcao == "s" :
   
     valor = float(input("Informe o Valor  R$ do Saque: "))

     excedeu_saldo = valor > saldo  
    
     excedeu_limite = valor > limite 

     excedeu_numerosaque = numero_saque >= limite_saque
 
     if excedeu_saldo: 
      print("Operação Falhou! Saldo insuficiente.")

     elif excedeu_limite:
      print("Valor  de saque permitido somente até R$500.")

     elif excedeu_numerosaque:
      print("Quantidade de saque diário permitido até 3.")

     elif valor > 0 :
      saldo = saldo - valor 
      extrato += f"\nSaque: R${valor:.2f}\n"
      numero_saque +=1

     else: 
   
      print ("Operação falhou! O valor informado está inválido!!") 

 
    elif opcao == "e":

     print ("\n----------------- EXTRATO ----------------------")
     print("Não foram realizada as movimentações." if not extrato else extrato )
     print(f"\nSaldo: R${valor:.2f}")
     print("----------------------------------------------------")

    elif opcao == "q":
     break

else : 
   
   print("Operação inválida ! Por favor selecione a operação novamente desejada.")

