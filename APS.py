import time
from datetime import date
data_atual = date.today()
print ("Bem-vindo(a) ao sistema de cálculo da empresa GreenRouts Aviation, agora são: ",time.strftime('%I:%M:%S %p %Z'), data_atual)
nome=str(input("Para começarmos, como podemos te chamar?:"))
x=nome.upper()
print("Perfeito!!!,",x)
den=int(input("Digite agora o trecho do seu voo\n Digite 1 para o trecho RIO - SAO PAULO;\n Digite 2 para o trecho CAMPINAS - RECIFE;\n Digite 3 para o trecho CURITIBA - BRASILIA;\nR:"))
qtd = int(input("Digite quantas pessoas irão viajar junto com você: ")) 
if den==1:
  car = 53*qtd
if den==2:
  car = 205*qtd
if den==3:
  car = 476*qtd
if car>=1000:
  car=car/1000 

arv = car // 7 

print("Seu vôo emitiu um total de",car,"kg de Co2. Para compensar sua emissão, The Green Arlines ira plantar um total de",arv, "árvores na floresta da mata atlatica.")
print("E foi gerado a empresa",car,"de carbono")
    