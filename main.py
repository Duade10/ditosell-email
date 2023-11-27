import requests
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class ActivationMailModel(BaseModel):
    to_mail: str
    activation_url: str
    template_code: str


@app.get("/")
async def root():
    return {"message": "Hello"}


@app.post("/send-activation-mail/")
async def send_activation_mail(item: ActivationMailModel):
    api_key = "SGFrZWVtLTM4NDE1MzQ4OTc3NS4xMTExNS0xMjU="
    url = "https://mailing.go-mailer.com/api/v1/transactionals/dispatch"
    headers = {
        "Authorization": f"Bearer {api_key}",
    }
    payload = {
        "recipient_email": item.to_mail,
        "template_code": item.template_code,
        "data": {
            "activate_url": item.activation_url,
        }
       
    }
    response = requests.post(url, headers=headers, data=payload)
    print(response.status_code)
    print(response.text)
    return response.status_code
