import ccxt
import pandas as pd
import time
import logging
import backtrader as bt

# === CONFIGURATION ===
API_KEY = "your_api_key"
API_SECRET = "your_api_secret"
SYMBOL = "BTC/USDT"
TIMEFRAME = "5m"
MA_SHORT = 9
MA_LONG = 21
TRADE_AMOUNT = 0.001  # BTC
STOP_LOSS_PERCENT = 0.02  # 2% stop loss
TAKE_PROFIT_PERCENT = 0.04  # 4% take profit
LIVE_TRADING = False  # Set to True for real trades

# === SETUP LOGGING ===
logging.basicConfig(filename="trading_bot.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# === CONNECT TO BINANCE ===
exchange = ccxt.binance({
    "apiKey": API_KEY,
    "secret": API_SECRET,
    "options": {"defaultType": "spot"},
})

# === FETCH MARKET DATA ===
def get_moving_averages(symbol, timeframe, short_period, long_period):
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe)
    df = pd.DataFrame(ohlcv, columns=["timestamp", "open", "high", "low", "close", "volume"])
    df["MA_Short"] = df["close"].rolling(short_period).mean()
    df["MA_Long"] = df["close"].rolling(long_period).mean()
    return df

# === PLACE TRADES ===
def place_order(order_type, amount):
    if LIVE_TRADING:
        if order_type == "buy":
            order = exchange.create_market_buy_order(SYMBOL, amount)
        else:
            order = exchange.create_market_sell_order(SYMBOL, amount)
        logging.info(f"Executed {order_type} order: {order}")
    else:
        print(f"Simulated {order_type} order: {amount} {SYMBOL}")

# === MAIN TRADING LOOP ===
def trading_loop():
    while True:
        try:
            df = get_moving_averages(SYMBOL, TIMEFRAME, MA_SHORT, MA_LONG)
            last_close = df["close"].iloc[-1]
            ma_short = df["MA_Short"].iloc[-1]
            ma_long = df["MA_Long"].iloc[-1]

            if ma_short > ma_long:
                logging.info("BUY Signal: MA Short above MA Long")
                place_order("buy", TRADE_AMOUNT)
            elif ma_short < ma_long:
                logging.info("SELL Signal: MA Short below MA Long")
                place_order("sell", TRADE_AMOUNT)

            time.sleep(300)  # Wait 5 minutes before next check
        except Exception as e:
            logging.error(f"Error: {e}")
            time.sleep(60)

# === BACKTESTING STRATEGY ===
class MovingAverageStrategy(bt.Strategy):
    def __init__(self):
        self.ma_short = bt.indicators.SimpleMovingAverage(self.data.close, period=MA_SHORT)
        self.ma_long = bt.indicators.SimpleMovingAverage(self.data.close, period=MA_LONG)

    def next(self):
        if self.ma_short[0] > self.ma_long[0] and not self.position:
            self.buy()
        elif self.ma_short[0] < self.ma_long[0] and self.position:
            self.sell()

def backtest():
    cerebro = bt.Cerebro()
    data = bt.feeds.GenericCSVData(dataname="historical_data.csv", dtformat="%Y-%m-%d")
    cerebro.adddata(data)
    cerebro.addstrategy(MovingAverageStrategy)
    cerebro.run()
    cerebro.plot()

# === RUN BOT ===
if __name__ == "__main__":
    mode = input("Enter mode (live/backtest): ").strip().lower()
    if mode == "live":
        trading_loop()
    elif mode == "backtest":
        backtest()
    else:
        print("Invalid mode. Use 'live' or 'backtest'.")
