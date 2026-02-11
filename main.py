from providers.playstationProvider import buscarPlaystation
from providers.nuuvemProviders import buscarNuuvem
import json

print("Qual jogo deseja buscar?")
jogoProcurado = input()

buscarPlaystation(jogoProcurado)
buscarNuuvem(jogoProcurado)

with open("precosNuuvem.json", "r" , encoding="utf-8") as arquivo:
    dadosNuuvem = json.load(arquivo)

with open("precosPlaystation.json", "r" , encoding="utf-8") as arquivo:
    dadosPlaystation = json.load(arquivo)

print("Resultados Nuuvem\n")
print(f"{dadosNuuvem["requestItens"]}{"\n"}")
print("Resultados PlayStation\n")
print(dadosPlaystation["requestItens"])
