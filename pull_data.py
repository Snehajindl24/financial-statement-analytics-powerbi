import yfinance as yf
import pandas as pd
import os
import time

tickers = {
    "TCS.NS": "IT", "INFY.NS": "IT", "WIPRO.NS": "IT",
    "HDFCBANK.NS": "Banking", "ICICIBANK.NS": "Banking", "SBIN.NS": "Banking",
    "HINDUNILVR.NS": "FMCG", "NESTLEIND.NS": "FMCG"
}

os.makedirs("raw_data", exist_ok=True)
log = []

for ticker, sector in tickers.items():
    stock = yf.Ticker(ticker)
    statements = {
        "income_stmt": stock.financials,
        "balance_sheet": stock.balance_sheet,
        "cash_flow": stock.cashflow
    }
    for name, df in statements.items():
        if not df.empty:
            df.to_csv(f"raw_data/{ticker.replace('.NS','')}_{name}.csv")
            log.append(f"OK  {ticker:15} {name:15} rows={df.shape[0]} years={df.shape[1]}")
        else:
            log.append(f"FAIL {ticker:15} {name:15} EMPTY")
    time.sleep(1)

print("\n".join(log))
with open("raw_data/pull_log.txt", "w") as f:
    f.write("\n".join(log))