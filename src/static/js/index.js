var botaoPesq = document.getElementById("botaoPesq")

botaoPesq.addEventListener("click", async function(){
    var pesqFilmes = document.getElementById("pesqFilmes")
    var filme = pesqFilmes.value
    window.location.href = `http://127.0.0.1:8787/filmes/pesquisa?filme=${filme}`;
})





var aluguelConfirma = document.getElementById("aluguelConfirma")

aluguelConfirma.addEventListener("click", async function(){
    let titularCartao = document.getElementById("titularCartao").value
    let cartao = document.getElementById("cartao").value
    let CVV = document.getElementById("CVV").value
    let venct = document.getElementById("venct").value
    let id = document.getElementById("idFilme").value
    await fetch(`http://127.0.0.1:8787/filmes/finalizarAlugar`,{
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({titularCartao: titularCartao, cartao: cartao,CVV:CVV,venct:venct,id:id})
      })
    document.getElementById("alertaAluguel").style.display="inline-block"
})


var fechaAlert = document.getElementById("fechaAlert")
fechaAlert.addEventListener("click", function(){
    document.getElementById("alertaAluguel").style.display="none"
})