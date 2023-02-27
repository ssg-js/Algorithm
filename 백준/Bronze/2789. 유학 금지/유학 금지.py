mail_context = input()

banned = 'CAMBRIDGE'

for m in mail_context:
    for b in banned:
        if m == b:
            mail_context = mail_context.replace(m, '')

print(mail_context)