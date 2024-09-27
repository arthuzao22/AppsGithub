--
-- JUNÇÃO DAS 6 EMPRESAS QUE VEM DA OMIE, USADO PARA JUNTAR EM UMA TABELA SÓ.
--
IF OBJECT_ID('MeuBancoDeDados.dbo.CASADAGRAFICA', 'U') IS NOT NULL
DROP TABLE MeuBancoDeDados.dbo.CASADAGRAFICA;

SELECT data_emissao, codigo_categoria, codigo_cliente_fornecedor, status_titulo, EMPRESA = 'CDG', observacao = '', valor_documento, valor_liq = '', data_vencimento, data_baixa = '', chave_nfe, id_conta_corrente
INTO MeuBancoDeDados.DBO.CASADAGRAFICA
FROM MeuBancoDeDados.[dbo].[CONTAS_A_RECEBER_CDG]
union all							  
SELECT data_emissao, codigo_categoria, codigo_cliente_fornecedor, status_titulo, EMPRESA = 'BENJAMIN', observacao = '', valor_documento, valor_liq = '', data_vencimento, data_baixa = '',chave_nfe, id_conta_corrente
FROM MeuBancoDeDados.[dbo].[CONTAS_A_RECEBER_BENJAMIN]
union all
SELECT data_emissao, codigo_categoria, codigo_cliente_fornecedor, status_titulo, EMPRESA = 'GRAFICA EDUCA', observacao = '', valor_documento, valor_liq = '', data_vencimento, data_baixa = '', chave_nfe, id_conta_corrente
FROM MeuBancoDeDados.[dbo].[CONTAS_A_RECEBER_GRAFICA_EDUCA]
union all
SELECT data_emissao, codigo_categoria, codigo_cliente_fornecedor, status_titulo, EMPRESA = 'ITAMAR', observacao = '', valor_documento, valor_liq = '', data_vencimento, data_baixa = '', chave_nfe, id_conta_corrente
FROM MeuBancoDeDados.[dbo].[CONTAS_A_RECEBER_ITAMAR]
union all
SELECT data_emissao, codigo_categoria, codigo_cliente_fornecedor, status_titulo, EMPRESA = 'SITE', observacao = '', valor_documento, valor_liq = '', data_vencimento, data_baixa = '', chave_nfe, id_conta_corrente
FROM MeuBancoDeDados.[dbo].[CONTAS_A_RECEBER_SITE]
union all
SELECT data_emissao, codigo_categoria, codigo_cliente_fornecedor, status_titulo, EMPRESA = 'CDF', observacao = '', valor_documento, valor_liq = '', data_vencimento, data_baixa = '', 'chave_nfe', id_conta_corrente
FROM MeuBancoDeDados.[dbo].[CONTAS_A_RECEBER_CDF]


-- ELEMINAÇÃO DE TODAS AS CONTAS ONDE NÃO HÁ NOTAS FISCAIS 
IF OBJECT_ID('tempdb..#TirandoNotasFiscais') IS NOT NULL
DROP TABLE #TirandoNotasFiscais;

SELECT * 
INTO #TirandoNotasFiscais
FROM MeuBancoDeDados.dbo.CASADAGRAFICA
WHERE chave_nfe IS NOT NULL


-- JUNÇÃO DE TODAS BASES DE DADOS - GERAL
IF OBJECT_ID('tempdb..#FILTROCLIENTES') IS NOT NULL
DROP TABLE #FILTROCLIENTES;
SELECT 
A.data_emissao, A.codigo_categoria ,B.NOME_FANTASIA, CONDICAO = ' ' ,A.status_titulo, A.EMPRESA, A.observacao, A.valor_documento, valor_liq = '', A.data_vencimento, A.data_baixa, A.id_conta_corrente
INTO #FILTROCLIENTES
FROM #TirandoNotasFiscais A
LEFT JOIN CLIENTES.dbo.CLIENTES_GERAL B
ON A.codigo_cliente_fornecedor = B.codigo_cliente_omie

IF OBJECT_ID('tempdb..#FILTROCATEGORIAS') IS NOT NULL
DROP TABLE #FILTROCATEGORIAS;
SELECT 
A.data_emissao, B.NOME ,A.NOME_FANTASIA, CONDICAO = ' ' ,A.status_titulo, A.EMPRESA, A.observacao, A.valor_documento, valor_liq = '', A.data_vencimento, A.data_baixa, A.id_conta_corrente
INTO #FILTROCATEGORIAS
FROM #FILTROCLIENTES A
LEFT JOIN CATEGORIAS.DBO.CATEGORIAS B
ON A.CODIGO_CATEGORIA = B.ID

--
IF OBJECT_ID('tempdb..#RESULT_FINAL') IS NOT NULL
DROP TABLE #RESULT_FINAL;
SELECT 
		A.DATA_EMISSAO, 
		A.NOME AS CATEGORIA,
		A.NOME_FANTASIA AS RECEITA, 
		CONDICAO = ' ' ,
		A.status_titulo, 
		A.EMPRESA, 
		A.observacao,
		A.valor_documento AS VALOR_BRUTO, 
		valor_liq = '', 
		A.data_vencimento, 
		A.data_baixa, 
		B.CONTA
INTO #RESULT_FINAL
FROM #FILTROCATEGORIAS A
LEFT JOIN CONTAS_BANCO.DBO.CONTAS_DE_BANCO B
ON A.id_conta_corrente = B.CODIGO
WHERE CONTA IS NOT NULL

SELECT * FROM #RESULT_FINAL
---------------------------------------------------------------------------------------------------------------



