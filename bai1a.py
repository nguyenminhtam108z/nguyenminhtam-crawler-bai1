import requests
import re
from bs4 import BeautifulSoup
link = 'http://45.79.43.178/source_carts/wordpress/wp-admin/'
response = requests.get(link)
action = re.search(pattern='action="(.*?)"', string=str(response.content)).group(1)
form_data = {
    'log':'admin',
    'pwd':'123456aA'
}
with requests.Session() as s:
    data = s.post(action, data=form_data)
    soup = BeautifulSoup(data.text, 'html.parser')
    li_tag = soup.find("li", attrs={'id': 'wp-admin-bar-my-account'})
    a_tag = li_tag.find('a', attrs={'class': 'ab-item'})
    name = a_tag.text.split(',')[0]
    print(name)
