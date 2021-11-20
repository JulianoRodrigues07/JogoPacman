def historico(nome, email):
    nome = input('Insira o seu nome:')
    email = input('Insira o seu e-mail:')
    historico = {'nome':nome,'e-mail':email,}
    login = open('logs.txt', 'a')
    login.write(str(historico) + '\n')