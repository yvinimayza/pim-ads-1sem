import json
import re
import getpass
import cursos
from cryptography.fernet import Fernet
from estatisticas_usuarios import exibir_estatisticas
from gerador_graficos import gerar_todos_graficos # CORRIGIDO: Adicionado 's' em 'graficos' no nome da função

# Arquivo onde os usuários são armazenados
USUARIOS_FILE = "usuarios.json"

# Carrega chave de criptografia
def load_key():
    try:
        return open("key.key", "rb").read()
    except FileNotFoundError:
        print("\033[91mErro: Arquivo de chave de criptografia não encontrado!\033[0m")
        exit()

key = load_key()
cipher = Fernet(key)

# Função para criptografar dados
def encrypt_data(data):
    return cipher.encrypt(data.encode()).decode()

# Função para descriptografar dados
def decrypt_data(encrypted_data):
    try:
        return cipher.decrypt(encrypted_data.encode()).decode()
    except Exception:
        # Retorna uma string vazia ou um valor padrão para evitar erros
        # se a descriptografia falhar, especialmente para dados que podem estar faltando.
        return "" 

# Função para carregar usuários
def carregar_usuarios():
    try:
        with open(USUARIOS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("\033[91mErro: Arquivo 'usuarios.json' está corrompido ou vazio. Criando um novo.\033[0m")
        return {} # Retorna um dicionário vazio se o JSON estiver inválido

# Função para salvar usuários
def salvar_usuarios(usuarios):
    with open(USUARIOS_FILE, "w") as file:
        json.dump(usuarios, file, indent=4)

# Função para verificar e-mail válido
def validar_email(email):
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

# Cadastro de usuário
def cadastrar():
    usuarios = carregar_usuarios()

    nome = input("Digite seu nome: ")
    
    while True:
        email = input("Digite seu email: ")
        if not validar_email(email):
            print("\033[91mE-mail inválido! Certifique-se de inserir um endereço válido.\033[0m")
        else:
            break

    senha = getpass.getpass("Crie uma senha (mínimo 8 caracteres): ")  

    if len(senha) < 8:
        print("\033[91mErro: A senha deve ter no mínimo 8 caracteres!\033[0m")
        return

    if email in usuarios:
        print("\033[91mEste e-mail já está cadastrado.\033[0m")
    else:
        usuarios[email] = {
            "nome": encrypt_data(nome),
            "email": encrypt_data(email),
            "senha": encrypt_data(senha),
            "idade": encrypt_data(input("Digite sua idade: ")),
            "acessos": encrypt_data("0"),  # Inicializa número de acessos
            "tempo_uso": encrypt_data("0")  # Inicializa tempo médio de uso
        }
        salvar_usuarios(usuarios)
        print("\033[92mUsuário cadastrado com sucesso!\033[0m")

# Login
def logar():
    usuarios = carregar_usuarios()

    email = input("Digite seu email: ")

    if email not in usuarios:
        print("\033[91mE-mail não cadastrado! Verifique e tente novamente.\033[0m")
        return  

    senha = getpass.getpass("Digite sua senha: ")  

    if senha == decrypt_data(usuarios[email]["senha"]):
        print(f"\nLogin realizado com sucesso! Bem-vindo, {decrypt_data(usuarios[email]['nome'])}.\n")
        
        # --- Modificação para tratar KeyError: 'acessos' e 'tempo_uso' ---
        # Garante que as chaves 'acessos' e 'tempo_uso' existam antes de tentar acessá-las.
        # Isso é útil para usuários cadastrados antes da adição dessas chaves.
        if "acessos" not in usuarios[email]:
            usuarios[email]["acessos"] = encrypt_data("0")
        if "tempo_uso" not in usuarios[email]:
            usuarios[email]["tempo_uso"] = encrypt_data("0")

        # Atualiza estatísticas de uso
        acessos_atuais = int(decrypt_data(usuarios[email]["acessos"]))
        tempo_uso_atual = float(decrypt_data(usuarios[email]["tempo_uso"]))
        
        usuarios[email]["acessos"] = encrypt_data(str(acessos_atuais + 1))
        usuarios[email]["tempo_uso"] = encrypt_data(str(tempo_uso_atual + 0.5))  # Simulando incremento de uso
        # --- Fim da modificação ---

        salvar_usuarios(usuarios)

        menu_usuario()
    else:
        print("\033[91mSenha incorreta! Tente novamente.\033[0m")

# Recuperação de senha
def recuperar_senha():
    usuarios = carregar_usuarios()

    email = input("Digite seu e-mail para recuperar a senha: ")

    if email in usuarios:
        senha_recuperada = decrypt_data(usuarios[email]["senha"])
        print(f"\033[93mSua senha cadastrada é: {senha_recuperada}\033[0m")  
    else:
        print("\033[91mE-mail não cadastrado! Verifique e tente novamente.\033[0m")

# Menu do usuário
def menu_usuario():
    while True:
        print("\n🔹 Menu do Usuário 🔹")
        print("1. Cursos")
        print("2. Estatísticas dos Usuários")
        print("3. Gerar Gráficos") # <-- Nova opção
        print("4. Sair")          # <-- Opção Sair agora é 4

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cursos.cursos()
        elif opcao == "2":
            usuarios_atuais = carregar_usuarios()
            exibir_estatisticas(usuarios_atuais, decrypt_data)
        elif opcao == "3": # <-- Nova condição para gráficos
            usuarios_atuais = carregar_usuarios()
            gerar_todos_graficos(usuarios_atuais, decrypt_data) # CORRIGIDO: Adicionado 's' em 'graficos' no nome da função
        elif opcao == "4": # <-- Ajuste o número da opção de saída
            break
        else:
            print("\033[91mOpção inválida! Tente novamente.\033[0m")

# Menu principal
def menu():
    while True:
        print("\n🔹 Bem-vindo à EVOM - Plataforma de Educação Digital Segura 🔹")
        print("1. Logar")
        print("2. Cadastre-se")
        print("3. Esqueci a senha")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            logar()
        elif opcao == "2":
            cadastrar()
        elif opcao == "3":
            recuperar_senha()
        elif opcao == "4":
            print("\nSaindo...\n")
            break
        else:
            print("\033[91mOpção inválida! Tente novamente.\033[0m")

# Executa o menu
if __name__ == "__main__":
    menu()