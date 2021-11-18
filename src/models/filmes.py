import requests

class filmes():
    def getFilmesEmCartaz(self):
        emCartaz = "https://api.themoviedb.org/3/movie/now_playing?api_key=540095a1bf72e74dd8872af32ee83ef2&language=pt-BR"
        req = requests.get(emCartaz)
        req = req.json()
        return req['results']

    def getFilmes(self,nome):
        filmes = f"https://api.themoviedb.org/3/search/movie?api_key=540095a1bf72e74dd8872af32ee83ef2&language=pt-BR&query={nome}"
        req = requests.get(filmes)
        req = req.json()
        return req['results']
    
    def getRecomendacao(self,id):
        recomendacao = f"https://api.themoviedb.org/3/movie/{id}/similar?api_key=540095a1bf72e74dd8872af32ee83ef2&language=pt-BR"
        req = requests.get(recomendacao)
        req = req.json()
        return req['results']

    def getReviews(self,id):
        reviews = f"https://api.themoviedb.org/3/movie/{id}/reviews?api_key=540095a1bf72e74dd8872af32ee83ef2&language=pt-BR"
        req = requests.get(reviews)
        req = req.json()
        return req['results']

    def getFilmesAtores(self,ator):
        atorFilmes = f"https://api.themoviedb.org/3/search/person?api_key=540095a1bf72e74dd8872af32ee83ef2&language=pt-BR&query={ator}"
        req = requests.get(atorFilmes)
        req = req.json()
        return req['results']

    def getPopulares(self):
        populares = "https://api.themoviedb.org/3/movie/popular?api_key=540095a1bf72e74dd8872af32ee83ef2&language=pt-BR"
        req = requests.get(populares)
        req = req.json()
        return req['results']

    def getProximosFilmes(self):
        proximosFilmes = "https://api.themoviedb.org/3/movie/upcoming?api_key=540095a1bf72e74dd8872af32ee83ef2&language=pt-BR"
        req = requests.get(proximosFilmes)
        req = req.json()
        return req['results']