import vectorbt as vbt
import datetime as dt

rn = dt.datetime.today()

start = rn - dt.timedelta(minutes=10079)

data = vbt.YFData.download('DOGE-USD', start=start, interval='1m').get('Close')
cash = 100

entries = None
exits = None

short_entries = None
short_exits = None


pf = vbt.Portfolio.from_signals(data, entries=entries,
                                exits=exits,
                                short_entries=short_entries,
                                short_exits=short_exits,
                                init_cash=cash,
                                freq='1m',
                                sl_stop=0.1,
                                fees=0.000)
fig1 = pf.plot()
fig1.show()

print(pf.stats())


