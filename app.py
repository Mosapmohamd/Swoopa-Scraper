from fastapi import FastAPI, HTTPException
import requests

app = FastAPI(title="ScrapingBee Proxy API")

SCRAPINGBEE_API_KEY = "YN1VF40U7FTTOS9C99DP667VGZ7I0NHAL29ON5TT4QLWAM2C8L9VEI6U0O3GN93CGF74X8KU1W558DQN"
TARGET_URL = "https://backend.getswoopa.com/api/marketplace/"
AUTH_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzY2NjAzNzg3LCJpYXQiOjE3NjY1MTczODcsImp0aSI6IjA3MzllZjhiNmZiNDQ3Y2FiMzllNDhiOWFiMWYwNzRkIiwidXNlcl9pZCI6Ijk1MjE2In0.EWRm0_Yn3Gv3px5TcWwh0klpMIV9S5jgKd9j2mFtC90"

SCRAPINGBEE_ENDPOINT = "https://app.scrapingbee.com/api/v1"


@app.get("/")
def health():
    return {"status": "running"}


@app.get("/fetch-marketplace")
def fetch_marketplace():
    try:
        response = requests.get(
            url=SCRAPINGBEE_ENDPOINT,
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

        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail=response.text
            )

        return response.json()

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))



