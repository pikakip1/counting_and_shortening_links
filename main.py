from urllib.parse import urlparse
from dotenv import load_dotenv
import requests
import os


def shorten_link(token, url):
    headers = {'Authorization': token}
    long_link = {'long_url': url}
    link = 'https://api-ssl.bitly.com/v4/bitlinks'
    response = requests.post(link, headers=headers, json=long_link)
    response.raise_for_status()
    return response.json()['link']


def count_clicks(token, url):
    parse_url = urlparse(url)
    bitlink = f'{parse_url.netloc}{parse_url.path}'
    link = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    headers = {'Authorization': token}

    count_relocations = {
      "units": -1,
      "unit": "day"
        }
    response = requests.get(link, headers=headers, params=count_relocations)
    response.raise_for_status()
    return response.json()['total_clicks']


def is_bitlink(url, token):
    headers = {'Authorization': token}
    url = urlparse(url)
    link = f'https://api-ssl.bitly.com/v4/bitlinks/{url.netloc.strip("www.")}{url.path}'
    response = requests.get(link, headers=headers)
    return response.ok


def main():
    url = input('Введите ссылку: ')
    load_dotenv('BITLINK_TOKEN.env')
    token = os.environ['BITLY_TOKEN']
    try:
        if is_bitlink(url, token):
            return count_clicks(token, url)
        return shorten_link(token, url)
    except requests.exceptions.HTTPError:
        return f'Неверная ссылка'


if __name__ == '__main__':
    print(main())



