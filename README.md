# tsetmc_state
وضعیت بازار بورس ایران

دریافت اطلاعات سایت http://www.tsetmc.com

market.state()
نمایش وضعیت بازار

pip install tsetmc_state
This is a http://www.tsetmc.com data crawler.

from tsetmc_state import market

if(__name__=="__main__"):
    market=market()
    print(pytse.state()) # وضعیت بازار بورس ایران را نمایش می دهد
