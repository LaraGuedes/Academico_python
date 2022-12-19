"""
Nome da programadora: Lara Calegário Guedes
Nome do programa: Sistema Academico
Data: 08/11/2021
Atualização:12/12/2021
"""

# Variaveis globais
nome = ("")
cpf = ()
identidade = ()
cep = ()
email = ("")

# Front and do cadrasto
def front1 ():
    print("-----------------------------------------------------------")
    print("-------------------------CADASTRO--------------------------")
    print("-----------------------------------------------------------")

# Entrada inicial de dados (cadastro do aluno)
def cadrasto():
    global nome
    nome = str(input("Informe seu nome completo: "))
    while (len(nome)<= 3):
        nome = str(input("Nome invalido. Informe seu nome completo novamente : "))
    print("")
        

    global cpf
    cpf = int(input("Informe seu CPF, somente números: "))
    cpf2 = str(cpf)
    if (cpf - 100000000000) < 0:
        while (len(cpf2) != 11):
            print("CPF invalido")
            cpf = int(input("Informe seu CPF, somente números: "))
            cpf2 = str(cpf)
    print ("")

    global identidade
    identidade = int(input("Informe seu número da identidade, somente números: "))
    identidade2 = str(identidade)
    if (identidade - 10000000) < 0 :
        while (len(identidade2) < 7):
            print("Identidade invalida")
            identidade = int(input("Informe seu número da identidade, somente números: "))
            identidade2 = str(identidade)
    print ("")

    global cep
    cep = int(input("Informe seu CEP: "))
    cep2 = str(cep)
    while (len(cep2) < 8):
        print("CEP invalida")
        cep = int(input("Informe seu CEP: "))
        cep2 = str(cep)
    print ("")

    global email
    email = str(input("Informe seu E-mail: "))
    while (len(email) < 11):
        email = str(input("E-mail invalido. Informe seu E-mail novamente: "))
    print("")


#Def feito para a confirmação dos dados do usuário
def confirmacao ():
    global nome
    print("Olá %s, confira seus dados:" %(nome))
    correto = str(input("Seu nome está correto [S/N]: "))
    while (correto == "N") or (correto == "n"):
        nome = str(input("Informe seu nome completo: "))
        while (len(nome)<= 3):
            nome = str(input("Nome invalido. Informe seu nome completo novamente : "))
            print("-----------------------------------------------------------")
            break
        break
    while (correto == "S") or (correto == "s"):
        print("-----------------------------------------------------------")
        break
        

    global cpf
    print("CPF: %d" %(cpf))
    correto4 = str(input("Seu CPF está correto [S/N]: "))
    while (correto4 == "N") or (correto4 == "n"):
        cpf = int(input("Informe seu CPF, somente números: "))
        cpf2 = str(cpf)
        if (cpf - 10000000000) < 0:
            while (len(cpf2) != 10):
                print("CPF invalido")
                cpf = int(input("Informe seu CPF, somente números: "))
                cpf2 = str(cpf)
                print("-----------------------------------------------------------")
                break
        break
    while (correto4 == "S") or (correto4 == "s"):
        print("-----------------------------------------------------------")
        break
    

    global identidade
    print("Identidade: %d" %(identidade))
    correto3 = str(input("Sua identidade está correta [S/N]: "))
    while (correto3 == "N") or (correto3 == "n"):
        identidade = int(input("Informe seu número da identidade, somente números: "))
        identidade2 = str(identidade)
        if (identidade - 10000000) < 0 :
            while (len(identidade2) < 7):
                print("Identidade invalida")
                identidade = int(input("Informe seu número da identidade, somente números: "))
                identidade2 = str(identidade)
                print("-----------------------------------------------------------")
                break
        break
    while (correto3 == "S") or (correto3 == "s"):
        print("-----------------------------------------------------------")
        break
    

    global cep
    print("CEP: %d" %(cep))
    correto1 = str(input("Seu CEP esta correto [S/N]: "))
    while (correto1 == "N") or (correto1 == "n"):
        cep = int(input("Informe seu CEP: "))
        cep2 = str(cep)
        while (len(cep2) < 8):
            print("CEP invalida")
            cep = int(input("Informe seu CEP: "))
            cep2 = str(cep)
            print("-----------------------------------------------------------")
            break
        break
    while (correto1 == "S") or (correto1 == "s"):
        print("-----------------------------------------------------------")
        break

    global email
    print("E-mail: %s" %(email))
    correto2 = str(input("Seu E-mail esta correto [S/N]: "))
    while (correto2 == "N") or (correto2 == "n"):
        email = str(input("Informe seu E-mail: "))
        while (len(email) < 11):
            email = str(input("E-mail invalido. Informe seu E-mail novamente: "))
            print("-----------------------------------------------------------")
            break
        break
    while (correto2 == "S") or (correto2 == "s"):
        print("-----------------------------------------------------------")
        break
    
