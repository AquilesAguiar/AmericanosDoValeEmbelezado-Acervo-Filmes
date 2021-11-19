var botaoPesq = document.getElementById("botaoPesq")

botaoPesq.addEventListener("click", async function(){
    var pesqFilmes = document.getElementById("pesqFilmes")
    var filme = pesqFilmes.value
    window.location.href = `http://127.0.0.1:8787/filmes/pesquisa?filme=${filme}`;
})
