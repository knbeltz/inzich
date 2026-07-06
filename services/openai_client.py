"""Generates an AI equity research summary via OpenAI with web search."""

from openai import OpenAI
from config.settings import OPENAI_API_KEY
from utils.logger import logger
from services.prompts import EQUITY_RESEARCH_PROMPT

def get_ai_summary(ticker, company_name):
    try: 
        client = OpenAI(api_key=OPENAI_API_KEY)
        response = client.responses.create(
            model="gpt-4o",
            tools=[{"type":"web_search_preview"}],
            input=[{"role": "system", "content": EQUITY_RESEARCH_PROMPT}, {"role": "user", "content": f"Please provide a summary of {company_name} ({ticker})"}]
        )
        return response.output_text
    except Exception as e:
        logger.error(f"Error fetching AI summary: {e}")
        return None
  




