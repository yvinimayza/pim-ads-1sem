import json
import statistics
import os

# Arquivo de usuários
USUARIOS_FILE = "usuarios.json"

# Função para limpar a tela
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para calcular estatísticas reais dos usuários cadastrados
# Agora, ela recebe 'usuarios' e 'decrypt_func' como argumentos
def calcular_estatisticas_reais(usuarios, decrypt_func):
    if not usuarios:
        print("\033[91mNenhum usuário cadastrado para calcular estatísticas.\033[0m")
        return

    idades = []
    acessos = []
    tempo_uso = []

    for dados in usuarios.values():
        try:
            # Use decrypt_func passada como argumento
            idade = decrypt_func(dados.get("idade", "0"))
            acessos_usuario = decrypt_func(dados.get("acessos", "0"))
            tempo_usuario = decrypt_func(dados.get("tempo_uso", "0"))

            # Certifica-se de que a idade seja um número antes de adicionar
            idades.append(int(idade) if idade.isdigit() else 0)
            acessos.append(int(acessos_usuario) if acessos_usuario.isdigit() else 0)
            tempo_uso.append(float(tempo_usuario) if tempo_usuario.replace(".", "", 1).isdigit() else 0)
        except Exception as e:
            print(f"\033[91mErro ao processar dados do usuário: {e}\033[0m")

    def calcular(dados, nome):
        if not dados or all(v == 0 for v in dados):
            print(f"\n🔹 Estatísticas de {nome}: \033[91mDados insuficientes.\033[0m")
            return

        media = statistics.mean(dados)
        try:
            moda = statistics.mode(dados)
        except statistics.StatisticsError:
            moda = "Sem moda definida (valores repetidos igualmente)"
        mediana = statistics.median(dados)

        print(f"\n🔹 Estatísticas de {nome}:")
        print(f"📊 Média: {media:.2f}")
        print(f"🎯 Moda: {moda}")
        print(f"📈 Mediana: {mediana}\n")

    # Exibir estatísticas reais dos usuários cadastrados
    calcular(idades, "Idade dos Usuários")
    calcular(acessos, "Número de Acessos")
    calcular(tempo_uso, "Tempo Médio de Uso")

# Função para exibir estatísticas no menu
# AQUI ESTÁ A CORREÇÃO: ADICIONE 'usuarios_data' E 'decrypt_function' COMO PARÂMETROS
def exibir_estatisticas(usuarios_data, decrypt_function):
    clear()
    print("\n📊 **Estatísticas dos Usuários Cadastrados**")
    calcular_estatisticas_reais(usuarios_data, decrypt_function)