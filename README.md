# Financial Statement Analytics Dashboard (Power BI)

Interactive multi-sector financial health dashboard for 8 NSE-listed companies across IT, Banking, and FMCG — built with a Python ETL pipeline, star-schema modeling, and 15+ custom DAX measures.

## Architecture
- **ETL:** Python (`yfinance`) → 24 CSVs (income statement, balance sheet, cash flow × 8 companies)
- **Model:** Star schema — `Fact_IncomeStatement`, `Fact_BalanceSheet`, `Fact_CashFlow` + `Dim_Company` + `Dim_Date`
- **DAX:** 15+ measures (ROE, margins, D/E, FCF, YoY growth) + composite **Financial Health Score** + RAG risk flags
- **Report:** 4 interactive pages + hidden tooltip page

## Report pages
1. **Executive Overview** — KPI cards, health score bars, sector mix, company risk snapshot  
2. **Trend Analysis** — multi-year trends, YoY growth, ROE vs leverage map, margin stress simulator  
3. **Sector Benchmark** — gradient heatmap matrix + sector profitability comparison  
4. **Drill-through** — company-level income statement line-item deep dive  

## Key features
- Composite Financial Health Score with Red/Amber/Green flags (`SWITCH`)
- Sector heatmap with conditional formatting
- Company drill-through navigation
- What-if margin stress simulator
- Custom hover tooltip page
- Bookmark story mode (Overview → IT → Banking)
- Page navigator + synced slicers

## Companies
| Sector | Companies |
|--------|-----------|
| IT | TCS, Infosys, Wipro |
| Banking | HDFC Bank, ICICI Bank, SBI |
| FMCG | Hindustan Unilever, Nestlé India |

## Key insight
Sector averages hide firm-level quality gaps. In IT, TCS and Infosys clear strong margins with a Financial Health Score of 100, while Wipro lags (~8.6% net margin, score 70). Nestlé India posts outsized ROE (~61%) on low leverage — efficiency over scale. SBI carries a Moderate risk flag (score 55) from higher D/E, even though Banking prints the strongest sector net margins.

## Screenshots
![Executive Overview](screenshots/01_executive_overview.png)
![Trend Analysis](screenshots/02_trend_analysis.png)
![Sector Benchmark](screenshots/03_sector_benchmark.png)
![Drill-through](screenshots/04_drillthrough.png)

## Tech stack
Python (yfinance) · Power BI Desktop · Power Query (M) · DAX · Git

## How to run
1. Clone this repo  
2. `pip install yfinance pandas`  
3. (Optional) refresh data: `python pull_data.py`  
4. Open `Financial_Analytics_Dashboard.pbix` in Power BI Desktop  

## Resume highlight
Built end-to-end financial analytics product: automated ETL → star schema → executive dashboard with drill-through, stress testing, and a defended cross-sector insight.