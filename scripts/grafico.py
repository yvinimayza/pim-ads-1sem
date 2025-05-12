import json
import matplotlib.pyplot as plt

# Carregar os dados dos usuários
with open("data/usuarios.json", "r") as file:
    dados = json.load(file)

if not dados:
    print("\n❌ Nenhum usuário cadastrado para gerar gráficos.")
else:
    idades = [usuario["idade"] for usuario in dados]
    tempos = [usuario["tempo_estudo"] for usuario in dados]

    # Criar gráfico de barras
    plt.figure(figsize=(8,5))
    plt.bar(idades, tempos, color='royalblue')
    plt.xlabel("Idade dos alunos")
    plt.ylabel("Tempo de estudo (horas)")
    plt.title("📊 Tempo de estudo por idade")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()