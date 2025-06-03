import os

# Função para limpar a tela do terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função principal do menu de cursos
def cursos():
    while True:
        clear()
        print("\n🔹 **Cursos disponíveis** 🔹")
        print("1 - Python para ensino de lógica computacional e programação básica")
        print("2 - Comparação de Sistemas Operacionais")
        print("3 - Cibersegurança")
        print("4 - LGPD (Lei Geral de Proteção de Dados)")
        print("5 - Ética e Sustentabilidade")
        print("6 - Direitos Humanos")
        print("7 - Voltar ao menu principal")

        opcao = input("Escolha um curso digitando o número correspondente: ")

        if opcao == "1":
            curso_python()
        elif opcao == "2":
            curso_sistemas_operacionais()
        elif opcao == "3":
            curso_ciberseguranca()
        elif opcao == "4":
            curso_lgpd()
        elif opcao == "5":
            curso_etica_sustentabilidade()
        elif opcao == "6":
            curso_direitos_humanos()
        elif opcao == "7":
            break
        else:
            print("\033[91mOpção inválida! Digite um número válido.\033[0m")

# Função para quiz interativo com explicações ao acertar ou errar
def quiz(perguntas):
    pontuacao = 0
    for conceito, pergunta, opcoes, resposta_correta, explicacao_correta, explicacoes_erradas in perguntas:
        print(f"\n🔹 {conceito}")  
        print(f"\n{pergunta}")  

        # Exibir opções de resposta corretamente sem duplicação
        for index, opcao in enumerate(opcoes, start=1):
            print(f"{index} - {opcao.replace(f'{index} - ', '')}")  # Remove números duplicados na exibição

        while True:
            resposta = input("\nDigite o número da resposta correta: ")

            if resposta.isdigit() and int(resposta) in range(1, len(opcoes) + 1):  
                if int(resposta) == opcoes.index(resposta_correta) + 1:  # Correção na verificação da resposta
                    print(f"\033[92mCorreto! {explicacao_correta}\033[0m")
                    pontuacao += 10
                    break
                else:
                    print(f"\033[91mErrado! A resposta correta é: {resposta_correta}. {explicacoes_erradas[opcoes.index(resposta_correta)]}\033[0m")
                    break
            else:
                print("\033[91mOpção inválida! Digite um número válido.\033[0m")

    return pontuacao


# 🔹 **Curso 1: Python**
def curso_python():
    clear()
    print("\n🔹 **Python para ensino de lógica computacional e programação básica**")
    
    perguntas_python = [
        ("Os laços de repetição são usados para executar um bloco de código várias vezes.",
         "Qual estrutura em Python é usada para repetir ações?",
         ["1 - for", "2 - while", "3 - if", "4 - switch"],
         "1 - for",
         "'For' é uma estrutura de repetição utilizada para iterar sobre listas ou sequências de valores.",
         ["While também é usado para repetição, mas depende de uma condição.", "If é utilizado para decisões, não repetição.", "Switch não existe em Python."]
        ),

        ("O símbolo '=' é usado em Python para atribuir valores a variáveis.",
         "Qual símbolo é usado para atribuir valores a variáveis?",
         ["1 - =", "2 - ==", "3 - :", "4 - ;"],
         "1 - =",
         "O '=' é usado para atribuir valores a variáveis, enquanto '==' serve para comparar valores.",
         ["'==' é usado para comparação, não atribuição.", "':' é utilizado em definições como funções ou listas.", "';' não é necessário em Python."]
        ),

        ("As funções em Python ajudam a reutilizar código e organizar o programa.",
         "Qual comando é usado para definir uma função em Python?",
         ["1 - def", "2 - function", "3 - create", "4 - define"],
         "1 - def",
         "O comando 'def' declara funções, permitindo modularização do código e reutilização eficiente.",
         ["'Function' não é um comando em Python.", "'Create' não existe para definir funções.", "'Define' também não é um comando válido."]
        )
    ]

    pontuacao = quiz(perguntas_python)
    print(f"\n🔹 **Pontuação final: {pontuacao} pontos!**")
    input("\nPressione Enter para voltar ao menu de cursos...")

