import json
import os

# Caminho do arquivo JSON
usuarios_path = "data/usuarios.json"

# Verificar se o arquivo já existe, caso contrário, criar um vazio
if not os.path.exists(usuarios_path):
    with open(usuarios_path, "w") as file:
        json.dump([], file)

def carregar_usuarios():
    """Carrega os usuários do arquivo JSON."""
    with open(usuarios_path, "r") as file:
        return json.load(file)

def salvar_usuarios(usuarios):
    """Salva os usuários no arquivo JSON."""
    with open(usuarios_path, "w") as file:
        json.dump(usuarios, file, indent=4)

def adicionar_usuario():
    """Adiciona um novo usuário ao sistema."""
    usuarios = carregar_usuarios()
    
    nome = input("\n➡️ Digite seu nome: ")
    idade = int(input("➡️ Digite sua idade: "))
    estudo = float(input("➡️ Quantas horas você estuda por dia? "))

    usuario = {"nome": nome, "idade": idade, "tempo_estudo": estudo}
    usuarios.append(usuario)  # Adiciona ao JSON corretamente

    salvar_usuarios(usuarios)  # Agora salva SEM apagar os anteriores!
    print("\n✅ Usuário cadastrado com sucesso!\n")

def mostrar_usuarios():
    """Mostra a lista de usuários cadastrados."""
    usuarios = carregar_usuarios()
    
    if not usuarios:
        print("\n❌ Nenhum usuário cadastrado ainda!")
    else:
        print("\n📜 Lista de usuários cadastrados:")
        for usuario in usuarios:
            print(f"👤 Nome: {usuario['nome']}, Idade: {usuario['idade']}, Estudo: {usuario['tempo_estudo']} horas/dia")

# Criar um menu de opções
while True:
    print("\n=== MENU ===")
    print("1️⃣ Cadastrar novo usuário")
    print("2️⃣ Mostrar usuários cadastrados")
    print("3️⃣ Sair")

    escolha = input("➡️ Escolha uma opção: ")

    if escolha == "1":
        adicionar_usuario()
    elif escolha == "2":
        mostrar_usuarios()
    elif escolha == "3":
        print("\n👋 Saindo do programa!")
        break
    else:
        print("\n❌ Opção inválida. Tente novamente.")