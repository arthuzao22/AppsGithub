var username = '25370117000198'; // Substitua pelo seu login
var password = 'Cdg102030'; // Substitua pela sua senha
var authorizationBasic = btoa(username + ':' + password); // Codificando em Base64

$.ajax({
    type: 'GET',
    url: 'https://api.braspress.com/v1/tracking/25370117000198/0/json',  // Substitua pelos valores corretos de CNPJ e Nota Fiscal
    dataType: 'json',  // Define que o retorno será no formato JSON
    contentType: 'application/json; charset=utf-8',
    xhrFields: {
        withCredentials: true
    },
    crossDomain: true,
    headers: {
        'Authorization': 'Basic ' + authorizationBasic,  // Insere a autenticação
    },
    success: function (result) {
        console.log(result);  // Manipule o resultado com a resposta da API
    },
    error: function (req, status, error) {
        console.error('Erro:', error);  // Exibe o erro no console
    }
});
