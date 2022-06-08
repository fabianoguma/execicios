# Faça um programa que pergunte o preço de três produtos e informe 
# qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
import time 
print("Escolha seu cafe , informe seu preco, pra informa qual e o mais em conta")
nome = input(str.title("Digite seu nome por favor ?\n"))

cafe1= input(str.title("digite o nome do cafe?\n ", end = "\r"));preco = float(input(f"Digite:qual e o preco do cafe {str.title(cafe1)} ?\n",end = "\r"))
cafe2 = input(str.title("Digite qual o outro cafe ?\n",end = "\r")); preco2 = float(input(f"Digite: qual e do cafe {str.title(cafe2)}? \n",end = "\r"))
cafe3 = input(str.title("Digite qual o terceiro cafe\n ",end = "\r")); preco3 = float(input(f"Digite: qual e o do cafe {str.title(cafe3)} ?\n",end = "\r"))

def countdown(num_of_secs):
      while num_of_secs:
         m, s = divmod(num_of_secs, 60)
         min_sec_format = '{:02d}:{:02d}'.format(m, s)
         print(min_sec_format, end = "\r")
         time.sleep(1)
         num_of_secs -= 1
if preco < preco2 or preco < preco2:
    print(f"Vou analiza qual e o mais barato para voce  {str.title(nome)}.") 
    
    f = countdown(10)
    print("analizei o melhor preço ")
    
    time.sleep(3)
   
    print(f" O cafe {cafe1}, e o mais barato com o preco {preco}, pode compra esse! ")
    
elif preco2 < preco or preco2 < preco:
   
   print(f"Vou analiza qual e o mais barato para voce  {nome}.")
   f = countdown(10)
   print("analizei o melhor preço ")
    
   time.sleep(3)

  
   print(f" O cafe {cafe2}, e o mais barato com o preco {preco2}, pode compra esse! ")

elif preco3 < preco or preco3 <preco2:
   print(f"Vou analiza qual e o mais barato para voce  {nome}.")
   f = countdown(10)
   print("analizei o melhor preço ")
    
   time.sleep(3)
   
   
   print(f" O cafe {cafe3}, e o mais barato com o preco {preco3}, pode compra esse! ")


