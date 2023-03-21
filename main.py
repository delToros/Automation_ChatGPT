import requests
import argparse
import os

# parser = argparse.ArgumentParser()
# parser.add_argument('prompt', help='The prompt to send to the OpenAI API')
# parser.add_argument('filename', help='Name for python file')
# args = parser.parse_args()

prompt = input('What do you want to do?\n')
filename = input('\nWhat file should be called?\n')

URL = 'https://api.openai.com/v1/completions'
API_KEY = os.getenv('PWS')
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + API_KEY
}
print(HEADERS)
REQUEST_DATA = {
    "model": "text-davinci-003",
    # "prompt": f"Write python script for {args.prompt}. Provide only code, no text",
    "prompt": f"Write python script for {prompt}. Provide only code, no text",
    "max_tokens": 1000,
    "temperature": 0.5
}

response = requests.post(url=URL, headers=HEADERS, json=REQUEST_DATA)

if response.status_code == 200:
    response_text = (response.json()['choices'][0]['text'])
    # with open(args.filename, 'w') as file:
    with open(f'{filename}.py', 'w') as file:
        file.write(response_text)
else:
    print(f'Request Failed with status: {str(response.status_code)}')
