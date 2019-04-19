from exchangelib import DELEGATE, IMPERSONATION, Account, Credentials, ServiceAccount, \
        EWSDateTime, EWSTimeZone, Configuration, NTLM, CalendarItem, Message, \
        Mailbox, Attendee, Q, ExtendedProperty, FileAttachment, ItemAttachment, \
        HTMLBody, Build, Version

creds = Credentials(
    username="ESINT\\OXR0MQY",
    password="APk@fk@072019!")

config = Configuration(server='fpl.com', credentials=creds)

account = Account(
    primary_smtp_address="Oswald.Ramirez@nexteraenergy.com",
    autodiscover=False,
    config = config,
    access_type=DELEGATE)
