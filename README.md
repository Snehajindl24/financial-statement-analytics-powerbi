# Financial Statement Analytics — Power BI

Interactive Power BI dashboard analyzing 5-year financial health (profitability, liquidity, leverage) 
across 8 companies in IT, Banking, and FMCG sectors.

## Pipeline
- **Data extraction**: Python script (`pull_data.py`) using `yfinance` to pull income statement, 
  balance sheet, and cash flow data for 8 companies
- **Data modeling**: Star schema built in Power Query (fact tables per statement type + Dim_Company + Dim_Date)
- **Analysis**: 15+ DAX measures (ROE, ROA, EBITDA margin, D/E ratio, FCF, custom Financial Health Score)
- **Report**: 4-page interactive dashboard with drill-through, what-if parameters, and sector comparison

## Companies covered
IT: TCS, Infosys, Wipro | Banking: HDFC Bank, ICICI Bank, SBI | FMCG: HUL, Nestlé India

## Tools
Python, yfinance, pandas, Power BI, Power Query, DAX
