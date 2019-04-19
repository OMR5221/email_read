import win32com.client

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

inbox = outlook.GetDefaultFolder(6).Folders.Item("Inbox")
#6 = Inbox (without mails from the subfolder)
messages = inbox.Items
message = messages.GetLast()
body_content = message.body
print(body_content.encode("utf-8")) #Sometimes has parsing error due to different encoding format
