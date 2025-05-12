from cryptography.fernet import Fernet
import json

# Criar chave de criptografia e salvar
chave = Fernet.generate_key()
with open("data/chave.key", "wb") as chave_file:
    chave_file.write(chave)

fernet = Fernet(chave)

# Carregar e criptografar dados dos usuários
with open("data/usuarios.json", "r") as file:
    dados = json.load(file)

dados_str = json.dumps(dados)
dados_criptografados = fernet.encrypt(dados_str.encode())

# Salvar dados protegidos
with open("data/usuarios_protegidos.json", "wb") as file:
    file.write(dados_criptografados)

print("\n✅ Dados criptografados com sucesso!")