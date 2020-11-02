# tsetmc_state
وضعیت بازار بورس ایران
<BR/>
دریافت اطلاعات سایت http://www.tsetmc.com
<BR/>

<div class="highlight highlight-source-js"><pre>
market.state()
</pre></div>

نمایش وضعیت بازار
<BR/>
<BR/>

<div class="highlight highlight-source-js"><pre>
pip install git+https://github.com/mrseyfi/tsetmc_state
</pre></div>
This is a http://www.tsetmc.com data crawler.
<BR/>
<BR/>

from tsetmc_state import market
<BR/>
if(__name__=="__main__"): <BR/>
    market=market()<BR/>
    print(pytse.state()) # وضعیت بازار بورس ایران را نمایش می دهد
