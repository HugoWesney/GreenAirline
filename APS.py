import time
from datetime import date
data_atual = date.today()
print ("Bem-vindo(a) ao sistema de cálculo da empresa The Green Airlines, agora são: ",time.strftime('%I:%M:%S %p %Z'), data_atual)
nome=str(input("Para iniciamos, como podemos te chamar?:"))
x=nome.upper()
print("Perfeito!!!,",x)
den=int(input("Digite agora o trecho do seu voo\n Digite 1 para o trecho RIO - SAO PAULO;\n Digite 2 para o trecho CAMPINAS - RECIFE;\n Digite 3 para o trecho CURITIBA - BRASILIA;\nR:"))
qtd = int(input("Digite a quantidade de pessoas que irão junto nessa viagem? : ")) 
if den==1:
  car = 53*qtd
if den==2:
  car = 205*qtd
if den==3:
  car = 476*qtd
if car>=1000:
  car=car/1000 

arv = car // 7 

print("Seu vôo emitiu um total de",car,"kg de Co2. Para compensar sua emissão, The Green Airlines deverá plantar um total de",arv, "árvores na floresta da mata atlantica.")
print("O credito gerado pela empresa foi ",car,)
    
