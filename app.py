import os
import streamlit as st
from llama_project_tasks import get_project_assignment
from llama_code_generation import generate_code
from llama_flowchart import create_flowchart

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

                # Generate code for the assigned tasks
                code_response = generate_code(assignment_response)
                st.subheader("Generated Blueprint Code")
                st.code(code_response)

                # Create and display flowchart
                flowchart_response = create_flowchart(assignment_response)
                st.subheader("Project Flowchart")
                st.write(flowchart_response)

if __name__ == "__main__":
    main()
