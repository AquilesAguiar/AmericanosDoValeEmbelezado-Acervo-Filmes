import json

def adicionarFilme(id,nome):
    with open("src\\database\\aluguelFilmes.json", encoding='utf-8') as js:
        aluguelFilmes = json.load(js)
        
        if id in aluguelFilmes:
            aluguelFilmes[id][1]+=1
        else:
            aluguelFilmes[id] = [nome,1]
    

        aluguelFilmes = json.dumps(aluguelFilmes)

        jsonFile = open("src\\database\\aluguelFilmes.json", "w", encoding='utf-8')
        jsonFile.write(aluguelFilmes)
        jsonFile.close()

def retornaFilmesGrafico():
    with open("src\\database\\aluguelFilmes.json", encoding='utf-8') as js:
        aluguelFilmes = json.load(js)
        return aluguelFilmes