# tsetmc_state
وضعیت بازار بورس ایران
<BR/>

دریافت اطلاعات سایت http://www.tsetmc.com
<BR/>

market.state()
نمایش وضعیت بازار
<BR/>
<BR/>

pip install tsetmc_state
This is a http://www.tsetmc.com data crawler.
<BR/>
<BR/>

from tsetmc_state import market
<BR/>
if(__name__=="__main__"): <BR/>
    market=market()<BR/>
    print(pytse.state()) # وضعیت بازار بورس ایران را نمایش می دهد
