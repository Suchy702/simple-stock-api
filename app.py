from flask import Flask, jsonify, request
import yfinance as yf

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({
        'message': 'Stock API',
        'usage': 'GET /stock?ticker=AAPL'
    })


@app.route('/stock', methods=['GET'])
def get_stock_info():
    ticker = request.args.get('ticker')
    
    if not ticker:
        return jsonify({'error': 'Ticker parameter is required'}), 400
    
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        
        # Wybierz najważniejsze informacje
        stock_data = {
            'ticker': ticker.upper(),
            'name': info.get('longName', 'N/A'),
            'currency': info.get('currency', 'N/A'),
            'currentPrice': info.get('currentPrice', info.get('regularMarketPrice', 'N/A')),
            'previousClose': info.get('previousClose', 'N/A'),
            'open': info.get('open', info.get('regularMarketOpen', 'N/A')),
            'dayHigh': info.get('dayHigh', info.get('regularMarketDayHigh', 'N/A')),
            'dayLow': info.get('dayLow', info.get('regularMarketDayLow', 'N/A')),
            'volume': info.get('volume', info.get('regularMarketVolume', 'N/A')),
            'marketCap': info.get('marketCap', 'N/A'),
            'fiftyTwoWeekHigh': info.get('fiftyTwoWeekHigh', 'N/A'),
            'fiftyTwoWeekLow': info.get('fiftyTwoWeekLow', 'N/A'),
            'sector': info.get('sector', 'N/A'),
            'industry': info.get('industry', 'N/A'),
        }
        
        return jsonify(stock_data)
    
    except Exception as e:
        return jsonify({'error': f'Failed to fetch data for ticker {ticker}: {str(e)}'}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
