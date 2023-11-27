import requests
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class ActivationMailModel(BaseModel):
    to_mail: str
    activation_url: str = None
    template_code: str = None


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
        },
    }
    response = requests.post(url, headers=headers, data=payload)
    return response.status_code


class WelcomeMailModel(BaseModel):
    recipient_email: str
    template_code: str
    first_name: str = None


@app.post("/send-welcome-mail")
async def send_welcome_mail(item: WelcomeMailModel):
    api_key = "SGFrZWVtLTM4NDE1MzQ4OTc3NS4xMTExNS0xMjU="
    url = "https://mailing.go-mailer.com/api/v1/transactionals/dispatch"
    headers = {
        "Authorization": f"Bearer {api_key}",
    }
    payload = {
        "template_code": item.template_code,
        "recipient_email": item.recipient_email,
        "data": {"first_name,": "Otunla",},
    }
    response = requests.post(url, headers=headers, data=payload)
    return response


class AddToContactModel(BaseModel):
    first_name: str = None
    last_name: str = None
    email: str = None
    


@app.post("/add-to-contact/")
async def add_to_contact(item: AddToContactModel):
    url = "https://users.go-mailer.com/api/contacts"
    api_key = "SGFrZWVtLTM4NDE1MzQ4OTc3NS4xMTExNS0xMjU="
    headers = {
        "Authorization": f"Bearer {api_key}",
    }
    payload = {
        "fname": item.first_name,
        "lname": item.last_name,
        "email": item.email
    }  
    response = requests.post(url=url, headers=headers, data=payload)
    return response
