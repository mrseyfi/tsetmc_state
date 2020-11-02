from bs4 import BeautifulSoup
from constants import BASE_URL
class market:
    def state(): 
        html_data=rq.get(BASE_URL, timeout=5).text        

        soup = BeautifulSoup(html_data, 'html.parser') #'html5lib' )
        col = soup.find('tr').find_all('td')
        if col and len(col)==2: return col[1].get_text()
        else: return "نامشخص"
