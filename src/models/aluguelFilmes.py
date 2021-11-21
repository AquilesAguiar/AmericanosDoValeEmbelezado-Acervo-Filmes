import json

def adicionarFilme(id):
    with open("src\\database\\aluguelFilmes.json", encoding='utf-8') as js:
        aluguelFilmes = json.load(js)
        
        if id in aluguelFilmes:
            aluguelFilmes[id]+=1
        else:
            aluguelFilmes[id] = 1
    

        aluguelFilmes = json.dumps(aluguelFilmes)

        jsonFile = open("src\\database\\aluguelFilmes.json", "w")
        jsonFile.write(aluguelFilmes)
        jsonFile.close()

def retornaFilmesGrafico():
    with open("src\\database\\aluguelFilmes.json", encoding='utf-8') as js:
        aluguelFilmes = json.load(js)
        return aluguelFilmes