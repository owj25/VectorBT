import vectorbt as vbt
import numpy as np
import datetime as dt

deltaDays = 366
cash = 500

rn = dt.datetime.today()
start = rn - dt.timedelta(days=deltaDays)

data = vbt.YFData.download('SPY', interval='1d', start=start).get('Close')

Sbbands = vbt.BBANDS.run(data, 10)
Lbbands = vbt.BBANDS.run(data, 50)
rsi = vbt.RSI.run(data)

entries = Sbbands.close_above(Sbbands.upper) | Sbbands.bandwidth_below(Lbbands.bandwidth)
exits = Sbbands.close_below(Sbbands.lower)

short_entries = Sbbands.close_below(Sbbands.lower)
short_exits = Sbbands.close_above(Sbbands.upper) | Sbbands.bandwidth_below(Lbbands.bandwidth)

pf = vbt.Portfolio.from_signals(data, entries=entries,
                                exits=exits,
                                init_cash=cash,
                                short_exits=short_exits,
                                short_entries=short_entries,
                                freq='1d',
                                fees=0,
                                sl_stop=0.01)

fig1 = pf.plot()
fig1.show()

print(pf.stats())



