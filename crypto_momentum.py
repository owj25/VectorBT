import vectorbt as vbt
import numpy as np
import datetime as dt

rn = dt.datetime.today()

start = rn - dt.timedelta(minutes=10079)

data = vbt.YFData.download('BTC-USD', start=start, interval='1m').get('Close')
cash = 100

fast_ma = vbt.MA.run(data, 2)
slow_ma = vbt.MA.run(data, 7)
=
entries = fast_ma.ma_above(slow_ma.ma) 
exits = fast_ma.ma_crossed_below(slow_ma)

short_entries = fast_ma.ma_below(slow_ma.ma) 
short_exits = fast_ma.ma_crossed_above(slow_ma)

pf = vbt.Portfolio.from_signals(data, entries=entries,
                                exits=exits,
                                init_cash=cash,
                                freq='1m',
                                fees=0.0,
                                sl_stop=0.1)
fig1 = pf.plot()
slow_ma.ma.vbt.plot(fig=fig1)
fast_ma.ma.vbt.plot(fig=fig1)
fig1.show()

print(pf.stats())

