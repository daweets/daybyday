# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "ACf7348fc95188d816dd47a5c9136f391c"
auth_token  = "31a62d8f5fa8a041226415bd3781fe02"
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='TEXT TEXT TEXT',
         from_='++18336481841',
         to='PHONENUMBER'
     )

print(message.sid)
