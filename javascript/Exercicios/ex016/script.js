function contar(){
    var ini = document.getElementById('inicio')
    var fim = document.getElementById('fim')
    var passo = document.getElementById('passo')
    var res = document.querySelector('div#res')

    var cinicio = Number(ini.value)
    var cfim = Number(fim.value)
    var cpasso = Number(passo.value)
    var emoji = "&#128073"
    var contador = cinicio
    var texto = ''

    if ( cinicio = 0 || cpasso <= 0 || cfim <= 0 ) {
         alert('Erro! Preencha todos os dados corretamente.')
    } else if (cinicio < cfim) {

        while (contador <= cfim) {
            texto += emoji + ' ' + contador
            contador += cpasso
        }

    } else {
        while ( contador >= cfim) {
            texto += emoji + ' ' + contador
            contador -= passo
        }
    }
    
    var titulo = document.createElement('p')
        titulo.innerHTML = 'Contando....:'
        res.appendChild(titulo)

        var contagem = document.createElement('p')
        contagem.innerHTML = texto
        res.appendChild(contagem)
}