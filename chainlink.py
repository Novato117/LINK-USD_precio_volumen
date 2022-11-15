import datetime 
from datetime import date,timedelta
import yfinance as yf
import plotly.graph_objects as go
import plotly.express as px

end_date=date.today().strftime("%Y-%m-%d")
#print(end_date)
d2=date.today() - timedelta(days=365)
start_date=d2.strftime("%Y-%m-%d")
#print(d2)

data=yf.download('LINK-USD',start=start_date,end=end_date,progress=False)
print(data)

data["Date"]=data.index
data=data[["Date","Open","High","Low","Close","Adj Close","Volume"]]
data.reset_index(drop=True,inplace=True)
print(data.head())

figure=go.Figure(data=[go.Candlestick(x=data["Date"],
                                      open=data["Open"],
                                      high=data["High"],
                                      low=data["Open"],
                                      close=data["Close"])])
figure.update_layout(title="Chainlink stock price Analysis",xaxis_rangeslider_visible=False)
figure.show()

figure=px.bar(data,x="Date",y="Close")
figure.show()

figure=px.bar(data,x="Date",y="Volume")
figure.show()

figure=px.line(data,x='Date',y='Close',title='stock chainlink with rangeslider')
figure.update_xaxes(rangeslider_visible=True)
figure.show()

figure = px.line(data, x='Date', y='Close', 
                 title='Stock Market Analysis with Time Period Selectors')
figure.update_xaxes(
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=3, label="3m", step="month", stepmode="backward"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)
