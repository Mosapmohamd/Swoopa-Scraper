from fastapi import FastAPI, HTTPException
import requests

app = FastAPI(title="ScrapingBee Proxy API")

SCRAPINGBEE_API_KEY = "YN1VF40U7FTTOS9C99DP667VGZ7I0NHAL29ON5TT4QLWAM2C8L9VEI6U0O3GN93CGF74X8KU1W558DQN"
TARGET_URL = "https://backend.getswoopa.com/api/marketplace/"
AUTH_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzY2Mzk3OTU5LCJpYXQiOjE3NjYzMTE1NTksImp0aSI6IjkzYjJmZDE1Y2NkMzRjNTJiZDg4MTdmYzMzMGNhZWU1IiwidXNlcl9pZCI6Ijk1MjE2In0.Mfoa3hcvQGBhjcmCcoaztbeCnKm4a7kpA8IIzIN7lAc"

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
                "spb-authorization": f"{AUTH_TOKEN}"
            },
            timeout=30
        )

        return {
            "status_code": response.status_code,
            "data": response.json()
        }

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))

