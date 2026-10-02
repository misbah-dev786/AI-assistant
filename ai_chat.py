from openai import OpenAI

api_key = "YOUR_API_KEY_HERE"
base_url = "URL"
model = "MODEL_NAME"

client = OpenAI(api_key=api_key,base_url=base_url)

def ask_Ai(command):
    
        responce = client.chat.completions.create(
            model=model,
            messages=[
                {"role":"system","content":"you ar a helpful assistant."},
                {"role":"user","content":command}
            ]
        )
        
        return "responce : ",responce.choices[0].message.content
