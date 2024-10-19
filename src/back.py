#Sean Broderick

import onnxruntime_genai as og
import os


model = og.Model('models\\phi3') #accuracy level 4 phi3 mini 128K cpu model
tokenizer = og.Tokenizer(model)
tokenizer_stream = tokenizer.create_stream()
 
# Set the max length to something sensible by default,
# since otherwise it will be set to the entire context length
search_options = {}
search_options['max_length'] = 2048

#we handle model contexting and RAG here
#excluded:
#You are an expert assistant that answers questions about #PURPOSE OF MODEL AND CREATING PROPOSALS#.


textContext = ""
def generation(self, userInput):
    global textContext
    #global prompt_template
    
    textInput = userInput
    if not textInput:
        print("Error, input cannot be empty")
        exit

    #include context along with input here
    prompt = f"<|system|>\n<|end|>\n<|user|>\nContext conversation:\n{textContext}\nMost recent user question:\n{textInput}<|end|>\n<|assistant|>\n"

    input_tokens = tokenizer.encode(prompt)

    params = og.GeneratorParams(model)
    params.set_search_options(**search_options)
    params.input_ids = input_tokens
    generator = og.Generator(model, params)

    print("pre-gen:\n")
    response = ""
    try:
        while not generator.is_done():
            generator.compute_logits()
            generator.generate_next_token()

            new_token = generator.get_next_tokens()[0]
            token_str = tokenizer_stream.decode(new_token)
            response += token_str
        
            self.update_str(token_str) 
            #print(tokenizer_stream.decode(new_token), end='', flush=True)
            #print(response)

    except Exception as e:
        print(f"An error occurred: {e}")
    except KeyboardInterrupt:
        print("  --control+c pressed, aborting generation--")

    #print()
        #reset context to the last input plus previous context here. (maybe put a limit on how far the context goes back? Counter of interations or tokens maybe)
    if not response:
        self.update_str("Sorry, unable to process that question. Could you please repeat or reword?")
        response = "No response"
    textContext += f"\n---\nUser: {textInput}\nAI Assistant: {response}\n"
    print("_______________________________________________________________")
    print(textContext)
    print("_______________________________________________________________")
    del generator


def main():
     text = input("enter: ")
     generation(text)

if __name__ == "__main__":
     main()
