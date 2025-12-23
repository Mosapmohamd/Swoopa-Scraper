from fastapi import FastAPI, HTTPException
import requests

app = FastAPI(title="ScrapingBee Proxy API")

SCRAPINGBEE_API_KEY = "4Z7NQS4HD6KZ37X8R46ACMJLZ0JG2INPMVNVSTRZJ9RUK5EE305BFU9XX1FFUGIEBY1UG7PIIQE3GA54"
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




