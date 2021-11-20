def historico(nome, email):
    nome = input('Insira o seu nome:')
    email = input('Insira o seu e-mail:')
    historico = {'nome':nome,'e-mail':email,}
    logs = open('logs.txt', 'a')
    logs.write(str(historico) + '\n')