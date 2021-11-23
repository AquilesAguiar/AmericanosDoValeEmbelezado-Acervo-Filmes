google.charts.load('current', {packages: ['corechart', 'bar']});
google.charts.setOnLoadCallback(graficoFilmes);

async function graficoFilmes() {
    let dadosGrafico = await fetch("http://127.0.0.1:8787/filmes/filmesGrafico")
    let res = await dadosGrafico.json();
    
    let listaFilmes = []
    const cont = 0
    for (const key in res) {
        if (cont==10) {
            return;
        }
        listaFilmes.push([res[key][0],res[key][1]])
    }
    
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Filmes');
    data.addColumn('number', 'Qtd alugueis');

    console.log(listaFilmes)
    data.addRows(listaFilmes)
    

    var options = {
    title: '10 filmes mais alugados do site',
    colors: ['#9575cd'],
    hAxis: {
        title: 'Filmes',
        viewWindow: {
        min: [7, 30, 0],
        max: [17, 30, 0]
        }
    },
    vAxis: {
        title:'Quantidade de alugueis' 
    }
    };

    var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
    chart.draw(data, options);
}