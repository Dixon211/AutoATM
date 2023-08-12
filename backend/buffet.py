import openai
from dotenv import load_dotenv
import os
import re

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

def assess(company_name = "NVIDIA"):
    principles = [
        f"Understanding the Business of {company_name}",
        f"Intrinsic Value of {company_name}",
        f"Economic Moats of {company_name}",
        f"Long-Term Thinking for {company_name}",
        f"Focus on Quality of {company_name}",
        f"Risk Aversion for {company_name}",
        f"Good Management of {company_name}",
        f"Market Trends for {company_name}",
        f"Margin of Safety for {company_name}",
        f"Market Sentiment for {company_name}",
        f"Return on Equity of {company_name}"
    ]

    prompt = "Please provide a numerical assessment between 0 and 100 for the following Warren Buffett principles in the form of a python list:\n"
    prompt += '\n'.join(principles)
    openai.api_key = os.getenv('OPENAI_API_KEY')
    print(openai.Model.list())
    print(prompt)
    
    response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=1500
    )

    # Extracting the list from the response
    #numeric_scores = re.findall(r'\d+\.\d+|\d+', response.choices[0].text)
    numeric_scores = response.choices[0].text.split("\n")
    print(response.choices[0].text)
    die

    # Converting the scores to float
    numeric_scores = [float(score) for score in numeric_scores]

    for i in len(numeric_scores):
        print(principles[i])
        print(numeric_scores[i])

assess()