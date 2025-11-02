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
        
        # Używamy fast_info - dużo szybsze i mniej zapytań do API
        fast_info = stock.fast_info
        
        # Pobierz tylko podstawowe dane cenowe
        stock_data = {
            'ticker': ticker.upper(),
            'open': fast_info.get('open', 'N/A'),
            'currency': fast_info.get('currency', 'USD'),
        }
        
        return jsonify(stock_data)
    
    except Exception as e:
        error_msg = str(e)
        
        # Specjalna obsługa błędu 429 (Too Many Requests)
        if '429' in error_msg or 'Too Many Requests' in error_msg:
            return jsonify({
                'error': 'Rate limit exceeded. Please try again in a moment.',
                'ticker': ticker.upper()
            }), 429
        
        return jsonify({'error': f'Failed to fetch data for ticker {ticker}: {str(e)}'}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
