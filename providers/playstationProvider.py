def buscarPlaystation(jogoProcurado):

    import requests
    import json
    from bs4 import BeautifulSoup

    # print("Qual jogo deseja buscar?")
    # jogoProcurado = input()

    procuraUrl = jogoProcurado.replace(" ", "%20")

    url = "https://store.playstation.com/pt-br/search/" + jogoProcurado

    response = requests.get(url)

    html = response.text

    search = BeautifulSoup(html, "html.parser")

    dados = {
            "jogoProcurado": jogoProcurado,
            "plataforma": "PlayStation Store",
            "requestItens": []
            }

    cardGames = search.find_all("div", class_="psw-product-tile psw-interactive-root")

    for cardGame in cardGames:

        gameName = cardGame.find("span", id="product-name")
        gameName = gameName.get_text(separator=" ", strip=True)

        if jogoProcurado.lower() not in gameName.lower():
            continue



        gamePlatforms = []
        gamePlatform = cardGame.find_all("span", class_="psw-platform-tag psw-p-x-2 psw-l-line-left psw-t-tag psw-on-graphic")
            
        for Platform in gamePlatform:
            Platform = Platform.get_text(separator=" ", strip=True)
            gamePlatforms.append(Platform)

        gameType = cardGame.find("span", class_="psw-product-tile__product-type psw-t-bold psw-t-size-1 psw-c-t-2 psw-t-uppercase psw-m-b-1 psw-m-t-2")
        if not gameType:
            gameType = "Jogo Base"
        else:
            gameType = gameType.get_text(separator=" ", strip=True)

        gamePrice = cardGame.find("span", class_="psw-m-r-3")
        gamePrice = gamePrice.get_text(separator=" ", strip=True)

        requestItem = {
            "nome": gameName,
            "preco": gamePrice,
            "plataforma": gamePlatforms,
            "tipo": gameType
        }

        dados["requestItens"].append(requestItem)

    with open("precosPlaystation.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

    return("Busca concluída!")


