import requests
import json
from bs4 import BeautifulSoup

# print("Qual jogo deseja buscar?")
# jogoProcurado = input()

def buscarNuuvem(jogoProcurado):

    procuraUrl = jogoProcurado.replace(" ", "%20")

    url = "https://www.nuuvem.com/br-pt/catalog/search/" + procuraUrl

    response = requests.get(url)

    html = response.text

    soup = BeautifulSoup(html, "html.parser")

    dados = {
            "jogoProcurado": jogoProcurado,
            "plataforma": "Nuuvem",
            "requestItens": []
            }

    cardGames = soup.find_all("div", class_="game-card__content")

    for cardGame in cardGames:

        gameName = cardGame.find("h3", class_="game-card__product-name")
        gameName = gameName.get_text(separator=" ", strip=True)

        if not gameName:
            continue
        
        if "dlc" in gameName.lower():
            gameType = "DLC"
        elif "pacote" in gameName.lower():
            gameType = "PACOTE"
        else:
            gameType = "JOGO"

        if any(platIndesejada in gameName.lower() for platIndesejada in ["xbox", "playstation"]):
            continue

        if jogoProcurado.lower() not in gameName.lower():
            continue

        priceInteger = cardGame.find("span", class_="integer")
        if not priceInteger:
            continue
        priceInteger = priceInteger.text.strip()
        priceDecimal = cardGame.find("span", class_="decimal")
        if not priceDecimal:
            continue
        priceDecimal = priceDecimal.text.strip()

        gamePrice = priceInteger + priceDecimal

        requestItem = {
        "nome": gameName,
        "preco": gamePrice,
        "tipo": gameType
    }
        dados["requestItens"].append(requestItem)

    with open("precosNuuvem.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

    return("Busca concluída!")
