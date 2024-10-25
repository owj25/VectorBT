import vectorbt as vbt
import datetime as dt

rn = dt.datetime.today()
start = rn - dt.timedelta(days=365)
data = vbt.YFData.download('SPY', start=start, interval='1d').get('Close')
cash = 100

macd = vbt.MACD.run(data)
Lbbands = vbt.BBANDS.run(data, 20)
Sbbands = vbt.BBANDS.run(data, 10)

entries = macd.macd_above(macd.signal) & Sbbands.bandwidth_below(Lbbands.bandwidth)
exits = macd.macd_below(macd.signal) & Sbbands.bandwidth_above(Lbbands.bandwidth)

short_entries = exits
short_exits = entries

pf = vbt.Portfolio.from_signals(data, entries=entries,
                                exits=exits,
                                init_cash=cash,
                                short_exits=short_exits,
                                short_entries=short_entries,
                                freq='1d',
                                fees=0)
fig1 = pf.plot()
fig1.show()

print(pf.stats())

