let cep = document.querySelector('#cep');

cep.addEventListener('blur', function(e){
    let cep = e.target.value;
    let script = document.createElement('script')
    script.src = 'https://viacep.com.br/ws/'+cep+'/json/?callback=endereçoForm';
    document.body.appendChild(script)
})

function endereçoForm(resposta){
    let estado = document.querySelector('#estado');
    let cidade = document.querySelector('#cidade');
    let logradouro = document.querySelector('#logradouro');
    estado.value = resposta.uf;
    cidade.value = resposta.localidade;
    logradouro.value = resposta.logradouro;
    let username = document.querySelector('#username').focus();
}