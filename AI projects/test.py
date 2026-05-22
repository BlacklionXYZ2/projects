from google import genai

client = genai.Client()

response = client.models.generate_content_stream(
    model = 'gemini-3.5-flash', contents = 'Hi gemini, this is my first API call'
)

for chunk in response:
    print(chunk.text, end = '', flush = True)