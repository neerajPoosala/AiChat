import openai

openai.api_key = "your open ai api key"
while True:
    ask =input("ask the question:")
    response = openai.Completion.create(
  model="text-davinci-003",
  prompt=ask,
  temperature=0,
  max_tokens=200,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0.6,
  )
    reply = response["choices"][0]["text"]
    print("answer:"+reply)
    
