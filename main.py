import requests
import os
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

print("Executing main.py")

app = FastAPI()

load_dotenv()


@app.get("/")
async def root():
    return {"message": "Hello"}


class ActivationMailModel(BaseModel):
    to_mail: str
    activation_url: str = None
    template_code: str = None


@app.post("/send-activation-mail/")
async def send_activation_mail(item: ActivationMailModel):
    api_key = os.environ.get("API_KEY")
    url = os.environ.get("TRANSACTIONAL_EMAIL_URL")
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
    api_key = os.environ.get("API_KEY")
    url = os.environ.get("TRANSACTIONAL_EMAIL_URL")
    headers = {
        "Authorization": f"Bearer {api_key}",
    }
    payload = {
        "template_code": item.template_code,
        "recipient_email": item.recipient_email,
        "data": {
            "first_name,": "Otunla",
        },
    }
    response = requests.post(url, headers=headers, data=payload)
    return response


class AddToContactModel(BaseModel):
    first_name: str = None
    last_name: str = None
    email: str = None


@app.post("/add-to-contact/")
async def add_to_contact(item: AddToContactModel):
    url = os.environ.get("CONTACT_EMAIL_URL")
    api_key = os.environ.get("API_KEY")
    headers = {
        "Authorization": f"Bearer {api_key}",
    }
    payload = {
        "firstname": item.first_name,
        "lastname": item.last_name,
        "email": item.email,
    }
    response = requests.post(url=url, headers=headers, data=payload)
    return response.status_code


@app.get("/get-audience/{email_address}/")
async def get_audience(email_address: str):
    url = f"https://users.go-mailer.com/api/contacts/{email_address}/audiences"
    api_key = os.environ.get("API_KEY")
    headers = {
        "Authorization": f"Bearer {api_key}",
    }
    payload = {"email_address": email_address}
    response = requests.get(url=url, headers=headers, data=payload)
    return response.status_code
