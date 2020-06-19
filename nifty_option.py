from nsepy import get_history
from datetime import date
from nsepy.derivatives import get_expiry_date
import mpl_finance as mpf
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
#data = get_history(symbol="SBIN", start=date(2020,5,1), end=date(2020,5,31))


nifty_opt = get_history(symbol="NIFTY",
                        start=date(2020,6,1),
                        end=date(2020,6,20),
                        index=True,
                        option_type='CE',
                        strike_price=10300,
                        expiry_date=date(2020,6,25))
nifty_opt.index = pd.to_datetime(nifty_opt.index)
dvalues = nifty_opt[['Open', 'High', 'Low', 'Close']].values.tolist()
pdates = mdates.date2num(nifty_opt.index)
ohlc = [ [pdates[i]] + dvalues[i] for i in range(len(pdates)) ]
plt.style.use('fivethirtyeight')
fig, ax = plt.subplots(figsize = (12,6))
mpf.candlestick_ohlc(ax, ohlc,colorup='g',colordown='r')
ax.set_xlabel('Date')
ax.set_ylabel('Price ($)')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
ax.set_title('NIFTY_JUN25_10300_CE')
fig.autofmt_xdate()
plt.show()


