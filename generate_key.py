from cryptography.fernet import Fernet

# Gera uma chave de criptografia
key = Fernet.generate_key()

# Salva a chave em um arquivo
with open("key.key", "wb") as key_file:
    key_file.write(key)

print("Chave de criptografia gerada e salva corretamente em key.key!")
