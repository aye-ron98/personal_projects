"""
Module for notifying if a booking is present
"""
import requests
import os


def send_notification(message):
    header = {'authorization': 'NzYyNTMzMTI1OTAwMzM3MTUy.GEHhyj.EbFpEic1UNqGSwvXjxuKgW4--COTpZOw0PzR6g'}
    payload = {'content': message}

    requests.post(os.environ['API_Key'], data=payload, headers=header)


def main():
    main()


if __name__ == '__main__':
    main()
