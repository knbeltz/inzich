"""Resolves free-text company names to confirmed tickers via OpenAI."""

import json
from openai import OpenAI
from config.settings import OPENAI_API_KEY
from services.prompts import COMPANY_RESOLVER_PROMPT

class CompanyResolverError(Exception):
    def __init__(self, reason, message):
        self.reason = reason
        self.message = message 
        super().__init__(message)

def resolve_company(user_input: str) -> tuple[str, str]: 
    "Takes user input and validates it with OpenAI"

    client = OpenAI(api_key=OPENAI_API_KEY)

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {"role": "system", "content": COMPANY_RESOLVER_PROMPT},
            {"role": "user", "content": user_input}
        ]
    )

    data = json.loads(response.output_text)

    if data["outcome"] == "recognized":
        return (data["ticker"].upper(), data["company_name"])
    
    if data["outcome"] == "not_traded":
        raise CompanyResolverError(reason="not_traded", message=f"{user_input} is not a publicly traded company.")
    
    if data["outcome"] == "multiple_companies":
        raise CompanyResolverError(reason="multiple_companies", message="Please enter one company at a time.")
    
    if data["outcome"] == "unrecognized":
        raise CompanyResolverError(reason="unrecognized", message="Please enter a valid company name.")


