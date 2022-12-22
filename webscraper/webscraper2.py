from bs4 import BeautifulSoup
import requests
import random
import string
import csv

def getwebsite(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    div = soup.find_all("div", {"class": "businessName__09f24__EYSZE display--inline-block__09f24__fEDiJ border-color--default__09f24__NPAKY"})

    new_urls = []
    for link in div:
        refresh = link.find('a', {'class': 'css-1m051bw'}).get('href')
        new_urls.append(refresh)

    return new_urls

def each_page(url_list):

    for element in url_list:
        url = 'https://www.yelp.ca/' + element
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')

        try:
            title = soup.find("h1", {"class": "css-1se8maq"}).getText()
            operating_preview = soup.find("span", {
                'class': 'display--inline__09f24__c6N_k margin-l1__09f24__m8GL9 border-color--default__09f24__NPAKY'}).getText()
            address = soup.find_all('p', {'class': 'css-r9996t'})[0].getText()
            location = soup.find_all('span', {'class': 'raw__09f24__T4Ezm'})[1].getText()
            image = soup.find('img', {'class': 'photo-header-media-image__09f24__A1WR_'}).get('src')
            # days_of_week = soup.find_all('p', {'class': 'day-of-the-week__09f24__JJea_ css-1p9ibgf'})
            # operating_hours = soup.find_all('p', {'class': 'no-wrap__09f24__c3plq css-1p9ibgf'})
        except:
            continue
        else:
            details = ''
            try:
                details = soup.find(("div", {
                    'class': 'arrange__09f24__LDfbs gutter-auto__09f24__W9jlL vertical-align-middle__09f24__zU9sE margin-b3__09f24__l9v5d border-color--default__09f24__NPAKY'})).find(
                    'div', {'class': 'margin-b1-5__09f24__NHcQi border-color--default__09f24__NPAKY'}).getText()
            except:
                try:
                    details = soup.find(("div", {
                        'class': 'arrange__09f24__LDfbs gutter-auto__09f24__W9jlL vertical-align-middle__09f24__zU9sE margin-b3__09f24__l9v5d border-color--default__09f24__NPAKY'})).find(
                        'p', {'class': 'css-1evauet'}).getText()
                except:
                    try:
                        details = soup.find(("div", {
                            'class': 'arrange__09f24__LDfbs gutter-auto__09f24__W9jlL vertical-align-middle__09f24__zU9sE margin-b3__09f24__l9v5d border-color--default__09f24__NPAKY'})).find(
                            'p', {'class': 'css - 11k8aw1'}).getText()
                    except:
                        details = 'details to come'

            gym_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))
            details = details
            rating = str(random.randint(1, 5))
            # week_day = []
            # for day, hours in zip(days_of_week, operating_hours):
            #     operation = str(day.getText() + ': ' + hours.getText())
            #     week_day.append(operation)

            try:
                with open('data.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([gym_id, title, details, address, location, image, operating_preview, rating])
            except FileNotFoundError:
                with open('test.json', 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([gym_id, title, details, address, location, image, operating_preview, rating])


def main(url):
    getwebsite(url)
    each_page(getwebsite(url))

if __name__ == '__main__':
    main('https://www.yelp.ca/search?cflt=gyms&find_loc=Coquitlam%2C+BC&start=10')
