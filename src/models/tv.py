import requests

class tv ():
    def getProgramas(self,nome):
        pesqTv = f"https://api.themoviedb.org/3/search/tv?api_key=540095a1bf72e74dd8872af32ee83ef2&language=pt-BR&page=1&query={nome}&include_adult=false"
        req = requests.get(pesqTv)
        req = req.json()
        return req['results']

    def getMelhoresProgramas(self):
        melhoresPrograma ="https://api.themoviedb.org/3/tv/top_rated?api_key=540095a1bf72e74dd8872af32ee83ef2&language=pt-BR"
        req = requests.get(melhoresPrograma)
        req = req.json()
        return req['results']

    def getProgramasDetalhes(self,idPrograma):
        programaDetalhes = f"https://api.themoviedb.org/3/tv/{idPrograma}?api_key=540095a1bf72e74dd8872af32ee83ef2&language=pt-BR"
        req = requests.get(programaDetalhes)
        req = req.json()
        return req['results']
    
    def getProgramasEp (self,idPrograma,numeroTemp):
        temporadas = f"https://api.themoviedb.org/3/tv/{idPrograma}/season/{numeroTemp}?api_key=540095a1bf72e74dd8872af32ee83ef2&language=pt-BR"
        req = requests.get(temporadas)
        req = req.json()
        return req['results']
    
    def getDetalhesEp(self,idPrograma,numeroTemp,episodio):
        episodios = f"https://api.themoviedb.org/3/tv/{idPrograma}/season/{numeroTemp}/episode/{episodio}?api_key=540095a1bf72e74dd8872af32ee83ef2&language=pt-BR"
        req = requests.get(episodios)
        req = req.json()
        return req['results']




