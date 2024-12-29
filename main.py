from llm import llm 
import os
import transforms
import inspect
import pandas as pd
import numpy as np
from transforms import *
'''Here is everything put together. First the python file is converted to a string, so it can be provided to llm as prompt.  Data Frame and categories are prepared'''
def get_imported_module_as_string(module):
    try:
        # Dohvati putanju modula
        module_path = inspect.getfile(module)
        # Pročitaj sadržaj modula
        with open(module_path, 'r', encoding="utf-8") as py_file:
            content = py_file.read()
        return content
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Primer korišćenja
trans = get_imported_module_as_string(transforms)
query = input() #For example: "I need employee ids for every person older than 33, with salary lower than 95000."

data = {
    "EmployeeID": range(1, 11),
    "Department": ["HR", "IT", "Sales", "IT", "HR", "Sales", "IT", "HR", "Sales", "IT"],
    "Age": np.random.randint(25, 60, size=10),
    "YearsExperience": np.random.randint(1, 35, size=10),
    "Salary": np.random.randint(30000, 120000, size=10),
    "Bonus": np.random.uniform(1000, 5000, size=10).round(2),
    "PerformanceScore": np.random.uniform(1.0, 5.0, size=10).round(2),
    "LeavesTaken": np.random.randint(0, 20, size=10),
    "WorkHoursPerWeek": np.random.randint(30, 50, size=10),
    "SatisfactionLevel": np.random.uniform(0.1, 1.0, size=10).round(2)
}
def get_column_names_as_string(df):
    return ",".join(df.columns)
df = pd.DataFrame(data)

cats = get_column_names_as_string(df) #Categories prepared for LLM
 
#print(df)
out = llm(query, trans,cats)
#print(out)
#print(exec(out))
exec(out)
print(output)

