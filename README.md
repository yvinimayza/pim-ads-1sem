<<<<<<< HEAD
# pim-ads-1sem
Projeto Integrado Multidisciplinar do 1º semestre de ADS
=======
# EVOM - Plataforma de Educação Digital Segura


Este é o Projeto Integrado Multidisciplinar (PIM) do 1º Semestre de 2025 do curso Análise e Desenvolvimento de Sistemas da Universidade Paulista (UNIP).

## 🚀 Visão Geral do Projeto

A **EVOM** é uma plataforma de educação digital segura, desenvolvida para promover a inclusão tecnológica e a educação digital em comunidades carentes e estudantes de escolas públicas. Focada em pensamento lógico computacional, infraestrutura computacional e cibersegurança, a plataforma oferece conteúdo interativo sobre tecnologia da informação, programação básica e boas práticas de segurança digital. O projeto assegura a proteção dos dados dos usuários, respeitando a LGPD e princípios éticos, e promove a cidadania digital.

## ✨ Funcionalidades Implementadas

* **Sistema de Autenticação Robusto:**
    * Cadastro de novos usuários com validação de e-mail e senha segura.
    * Login de usuários existentes.
    * Funcionalidade de recuperação de senha.
    * **Segurança:** Dados sensíveis (nome, e-mail, senha, idade, acessos, tempo de uso) são **criptografados** usando `cryptography.fernet` antes do armazenamento.
* **Gestão de Usuários e Estatísticas Detalhadas:**
    * Registro de acessos (simulado) e tempo de uso (simulado) por sessão de usuário.
    * Cálculo e exibição de estatísticas descritivas (Média, Moda, Mediana) para idade, número de acessos e tempo de uso dos usuários.
    * Geração de **gráficos comparativos** interativos (`matplotlib`) para visualizar o perfil e o engajamento de cada usuário.
* **Módulos Educacionais:**
    * Menu para acesso a diferentes áreas de cursos.
* **Armazenamento de Dados:**
    * Utiliza arquivos JSON (`usuarios.json`) para persistência de dados de forma estruturada.

## 📦 Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Bibliotecas Principais:**
    * `json`: Para manipulação de arquivos JSON.
    * `re`: Para validação de e-mail (Expressões Regulares).
    * `getpass`: Para entrada segura de senhas no terminal.
    * `cryptography`: Para criptografia e descriptografia de dados.
    * `matplotlib`: Para geração de gráficos visualmente atraentes.
    * `numpy`: Auxiliar na manipulação e preparação de dados para gráficos.

## 📂 Estrutura do Projeto

O projeto `EVOM` mantém uma estrutura de arquivos simplificada, com todos os módulos e dados principais localizados na pasta raiz do projeto para fácil acesso e execução:

EVOM/
├── pycache/             # Cache de bytecode do Python
├── cursos.py                # Módulo para o conteúdo dos cursos
├── estatisticas_usuarios.py # Módulo para cálculos e exibição de estatísticas descritivas
├── evom.db                  # [Seu arquivo de banco de dados, se usado]
├── generate_key.py          # Script para gerar a chave de criptografia
├── gerador_graficos.py      # Módulo para geração de gráficos dos dados dos usuários
├── key.key                  # Arquivo da chave de criptografia (NÃO COMPARTILHAR PUBLICAMENTE)
├── TelaInicial.py           # Script principal que contém os menus e a lógica de interação
├── usuarios.json            # Dados dos usuários (criptografados, NÃO COMPARTILHAR PUBLICAMENTE)
├── README.md                # Este arquivo de documentação
└── requirements.txt         # Lista de dependências do Python


## ⚙️ Como Configurar e Executar o Projeto

Siga estes passos para configurar e rodar a plataforma EVOM em seu ambiente local:

1.  **Clone o Repositório:**
    ```bash
    git clonehttps://github.com/yvinimayza/pim-ads-1sem.git
    cd PIM-ADS-1SEM\EVOM
    ```
   
2.  **Crie um Ambiente Virtual (Opcional, mas Altamente Recomendado):**
    ```
    py -m venv venv
    ```
    * **Ative o Ambiente Virtual:**
        * **No Windows:** `.\venv\Scripts\activate`
        * **No macOS/Linux:** `source venv/bin/activate`
3.  **Instale as Dependências:**
    ```
    pip install -r requirements.txt
    ```
    *(Se você não tiver o `requirements.txt` ainda, crie-o executando `pip freeze > requirements.txt` na raiz do projeto.)*
4.  **Gere a Chave de Criptografia:**
    A plataforma requer uma chave para criptografar os dados. Execute o script `generate_key.py` para criar o arquivo `key.key`:
    ```
    py generate_key.py
    ```
    * **Importante:** Este arquivo `key.key` é **sensível** e não deve ser compartilhado em um repositório público. Ele já está configurado no `.gitignore` para ser ignorado pelo Git.
5.  **Execute o Programa Principal:**
    ```
    py TelaInicial.py
    ```

## 📚 Outras Áreas do PIM Abordadas

Além do desenvolvimento do sistema, o PIM aborda análises e diretrizes importantes:

* **Infraestrutura Computacional:** Análise comparativa de sistemas operacionais (Windows vs. Linux) e justificativa da escolha.
* **Tecnologia da Informação e da Comunicação (TIC):** Apresentação das aplicações e ferramentas de software para a consultoria.
* **Cibersegurança:** Definição de boas práticas de segurança digital para usuários e sistema.
* **Lei Geral de Proteção de Dados (LGPD):** Políticas de proteção de dados pessoais e conformidade.
* **Ética, Cidadania e Sustentabilidade Digital:** Estratégias para menor consumo de energia e descarte de equipamentos, promoção do uso responsável.
* **Direitos Humanos:** Definição de uma estratégia de comunicação inclusiva para a ONG.

>>>>>>> 970b46d ( Projeto PIM EVOM -FINALIZADO)
