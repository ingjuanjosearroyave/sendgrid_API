import os
import sendgrid
from sendgrid.helpers.mail import Mail
from config import TO_EMAIL, FROM_EMAIL, SENDGRID_API_KEY

def send_email():
    with open("email.html", "r") as file:
        html_content = file.read()

    message = Mail(
        from_email=FROM_EMAIL,
        to_emails=TO_EMAIL,
        subject="Presentación Profesional",
        html_content=html_content
    )
    try:
        sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
        response = sg.send(message)
        print(f"Status Code: {response.status_code}")
        print(f"Body: {response.body}")
        print(f"Headers: {response.headers}")
    except Exception as e:
        print(f"Error: {e}")

#Postman
def send_email_via_postman(data):
   
    with open("email.html", "r") as file:
        html_content = file.read()

 
    to_email = data.get('to_email', TO_EMAIL)
    subject = data.get('subject', 'No Subject')

    message = Mail(
        from_email=FROM_EMAIL,
        to_emails=to_email,
        subject=subject,
        html_content=html_content
    )

  
    try:
        sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
        response = sg.send(message)
        return {"status": "success", "response_code": response.status_code}
    except Exception as e:
        return {"status": "error", "message": str(e)}

