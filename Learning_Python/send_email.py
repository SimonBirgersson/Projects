# send_email.py 220723
import smtplib
import ssl
from email.message import EmailMessage


def send_mail(
    sender_email: str, password: str, receiver_email: str, subject: str, body: str
):
    """
    Function that allows user to send an email from a gmail server to another email adress.
    """
    # Intantiate message Class
    message = EmailMessage()

    # configure email to send
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # create HTML for the message, could add attachments and things here if desired.
    html = f"""
    <html>
        <body>
            <h1>{subject}</h1>
            <p>{body}</p>
        </body>
    </html>
    """

    # construct message according to html
    message.add_alternative(html, subtype="html")

    # create secure connection
    context = ssl.create_default_context()

    print("sending email...")
    # set up secure connection to gmail server
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:

        # log in to account
        server.login(sender_email, password)

        # send email as str
        server.sendmail(sender_email, receiver_email, message.as_string())
    print("sent succesfully!")


def main():
    """main script"""

    # Enter email information
    subject = "BC: status update"
    body = "Hello, you're debt is currently xxx, please make sure to swish xxx at phone number xxx. \n\n / Kind Regards, BC manager"

    sender_email = "BC_manager@gmail.com"
    receiver_email = "test@gmail.com"
    password = input("Enter your password: ")

    send_mail(
        sender_email=sender_email,
        password=password,
        receiver_email=receiver_email,
        subject=subject,
        body=body,
    )


if __name__ == "__main__":
    main()
