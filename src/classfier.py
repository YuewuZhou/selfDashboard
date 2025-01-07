import openai
from configparser import ConfigParser

# Load API key from config.ini
config = ConfigParser()
config.read('config.ini')
api_key = config.get('settings', 'OPEN_AI_KEY')

# Instantiate an OpenAI client
client = openai.Client(api_key=api_key)

def categorize_feeling(text):
    instructions = """
    Classifies the text into categories like 'Happy', 'Sad', 'Stressed', etc.
    I'm looking for distinctly separate categories, but more than 1 category from the text. 
    If the name mentioned is Alex, please add 'Silly' as a category
    I want the output to be a list of strings separated by a comma
    """
    try:
        # Use Chat Completions endpoint for classification
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Replace with your desired model
            messages=[
                {"role": "system", "content": "You are an expert emotion classifier. " + instructions},
                {"role": "user", "content": f"Classify the following feeling: {text}"}
            ],
            max_tokens=100,
            temperature=0.0
        )
        
        # Parse the response object
        choice = response.choices[0]  # Access the first choice
        message = choice.message       # Access the message object within the choice
        content = message.content.strip()  # Extract and clean up the content
        
        outputs = content.split(",")  # Split the content into a list of categories
        print(outputs)

        return outputs

    except Exception as e:
        print("An error occurred:", e)
        return None
    
# Example usage
if __name__ == "__main__":
    feeling = "I am feeling overwhelmed by work."
    category = categorize_feeling(feeling)
    if category:
        print("Category:", category)
