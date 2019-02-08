from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Defines permissions needed for calendar access
# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.events']

def main():
    creds = None
    # If it exists, uses token file to load credentials
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If no (valid) credentials available, take the user to login page
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Saves credentials in pickle file
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    # Prepares calendar api for use
    service = build('calendar', 'v3', credentials=creds)

    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming events')

    # Fetches all events with starting dates from now
    events_result = service.events().list(calendarId='primary', timeMin=now, singleEvents=True, orderBy='startTime').execute()
    events = events_result.get('items', [])
    if not events:
        print('No upcoming events found.')
    # Prints out event starting time and name
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])

    # Creates information for new event
    new_event_body = {
        "summary": "Meeting with Prof Collins",
        "location":"Simon Fraser University, Burnaby, Canada",
        "start": {
            'dateTime': '2019-02-06T14:00:00',
            'timeZone': 'America/Vancouver',
        },
        "end": {
            'dateTime': '2019-02-06T15:00:00',
            'timeZone': 'America/Vancouver',
        },
        'reminders': {
            'useDefault': False,
        },
        'visibility': "public",
        "attendees": [
            {
                "displayName": "Professor Michael Collins",
                "email": "drmichael@fakeschool.ca",
            },
        ],
    }

    # Inserts new event into primary calendar
    insert_result = service.events().insert(calendarId='primary', body = new_event_body).execute()
    
    #Prints out link to new event
    print('New event added:')
    print(insert_result.get('htmlLink'))

if __name__ == '__main__':
    main()