
def save_prompt(prompt:str):
    with open('prompt.txt', 'w') as j:
        j.write(prompt)

def load_prompt(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        string_ = f.read()
        print("string_")
    return string_


from str_prompt import str_prompt

save_prompt(str_prompt)

Intial_prompt = load_prompt('Intial_prompt.txt')
save_prompt(Intial_prompt+'asdasdas sasads')
