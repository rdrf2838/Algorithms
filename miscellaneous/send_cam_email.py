"""Send email from arbitrary cam.ac.uk email addresses."""

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
    # print(to_addr, from_addr, subject)
    # print(body)
    # return
    """Send email!."""
    msg = MIMEText(body)
    msg['from'] = formataddr((str(Header(sender_name, 'utf-8')), from_addr))
    msg['to'] = to_addr
    msg['subject'] = subject
    # TODO, set name
    server.sendmail(from_addr, to_addr, msg.as_string())

def send_emails():
    server = get_server(SMTP_SRVR)

    qed_emails = "djh246; mm2258; gh454; ak2091; mamc7@eng.cam.ac.uk <mamc7@eng.cam.ac.uk>; zs371@eng.cam.ac.uk <zs371@eng.cam.ac.uk>; kef42@eng.cam.ac.uk <kef42@eng.cam.ac.uk>; hf360@eng.cam.ac.uk <hf360@eng.cam.ac.uk>; cl854@eng.cam.ac.uk <cl854@eng.cam.ac.uk>; tr470@eng.cam.ac.uk <tr470@eng.cam.ac.uk>; cjd88@eng.cam.ac.uk <cjd88@eng.cam.ac.uk>; ch898@eng.cam.ac.uk <ch898@eng.cam.ac.uk>; vjm32@eng.cam.ac.uk <vjm32@eng.cam.ac.uk>; vs503@eng.cam.ac.uk <vs503@eng.cam.ac.uk>; jw2183@eng.cam.ac.uk <jw2183@eng.cam.ac.uk>; kjeg2@eng.cam.ac.uk <kjeg2@eng.cam.ac.uk>; ksr31@eng.cam.ac.uk <ksr31@eng.cam.ac.uk>; mch79@eng.cam.ac.uk <mch79@eng.cam.ac.uk>; ss2744@eng.cam.ac.uk <ss2744@eng.cam.ac.uk>; fjg37@eng.cam.ac.uk <fjg37@eng.cam.ac.uk>; ajs343@eng.cam.ac.uk <ajs343@eng.cam.ac.uk>; wb310@eng.cam.ac.uk <wb310@eng.cam.ac.uk>; al2008@eng.cam.ac.uk <al2008@eng.cam.ac.uk>; kac53@eng.cam.ac.uk <kac53@eng.cam.ac.uk>; hc536@eng.cam.ac.uk <hc536@eng.cam.ac.uk>; ed546@eng.cam.ac.uk <ed546@eng.cam.ac.uk>; af702@eng.cam.ac.uk <af702@eng.cam.ac.uk>; ych31@eng.cam.ac.uk <ych31@eng.cam.ac.uk>; ljth2@eng.cam.ac.uk <ljth2@eng.cam.ac.uk>; jh2217@eng.cam.ac.uk <jh2217@eng.cam.ac.uk>; dl641@eng.cam.ac.uk <dl641@eng.cam.ac.uk>; ngcm2@eng.cam.ac.uk <ngcm2@eng.cam.ac.uk>; jm2323@eng.cam.ac.uk <jm2323@eng.cam.ac.uk>; vp392@eng.cam.ac.uk <vp392@eng.cam.ac.uk>; ep593@eng.cam.ac.uk <ep593@eng.cam.ac.uk>; gns30@eng.cam.ac.uk <gns30@eng.cam.ac.uk>; sls81@eng.cam.ac.uk <sls81@eng.cam.ac.uk>; kt482@eng.cam.ac.uk <kt482@eng.cam.ac.uk>; waov2@eng.cam.ac.uk <waov2@eng.cam.ac.uk>; xw363@eng.cam.ac.uk <xw363@eng.cam.ac.uk>; hw527@eng.cam.ac.uk <hw527@eng.cam.ac.uk>; vb395@eng.cam.ac.uk <vb395@eng.cam.ac.uk>; cmb237@eng.cam.ac.uk <cmb237@eng.cam.ac.uk>; eb739@eng.cam.ac.uk <eb739@eng.cam.ac.uk>; cac213@eng.cam.ac.uk <cac213@eng.cam.ac.uk>; af662@eng.cam.ac.uk <af662@eng.cam.ac.uk>; sj562@eng.cam.ac.uk <sj562@eng.cam.ac.uk>; jwk33@eng.cam.ac.uk <jwk33@eng.cam.ac.uk>; pl452@eng.cam.ac.uk <pl452@eng.cam.ac.uk>; rm916@eng.cam.ac.uk <rm916@eng.cam.ac.uk>; gm620@eng.cam.ac.uk <gm620@eng.cam.ac.uk>; srp60@eng.cam.ac.uk <srp60@eng.cam.ac.uk>; np499@eng.cam.ac.uk <np499@eng.cam.ac.uk>; js2427@eng.cam.ac.uk <js2427@eng.cam.ac.uk>; ds866@eng.cam.ac.uk <ds866@eng.cam.ac.uk>; ae430@eng.cam.ac.uk <ae430@eng.cam.ac.uk>; gh454@eng.cam.ac.uk <gh454@eng.cam.ac.uk>; gec45@eng.cam.ac.uk <gec45@eng.cam.ac.uk>; ab2545@eng.cam.ac.uk <ab2545@eng.cam.ac.uk>"
    qed_emails += "vb395@eng.cam.ac.uk <vb395@eng.cam.ac.uk>; cmb237@eng.cam.ac.uk <cmb237@eng.cam.ac.uk>; eb739@eng.cam.ac.uk <eb739@eng.cam.ac.uk>; cac213@eng.cam.ac.uk <cac213@eng.cam.ac.uk>; af662@eng.cam.ac.uk <af662@eng.cam.ac.uk>; sj562@eng.cam.ac.uk <sj562@eng.cam.ac.uk>; jwk33@eng.cam.ac.uk <jwk33@eng.cam.ac.uk>; pl452@eng.cam.ac.uk <pl452@eng.cam.ac.uk>; rm916@eng.cam.ac.uk <rm916@eng.cam.ac.uk>; gm620@eng.cam.ac.uk <gm620@eng.cam.ac.uk>; srp60@eng.cam.ac.uk <srp60@eng.cam.ac.uk>; np499@eng.cam.ac.uk <np499@eng.cam.ac.uk>; js2427@eng.cam.ac.uk <js2427@eng.cam.ac.uk>; ds866@eng.cam.ac.uk <ds866@eng.cam.ac.uk>; ae430@eng.cam.ac.uk <ae430@eng.cam.ac.uk>; kea37@eng.cam.ac.uk <kea37@eng.cam.ac.uk>; wjb48@eng.cam.ac.uk <wjb48@eng.cam.ac.uk>; sd784@eng.cam.ac.uk <sd784@eng.cam.ac.uk>; pgj27@eng.cam.ac.uk <pgj27@eng.cam.ac.uk>; sg836@eng.cam.ac.uk <sg836@eng.cam.ac.uk>; tww26@eng.cam.ac.uk <tww26@eng.cam.ac.uk>; leyt2@eng.cam.ac.uk <leyt2@eng.cam.ac.uk>; oaj24@eng.cam.ac.uk <oaj24@eng.cam.ac.uk>; mxt22@eng.cam.ac.uk <mxt22@eng.cam.ac.uk>; ilyh2@eng.cam.ac.uk <ilyh2@eng.cam.ac.uk>; bl434@eng.cam.ac.uk <bl434@eng.cam.ac.uk>; ryo20@eng.cam.ac.uk <ryo20@eng.cam.ac.uk>; gx218@eng.cam.ac.uk <gx218@eng.cam.ac.uk>; cdd43@eng.cam.ac.uk <cdd43@eng.cam.ac.uk>; cs802@eng.cam.ac.uk <cs802@eng.cam.ac.uk>"
    qed_emails += "il315"

    old_jcr_emails = "tww26 kdb35 izlc2 jat88 dm851 arw92 tegb2 ajo41 rb917 ych31 crc63 mb2345 bcn22 hb525 om349 emgs2 bpc38 pla23 sd834 als206 hc536"
    new_jcr_emails = "jat88 gde25 akrg2 tegb2 ab2637 mb2345 kdb35 lb871 lej41 cm2034 fk339 bhml2 kh692 emc97 jdq21 lp553 np523 om349 emgs2 hc536 bpc38 eeb49"
    old_jcr_emails += " js2427 il315"
    new_jcr_emails += " js2427 il315"

    with open("qjcr.csv") as f:
        qjcr = f.readlines()

    qed = [tuple(line.split(",")) for line in qjcr if len(line.split(",")[0]) > 2 and line.split(",")[0] in qed_emails]
    qed_permute = copy.deepcopy(qed)
    random.seed(10101)
    random.shuffle(qed_permute)

    new_jcr = [tuple(line.split(",")) for line in qjcr if len(line.split(",")[0]) > 2 and line.split(",")[0] in new_jcr_emails]
    old_jcr = [tuple(line.split(",")) for line in qjcr if len(line.split(",")[0]) > 2 and line.split(",")[0] in old_jcr_emails]
    all_jcr = [tuple(line.split(",")) for line in qjcr if len(line.split(",")[0]) > 2 and (line.split(",")[0] in new_jcr_emails or line.split(",")[0] in old_jcr_emails)]

    qed_pres = ["ep593", "Emilie Pauwels"]
    old_jcr_pres = ["tww26", "Tomos Wood"]
    new_jcr_pres = ["jat88", "Jacob Turner"]

    # for sender, recipent in zip(qed, qed_permute):
    #     sender_crsid, sender_name = qed_pres
    #     recipent_crsid, recipent_name = recipent
    #
    #     FROM_CRSID = sender_crsid
    #     TO_CRSID = recipent_crsid
    #     FROM_NAME = sender_name
    #     SUBJECT = "Exlusive exam updates"
    #     BODY = "Dear all,\n" + \
    #            "\n" + \
    #            "I have been speaking with Prof Durkan and have arranged that during the exam, you may use any additional\n" + \
    #            "items you were able to fit in your boiler suit. This has been added to incentivise a proper engineer's\n" + \
    #            "dresscode and as a way to allow open book exams without the central university noticing and getting upset.\n" + \
    #            "You are still not allowed to communicate with the outside world during the exam so anything you bring must\n" + \
    #            "be offline. On the other hand you are allowed to bring lecture notes as long as you print them on A6 paper\n" + \
    #            "so that they fit in your pocket. Further clarification will come closer to the exam date from Prof Durkan.\n" + \
    #            "This new rule may seem to be giving an advantage to QED but every reasonable engineer should already own\n" + \
    #            "one and it shows that the department's senior management recognizes QED is a paragon of etiquette.\n" + \
    #            "\n" + \
    #            "Best,\n" + \
    #            sender_name + \
    #            "\nQED president"
    #     print(TO_CRSID)
    #     send_msg(server, FROM_CRSID + EXTENSION, TO_CRSID + EXTENSION, SUBJECT,
    #              BODY, FROM_NAME)
    #
    # print("QED part1 done")
    #
    # for recipent in all_jcr:
    #     sender_crsid, sender_name = old_jcr_pres
    #     recipent_crsid, recipent_name = recipent
    #
    #     FROM_CRSID = sender_crsid
    #     TO_CRSID = recipent_crsid
    #     FROM_NAME = sender_name
    #     SUBJECT = "Unlawful JCR elections!!!"
    #     BODY = "Dear all,\n" + \
    #            "\n" + \
    #            "I write to you because I have noticed a clear case of voting fraud during the most recent JCR elections.\n" + \
    #            "From public discourse it was clear the presidential election was going to be a landslide for RON. I can\n" + \
    #            "vouch that RON would be a perfectly qualified president. But then during the election all those votes\n" + \
    #            "vanished, as if RON wasn't even a person. I call out Jacob to address this clear case of fraud or to step\n" + \
    #            "down and let RON take their rightful place. If this doesn't happen I call out everyone else to occupy\n" + \
    #            "the mathematical bridge and let nobody pass until this egregious act is made right!\n" + \
    #            "\n" + \
    #            "Best,\n" + \
    #            sender_name + \
    #            "\nJCR president 2020-21"
    #     print(TO_CRSID)
    #     send_msg(server, FROM_CRSID + EXTENSION, TO_CRSID + EXTENSION, SUBJECT,
    #              BODY, FROM_NAME)
    #
    # print("JCR part1 done")
    # time.sleep(60 * 5)
    # print("part2")
    #
    # for sender, recipent in zip(qed, qed_permute):
    #     sender_crsid, sender_name = sender
    #     recipent_crsid, recipent_name = recipent
    #     FROM_CRSID = sender_crsid
    #     TO_CRSID = recipent_crsid
    #     FROM_NAME = recipent_name
    #     SUBJECT = "Re: Exlusive exam updates"
    #     BODY = "Hey " + recipent_name[0] + ",\n" + \
    #            "\n" + \
    #            "Did you see the email from Emilie? I feel like she must just be making fun of us. It's April fools, isn't it.\n" + \
    #            "Well, since we already started talking, might be good to reconnect with QED. It's been such a lonely and\n" + \
    #            "exhausting year, and it's a while since I have spoken to a lot of them. Would you be up for a call with the rest?\n" + \
    #            "\n" + \
    #            "Enjoy your easter break, and good luck with exams if you're in part II!\n" + \
    #            "\n" + \
    #            "Best,\n" + \
    #            sender_name[0]
    #     print(TO_CRSID)
    #     send_msg(server, FROM_CRSID + EXTENSION, TO_CRSID + EXTENSION, SUBJECT,
    #              BODY, FROM_NAME)
    #
    # print("QED part2 done")
    #
    # for recipent in all_jcr:
    #     sender_crsid, sender_name = new_jcr_pres
    #     recipent_crsid, recipent_name = recipent
    #
    #     FROM_CRSID = sender_crsid
    #     TO_CRSID = recipent_crsid
    #     FROM_NAME = sender_name
    #     SUBJECT = "Re: Unlawful JCR elections!!!"
    #     BODY = "Dear all\n" + \
    #            "\n" + \
    #            "Thank you Tomos for bringing this to the JCR committee's attention. After discussing this through, we have\n" + \
    #            "decided that there is a clear case for RON to have won the Presidency, so I shall step down but under one\n" + \
    #            "condition:\n" + \
    #            "\n" + \
    #            "I will come to the mathematical bridge, at first light, on the fifth day. At dawn, be on the bridge.\n" + \
    #            "\n" + \
    #            "If I find you there as the first light of day touches the brige, I shall resign my presidency to you RON.\n" + \
    #            "\n" + \
    #            "Best,\n" + \
    #            sender_name + \
    #            "\nPotentially Interim JCR president 2021-22"
    #     print(TO_CRSID)
    #     send_msg(server, FROM_CRSID + EXTENSION, TO_CRSID + EXTENSION, SUBJECT,
    #              BODY, FROM_NAME)
    #
    # print("JCR part2 done")
    # time.sleep(60 * 60)  # wait an hour
    print("part3")

    for sender, recipent in zip(qed, qed_permute):
        sender_crsid, sender_name = sender
        recipent_crsid, recipent_name = recipent
        FROM_CRSID = sender_crsid
        TO_CRSID = recipent_crsid
        FROM_NAME = recipent_name
        SUBJECT = "damage control :-P"
        BODY = "Hey me,\n" + \
               "\n" + \
               f"Just a note that the emails I received from {qed_pres} and {sender} were sent without their knowledge\n" + \
               "or approval and hence don't reflect their views and opinions. Well and same goes for this one, I didn't\n" + \
               "write this... 🤔\n" + \
               "\n" + \
               "Happy Halloween, merry Christmas and an eventful April Fools me! :-)"
        print(TO_CRSID)
        send_msg(server, FROM_CRSID + EXTENSION, TO_CRSID + EXTENSION, SUBJECT,
                 BODY, FROM_NAME)

    print("QED part3 done")

    for recipent in all_jcr:
        sender_crsid, sender_name = new_jcr_pres
        recipent_crsid, recipent_name = recipent

        FROM_CRSID = sender_crsid
        TO_CRSID = recipent_crsid
        FROM_NAME = sender_name
        SUBJECT = "damage control :-P"
        BODY = "Hey me,\n" + \
               "\n" + \
               f"Just a note that the emails I received from {old_jcr_pres} and {new_jcr_pres} were sent without their knowledge\n" + \
               "or approval and hence don't reflect their views and opinions. Well and same goes for this one, I didn't\n" + \
               "write this... 🤔\n" + \
               "\n" + \
               "Happy Halloween, merry Christmas and an eventful April Fools me! :-)"
        print(TO_CRSID)
        send_msg(server, FROM_CRSID + EXTENSION, TO_CRSID + EXTENSION, SUBJECT,
                 BODY, FROM_NAME)

    print("JCR part3 done")
    server.quit()


if __name__ == "__main__":
    send_emails()
