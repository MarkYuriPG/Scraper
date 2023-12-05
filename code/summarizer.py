from dotenv import load_dotenv
import os
import openai
import scraper

def summarize_source(source):
    load_dotenv()

    openai.api_key = os.getenv("API_KEY")

    example = scraper.scrape_txt("example.txt")
    system_prompt = scraper.scrape_txt("sys_prompt.txt") + '\n' +example

    prompt = "Craft a concise and complete summary of this text:\n" + source

    completion = openai.ChatCompletion.create(
    model="gpt-4",
    top_p=0,
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt}
        ]
    )
    reply = completion['choices'][0]['message']['content']
    return reply

source = scraper.scrape_pdf("long_test.pdf")

print(summarize_source(source))