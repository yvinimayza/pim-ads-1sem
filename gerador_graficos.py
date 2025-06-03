import matplotlib.pyplot as plt
import numpy as np

# Função para gerar um único gráfico comparando usuários
def gerar_grafico_comparativo_usuarios(usuarios_data, decrypt_function):
    if not usuarios_data:
        print("\033[91mNenhum usuário cadastrado para gerar o gráfico comparativo.\033[0m")
        return

    nomes_usuarios = []
    idades = []
    acessos = []
    tempo_uso = []

    for email, dados in usuarios_data.items():
        try:
            nome = decrypt_function(dados.get("nome", "Usuário Desconhecido"))
            idade_str = decrypt_function(dados.get("idade", "0"))
            acessos_str = decrypt_function(dados.get("acessos", "0"))
            tempo_uso_str = decrypt_function(dados.get("tempo_uso", "0"))

            # Adicionar apenas se os dados forem válidos
            # E garantir que os valores convertidos sejam tratados para o gráfico
            idade_val = int(idade_str) if idade_str.isdigit() else 0
            acessos_val = int(acessos_str) if acessos_str.isdigit() else 0
            tempo_uso_val = float(tempo_uso_str) if tempo_uso_str.replace(".", "", 1).isdigit() else 0.0

            # Adicione o usuário apenas se tivermos pelo menos um dado significativo
            if idade_val > 0 or acessos_val > 0 or tempo_uso_val > 0:
                nomes_usuarios.append(nome)
                idades.append(idade_val)
                acessos.append(acessos_val)
                tempo_uso.append(tempo_uso_val)
            else:
                print(f"\033[93mAviso: Dados insuficientes para o usuário {nome}. Ignorando no gráfico comparativo.\033[0m")
        except Exception as e:
            print(f"\033[91mErro ao processar dados do usuário para o gráfico comparativo: {e}\033[0m")

    if not nomes_usuarios:
        print("\033[91mDados válidos insuficientes para gerar o gráfico comparativo de usuários.\033[0m")
        return

    # Definir a largura das barras e as posições para os grupos
    bar_width = 0.25 # Aumenta um pouco a largura das barras
    index = np.arange(len(nomes_usuarios)) # Posições para os nomes dos usuários

    plt.style.use('seaborn-v0_8-darkgrid') # Usa um estilo mais agradável para o gráfico
    plt.figure(figsize=(15, 8)) # Aumenta o tamanho da figura para melhor visualização

    # Cores personalizadas para as barras
    colors = ['#66c2e3', '#8cd98c', '#ff9999'] # Azul, Verde, Rosa

    # Barras para Idade
    bars1 = plt.bar(index - bar_width, idades, bar_width, label='Idade', color=colors[0])

    # Barras para Número de Acessos
    bars2 = plt.bar(index, acessos, bar_width, label='Acessos', color=colors[1])

    # Barras para Tempo de Uso
    bars3 = plt.bar(index + bar_width, tempo_uso, bar_width, label='Tempo de Uso (horas)', color=colors[2])

    # Adicionar os valores nas barras
    def add_values_on_bars(bars):
        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, yval + 0.1, round(yval, 1), ha='center', va='bottom', fontsize=9) # Ajuste 0.1 para espaçamento

    add_values_on_bars(bars1)
    add_values_on_bars(bars2)
    add_values_on_bars(bars3)

    plt.xlabel('Usuário', fontsize=12)
    plt.ylabel('Valor', fontsize=12) # Eixo Y com escala variada, manter como 'Valor'
    plt.title('Comparativo de Dados por Usuário', fontsize=16, fontweight='bold')
    plt.xticks(index, nomes_usuarios, rotation=45, ha='right', fontsize=10) # Nomes dos usuários no eixo X
    plt.yticks(fontsize=10) # Ajusta o tamanho da fonte dos ticks do eixo Y
    plt.legend(fontsize=10, loc='upper left') # Mostra a legenda das barras e ajusta a posição
    plt.grid(axis='y', linestyle='--', alpha=0.5) # Linhas de grade mais suaves

    # Ajustar o limite do eixo Y para dar um pouco de espaço acima das barras
    # Encontra o valor máximo entre todas as barras e adiciona uma margem
    max_val = max(max(idades), max(acessos), max(tempo_uso)) if idades or acessos or tempo_uso else 0
    plt.ylim(0, max_val * 1.2) # Aumenta o limite Y em 20% acima do maior valor

    plt.tight_layout() # Ajusta o layout para não cortar rótulos
    plt.show()

# A função principal para gerar todos os gráficos permanece a mesma:
def gerar_todos_graficos(usuarios_data, decrypt_function):
    print("\nGerando gráfico comparativo de usuários...")
    gerar_grafico_comparativo_usuarios(usuarios_data, decrypt_function)
    print("\nGráfico gerado com sucesso!")