import Qmail

def send_email(email,password,smtp,port,reciever_emails,subject,txt):

    # pffq ormx vmbm tsvx
    sender =Qmail.SMTP(EMAIL=email,PASSWORD=password,smtp=smtp,port=port,reciever_emails=reciever_emails)
    message = Qmail.MSG(subject=subject,txt=txt)
    sender.send_mail(message=message)