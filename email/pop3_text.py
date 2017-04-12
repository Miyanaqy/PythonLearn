from email.parser import Parser
import poplib

email = input('Email:')
password = input('Password:')
pop3_server = input('POP3 server:')

server = poplib.POP3_SSL(pop3_server, 995)
server.set_debuglevel(1)
print('1' + server.getwelcome().decode('utf-8'))

server.user(email)
server.pass_(password)

print('2' + 'Messages: %s Size: %s' % server.stat())
resp, mails, octets = server.list()
print('3',mails)

index = len(mails)
resp, lines, octets = server.retr(index)

msg_content = b'\r\n'.join(lines).decode('utf-8')
msg = Parser().parsestr(msg_content)
server.quit()
