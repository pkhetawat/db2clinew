import smtplib
import os
import subprocess
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = ""
def appendMessage(stmt):
    '''
    Function
    ---------------

    Name : appendMessage

    Arguments : String contaning the statement to be appended to the mail body

    Output
    ------------

    Prepares the mail body to be send.
    '''
    global msg
    msg = msg+str(stmt)

def mail():
    '''
    Function
    --------------

    Name : mail

    Arguments : 
    1. String containing the failure or success

    Output
    -----------

    Sends an email notifying recipients after reading the file "mailList.t" with the formated details of the new Images in box.
    '''
    s = smtplib.SMTP("smtp.rocketsoftware.com")
#    s.starttls()
#    s.ehlo()
    mailList = []
    readMailListFile = open("mailList.t","r+")
    mailListTemp = [i.strip() for i in readMailListFile.readlines()]
    for mailTo in mailListTemp:
        if not mailTo.startswith("#"):
            mailList.append(mailTo)
    global msg
    msg = """\
Subject: Connection Details in Docker Container in amazon Linux Machine

-----------------------------------------------------------------------------------------------------------
Information on the connection in docker container for python, node, go and sslcertificate
-----------------------------------------------------------------------------------------------------------
\n\r"""
#    node_version = subprocess.check_output(['node --version'])
#    appendMessage(node_version)
    
    appendMessage("\nPython Connection Detail using pip ibm_db :\n")
    f = open("python-result.txt", "r")
    appendMessage(f.read())
    appendMessage("\n---------------------------------------------------------------------------------------\n")
    f.close()
    appendMessage("\nNode Connection Detail:\n")
    f = open("node-result.txt", "r")
    appendMessage(f.read())
    appendMessage("\n---------------------------------------------------------------------------------------\n")
    f.close()
    appendMessage("\nGo Connection Detail:\n")
    f = open("go-result.txt", "r")
    appendMessage(f.read())
    appendMessage("\n---------------------------------------------------------------------------------------\n")
    f.close()
    appendMessage("\nMachine and Version Details :\n")
    appendMessage("\nGCC Version:")
    p = subprocess.Popen('gcc --version',universal_newlines=True,stdout=subprocess.PIPE,shell=True)
    out, error = p.communicate()
    appendMessage(out)
    appendMessage("\nmachine details:")
    p = subprocess.Popen('uname -a',universal_newlines=True,stdout=subprocess.PIPE,shell=True)
    out, error = p.communicate()
    appendMessage(out)
    appendMessage("\nos details:")
    p = subprocess.Popen('cat /etc/*release',universal_newlines=True,stdout=subprocess.PIPE,shell=True)
    out, error = p.communicate()
    appendMessage(out)
    appendMessage("\nPython Version:")
    process = subprocess.Popen('python3 --version',universal_newlines=True, stdout=subprocess.PIPE,shell=True)
    out, error = process.communicate()
    appendMessage(out)
    appendMessage("\nDocker Version:")
    f = open("dockerversion.txt", "r")
    appendMessage(f.read()) 
    f.close()
    appendMessage("\nNode Version:")
    p = subprocess.Popen( 'node --version',universal_newlines=True, stdout=subprocess.PIPE,shell=True)
    out, error = p.communicate()    
    appendMessage(out)
    appendMessage("\nNPM Version:")
    p = subprocess.Popen( 'npm --version',universal_newlines=True, stdout=subprocess.PIPE,shell=True)
    out, error = p.communicate()
    appendMessage(out)
    appendMessage("\nGO Version:")
    p = subprocess.Popen( 'go version',universal_newlines=True, stdout=subprocess.PIPE,shell=True)
    out, error = p.communicate()
    appendMessage(out)
    s.sendmail("qa_cli@rocketsoftware.com", mailList, msg)
    s.quit()
mail()
