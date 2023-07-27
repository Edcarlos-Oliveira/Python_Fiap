from ftplib import *

ftp = FTP('ftp.ibiblio.org')
print(ftp.getwelcome())
ftp.login()
ftp.cwd('/pub/linux/logos/pictures')
with open('pai_do_linux.jpg', 'wb') as arq: #'wb' => especifica que é binario
    ftp.retrbinary('RETR linus-father-of-linux.jpg', arq.write)
ftp.quit()
