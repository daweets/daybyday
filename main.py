from google.oauth2 import service_account
from googleapiclient.discovery import build
import pytz
from twilio.rest import Client

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
    TWILIO_SID = ''


def main():
    cal_service = get_google_calendar()
    schedule = get_events(cal_service)
    send_schedule_text(schedule)
