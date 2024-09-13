let 
    body = Json.FromValue([
        call = "LIstarClientes",
        app_key = app_key,
        app_secret = app_secret,
        param = {
            [
                pagina = 1,
                registros_por_pagina = 100,
                apenas_importado_api = "N"
            ]
        }
    ]),
    header = [
        #"Content-type" = "application/json"
    ],
    request = Json.Document(
        Web.Contents(
            "http://app.omie.com.br/api/v1",
            [
                RelativePath = "/geral/clientes/",
                Headers = header,
                Content = body
            ]
        )
        ,
        1252
    ),
    clientes_cadastro = request[clientes_cadastro]
in
    clientes_cadastro