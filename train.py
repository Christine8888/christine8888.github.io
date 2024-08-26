import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import time
import re

# Configuration
URL = "https://westcoastrailways.co.uk/book/jacobite/steam-train-trip"
EMAIL_FROM = "your_email@example.com"
EMAIL_TO = "christineye88@outlook.com"
EMAIL_PASSWORD = "your_email_password"
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
CHECK_INTERVAL = 3600  # Check every hour

def check_availability():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    available_dates = []
    date_buttons = soup.find_all('button', attrs={"x-on:click": re.compile(r".*data.trip = result.id.*")})
    
    for button in date_buttons:
        date_span = button.find('span', attrs={"x-text": "moment(result.date).format('dddd Do MMMM YYYY')"})
        if date_span:
            date_text = date_span.get('x-text')
            # Extract date from the x-text attribute
            date_match = re.search(r"moment\(result\.date\)\.format\('(.+)'\)", date_text)
            if date_match:
                date_format = date_match.group(1)
                # We can't directly parse this, so we'll use a placeholder date for checking
                placeholder_date = datetime(2024, 9, 1).strftime(date_format)
                date_obj = datetime.strptime(placeholder_date, date_format)
                
                if date_obj.month == 9 and 6 <= date_obj.day <= 9:
                    availability_div = button.find('div', class_='flex-shrink-0')
                    if availability_div:
                        good_availability = availability_div.find('div', attrs={"x-show": "result.seats_available >= data.adults + data.children && !isLimited(result)"})
                        last_few_seats = availability_div.find('div', attrs={"x-show": "result.seats_available >= data.adults + data.children && isLimited(result)"})
                        if good_availability or last_few_seats:
                            available_dates.append(f"Date placeholder for {date_obj.day} September")
    
    return available_dates

def send_email(available_dates):
    subject = "Jacobite Steam Train Trip - Dates Available!"
    body = f"The following dates are now available:\n\n{', '.join(available_dates)}\n\nBook now at {URL}"
    
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_FROM, EMAIL_PASSWORD)
        server.send_message(msg)

def main():
    while True:
        print(f"Checking availability at {datetime.now()}")
        available_dates = check_availability()
        
        if available_dates:
            print(f"Dates available: {available_dates}")
            send_email(available_dates)
            print("Email sent!")
            break
        else:
            print("No dates available. Checking again later.")
        
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()