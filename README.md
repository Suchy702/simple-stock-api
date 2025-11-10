# Simple Stock API

Proste REST API w Pythonie do pobierania danych o akcjach za pomocą yfinance. Aplikacja jest gotowa do wdrożenia na Render.

## 📋 Wymagania

- Python 3.11+
- Konto na [Render](https://render.com) (do deploymentu)

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

## 🌐 Deployment na Render

### Metoda 1: Przez Dashboard (Najprostsza)

1. Wejdź na [Render Dashboard](https://dashboard.render.com/)
2. Kliknij **"New +"** → **"Web Service"**
3. Połącz swoje repozytorium GitHub
4. Wybierz repozytorium `simple-stock-api`
5. Render automatycznie wykryje plik `render.yaml` i skonfiguruje wszystko
6. Kliknij **"Create Web Service"**

Render automatycznie:
- Zainstaluje zależności z `requirements.txt`
- Uruchomi aplikację przez Gunicorn
- Przydzieli darmowy subdomain (np. `simple-stock-api.onrender.com`)

### Metoda 2: Przez render.yaml (Blueprint)

1. Zaloguj się na [Render](https://render.com)
2. Przejdź do **Blueprints**
3. Kliknij **"New Blueprint Instance"**
4. Połącz repozytorium GitHub
5. Render automatycznie wykryje `render.yaml` i wdroży aplikację

### Ważne informacje o Render

**Darmowy tier:**
- Aplikacje "usypiają" po 15 minutach bezczynności
- Pierwsze uruchomienie po uśpieniu może potrwać 30-60 sekund
- 750 godzin/miesiąc darmowego czasu działania
- Nie wymaga karty kredytowej

**Konfiguracja (render.yaml):**
- Runtime: Python 3.11
- Build: `pip install -r requirements.txt`
- Start: `gunicorn app:app`
- Auto-deploy po push do repozytorium

### Deployment ręczny (opcjonalnie)

Jeśli wolisz konfigurować ręcznie:

1. Utwórz nowy Web Service w Render Dashboard
2. Skonfiguruj:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Environment:** Python 3

## 🚀 Po wdrożeniu

Twoja aplikacja będzie dostępna pod adresem:
```
https://simple-stock-api.onrender.com
```

Przykładowe wywołania:
```bash
# Apple
curl "https://simple-stock-api.onrender.com/stock?ticker=AAPL"

# Microsoft  
curl "https://simple-stock-api.onrender.com/stock?ticker=MSFT"
```

**Uwaga:** Przy pierwszym wywołaniu po okresie bezczynności, odpowiedź może potrwać ~30-60 sekund (cold start).

## 🛠️ Technologie

- **Flask** - framework webowy
- **yfinance** - biblioteka do pobierania danych giełdowych
- **Gunicorn** - serwer WSGI do produkcji
- **Render** - platforma deploymentowa (darmowy tier)

## 📝 Licencja

MIT
