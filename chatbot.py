from patterns import patterns   # only import patterns, not itself
import pandas as pd

df = pd.read_csv("cleaned_dataset.csv", encoding='utf-8') 

def respond(message: str):
    message = message.strip().lower()
    for _, row in df.iterrows():
        company_name = row['Name'].lower()
        website = row['Website']
        if company_name in message:
            # First, check patterns for the company
            for pattern, responses in patterns:
                if pattern.search(message):
                    answer = responses[0]
                    return f"{answer}\n\nFor more information about the company, please visit: {website}"
            # If there is no specific pattern for the company, return only the website
            return f"For more information about the company, please visit: {website}"

    # ====== Other responses like funding stages or identity ======
    for pattern, responses in patterns:
        if pattern.search(message):
            return responses[0]

    # ====== Fallback ======
    return "Sorry, I don't have enough information about your question, but don't worry — with Marqab, no one needs to be afraid!"

  