# Front and com o a tela visivel do cadrasto ao usuário
def resultado ():
    print("-----------------------------------------------------------")
    print("------------------------CADASTRO---------------------------")
    global nome
    print("NOME:", nome)
    print("-----------------------------------------------------------")
    global cpf
    print("CPF:", cpf)
    print("-----------------------------------------------------------")
    global identidade
    print("IDENTIDADE:", identidade)
    print("-----------------------------------------------------------")
    global cep
    print("CEP:", cep)
    print("-----------------------------------------------------------")
    global email
    print("E-MAIL:", email)
    print("-----------------------------------------------------------")

# Front and de conclusão do cadrasto   
def front2 ():
    print("")
    print("")
    print("-----------------------------------------------------------")
    print("----------------CADRASTO CONCLUIDO-------------------------")
    print("-----------------------------------------------------------")
    print("------------------------------------------------OBRIGADO(a)")
    print("")

# Front and para o inicio de cadrasta notas
def front3():
    print("")
    print("")
    print("-----------------------------------------------------------")
    print("-----------------CADRASTO DE NOTAS FINAIS------------------")
    print("-----------------------------------------------------------")

# Front and para mostrar os dados cadrastado 
def front4():
    print("-----------------------------------------------------------")
    print("--------------ESSES SÃO SEUS DADOS CADRASTRADOS------------")
    print("-----------------------------------------------------------")

# Front and para mostrar a situação da disciplina 
def front5():
    print("-----------------------------------------------------------")
    print("-------------------SITUAÇÃO NAS DICIPLINAS-----------------")
    print("-----------------------------------------------------------")
    

front1() # Chama o primeiro front and   
cadrasto() # Chama o cadrasto
confirmacao() # Chama a confirmação do cadrasto
front2() # Chama o segundo front and 
front3() # Chama o terceiro front and 

#--------- Notas-------------

# Listas:
disciplinas = ["Portugues", "Matemática","Física", "Química","Historia", "Educação física","Filosofia", "Sociologia", "Artes", "Sistema operacionais", "Fundamentos de hardware", "Lógica de programação" ]
notas = []
aprovado = []
reprovado = []

# Entrada e processamento das listas:
w = 0
while w < len (disciplinas):
    nota = float(input("Qual foi sua nota final em %s: " %(disciplinas[w])))

    while (nota < 0) or (nota > 100):
        print("Nota invalida, ela deve ser de 0 até 100.")
        nota = float(input("Sua nota em %s :" %(disciplinas[w])))
        notas.append(nota)

    if (nota < 60):
        reprovado.append(nota)
    elif (nota > 60):
        aprovado.append(nota)
    w += 1

front4() # Chama o quarto front and 
resultado() # Chama o resultado
front5() # Chama o quinto front and

# Mostra as situações da diciplina
print("Essas são as diciplinas: ", disciplinas)
print("Você foi aprovado: ", aprovado)
print("Você foi reprovado: ", reprovado)
print("-----------------------------------------------------------")

# Confirma a situação da disciplina
if len(reprovado) >= 3:
    print("Você está reprovado")
elif (len(reprovado) <= 2) and (len(reprovado) > 0):
    print("Você está aprovado com dependência")
else:
    print("Você está aprovado sem dependência")
print("-----------------------------------------------------------")



