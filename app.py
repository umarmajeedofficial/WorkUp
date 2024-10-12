# Import necessary libraries
import streamlit as st
from openai import OpenAI

# Function to get response from Llama-3.2-3B-Instruct-Turbo
def get_llama_response(api_key, user_input):
    # Set up the OpenAI client
    client = OpenAI(
        api_key=api_key,  # Replace with your actual API key
        base_url="https://api.aimlapi.com",  # Replace with the correct base URL if needed
    )

    # Send a request to the Llama-3.2-3B-Instruct-Turbo model
    response = client.chat.completions.create(
        model="meta-llama/Llama-3.2-3B-Instruct-Turbo",  # Model name
        messages=[
            {
                "role": "system",
                "content": "You are an AI assistant who knows everything.",
            },
            {
                "role": "user",
                "content": user_input
            },
        ],
    )

    # Extract and return the response from the model
    message = response.choices[0].message.content
    return message

# Streamlit app interface
def main():
    # Set the title of the app
    st.title("Llama-3.2-3B Instruct Turbo Chat")
    
    # Sidebar for API key input
    st.sidebar.title("Settings")
    api_key = st.sidebar.text_input("Enter your API Key:", type="password")

    # Text area for user input
    user_input = st.text_area("Ask the AI assistant a question:", value="Why is the sky blue?")
    
    # Add some custom CSS to style the "Get Response" button
    st.markdown(
        """
        <style>
        div.stButton > button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        div.stButton > button:hover {
            background-color: #45a049;
        }
        </style>
        """, unsafe_allow_html=True
    )

    # Button to submit the query
    if st.button("Get Response"):
        if api_key and user_input:
            with st.spinner("Fetching response..."):
                # Get the response from the Llama model
                response = get_llama_response(api_key, user_input)
                st.success("Response received!")
                st.write(f"**Assistant:** {response}")
        else:
            st.error("Please provide both an API key and a question.")

# Run the app
if __name__ == "__main__":
    main()
