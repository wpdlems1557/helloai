import yfinance as yf

def get_stock_info(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(period="2d")

    if len(data) < 2:
        print("데이터를 가져올 수 없습니다.")
        return

    yesterday = data['Close'][-2]
    today = data['Close'][-1]

    change = today - yesterday
    percent = (change / yesterday) * 100

    print(f"\n📊 {ticker} 주식 정보")
    print(f"현재가: {today:.2f}")
    print(f"전일 대비: {change:.2f}")
    print(f"변동률: {percent:.2f}%")

# 사용자 입력
ticker = input("종목 코드 입력 (예: AAPL, TSLA, 005930.KS): ")
get_stock_info(ticker)
