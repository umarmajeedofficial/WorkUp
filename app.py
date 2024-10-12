import os
import streamlit as st
from openai import OpenAI, OpenAIError

# Define API parameters
api_key ="8772096b1b3248128cf4072be826ee90"  # Ensure this is set in your environment
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
        return message

    except OpenAIError as e:
        return f"API request failed: {str(e)}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Streamlit App
def main():
    st.set_page_config(page_title="WorkUp - Project Task Assignment", layout="wide")
    st.title("WorkUp - Project Task Assignment")

    # Sidebar for team configuration
    st.sidebar.header("Team Configuration")
    num_team_members = st.sidebar.number_input(
        "Number of Team Members",
        min_value=1,
        max_value=20,
        step=1,
        value=2,
        help="Select the number of team members."
    )

    # Dynamically generate input fields for each team member
    team_members = []
    for i in range(1, num_team_members + 1):
        st.sidebar.subheader(f"Member {i}")
        name = st.sidebar.text_input(f"Name of Member {i}", key=f"name_{i}")
        expertise = st.sidebar.text_area(f"Expertise of Member {i}", key=f"expertise_{i}", height=100)
        if name and expertise:
            team_members.append({"name": name.strip(), "expertise": expertise.strip()})

    st.sidebar.markdown("---")
    st.sidebar.info("Please enter all team members' names and their areas of expertise.")

    # Main area for project description
    st.header("Project Description")
    project_description = st.text_area("Enter the project description:", height=200)

    # Button to trigger the task assignment
    if st.button("Assign Tasks"):
        # Validate inputs
        missing_info = []
        if not project_description.strip():
            missing_info.append("Project description")
        if len(team_members) != num_team_members:
            missing_info.append("All team members' names and expertise")

        if missing_info:
            st.error(f"Please provide the following missing information: {', '.join(missing_info)}.")
        else:
            with st.spinner("Assigning tasks..."):
                assignment_response = get_project_assignment(project_description, team_members)
                st.success("Tasks Assigned Successfully!")
                st.subheader("Task Assignments")

                # Display the assignments
                st.write(assignment_response)

                # Optional: Format the assignments nicely
                # Assuming the response is in a structured format, like JSON
                # You can parse and display it accordingly
                # For now, we'll display it as plain text

if __name__ == "__main__":
    main()
