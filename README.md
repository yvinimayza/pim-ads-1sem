# 📚 Plataforma de Educação Digital 🚀

## 🎯 Objetivo do Projeto
Este projeto foi desenvolvido para auxiliar alunos no aprendizado de **lógica computacional, estatísticas e segurança digital** de forma interativa.  

Ele conta com **cadastro de usuários**, **análise estatística**, **proteção de dados** e **visualização gráfica** para facilitar a interpretação dos resultados.

---

## 🛠️ Tecnologias Utilizadas
O projeto foi construído utilizando as seguintes tecnologias e bibliotecas:
- **Python** → Linguagem principal para desenvolvimento
- **JSON** → Para armazenamento de dados dos usuários
- **Cryptography** → Para proteger as informações com criptografia
- **Matplotlib** → Para gerar gráficos de análise dos estudantes
- **Git/GitHub** → Para versionamento de código e colaboração

---

## 📂 Estrutura do Projeto
A organização dos arquivos segue esta estrutura:

📁 meu-projeto/
 ├── 📂 data/                 # Armazena dados dos usuários e chave de criptografia
 │   ├── usuarios.json        # Banco de dados dos alunos
 │   ├── usuarios_protegidos.json  # Dados criptografados
 │   ├── chave.key            # Chave de criptografia
 │
 ├── 📂 scripts/              # Códigos principais do projeto
 │   ├── usuarios.py          # Cadastro de alunos
 │   ├── estatisticas.py      # Cálculo de média, moda e mediana
 │   ├── seguranca.py         # Proteção dos dados com criptografia
 │   ├── grafico.py           # Geração de gráficos dos usuários
 │
 ├── README.md                # Documentação do projeto
 ├── requirements.txt         # Lista de dependências para instalação


---

## 🚀 Como Rodar o Projeto
### 📌 **1. Instale as dependências**
Antes de rodar o projeto, instale as bibliotecas necessárias:
bash
pip install -r requirements.txt


### 📌 **2. Execute cada funcionalidade**
✅ **Cadastrar e visualizar usuários**  
bash
python scripts/usuarios.py

✅ **Calcular estatísticas dos alunos**  
bash
python scripts/estatisticas.py

✅ **Criptografar dados para segurança**  
bash
python scripts/seguranca.py

✅ **Gerar gráficos de análise**  
bash
python scripts/grafico.py


---

## 🔒 Segurança e Criptografia
Este projeto usa **criptografia simétrica (Fernet)** para proteger os dados dos alunos. Cada usuário registrado tem suas informações armazenadas em um arquivo JSON e, posteriormente, criptografadas com uma chave gerada automaticamente.

✔️ **Para visualizar dados protegidos**, execute:  
bash
python scripts/seguranca.py

E siga as instruções no terminal.

---

## 📊 Visualização Gráfica
Os gráficos gerados mostram **correlações entre idade e tempo de estudo** dos alunos. Isso permite **interpretar padrões de aprendizado** e ajuda a ajustar estratégias educacionais.

---

## 🔗 GitHub e Versionamento
Este projeto está versionado no GitHub para permitir colaboração e melhorias contínuas.  
Para contribuir ou explorar o código, siga os passos:
bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio
```

Se quiser sugerir melhorias, faça um *pull request*! 🚀

---

## 🏆 Conclusão
Este sistema oferece uma abordagem prática e interativa para *ensinar lógica, estatísticas e segurança digital*. Ele pode ser expandido para incluir mais funcionalidades e ser integrado a plataformas educacionais maiores.