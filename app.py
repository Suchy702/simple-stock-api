from flask import Flask, jsonify, request
from flask_cors import CORS
import yfinance as yf

app = Flask(__name__)

CORS(app, resources={
    r"/*": {
        "origins": [
            'https://simple-fund-cf708.web.app',
            'https://simple-fund-cf708.firebaseapp.com'
        ]
    }
})


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
        
        # Próbujemy różne okresy - Yahoo czasem ma problemy z niektórymi
        hist = None
        for period in ['1d', '5d', '1mo']:
            try:
                hist = stock.history(period=period)
                if not hist.empty:
                    break
            except:
                continue
        
        if hist is None or hist.empty:
            # Fallback - próbuj download
            try:
                data = yf.download(ticker, period='1d', progress=False)
                if not data.empty:
                    hist = data
            except:
                pass
        
        if hist is None or hist.empty:
            return jsonify({
                'error': f'No data available for ticker {ticker}',
                'suggestion': 'Yahoo Finance may be experiencing issues or ticker symbol is incorrect. Try again later.'
            }), 404
        
        # Pobierz ostatni wiersz z danymi (najnowsze dane)
        last = hist.iloc[-1]
        previous = hist.iloc[-2] if len(hist) > 1 else last
        
        # Pobierz informację o walucie
        try:
            info = stock.info
            currency = info.get('currency', None)
        except:
            currency = None
        
        stock_data = {
            'ticker': ticker.upper(),
            'currentPrice': round(float(last['Close']), 2),
            'previousClose': round(float(previous['Close']), 2),
            'open': round(float(last['Open']), 2),
            'dayHigh': round(float(last['High']), 2),
            'dayLow': round(float(last['Low']), 2),
            'volume': int(last['Volume']),
            'currency': currency,
        }
        
        return jsonify(stock_data)
    
    except Exception as e:
        error_msg = str(e)
        
        # Specjalna obsługa błędu 429 (Too Many Requests)
        if '429' in error_msg or 'Too Many Requests' in error_msg:
            return jsonify({
                'error': 'Rate limit exceeded. Yahoo Finance has request limits.',
                'suggestion': 'Please try again in a few moments.',
                'ticker': ticker.upper()
            }), 429
        
        return jsonify({
            'error': f'Failed to fetch data for ticker {ticker}',
            'details': error_msg
        }), 500


if __name__ == '__main__':
    # Lokalnie możesz ustawić PORT, a Heroku zrobi to automatycznie
    import os
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
