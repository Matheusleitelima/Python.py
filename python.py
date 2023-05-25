print('bem vindo ao sistema de cadastro do liceu')


alunos = {}

def cadastrar_aluno():
    nome = input(f"Digite o nome do aluno: ")

    print (f"seja bem vindo ", nome)

    matricula = input(f'qual sua matricula?')

    idade = input(f"Digite a idade do aluno: ")

    print (f'o aluno tem ', idade ,'anos')

    curso = input(f'qual é seu curso?')

    print(f'curso do aluno é', curso)

    horario = input(f'qual seu horario?')

    nota = input(f'sua nota na avaliação: ')

    print(f'nota do aluno ' , nota)

    alunos[nome] = matricula ,idade , curso, horario, nota

    print("Aluno cadastrado!")

def gerar_relatorio():

    print("Relatório :")

    for aluno, (matricula, idade, curso, horario, nota) in alunos.items():

        status = "Aprovado" if float(nota) >= 6 else "Reprovado"

        print(f"Nome: {aluno} | Matricula:{matricula} Idade: {idade} |Curso: {curso} | Horario: {horario} Nota: {nota} | Status: {status} ")

def gerar_nota():

    print("Nota:")

    for aluno, (matricula, idade, curso, horario, nota) in alunos.items():

        print(f"Aluno: {aluno} | Nota: {nota}")

def remover_aluno():

    nome = input("Digite o nome do aluno que deseja remover: ")

    if nome in alunos:

        del alunos[nome]

        print("Aluno removido com sucesso!")

    else:
        print("Aluno não encontrado,tente novamente.")

while True:

    print("Nosso menu:")

    print("1 - Cadastro do Aluno")

    print("2 - Relatório")

    print("3 - Remover o Aluno")

    print("4 - Ver nota")
    
    print("0 - Desconectar-se")

    opcao = input("Como podemos ajuda-lo ? ")
    
    if opcao == "1":
        cadastrar_aluno()

    elif opcao == "2":
        gerar_relatorio()

    elif opcao == "3":
        remover_aluno()

    elif opcao == "4":
        gerar_nota()
        
    elif opcao == "0":
        print("Espero ter ajudado.")
        break
    else:
        print("Ops,essa opção é inválida. Tente novamente.")
