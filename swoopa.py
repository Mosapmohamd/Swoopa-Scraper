from fastapi import FastAPI, HTTPException
import requests

app = FastAPI(title="ScrapingBee Proxy API")

SCRAPINGBEE_API_KEY = "YOUR_API_KEY"
TARGET_URL = "https://backend.getswoopa.com/api/marketplace/"
AUTH_TOKEN = "YOUR_BEARER_TOKEN"

@app.get("/fetch-marketplace")
def fetch_marketplace():
    try:
        response = requests.get(
            url="https://app.scrapingbee.com/api/v1",
            params={
                "api_key": SCRAPINGBEE_API_KEY,
                "url": TARGET_URL,
                "premium_proxy": "true",
                "country_code": "ca",
                "forward_headers": "true"
            },
            headers={
                "spb-accept": "application/json",
                "spb-authorization": f"Bearer {AUTH_TOKEN}"
            },
            timeout=30
        )

        return {
            "status_code": response.status_code,
            "data": response.json()
        }

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
