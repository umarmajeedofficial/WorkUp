
import os
from openai import OpenAI, OpenAIError

# Define API parameters
api_key = "8772096b1b3248128cf4072be826ee90" # Set in your environment
base_url = "https://api.aimlapi.com"
model_name = "meta-llama/Llama-3.2-3B-Instruct-Turbo"

client = OpenAI(api_key=api_key, base_url=base_url)

# Function to create flowchart from project documentation
def create_flowchart(project_documentation):
    try:
        user_input = (
            f"Based on the following project documentation:\n{project_documentation}\n"
            "Please provide a flowchart describing the inputs, outputs, and processes involved."
        )
        
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {
                    "role": "system",
                    "content": "You are an AI assistant who creates flowcharts based on project documentation.",
                },
                {
                    "role": "user",
                    "content": user_input,
                },
            ],
        )

        # Extract and return the assistant's response
        message = response.choices[0].message.content
        return message

    except OpenAIError as e:
        return f"API request failed: {str(e)}"
    except Exception as e:
        return f"An error occurred: {str(e)}"
