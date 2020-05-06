import smtplib

inicio = 'sim'

while inicio == "sim" :
    servidor = input('Escolha os servidor que deseja usar como remetente \n'
                     'GMAIL : 1\n'
                     'OUTLOOK : 2\n')
                     

    if servidor == '1' :
        smtpGml = smtplib.SMTP('smtp.gmail.com', 587)
        smtpGml.ehlo()  
        smtpGml.starttls()  # Conectando

        login = input("Digite seu email: ") 
        senha = input("Senha: ") 
        smtpGml.login(login, senha)

        dest = input('Digite o email  do destinatario:  ')
        assunto = input('Digite aqui o assunto:  ')
        msg = input('Digite aqui a mensagem: ')
        
        print(smtpGml.sendmail(login, dest, 'Subject: %s\n\n %s' % (assunto, msg)))
        smtpGml.quit()

    elif servidor == '2' :
        smtpLook = smtplib.SMTP('smtp-mail.outlook.com', 587)
        smtpLook.ehlo()
        smtpLook.starttls()
        
        login = input('Digite seu e-mail: ')
        senha = input('Senha: ')
        smtpLook.login(login, senha)

        dest = input('Digite o email Destinatario: ')
        assunto = input('Digite aqui o assunto:  ')
        msg = input('Digite aqui a mensagem: ')
        
        print(smtpLook.sendmail(login, dest, 'Subject: %s\n\n %s' % (assunto, msg)))
        smtpLook.quit()

    else :
        print('Digite o servidor correto! ')

    inicio = input("para repetir digite sim: ")
print("fim do programa")
