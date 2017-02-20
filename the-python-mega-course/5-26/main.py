emails = ["noreply@gmail.com", "noreply@hotmail.com", "noreply@yahoo.com"]
emailDomains = "gmail.com"
for email in emails:
  if emailDomains in email:
    print(email)
  if email.endswith(emailDomains):
    print(email)  