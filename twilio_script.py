#!/usr/bin/env python

from twilio.rest import Client

message = "MESSAGE STRING"

account_sid = "AXXXXXX"
auth_token = "XXXXXXX"
client = Client(account_sid, auth_token)

message = client.api.account.messages.create(to="+15109256372", from_="+12133445909", body=message)
