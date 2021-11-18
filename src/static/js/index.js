var botaoPesq = document.getElementById("botaoPesq")

botaoPesq.addEventListener("click", async function(){
    var pesqFilmes = document.getElementById("pesqFilmes")
    var filme = pesqFilmes.value
    await fetch(`http://127.0.0.1:8787/filmes/pesquisa?filme=${filme}`,
    {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({"filme": filme})
    }
    );
})