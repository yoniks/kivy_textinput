import smtplib,ssl
from email import encoders
from email.mime.base import  MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
load_dotenv()


"""send email with pdf after we create it """
def send_email_with_pdf(recive_email,id_order):
   body = "Invoice from Hani's Design. \n"
   msg = MIMEMultipart()
   msg['From'] = "invoice.hani.design@gmail.com"
   msg['To'] = recive_email
   msg['Subject'] = "Hain's Design"
   msg["Bcc"] = "developeryouridea@gmail.com"

   msg.attach(MIMEText(body, "plain"))
   file_name = f"{id_order}.pdf"


   # Open PDF file in binary mode
   with open(file_name, "rb") as attachment:
      # Add file as application/octet-stream
      # Email client can usually download this automatically as attachment
      part = MIMEBase("application", "octet-stream")
      part.set_payload(attachment.read())


   # Encode file in ASCII characters to send by email
   encoders.encode_base64(part)

   # Add header as key/value pair to attachment part
   part.add_header("Content-Disposition",f"attachment; filename= {file_name}",)

   # Add attachment to message and convert message to string
   msg.attach(part)
   text = msg.as_string()
   #msg.set_charset(text)
   # Log in to server using secure context and send email
   context = ssl.create_default_context()
   try:
      with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
          server.login("invoice.hani.design@gmail.com", os.environ.get('PASS_EMAIL'))
          #server.send_message(msg)
          server.sendmail("invoice.hani.design@gmail.com",recive_email, text)
          server.sendmail("invoice.hani.design@gmail.com","invoice.hani.design@gmail.com" , text)
          server.quit()
          if os.path.exists(file_name):
              os.remove(file_name)
          return True
   except Exception as e:
       print(e)
   return False