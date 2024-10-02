import json 

#classe ArquivosJson
class Manipulador:
    #criar arquivo json do 0
    def criar_arquivo(self, nome_arquivo):
        try:
            #lista de dicionarios
            usuarios= [
                {
                    #admin é criado para cada novo arquivo json
                    #assim que gerar o arquivo json, ele sera gerado com esses dados daqui
                    'codigo':0,
                    'nome':'admin',
                    'cpf':'000.000.000-00',
                    'e-mail':'admin@admin.com.br',
                    'profissao':'Administrador'
                }
            ]

            #serialisar objeto python como json (consigo ao inves de transcrever os dados, voce ira adicionar, assim ele le como um dicionario)
            #pegar o dicionario criado acima, e converter ele pro json, e convertendo ele, voce consegue gravar num arquivo.json

            #serializar: pega objeto python e converter o dicionario para um objeto json (nao para arquivo ainda), vai entender que o objeto é um json
            json_dados = json.dumps(usuarios)    #arquivo nao existe ainda

            #gravacao de arquivo, cria o arquivo .json / 'w': parametro que tem que colocar de forma obrigatoria(quer ler o arquivo?'r' (r: read)/ quer escrever o arquivo?'w'(w: write))
            with open(f'{nome_arquivo}.json','w',encoding='utf-8') as f:
                f.write(json_dados)
            return f'{nome_arquivo}.json foi criado com sucesso'

        except Exception as e:
            return f'Não foi possível criar o arquivo. {e}.'

    def abrir_arquivo(self, nome_arquivo):
        #deserializando: pegar objeto json e converte em dicionario
        with open(f'{nome_arquivo}.json','r',encoding='utf-8') as f:
            dados = json.load(f)
        return dados

    def salvar_dados(self, usuarios, nome_arquivo):
        try:
            with open(f'{nome_arquivo}.json','w',encoding='utf-8') as f:
                json.dump(usuarios, f) #dump: o arquivo ja existe, quer acrescentar novos dados
            return f'Dados gravados com sucesso.'

        except Exception as e:
            return f'Não foi possível salvar os dados. {e}.'

    #destrutor
    def __del__(self):
        return f'Manipulador destruído.'
    
