import yagmail


yag = yagmail.SMTP("phtynkers@gmail.com" ,"password")



try:
  yag.send(to = "phtynkers@gmail.com", cc = "phtynkers@gmail.com", bcc = "phtynkers@gmail.com",
  subject="Test Email", contents=["This is a test email sent from Python."],
  attachments =[r"C:\Python-Robotic-Process-Automation-Engineer\WSL-Comandos.txt"])


  print("email send")
except:

  print("Error sending email")
