import requests
import json

def inquire_prompt(prompt, temp=0):
    url = 'http://localhost:5000/generate'
    payload = {
        'prompt': prompt,
        'temp': temp
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Request failed with status code {response.status_code}: {response.text}")

# Example usage
prompt = 'hello'
response = inquire_prompt(prompt)
print('Generated Response:', response['response'])
print('Chat Session:', response['chat_session'])
