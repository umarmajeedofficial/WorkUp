
import os
from openai import OpenAI, OpenAIError

# Define API parameters
api_key = "8772096b1b3248128cf4072be826ee90"  
base_url = "https://api.aimlapi.com"
model_name = "meta-llama/Llama-3.2-3B-Instruct-Turbo"

client = OpenAI(api_key=api_key, base_url=base_url)

# Function to get project assignment
def get_project_assignment(project_description, team_members):
    try:
        # Construct expertise list
        expertise_list = "\n".join([f"{member['name']}: {member['expertise']}" for member in team_members])
        
        user_input = (
            f"The project is described as: '{project_description}'.\n"
            f"The following team members with different expertise are involved:\n{expertise_list}.\n"
            "Please intelligently assign tasks based on their expertise and guide them."
        )
        
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {
                    "role": "system",
                    "content": "You are an AI assistant who assigns project tasks intelligently based on expertise and project details.",
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
