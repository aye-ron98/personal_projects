"""
Module for notifying if a booking is present
"""
import requests
import os
from dotenv import load_dotenv


def send_notification(message: str) -> None:
    load_dotenv()

    header = {'authorization': 'NzYyNTMzMTI1OTAwMzM3MTUy.GEHhyj.EbFpEic1UNqGSwvXjxuKgW4--COTpZOw0PzR6g'}
    payload = {'content': message}

    requests.post(os.getenv('API_Key'), data=payload, headers=header)


def main():
    main()


if __name__ == '__main__':
    main()
