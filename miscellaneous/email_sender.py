import smtplib
import copy
import random
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.header import Header
from email.utils import formataddr
EXTENSION = "@cam.ac.uk"
SMTP_SRVR = ("ppsw.cam.ac.uk", 25)
def get_server(SMTP_SRVR):
    """Return smtplib.SMTP object."""
    server = smtplib.SMTP(*SMTP_SRVR)
    server.starttls()
    return server
def send_msg(server, from_addr, to_addr, subject, body, sender_name):
    """Send email!."""
    msg = MIMEText(body)
    msg['from'] = formataddr((str(Header(sender_name, 'utf-8')), from_addr))
    msg['to'] = to_addr
    msg['subject'] = subject
    # TODO, set name
    server.sendmail(from_addr, to_addr, msg.as_string())
def send_emails():
    server = get_server(SMTP_SRVR)
    # for sender, recipent in zip([["js2427", "J"]], [["js2427", "J"]]):
    for sender, recipent in zip([["js2427", "J"], ["js2427", "J"]], [["js2427", "J"],["il315", "I"]]):
        sender_crsid, sender_name = sender
        recipent_crsid, recipent_name = recipent
        FROM_CRSID = recipent_crsid
        TO_CRSID = recipent_crsid
        FROM_NAME = recipent_name
        SUBJECT = "Diary entry 1/4/2020"
        BODY = "Dear diary,\n" + \
               "\n" + \
               "I just got such a wholesome email! I am so glad\n" + \
               "that QED is such a nice community! Of course I am\n" + \
               "being responsible! But that is a good point that I\n" + \
               "should reach out to my friends, I haven't talked with\n" + \
               "some of them for a while. Will go do that straight away!\n" + \
               "Or even doing a group call with my fellow engineers\n" + \
               "might be a cool idea!"
        print(TO_CRSID)
        send_msg(server, FROM_CRSID + EXTENSION, TO_CRSID + EXTENSION, SUBJECT,
                 BODY, FROM_NAME)
    server.quit()
if __name__ == "__main__":
    send_emails()