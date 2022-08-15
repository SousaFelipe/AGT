from app.models.cliente import Cliente

cliente = Cliente()

response = cliente.create({
    'razao': 'TESTE CADASTRO API PYTHON',
    'tipo_assinante': 3,
    'tipo_pessoa': 'F',
    'cnpj_cpf': '025.076.083-58',
    'ie_identidade': '200812945685',
    'rg_orgao_emissor': 'SSP',
    'contribuinte_icms': 'N',
    'data_nascimento': '10/11/1996',
    'ativo': 'S',
    'filial_id': 1,
    'Sexo': 'M',
    'data_cadastro': '',
    'tipo_cliente_scm': '03',
    'cep': '63800-000',
    'endereco': 'ENDERECO TESTE',
    'numero': 'SN',
    'complemento': 'COMPLEMENTO TESTE',
    'bairro': 'BAIRRO TESTE',
    'cidade': 1040,
    'referencia': 'REFERENCIA TESTE',
    'tipo_localidade': 'R',
    'fone': '(88) 9 8188-1375',
    'telefone_comercial': '(88) 9 8188-1375',
    'telefone_celular': '(88) 9 8188-1375',
    'whatsapp': '(88) 9 8188-1375',
    'contato': 'sousa.felipe@outlook.com',
    'hotsite_email': 'flpssdocarmo@gmail.com',
    'senha': '12345678',
    'acesso_automatico_central': 'P',
    'alterar_senha_primeiro_acesso': 'P',
    'senha_hotsite_md5': 'N',
    'iss_classificacao_padrao': 99,
    'obs': '',
    'alerta': ''
})

print(response.is_ok())
print(response.get_type())
print(response.get_message())
