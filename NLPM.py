from transformers  import pipeline 


def chat_answer (message :str):
    model = pipeline("text-generation", model="gpt2")
    
    response = model(message,max_new_tokens=30, num_return_sequences=1, do_sample=True,
         temperature=0.7 ,top_k=50,top_p=0.9)
    answer = response[0]["generated_text"]
    answer = answer[len(message):].strip()
    answer = answer.split("\n")[0]    

    return answer