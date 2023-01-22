import cohere 
from cohere.classify import Example 


co = cohere.Client('722SXCwoVzqyYpxbTYyW14y271kdWSBwjgHdWxOf') 

def convo_2(input_):
    response = co.classify( 
        model='large', 
        inputs=input_, 
        examples=[Example("I want to kill myself", "emergency"), 
        Example("i am not feeling very well", "not emergency"), 
        Example("I want to end my life", "emergency"), 
        Example("i am disappointed today", "not emergency"), 
        Example("I do not want to talk and i want to stay in my room forever", "emergency"), 
        Example("I got bullied and my mental health is really bad", "emergency"), 
        Example("I am feeling a little sad", "not emergency"), 
        Example("i am so scared, i dont know what to do", "emergency"), 
        Example("I can\'t stop worrying about this.", "not emergency"), 
        Example("I can\'t do this, it\'s too hard.", "not emergency"), 
        Example("What if something goes wrong?", "not emergency"), 
        Example("I feel like I\'m going to have a panic attack.", "emergency"), 
        Example("I don\'t think I can handle this situation.", "emergency"), 
        Example("I\'m not sure if I can trust anyone.", "not emergency"), 
        Example("I don\'t want to disappoint anyone.", "not emergency"), 
        Example("I feel like I\'m losing control.", "emergency"), 
        Example("I\'m just so stressed all the time.", "not emergency"), 
        Example("I keep having panic attacks.", "emergency"), 
        Example("I\'m so worried about the future.", "not emergency"), 
        Example("I\'m so worried about my health.", "emergency"), 
        Example("I feel like I\'m stuck in this cycle of anxiety.", "emergency")],
        truncate = "start")
    res ='The confidence levels of the labels are: {}'.format(response.classifications)
    return response.classifications[0].prediction


#print(response.classifications[0].prediction)
