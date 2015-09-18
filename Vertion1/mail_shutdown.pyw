# encoding: UTF-8
#import smtplib
#import email
import imaplib
import re
import time
from os import system
#smtp = smtplib.SMTP()
#smtp.connect("smtp.qq.com", "25")
#smtp.login('857348270@qq.com','lzysdsg123')
#smtp.sendmail('857348270@qq.com', '2829518175@qq.com', 'From: 857348270@qq.com\r\nTo: 2829518175@qq.com\r\nSubject: this is a email from python demo\r\rJust for test~_~')
#smtp.quit() 
##############send mail###
while(1):
    
    try:
        conn = imaplib.IMAP4_SSL("imap.qq.com",993)
        conn.login('857348270@qq.com','lzysdsg123')
        conn.select()
        resp, items = conn.search(None, "UNSEEN") 
        for i in items[0].split():
            resp, mailData = conn.fetch(i, "(RFC822)") 
            mailText = str(mailData[0][1])
            #print(mailText)
            pattern = re.compile(r'Subject: GG\\r\\n')
            findit = pattern.findall(mailText)
            if findit!=[]:
                conn.store(i, '+FLAGS', '\Seen')
                #print('succeed!')
                system('shutdown.exe -s')
        conn.logout()
        time.sleep(60)
    except:
        print('no connection')
    finally:
        print('go on')
