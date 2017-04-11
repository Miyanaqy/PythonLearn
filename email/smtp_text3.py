from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr, formatdate
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import smtplib, mimetypes

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = input('From: ')
password = input('Password: ')
to_addr = input('To: ')
smtp_server = input('SMTP server: ')

msg = MIMEMultipart()
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

with open('/111/360_n.jpg', 'rb') as f:
    mime = MIMEBase('image', 'jpg', filename='360_n.jpg')
    mime.add_header('Content-Disposition', 'attachment', filename='360_n.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)

server = smtplib.SMTP_SSL(smtp_server, 465)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
