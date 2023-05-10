import streamlit as st
import pandas as pd

# Define a class to represent a state
class State:
    def __init__(self, name, state_code,status):
        self.name = name
        self.state_code = state_code
        self.status = status

# Define a list to store the states
states = [
    State("Andhra Pradesh", "AP",'Active'),
    State("Karnataka", "KN","Inactive"),
    State("Tamilnadu", "TN","Inactive"),
    State("Telangana", "TG","Inactive"),
]
# Page for listing all states
def list_states():
    st.header("List of States")
    if not states:
        st.write("No states available.")
    else:
        state_data = {
            "State Name": [state.name for state in states],
            "Code": [state.state_code for state in states],
            "Status": [state.status for state in states],
            "Edit": ['<a href="state://edit/{}">edit</a>'.format(state.name) for state in states],
            "Delete": ['<a href="state://delete/{}">delete</a>'.format(state.name) for state in states]
        }
        df = pd.DataFrame(state_data)
        st.write(df.to_html(escape=False), unsafe_allow_html=True)

# Page for adding a state
def add_state():
    st.header("Add a State")
    name = st.text_input("State Name")
    state_code = st.text_input("State Code")
    status = st.radio("Status",('Active', 'Inactive'))

    if st.button("Add"):
        if name and state_code and status:
            states.append(State(name, state_code,status))
            st.success("State added successfully.")
        else:
            st.error("Please enter both state name and code.")

# Page for editing a state
def edit_state():
    st.header("Edit a State")
    if not states:
        st.write("No states available.")
    else:
        state_names = [state.name for state in states]
        selected_state = st.selectbox("Select a state", state_names)
        new_state = st.text_input("New name for State")
        state_code = st.text_input("New State Code")
        status = st.radio("Status",('Active', 'Inactive'))
        if st.button("Edit"):
            for state in states:
                if state.name == selected_state:
                    state.state_code = state_code
                    st.success("State edited successfully.")
                    break

# Page for deleting a state
def delete_state():
    st.header("Delete a State")
    if not states:
        st.write("No states available.")
    else:
        state_names = [state.name for state in states]
        selected_state = st.selectbox("Select a state", state_names)
        if st.button("Delete"):
            for state in states:
                if state.name == selected_state:
                    states.remove(state)
                    st.success("State deleted successfully.")
                    break

# Main application
def main():
    st.title("States")
    
    # Create select box in the sidebar
    st.sidebar.title("Navigation")
    pages = {
        "List States": list_states,
        "Add State": add_state,
        "Edit State": edit_state,
        "Delete State": delete_state
    }
    page = st.sidebar.selectbox("Go to", tuple(pages.keys()), index=0)
    pages[page]()

if __name__ == "__main__":
    main()
