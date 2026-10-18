import requests

API_KEY = "XXX"
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent"

headers = {
    "x-goog-api-key": API_KEY,
    "content-type": "application/json"
}

lead_message = input("Enter the leads message: ")
prompt = f"""
You are a qualification assistant. Based on the message below, respond in exactly this format:

label : <Hot, Warm, or Cold>
Reply: <a short friendly reply to the lead>

message:{lead_message}
"""
data = {
    "contents":[
        {
            "parts":[
                {"text": prompt}
            ]
        }
    ]
}

response = requests.post(url, headers=headers, json=data)
result = response.json()
if "error" in result:
    print("Something went wrong:", result["error"]["message"])
else:
    reply_text = result['candidates'][0]['content']['parts'][0]['text']
    print(reply_text)

    with open("leads_log.txt", "a") as file:
        file.write(f"lead: {lead_message}\n")
        file.write(f"Reply: {reply_text}\n")
        file.write("---\n")
