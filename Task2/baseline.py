import openai
import os
from pyswip import Prolog

# API Key: made in an environment variable -- safer
openai.api_key = os.getenv("OPENAI_API_KEY")

def fetch_prolog_code(prompt):
    """
    Uses OpenAI API to generate Prolog code based on the given prompt.
    """
    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You're a Prolog expert. Provide only valid Prolog code, no extra explanations."},
                {"role": "user", "content": prompt},
            ],
        )

        # Extract the response and clean unnecessary formatting
        response_dict = response.model_dump()    # <--- convert to dictionary
        code = response_dict['choices'][0]['message']['content'].strip()
        return code.replace("```prolog", "").replace("```", "").strip()

    except Exception as e:
        print(f"Error fetching Prolog code from OpenAI: {e}")
        return None

def format_statements(prolog_code):
    """
    Reformat Prolog code to ensure statements are properly grouped and complete.
    """
    statements, temp = [], []
   
    for line in prolog_code.splitlines(): # split by new line
        line = line.strip()
        if line and not line.startswith("%"): # ignore comments and empty lines
            temp.append(line)
            if line.endswith('.'):
                statements.append(" ".join(temp))
                temp.clear()
    
    return statements

def execute_code(prolog_code, query):
    """
    Load and execute Prolog code to run a query against it.
    """
    prolog = Prolog()
    statements = format_statements(prolog_code)
    
    try:
        for smt in statements:
            prolog.assertz(smt.rstrip('.'))  # Add fact or rule to knowledge base
        
        return list(prolog.query(query))  # Execute the query
    except Exception as error:
        raise Exception(f"Prolog execution failed: {error}")

def run_baseline_test():
    prompt = "Define parent-child relationships for mary and others and a rule for grandparent in Prolog."
    prolog_code = fetch_prolog_code(prompt)
    
    if prolog_code:
        print("Prolog Code:\n", prolog_code)
    
        test_query = "grandparent(mary, X)."  # defining the query to run
        
        try:
            results = execute_code(prolog_code, test_query)
            print("Query Results:", results)
        except Exception as error:
            print(f"Error during Prolog execution: {error}")
    else:
        print("Failed to fetch Prolog code.")

if __name__ == "__main__":
    run_baseline_test()
