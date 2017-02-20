emails = ["noreply@gmail.com", "noreply@hotmail.com", "noreply@yahoo.com"]
names = ["john", "jack", "james"]

emailDomains = "gmail.com"
for email, name in zip(emails, names):
  if email.endswith(emailDomains):
    print(email, name)  