# 🔹 **Curso 2: Sistemas Operacionais**
def curso_sistemas_operacionais():
    clear()
    print("\n🔹 **Comparação de Sistemas Operacionais (Linux vs. Windows)**")

    perguntas_so = [
        ("Linux é um sistema operacional gratuito e conhecido por sua segurança.",
         "Qual sistema é gratuito e mais seguro contra ataques?",
         ["1 - Linux", "2 - Windows", "3 - MacOS", "4 - Android"],
         "1 - Linux",
         "O Linux tem código aberto, o que permite que especialistas corrijam vulnerabilidades rapidamente, tornando-o mais seguro.",
         ["Windows é pago e tem mais vulnerabilidades.", "MacOS é seguro, mas não é gratuito.", "Android é um sistema móvel, não adequado para servidores."]
        ),

        ("Windows tem uma interface mais intuitiva e fácil de usar para iniciantes.",
         "Qual sistema operacional é mais intuitivo para iniciantes?",
         ["1 - Linux", "2 - Windows", "3 - Ubuntu", "4 - Fedora"],
         "2 - Windows",
         "Windows possui interface gráfica amigável e suporte amplo, facilitando a adaptação de novos usuários.",
         ["Linux requer mais comandos no terminal.", "Ubuntu é intuitivo, mas menos utilizado.", "Fedora não é tão popular entre iniciantes."]
        ),

        ("Linux é amplamente utilizado em servidores devido à sua estabilidade.",
         "Por que Linux é preferido para servidores?",
         ["1 - Maior compatibilidade com software comercial", "2 - Estabilidade e segurança", "3 - Melhor desempenho gráfico", "4 - Menos custo de licença"],
         "2 - Estabilidade e segurança",
         "Linux é altamente confiável, pois tem melhor gerenciamento de recursos e menos necessidade de reinicializações.",
         ["Compatibilidade não é prioridade para servidores.", "Desempenho gráfico não é relevante em servidores.", "Custo de licença pode ser baixo, mas não é o único fator."]
        )
    ]

    pontuacao = quiz(perguntas_so)
    print(f"\n🔹 **Pontuação final: {pontuacao} pontos!**")
    input("\nPressione Enter para voltar ao menu de cursos...")

# 🔹 **Curso 3: Cibersegurança**
def curso_ciberseguranca():
    clear()
    print("\n🔹 **Cibersegurança - Boas Práticas**")

    perguntas_ciberseguranca = [
        ("Phishing é um ataque onde criminosos enviam e-mails falsos para roubar dados.",
         "O que é phishing?",
         ["1 - Ataque de senha", "2 - Tentativa de roubo via e-mail", "3 - Vírus", "4 - Firewall"],
         "2 - Tentativa de roubo via e-mail",
         "O phishing engana usuários para que revelem informações sensíveis, como senhas e dados bancários.",
         ["Ataque de senha envolve força bruta.", "Vírus infecta o sistema, mas não envolve engano.", "Firewall protege a rede, mas não impede phishing."]
        ),

        ("Os antivírus ajudam a proteger computadores contra ameaças cibernéticas.",
         "O que ajuda a proteger contra vírus no computador?",
         ["1 - Antivírus", "2 - Backup", "3 - Firewall", "4 - VPN"],
         "1 - Antivírus",
         "Os antivírus detectam e removem softwares maliciosos antes que causem danos ao sistema.",
         ["Backup mantém cópias de arquivos, mas não protege contra vírus.", "Firewall protege a rede, mas não remove vírus.", "VPN protege a privacidade, mas não impede infecções por vírus."]
        ),

        ("Os backups garantem que seus arquivos estejam seguros mesmo em caso de falha.",
         "O que deve ser feito regularmente para evitar perda de dados?",
         ["1 - Backup", "2 - Antivírus", "3 - Firewall", "4 - Criptografia"],
         "1 - Backup",
         "Ter cópias dos arquivos evita perda permanente em caso de ataques, falhas de hardware ou erros humanos.",
         ["Antivírus protege contra malware, mas não recupera arquivos perdidos.", "Firewall protege redes, mas não salva arquivos.", "Criptografia protege dados, mas não previne perda de arquivos."]
        )
    ]

    pontuacao = quiz(perguntas_ciberseguranca)
    print(f"\n🔹 **Pontuação final: {pontuacao} pontos!**")
    input("\nPressione Enter para voltar ao menu de cursos...")

# 🔹 **Curso 4: LGPD**
def curso_lgpd():
    clear()
    print("\n🔹 **LGPD - Lei Geral de Proteção de Dados**")

    perguntas_lgpd = [
        ("O direito ao esquecimento permite ao usuário solicitar a remoção de seus dados.",
         "Qual direito permite ao usuário solicitar a exclusão dos seus dados?",
         ["1 - Direito ao esquecimento", "2 - Anonimato", "3 - Proteção de dados", "4 - Privacidade"],
         "1 - Direito ao esquecimento",
         "Esse direito garante que um usuário possa solicitar a exclusão de seus dados pessoais armazenados por uma empresa.",
         ["O anonimato protege a identidade, mas não garante exclusão de dados.", "Proteção de dados envolve segurança, mas não remoção.", "Privacidade regula acesso, mas não exige exclusão de dados."]
        ),

        ("O consentimento do usuário é necessário para que empresas utilizem seus dados.",
         "O que as empresas devem obter antes de utilizar dados pessoais?",
         ["1 - Consentimento", "2 - Licença", "3 - Autorização do governo", "4 - Isenção"],
         "1 - Consentimento",
         "O consentimento é fundamental para garantir que os dados pessoais sejam usados de forma justa e transparente.",
         ["Licença se aplica a software, não a dados pessoais.", "Autorização do governo não é exigida em todos os casos.", "Isenção significa não estar sujeito a regras, o que não se aplica à LGPD."]
        ),

        ("A LGPD exige medidas de segurança para proteger informações sensíveis.",
         "O que deve ser feito para proteger dados pessoais?",
         ["1 - Criptografia e controle de acesso", "2 - Compartilhar publicamente", "3 - Armazenar sem segurança", "4 - Negligenciar proteção"],
         "1 - Criptografia e controle de acesso",
         "A criptografia e controle de acesso são essenciais para impedir que dados sensíveis sejam acessados por pessoas não autorizadas.",
         ["Compartilhar publicamente expõe dados ao risco.", "Armazenar sem segurança pode levar a vazamentos.", "Negligenciar proteção aumenta riscos de ataques."]
        )
    ]

    pontuacao = quiz(perguntas_lgpd)
    print(f"\n🔹 **Pontuação final: {pontuacao} pontos!**")
    input("\nPressione Enter para voltar ao menu de cursos...")

