from gpt4all import GPT4All


model = GPT4All(model_name='orca-mini-3b.ggmlv3.q4_0.bin')
with model.chat_session():
    response1 = model.generate(prompt='hello', temp=0)
    print(model.current_chat_session)