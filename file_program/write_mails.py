email_id=[
    "merlin@gmail.com"
    "smitha@gmail.com"
    "sijo@gmail.com"
    "jhons@gmail.com"
]
f=open("C:\\Users\\HELEN VIJU\\OneDrive\\Documents\\OneDrive\\Documents\\PYTHON\\FUNDAMENTALS\\file_program\\emails.txt","w")
for email in email_id:
    f.write(email+"\n")