from exchangelib import DELEGATE, IMPERSONATION, Account, Credentials, ServiceAccount, \
        EWSDateTime, EWSTimeZone, Configuration, NTLM, CalendarItem, Message, \
        Mailbox, Attendee, Q, ExtendedProperty, FileAttachment, ItemAttachment, \
        HTMLBody, Build, Version

creds = Credentials(
    username="",
    password="")

config = Configuration(server='', credentials=creds)

account = Account(
    primary_smtp_address="",
    autodiscover=False,
    config = config,
    access_type=DELEGATE)
