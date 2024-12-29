from groq import Groq
import os
from dotenv import load_dotenv



'''Since the task specified, that the set of transformations was "very restricted", the thought process here was to use simple prompt engineering technique.
Basically, converting the python file with transformations to string and providing it as a prompt to an LLM.
If the case was different, and the set of transformations was larger, this part of the task would include the RAG implementation, so the prompt in that case gets only top K most-relevant functions.
The whole file was provided, so the LLM can have a bigger context of what each function does, and to provide the right answer. Also, the column names are provided, to prevent the mistake of model not guessing the name right.'''
def llm(query, functions, categories):
    load_dotenv()
    API_KEY = os.getenv("GROQ_KEY")


    
    llm = Groq(
        api_key=API_KEY,
    )
    response = llm.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": query,
            },
            {
                "role": "system",
                "content": " You are supposed based on query, to return python code that executes the given transformation on a pandas DataFrame. You must use only the found in the that were provided, and respond only with code, no other sentences! DataFrame is already provided as df. Keep in mind that every function must be imported from transforms.py! This is the content of transforms.py, with functions you can use:" + functions+ "Plesae pay attention to what these functions do. It is very important to only use the functions from transforms.py and to only perform those and nothing else, so no prints or similar. Please import every function that exists in transforms.py. These are the columns that exist in DataFrame:" + categories + "They are case sensitive. The name of the output variable should be output",
            }
        ],
        model="llama3-70b-8192",
    )
    return response.choices[0].message.content