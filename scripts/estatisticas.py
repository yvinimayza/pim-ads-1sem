import json
import statistics

# Carregar dados dos usuários
with open("data/usuarios.json", "r") as file:
    dados = json.load(file)

tempos = [usuario["tempo_estudo"] for usuario in dados]
idades = [usuario["idade"] for usuario in dados]

# Calcular estatísticas
media_estudo = statistics.mean(tempos)
moda_estudo = statistics.mode(tempos)
mediana_estudo = statistics.median(tempos)

media_idade = statistics.mean(idades)
moda_idade = statistics.mode(idades)
mediana_idade = statistics.median(idades)

# Exibir os resultados
print("\n📊 Estatísticas dos alunos cadastrados:")
print(f"🕒 Média de estudo diário: {media_estudo:.2f} horas")
print(f"📈 Moda de estudo: {moda_estudo} horas")
print(f"📊 Mediana de estudo: {mediana_estudo} horas")
print("\n📏 Estatísticas sobre idade dos alunos:")
print(f"🔎 Média de idade: {media_idade:.1f} anos")
print(f"🎯 Moda da idade: {moda_idade} anos")
print(f"📊 Mediana da idade: {mediana_idade} anos")