# # Import necessary libraries
# import streamlit as st
# from openai import OpenAI

# # Function to get response from Llama-3.2-3B-Instruct-Turbo
# def get_llama_response(api_key, user_input):
#     # Set up the OpenAI client
#     client = OpenAI(
#         api_key=api_key,  # Replace with your actual API key
#         base_url="https://api.aimlapi.com",  # Replace with the correct base URL if needed
#     )

#     # Send a request to the Llama-3.2-3B-Instruct-Turbo model
#     response = client.chat.completions.create(
#         model="meta-llama/Llama-3.2-3B-Instruct-Turbo",  # Model name
#         messages=[
#             {
#                 "role": "system",
#                 "content": "You are an AI assistant who knows everything.",
#             },
#             {
#                 "role": "user",
#                 "content": user_input
#             },
#         ],
#     )

#     # Extract and return the response from the model
#     message = response.choices[0].message.content
#     return message

# # Streamlit app interface
# def main():
#     # Set the title of the app
#     st.title("Llama-3.2-3B Instruct Turbo Chat")
    
#     # Sidebar for API key input
#     st.sidebar.title("Settings")
#     api_key = st.sidebar.text_input("Enter your API Key:", type="password")

#     # Text area for user input
#     user_input = st.text_area("Ask the AI assistant a question:", value="Why is the sky blue?")
    
#     # Add some custom CSS to style the "Get Response" button
#     st.markdown(
#         """
#         <style>
#         div.stButton > button {
#             background-color: #4CAF50;
#             color: white;
#             padding: 10px 20px;
#             border: none;
#             border-radius: 4px;
#             cursor: pointer;
#             font-size: 16px;
#         }
#         div.stButton > button:hover {
#             background-color: #45a049;
#         }
#         </style>
#         """, unsafe_allow_html=True
#     )

#     # Button to submit the query
#     if st.button("Get Response"):
#         if api_key and user_input:
#             with st.spinner("Fetching response..."):
#                 # Get the response from the Llama model
#                 response = get_llama_response(api_key, user_input)
#                 st.success("Response received!")
#                 st.write(f"**Assistant:** {response}")
#         else:
#             st.error("Please provide both an API key and a question.")

# # Run the app
# if __name__ == "__main__":
#     main()





import os
import streamlit as st
from openai import OpenAI, OpenAIError

# Define API parameters
api_key = os.getenv("OPENAI_API_KEY", "8772096b1b3248128cf4072be826ee90")  
base_url = os.getenv("API_BASE_URL", "https://api.aimlapi.com")
model_name = os.getenv("MODEL_NAME", "meta-llama/Llama-3.2-3B-Instruct-Turbo")

client = OpenAI(api_key=api_key, base_url=base_url)

# Define the function to get project assignment
def get_project_assignment(project_description, expertise_list):
    try:
        user_input = f"The project is described as: '{project_description}'. The following people with different expertise are involved: {expertise_list}. Please intelligently assign tasks based on their expertise and guide them."
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {
                    "role": "system",
                    "content": "You are an AI assistant who assigns project tasks intelligently based on expertise.",
                },
                {
                    "role": "user",
                    "content": user_input,
                },
            ],
        )

        # Extract and return the assistant's response
        message = response.choices[0].message.content
        return f"Assistant: {message}"

    except OpenAIError as e:
        return f"API request failed: {str(e)}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Streamlit App
def main():
    st.title("WorkUp")

    # Input fields for the project description and expertise list
    project_description = st.text_area("Enter the project description:")
    expertise_list = st.text_area("Enter the people and their expertise involved:")

    # Button to trigger the task assignment
    if st.button("Assign Tasks"):
        if project_description and expertise_list:
            assignment_response = get_project_assignment(project_description, expertise_list)
            st.write(assignment_response)
        else:
            st.write("Please enter both the project description and expertise list.")

if __name__ == "__main__":
    main()



