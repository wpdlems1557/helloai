import yfinance as yf
import matplotlib.pyplot as plt

def get_stock_info(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(period="5d") # 흐름을 보기 위해 5일치로 변경 권장

    if len(data) < 2:
        print("데이터를 가져올 수 없습니다.")
        return None, None, None

    yesterday = data['Close'].iloc[-2]
    today = data['Close'].iloc[-1]
    change = today - yesterday
    percent = (change / yesterday) * 100
    
    return data, change, today, percent

ticker = input("종목 코드 입력: ")
data, change, today, percent = get_stock_info(ticker)

if data is not None:
    print(f"\n📊 {ticker} 주식 정보")
    print(f"현재가: {today:.2f}")
    print(f"전일 대비: {change:.2f}")
    print(f"변동률: {percent:.2f}%")

    if change > 0:
        print("📈 상승")
    else:
        print("📉 하락")
        
    data['Close'].plot(title=f"{ticker} Stock Price")
    plt.show()
