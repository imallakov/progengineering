class Mail:
    def __init__(self, from_server, to_server, from_user, to_user, text):
        self.from_server = from_server
        self.to_server = to_server
        self.from_user = from_user
        self.to_user = to_user
        self.text = text

    def __str__(self) -> str:
        return (f'Sender\'s server:{self.from_server}\n'
                f'Sender:{self.from_user}\n'
                f'Receiver\'s server:{self.to_user}\n'
                f'Receiver:{self.to_user}\n'
                f'Text:\n{self.text}')


mails: list[Mail] = []


class MailClient:
    def __init__(self, server, user):
        self.server = server
        self.user = user

    def send_mail(self, client1, message):
        mail = Mail(from_server=self.server, from_user=self.user, to_server=client1.server, to_user=client1.user,
                    text=message)
        mails.append(mail)

    def receive_mail(self):
        my_mails: list[Mail] = []
        for mail in mails:
            if mail.to_server == self.server and mail.to_user == self.user:
                my_mails.append(mail)
                mails.remove(mail)

        if len(my_mails) == 0:
            print(f'Почтовый ящик клиента {self.user} на сервере {self.server} пуст!\n\n')
        else:
            print(f'Новые писма клиента {self.user} на сервере {self.server}:\n')
            for mail in my_mails:
                print(f'{mail}\n')
            my_mails.clear()


client1 = MailClient('server1', 'user1')
client2 = MailClient('server1', 'user2')
client3 = MailClient('server2', 'user1')
client4 = MailClient('server2', 'user2')

client1.send_mail(client2, 'hello to client2 from client1')
client2.send_mail(client4, 'hello to client4 from client2')
client1.receive_mail()
client2.receive_mail()
client3.receive_mail()
client4.receive_mail()
