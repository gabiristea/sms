from twilio.rest import Client

account_sid = 'ACd7d6af914de7ca0f5c1bbfa2ef64d87a'
auth_token = 'd78ee3cbd6f382e67b9dcb910f4f5e8d'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+12029913935',
    body='Gabrielos is a Python programmer! How cool is that',
    to='+40784------'
)

print(message.sid)

