# 🚀 PyQuotex API Server

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-green.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-009688.svg)](https://fastapi.tiangolo.com)

**Modified version of [PyQuotex](https://github.com/cleitonleonel/pyquotex) by Cleiton Leonel Creton**

A production-ready FastAPI server providing REST API endpoints for the Quotex trading platform. This project is built on top of the open-source PyQuotex library and provides a clean HTTP interface for candle data retrieval.

---

## ⚠️ Important Notice

This is a **modified version** of the original [PyQuotex library](https://github.com/cleitonleonel/pyquotex) created by **Cleiton Leonel Creton**. All modifications are released under the same **GNU GPL v3 license** to comply with the original license terms.

**Original Author**: Cleiton Leonel Creton  
**Original Repository**: https://github.com/cleitonleonel/pyquotex  
**License**: GNU General Public License v3.0

This library is **not a trading bot** and does not make trading decisions. It's a tool for developers to integrate with the Quotex platform.

---

## 🎯 Features

- ✅ **FastAPI REST API** - Clean HTTP endpoints for candle data
- ✅ **Real-time WebSocket** - Live connection to Quotex platform
- ✅ **Candle Data Retrieval** - Fetch historical and real-time candles
- ✅ **Multiple Timeframes** - Support for various candle periods
- ✅ **Auto-reconnection** - Handles connection drops gracefully
- ✅ **Production Ready** - Optimized for deployment on Render.com
- ✅ **GPL v3 Compliant** - Fully open-source

---

## 📋 Requirements

- Python 3.12 or higher
- Quotex account (email & password)
- Playwright browsers installed

---

## 🛠 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/pyquotex-api.git
cd pyquotex-api
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
playwright install
```

### 3. Configure credentials

Create a `.env` file:

```bash
cp .env.example .env
```

Edit `.env` with your credentials:

```env
PYQUOTEX_EMAIL=your_email@example.com
PYQUOTEX_PASSWORD=your_password_here
LOG_LEVEL=INFO
```

### 4. Run the server

```bash
uvicorn api:app --host 0.0.0.0 --port 10000
```

The API will be available at `http://localhost:10000`

---

## 🌐 API Endpoints

### Health Check

```http
GET /health
```

**Response:**
```json
{
  "status": "ok"
}
```

---

### Get Last N Candles

```http
GET /candles/last?asset=EURUSD_otc&count=50&period=60
```

**Parameters:**
- `asset` (required): Asset symbol (e.g., `EURUSD_otc`, `USDJPY_otc`)
- `count` (optional): Number of candles (default: 50, max: 2000)
- `period` (optional): Candle period in seconds (default: 60)

**Response:**
```json
{
  "asset": "EURUSD_otc",
  "period": 60,
  "count": 50,
  "candles": [
    {
      "asset": "EURUSD_otc",
      "time": 1704067200,
      "date": "2024-01-01",
      "time_hm": "12:00",
      "open": 1.10450,
      "close": 1.10475,
      "low": 1.10440,
      "high": 1.10480,
      "ticks": 120,
      "color": "green"
    }
  ]
}
```

---

### Get Candles by Time Range

```http
GET /candles/range?asset=EURUSD_otc&period=60&offset=3600
```

**Parameters:**
- `asset` (required): Asset symbol
- `period` (optional): Candle period in seconds (default: 60)
- `offset` (optional): Time offset in seconds from now (default: 3600)

**Response:** Same format as `/candles/last`

---

## 🚀 Deploy to Render.com (FREE)

### 1. Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/pyquotex-api.git
git push -u origin main
```

### 2. Create Web Service on Render

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click **New +** → **Web Service**
3. Connect your GitHub repository
4. Configure:
   - **Name**: `pyquotex-api`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt && playwright install`
   - **Start Command**: `uvicorn api:app --host 0.0.0.0 --port 10000`
   - **Instance Type**: `Free`

### 3. Add Environment Variables

In Render dashboard, add:
- `PYQUOTEX_EMAIL` = your_email@example.com
- `PYQUOTEX_PASSWORD` = your_password

### 4. Deploy

Click **Create Web Service** and wait for deployment to complete.

Your API will be live at: `https://your-app-name.onrender.com`

---

## 📚 Usage Examples

### Python

```python
import requests

# Get last 100 candles
response = requests.get(
    "http://localhost:10000/candles/last",
    params={
        "asset": "EURUSD_otc",
        "count": 100,
        "period": 60
    }
)
data = response.json()
print(f"Fetched {data['count']} candles for {data['asset']}")
```

### cURL

```bash
curl "http://localhost:10000/candles/last?asset=EURUSD_otc&count=50&period=60"
```

### JavaScript

```javascript
fetch('http://localhost:10000/candles/last?asset=EURUSD_otc&count=50&period=60')
  .then(res => res.json())
  .then(data => console.log(data));
```

---

## 🔧 Configuration

### Supported Assets

Common OTC pairs:
- `EURUSD_otc`, `GBPUSD_otc`, `USDJPY_otc`
- `AUDCAD_otc`, `NZDCAD_otc`, `USDCAD_otc`
- `XAUUSD_otc` (Gold), `XAGUSD_otc` (Silver)
- `BTCUSD_otc`, `ETHUSD_otc`

### Supported Timeframes

- `60` - 1 minute
- `300` - 5 minutes
- `900` - 15 minutes
- `1800` - 30 minutes
- `3600` - 1 hour

---

## 📄 License

This project is licensed under the **GNU General Public License v3.0** - see the [LICENSE](LICENSE) file for details.

### Original Work

This is a modified version of [PyQuotex](https://github.com/cleitonleonel/pyquotex) by **Cleiton Leonel Creton**, also licensed under GPL v3.

As required by the GPL v3 license:
- ✅ Source code is publicly available
- ✅ Original author credits are maintained
- ✅ Modifications are documented
- ✅ Same license is applied to derivative work

---

## 🤝 Credits

**Original Author**: [Cleiton Leonel Creton](https://github.com/cleitonleonel)  
**Original Project**: [PyQuotex](https://github.com/cleitonleonel/pyquotex)

### Support the Original Author

- Telegram: [@cleitonleonel](https://t.me/cleitonleonel)
- Buy Me a Coffee: [cleiton.leonel](https://www.buymeacoffee.com/cleiton.leonel)

**Crypto Donations:**
- **Dogecoin**: `DMwSPQMk61hq49ChmTMkgyvUGZbVbWZekJ`
- **Bitcoin**: `bc1qtea29xkpyx9jxtp2kc74m83rwh93vjp7nhpgkm`
- **Ethereum**: `0x20d1AD19277CaFddeE4B8f276ae9f3E761523223`
- **Solana**: `4wbE2FVU9x4gVErVSsWwhcdXQnDBrBVQFvbMqaaykcqo`

---

## ⚠️ Disclaimer

This software is for educational purposes only. Use at your own risk. The authors are not responsible for any financial losses incurred while using this software.

Trading binary options involves substantial risk of loss and is not suitable for all investors.

---

## 📞 Contact

For issues related to this modified version, please open an issue on GitHub.

For questions about the original PyQuotex library, contact the original author:
- Telegram: [@cleitonleonel](https://t.me/cleitonleonel)
- GitHub: [cleitonleonel](https://github.com/cleitonleonel)

---

**Made with ❤️ using [PyQuotex](https://github.com/cleitonleonel/pyquotex)**
