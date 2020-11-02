import requests as rq
from bs4 import BeautifulSoup
from tsetmc_state.constants import MAIN_URL
class market:
    def state(): 
        html_data=rq.get(MAIN_URL, timeout=5).text        

        soup = BeautifulSoup(html_data, 'html.parser') #'html5lib' )
        col = soup.find('tr').find_all('td')
        if col and len(col)==2: return col[1].get_text().strip()
        else: return "نامشخص"

#   by: mehrdad seyfi
#   www.mrseyfi.ir
#   2020-9-2
