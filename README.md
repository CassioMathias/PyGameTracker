
==================== 🎮 PyGame Tracker — Python ====================

Projeto em Python que realiza web scraping de preços de jogos em mídia digital.

Inicialmente, o foco do projeto é o site da Nuuvem, onde o script busca jogos pelo nome, filtra resultados indesejados (DLCs, pacotes e plataformas específicas)
e armazena os dados de preço em um arquivo JSON estruturado, facilitando análises posteriores.


==================== 📌 Motivação do Projeto ====================

A ideia do projeto surgiu de uma necessidade pessoal: comparar preços de jogos entre diferentes plataformas e lojas digitais.

No meu caso, utilizo principalmente PlayStation e Steam, e isso gera um problema recorrente:
a Steam vende jogos no site oficial e também por varejistas parceiras.
Cada loja apresenta preços diferentes, promoções em períodos distintos e estruturas próprias de busca.
Isso me obrigava a abrir vários sites, pesquisar manualmente o mesmo jogo e comparar valores, o que consome tempo e torna o processo pouco prático.

Como forma de otimizar esse processo, encontrei na linguagem Python uma maneira eficiente de:

- acessar páginas HTML
- coletar os dados relevantes
- tratar essas informações
- organizar os resultados de forma estruturada

O objetivo do projeto é justamente ganho de tempo e otimização de buscas, criando uma ferramenta que centraliza os dados em um único lugar.


==================== ⚙️ Como o Projeto Funciona Atualmente ====================

O script realiza as seguintes etapas:

- recebe o nome do jogo a ser buscado
- monta a URL de pesquisa da Nuuvem
- percorre os cards de jogos retornados
- filtra resultados
- classifica os resultados (JOGO, DLC ou PACOTE)
- extrai o preço
- salva os dados em um arquivo precosNuuvem.json


==================== 🚧 Próximos Passos ====================

- Implementar paginação automática para varrer todos os resultados da busca
- Normalizar melhor os termos de pesquisa
- Adicionar suporte para outras lojas:
    Steam
    PlayStation Store
    G2A
    outras que façam sentido
- Melhorar filtros e critérios de exibição
- Criar um frontend simples para visualização dos dados
- Avaliar técnicas mais robustas de coleta e tratamento dos dados


==================== ⚠️ Observação ====================

Este projeto tem fins educacionais e de estudo, com foco em aprendizado de web scraping, tratamento de dados e organização de informações em Python.