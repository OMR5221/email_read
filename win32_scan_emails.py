import win32com.client
session = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = session.GetDefaultFolder(6)
print(len(inbox.Items))
message = inbox.Items

body_sender = ''

for msg in message:
    try:
        body_sender = msg.Sender
    except:
        body_sender = ''

    print(body_sender, msg.Subject, msg.Body)
