from google.oauth2 import service_account
from googleapiclient.discovery import build
import pytz

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



def main ():
    cal_service = get_google_calendar()
    schedule = get_events(cal_service)
    send_schedule_text(schedule)
