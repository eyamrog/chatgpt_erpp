# Defining a function to query ChatGPT
import openai
from IPython.display import clear_output

def get_completion(prompt, model = 'gpt-3.5-turbo'):
    client = openai.OpenAI()
    messages = [{'role': 'user', 'content': prompt}]
    response = client.chat.completions.create(
        model = model,
        messages = messages,
        temperature = 0
    )
    return response.choices[0].message.content

# Collecting input
end = False
openai.api_key = ''
while end == False:
    openai.api_key = str(input('Enter your OpenAI API key: '))
    if openai.api_key != '':
        end = True
end = False
filename = ''
file = 'dummy.txt'
while end == False:
    filename = str(input('Enter the output filename without extension: '))
    if filename != '':
        file = filename + '.txt'
        end = True
        clear_output()

# Prompting ChatGPT
with open(file, 'a') as responses:
    responses.write('ChatGPT revision of writing in ERPP' + '\n\n')
    prompt = 'Dear ChatGPT, would it be possible for you to improve the writing of certain passages of a research article considering the generally accepted standards of English for Academic Purposes? I am going to provide you with a passage at a time. OK?'
    responses.write(prompt + '\n\n')
    query = get_completion(prompt)
    responses.write(query + '\n\n')
with open(file, 'r') as responses:
    print(responses.read())

# Getting improved passages from ChatGPT
sequence = 1
end = False
passage = ''
while end == False:
    passage = str(input('Enter passage ' + str(sequence) + ': '))
    if passage != '':
        with open(file, 'a') as responses:
            responses.write('Passage ' + str(sequence) + ':\n' + passage + '\n\n')
            query = get_completion(passage)
            responses.write('Improved passage ' + str(sequence) + ':\n' + query + '\n\n')
            print('\nImproved passage ' + str(sequence) + ':\n' + query)
            clear_output(wait = True)
        sequence += 1
    else:
        end = True
        clear_output()