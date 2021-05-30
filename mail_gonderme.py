import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

"""
SMTP Modülü ile mail gönderme

İlk olarak daha az güvenli uygulamalar için öncelikle aşağıdaki linke gidiyoruz ve güvenliği
kaldırıyoruz.

https://myaccount.google.com/lesssecureapps

"""

mesaj = MIMEMultipart()

mesaj["From"] = "benim_mailim@gmail.com"

mesaj["To"] = "gonderilecek_adres@gmail.com"

mesaj["Subject"] = "Smtp Mail Gonderme"


yazi = """

Smtp ile mail gonderiyorum

deniz tarafindan gonderildi.

"""

mesaj_govdesi = MIMEText(yazi,"plain")

mesaj.attach(mesaj_govdesi)

try:
    mail = smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo() # servera baglanmak icin

    mail.starttls() # sifrelenmesi icn

    mail.login("benim_mailimgmail.com","")

    mail.sendmail(mesaj["From"],mesaj["TO"],mesaj.as_string())

    print("Mail basariyla gonderildi")

    mail.close()

except:
    sys.stderr.write("Bir sorun olustu")
    sys.stderr.flush()
