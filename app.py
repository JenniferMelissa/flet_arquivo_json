import json
import flet as ft
from manipulador import * 



def main(page: ft.Page):
    manipulador = Manipulador()

    def criar_arquivo(e):
        nome_arquivo = nome_arquivo_input.value
        resultado = manipulador.criar_arquivo(nome_arquivo)
        resultado_text.value = resultado
        page.update()

    def abrir_arquivo(e):
        nome_arquivo = nome_arquivo_input.value
        dados = manipulador.abrir_arquivo(nome_arquivo)
        resultado_text.value = json.dumps(dados, indent=4)
        page.update()

    def cadastro_usuario(e):
       
        try:
            print(f'Arquivo aberto: {abrir_arquivo}.json.\n')
            usuarios = Manipulador.abrir_arquivo(abrir_arquivo)
            p_codigo = len(usuarios)
            p_nome = ft.TextField(label="Informe o nome:")
            p_cpf = ft.TextField(label="Informe o CPF:")
            p_email = ft.TextField(label="Informe o e-mail:")
            p_profissao = ft.TextField(label="Informe a profissão:")

            def salvar_usuario(e):
                usuario = {
                    "codigo": p_codigo,
                    "nome": p_nome.value,
                    "cpf": p_cpf.value,
                    "email": p_email.value,
                    "profissao": p_profissao.value
                }
                usuarios.append(usuario)
                print(f'Usuário salvo: {usuario}')
                # Aqui você pode adicionar a lógica para salvar os dados    no arquivo
                # print(m.salvar_dados(usuarios, abrir_arquivo))

            salvar_button = ft.ElevatedButton(text="Salvar",    on_click=salvar_usuario)

            page.add(p_nome, p_cpf, p_email, p_profissao, salvar_button)

        except Exception as e:
            print(f'Não foi possível realizar a operação. {e}.')

  
    def alterar_dados_usuario(e):
        try:
            print(f'Arquivo aberto: {abrir_arquivo}.json.\n')

            usuarios = Manipulador.abrir_arquivo(abrir_arquivo)    

            codigo = int(input('Informe o código do usuário que deseja  alterar os dados: '))
            

            for campo in usuarios[codigo]:
                print(f'Valor atual do campo: {campo}: {usuarios[codigo].   get(campo)}')
                novo_dado = input(f'Informe o novo dado do campo {campo}    ou aperte "Enter" caso deseje manter o mesmo valor: ')
                if novo_dado:
                    usuarios[codigo][campo] = novo_dado
                else:
                    pass
                
            print(manipulador.salvar_dados(usuarios, abrir_arquivo))
        
        except Exception as e:
            print('Não foi possível alterar os dados.')
        
        finally:
            pass

    def deletar_usuario(e):
        nome_arquivo = nome_arquivo_input.value
        codigo = int(codigo_input.value)
        resultado = manipulador.deletar_usuario(nome_arquivo, codigo)
        resultado_text.value = resultado
        page.update()



    nome_arquivo_input = ft.TextField(label="Nome do Arquivo")
    codigo_input = ft.TextField(label="Código do Usuário")
    resultado_text = ft.Text()
    salvar_button = ft.ElevatedButton(text="Salvar", on_click=cadastro_usuario)

    page.add(
        nome_arquivo_input,
        ft.Row([
            ft.ElevatedButton("Criar Arquivo", on_click=criar_arquivo),
            ft.ElevatedButton("Abrir Arquivo", on_click=abrir_arquivo),
            ft.ElevatedButton("Salvar Dados", on_click=cadastro_usuario),
            ft.ElevatedButton("Alterar Usuário", on_click=alterar_dados_usuario),
            ft.ElevatedButton("Deletar Usuário", on_click=deletar_usuario),
        ]),
        cadastro_usuario, salvar_button,
        codigo_input,
        resultado_text
    )

ft.app(target=main)
