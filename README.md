## IBLUEIT 🐬
Este repositório trata-se de um fork/estudo do projeto **[UDESC-LARVA/IBLUEIT](https://github.com/UDESC-LARVA/IBLUEIT)** no propósito de TCC na Universidade UniSociesc tendo como objetivo a sugestão de melhoria da aplicação.

#### Integrantes
- [@alexandrebfaust](https://github.com/alexandrebfaust) 
- [@kalitasilva](https://github.com/kalitasilva) 
- [@Leandro-Custodio](https://github.com/Leandro-Custodio) 
- [@Lucas-Besen](https://github.com/Lucas-Besen) 
- [@welingtonlarsen](https://github.com/welingtonlarsen) 

## Sobre
Esta aplicação *IA* foi desenvolvida para agregar funcionalidade utilizando Inteligencia Artificial na Aplicação do Sistema IblueIt usando a Linguagem Python devido ao seu maior suporte pela comunidade.

## Tecnologias e Bibliotecas Utilizadas
- [Python](https://www.python.org/doc/) 3.10.4
- [Flask](https://flask.palletsprojects.com/en/2.1.x/) 2.1.2
- [pymongo](https://pymongo.readthedocs.io/en/stable/) 4.1.1
- [python-dotenv](https://pypi.org/project/python-dotenv/) 0.20.0

### Instalação e Inicialização SEM Docker-Compose
1. Instale o [Python](https://www.python.org/downloads/) 3.10.4
2. Instale [pip](https://pip.pypa.io/en/latest/installation/)
3. Instale o pymongo com o seguinte comando:
```
pip install pymongo
pip install "pymongo[srv]
```
4. Instale o flask com o seguinte comando:
```
pip install flask
```
5. Instale o python-dotenv com o seguinte comando:
```
pip install python-dotenv
```
6. Crie um arquivo chamado .env com a seguintes informações:
```
MongoDbAtlas="mongodb://usuarioiblueit:senhaiblueit@iblueit-mongo/?retryWrites=true&w=majority Alterar Usuario e senha"
```
7. Rode o Script de Start do Python:
```
python3 main.py
```

### Repositórios GitHub - Código fonte
- Aplicação (BackEnd) [Blue_It_BackEnd](https://github.com/unisocisec/Blue_It_BackEnd)
- Interface gráfica (FrontEnd) [blue_It_front](https://github.com/unisocisec/blue_It_front)
- Inteligência artificial [Blue_It_IA](https://github.com/unisocisec/Blue_It_IA)
- Repositório do Jogo [Blue_It_Game](https://github.com/unisocisec/Blue_It_Game)
