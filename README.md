# Simple Stock API

Proste REST API w Pythonie do pobierania danych o akcjach za pomocą yfinance. Aplikacja jest gotowa do wdrożenia na fly.io.

## 📋 Wymagania

- Python 3.11+
- Konto na [fly.io](https://fly.io) (do deploymentu)
- flyctl CLI (do deploymentu)

## 🚀 Instalacja lokalna

1. Sklonuj repozytorium:
```bash
git clone https://github.com/Suchy702/simple-stock-api.git
cd simple-stock-api
```

2. Zainstaluj zależności:
```bash
pip install -r requirements.txt
```

3. Uruchom aplikację:
```bash
python app.py
```

Aplikacja będzie dostępna pod adresem: `http://localhost:8080`

## 📡 Użycie API

### Endpoint główny
```
GET /
```
Zwraca informacje o API i instrukcje użycia.

### Pobierz dane o akcji
```
GET /stock?ticker=AAPL
```

Parametry:
- `ticker` (wymagany) - symbol tickera giełdowego (np. AAPL, MSFT, TSLA)

Przykładowa odpowiedź:
```json
{
  "ticker": "AAPL",
  "name": "Apple Inc.",
  "currency": "USD",
  "currentPrice": 178.72,
  "previousClose": 177.38,
  "open": 177.83,
  "dayHigh": 179.26,
  "dayLow": 177.62,
  "volume": 45678900,
  "marketCap": 2789000000000,
  "fiftyTwoWeekHigh": 199.62,
  "fiftyTwoWeekLow": 164.08,
  "sector": "Technology",
  "industry": "Consumer Electronics"
}
```

### Przykłady wywołań

```bash
# Apple
curl "http://localhost:8080/stock?ticker=AAPL"

# Microsoft
curl "http://localhost:8080/stock?ticker=MSFT"

# Tesla
curl "http://localhost:8080/stock?ticker=TSLA"
```

## 🌐 Deployment na fly.io

1. Zainstaluj flyctl:
```bash
curl -L https://fly.io/install.sh | sh
```

2. Zaloguj się do fly.io:
```bash
flyctl auth login
```

3. Uruchom aplikację (pierwsza komenda utworzy aplikację):
```bash
flyctl launch
```

4. Deploy aplikacji:
```bash
flyctl deploy
```

5. Otwórz aplikację w przeglądarce:
```bash
flyctl open
```

Twoja aplikacja będzie dostępna pod adresem: `https://simple-stock-api.fly.dev`

### Konfiguracja fly.io

Plik `fly.toml` zawiera konfigurację:
- Region: `waw` (Warszawa)
- Port wewnętrzny: `8080`
- Auto-scaling: włączony
- Minimalna ilość maszyn: 0 (oszczędność kosztów)

## 🛠️ Technologie

- **Flask** - framework webowy
- **yfinance** - biblioteka do pobierania danych giełdowych
- **Gunicorn** - serwer WSGI do produkcji
- **Docker** - konteneryzacja
- **fly.io** - platforma deploymentowa

## 📝 Licencja

MIT
