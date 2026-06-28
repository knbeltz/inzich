'''
Psedocode: 

function resolve_company(user_input: str) -> tuple[str, str]:

    build OpenAI messages: system prompt + user_input as user message

    call OpenAI chat completion (gpt-4.1-mini), get response text

    parse response text with json.loads() → data dict

    if data["outcome"] == "recognized":
        return (data["ticker"].upper(), data["company_name"])

    if data["outcome"] == "not_traded":
        raise CompanyResolverError(reason="not_traded", message="...")

    if data["outcome"] == "multiple_companies":
        raise CompanyResolverError(reason="multiple_companies", message="...")

    if data["outcome"] == "unrecognized":
        raise CompanyResolverError(reason="unrecognized", message="...")


'''
import json 
from openai import OpenAI 
from config.settings import OPENAI_API_KEY

prompt = """You are a financial data assistant. The user will give you a company name, possibly misspelled or informally written. Your job is to determine if it is a single, publicly traded company available on Yahoo Finance.

You must always respond with a JSON object and nothing else. No explanation, no prose.

The JSON must have exactly one field: "outcome". Based on what you find:

If recognized and publicly traded: {"outcome": "recognized", "ticker": "AAPL", "company_name": "Apple Inc."}
If not publicly traded: {"outcome": "not_traded", "company_name": "..."}
If the input refers to multiple companies: {"outcome": "multiple_companies"}
If unrecognizable/gibberish: {"outcome": "unrecognized"}"""

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
            {"role": "system", "content": prompt },
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


