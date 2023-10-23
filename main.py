from google.oauth2 import service_account
from googleapiclient.discovery import build
import pytz
from twilio.rest import Client
import datetime

def get_google_calendar():
    scopes = ['https://www.googleapis.com/auth/calendar.readonly']
    creds_file = "credentails.json"

    creds = service_account.Credentials.from_service_account(
        creds_file, scopes
    )

    service = build(
        'calendar',
        'v3',
        credentials=creds
    )
    return service

def get_events(calendar_service):
    pst = pytz.timezone('America/Los Angeles') 
    now = datetime.now(pst)
    end_of_day = datetime(now.year, now.month, now.day, 23, 0, 0)

    events_result = calendar_service.events().list(
        calendarId = 'primary',
        timeMin=now.isoformat(),
        timeMax=end_of_day.isoformat(),
        singleEvents = True,
        orderBy='startTime'
    ).execute()

    events = events_result.get(
        'items',
        []
    )

    return events

def send_schedule_text(schedule):
    #Twilio Set-up
    TWILIO_SID = 'TWILIO_SID'
    TWILIO_AUTH_TOKEN = 'AUTH_TOKEN'
    TWILIO_PHONE_NUMBER = 'PHONE'
    RECIPIENT_PHONE_NUMBER = 'PHONE'

    client = Client (TWILIO_SID, TWILIO_AUTH_TOKEN)

    if not schedule:
        message = "You don't have anything today! Relax :D"
    else: 
        message = "Your schedule for today:\n"
        for event in schedule: # iterating in the schedule to grab start_time nd etc. 
            start_time = event['start'].get('dateTime', event['start'].get('date'))
            end_time = event['end'].get('dateTime', event['end'].get('date'))

            event_summary = event['summary']
            message = f"{start_time} - {end_time}: {event_summary}\n" #geeks4geeks F-Strings

    message = client.message.create( #Final Part, just sending the schedule to my phone number now
        body = message,
        from_= TWILIO_PHONE_NUMBER,
        to=RECIPIENT_PHONE_NUMBER
    )


def main():
    cal_service = get_google_calendar()
    schedule = get_events(cal_service)
    send_schedule_text(schedule)
