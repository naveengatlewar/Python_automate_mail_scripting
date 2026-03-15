# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.image import MIMEImage

# def send_report():

#     sender_email = "ngatlewar745@gmail.com"
#     receiver_email = "naveengatlewar021@gmail.com"
#     password = "exjvhowwkwhzqlja"

#     msg = MIMEMultipart()
#     msg["Subject"] = "Daily Subscription Report"
#     msg["From"] = sender_email
#     msg["To"] = receiver_email

#     body = """
#     Hello,

#     Please find the attached Daily Subscription Revenue Chart.

#     Regards,
#     Data Team
#     """

#     msg.attach(MIMEText(body, "plain"))

#     with open("../charts/revenue_chart.png", "rb") as f:
#         img = MIMEImage(f.read())

#     msg.attach(img)

#     server = smtplib.SMTP("smtp.gmail.com", 587)
#     server.starttls()

#     server.login(sender_email, password)

#     server.send_message(msg)

#     server.quit()



import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os

def send_report():
    sender_email = "ngatlewar745@gmail.com"
    receiver_email = "naveengatlewar021@gmail.com"
    password = "exjvhowwkwhzqlja" # Good job using an App Password!

    msg = MIMEMultipart()
    msg["Subject"] = "Daily Subscription Report"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    body = """
    Hello,

    Please find the attached Daily Subscription Revenue Chart.

    Regards,
    Data Team
    """
    msg.attach(MIMEText(body, "plain"))

    # --- THE PATH FIX ---
    # Get the directory of this specific script
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # Build the path to the chart: up one level, then into 'charts'
    chart_path = os.path.join(base_dir, "..", "charts", "revenue_chart.png")

    try:
        with open(chart_path, "rb") as f:
            img = MIMEImage(f.read())
            img.add_header('Content-Disposition', 'attachment', filename="revenue_chart.png")
            msg.attach(img)
    except FileNotFoundError:
        print(f"Error: The chart was not found at {chart_path}")
        return

    # --- SENDING ---
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)
    server.send_message(msg)
    server.quit()
    print("Email sent successfully!")