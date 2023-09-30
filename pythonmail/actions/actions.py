# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import smtplib

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import re

class ActionSubmit(Action):

    def name(self) -> Text:
        return "action_submit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        email = tracker.get_slot('email')
        self.Send_Mail(email)
        dispatcher.utter_message(text="Mail Sent")

        return []

    def Send_Mail(self, email):

        receiver_email = email
        sender_email = 'jatin.heyall@gmail.com'
        subject = 'Test'
        message = 'Hi'
        text = f"Subject: {subject}\n\n{message}"

        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(sender_email,"mvwyhnrnrtdipwiw")
        server.sendmail(sender_email,receiver_email,text)