# 🔹 **Curso 5: Ética e Sustentabilidade**
def curso_etica_sustentabilidade():
    clear()
    print("\n🔹 **Ética e Sustentabilidade na Tecnologia**")

    perguntas_etica = [
        ("O uso de monitores de LED reduz o consumo de energia e ajuda na economia.",
         "Qual tecnologia de monitor consome menos energia?",
         ["1 - LCD", "2 - LED", "3 - Plasma", "4 - OLED"],
         "2 - LED",
         "Monitores LED consomem menos energia e possuem maior durabilidade comparados a tecnologias mais antigas.",
         ["LCD gasta mais energia que LED.", "Plasma consome mais energia e gera calor excessivo.", "OLED é eficiente, mas pode ser caro."]
        ),

        ("A reciclagem de lixo eletrônico evita impactos negativos no meio ambiente.",
         "O que deve ser feito ao descartar eletrônicos?",
         ["1 - Jogar no lixo comum", "2 - Queimar", "3 - Reciclar", "4 - Enterrar"],
         "3 - Reciclar",
         "Reciclar dispositivos eletrônicos evita contaminação do solo e reaproveita componentes valiosos.",
         ["Jogar no lixo comum causa contaminação.", "Queimar pode liberar substâncias tóxicas.", "Enterrar eletrônicos polui o solo."]
        ),

        ("O consumo consciente de energia elétrica reduz impactos ambientais.",
         "Qual ação ajuda a reduzir o consumo excessivo de energia?",
         ["1 - Usar lâmpadas fluorescentes", "2 - Deixar luzes acesas sem necessidade", "3 - Utilizar sensores de presença", "4 - Manter equipamentos eletrônicos ligados"],
         "3 - Utilizar sensores de presença",
         "Sensores de presença evitam desperdício ao desligar automaticamente luzes em ambientes vazios.",
         ["Lâmpadas fluorescentes são mais econômicas que incandescentes, mas menos que LED.", "Deixar luzes acesas causa desperdício.", "Manter eletrônicos ligados sem necessidade aumenta o consumo."]
        )
    ]

    pontuacao = quiz(perguntas_etica)
    print(f"\n🔹 **Pontuação final: {pontuacao} pontos!**")
    input("\nPressione Enter para voltar ao menu de cursos...")

# 🔹 **Curso 6: Direitos Humanos**
def curso_direitos_humanos():
    clear()
    print("\n🔹 **Direitos Humanos e Inclusão Digital**")

    perguntas_direitos_humanos = [
        ("Materiais inclusivos como vídeos e infográficos ajudam na acessibilidade digital.",
         "O que pode tornar conteúdos mais acessíveis?",
         ["1 - Textos longos", "2 - Vídeos e infográficos", "3 - Imagens pesadas", "4 - Códigos fechados"],
         "2 - Vídeos e infográficos",
         "Recursos audiovisuais facilitam a compreensão para pessoas com dificuldades de leitura e deficiências visuais.",
         ["Textos longos dificultam o acesso a pessoas com dislexia.", "Imagens pesadas podem prejudicar carregamento.", "Códigos fechados não têm relação com acessibilidade."]
        ),

        ("Campanhas nas redes sociais ajudam a divulgar informações sobre inclusão digital.",
         "Qual meio digital é eficiente para divulgar campanhas?",
         ["1 - Livros físicos", "2 - Redes sociais", "3 - Cartazes locais", "4 - Rádio"],
         "2 - Redes sociais",
         "As redes sociais permitem alcançar um público amplo e engajar comunidades em debates sobre inclusão digital.",
         ["Livros físicos são úteis, mas não são o melhor meio digital.", "Cartazes locais têm alcance limitado.", "Rádio pode ser eficaz, mas redes sociais têm maior impacto."]
        ),

        ("Uso de linguagem acessível facilita a comunicação para todos os públicos.",
         "Por que é importante adaptar a comunicação para diferentes públicos?",
         ["1 - Marketing", "2 - Exclusividade", "3 - Acessibilidade", "4 - Estética"],
         "3 - Acessibilidade",
         "Uma linguagem clara e acessível garante que todos possam entender e participar de discussões importantes.",
         ["Marketing foca na venda, não na inclusão.", "Exclusividade significa restringir o acesso, o que não é inclusivo.", "Estética é importante, mas não é o principal fator para acessibilidade."]
        )
    ]

    pontuacao = quiz(perguntas_direitos_humanos)
    print(f"\n🔹 **Pontuação final: {pontuacao} pontos!**")
    input("\nPressione Enter para voltar ao menu de cursos...")