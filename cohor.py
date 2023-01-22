import cohere

co = cohere.Client('051jhJXOSphrR0cDrjp9jPlcaYsxendqBaa7acq3')


def convo(req):
    prompt = req

    response = co.generate(  
        model='command-xlarge-nightly',  
        prompt = prompt,  
        max_tokens=100,  
        temperature=0.6,  
        stop_sequences=["--","?","."],
        truncate = "start")
    res = response.generations[0].text

    return res
