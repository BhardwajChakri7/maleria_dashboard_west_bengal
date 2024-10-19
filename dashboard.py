import streamlit as st
import pandas as pd

# Set page title
st.title('Malaria Cases Dashboard by State')

# Load data
csv_file_path = 'malaria_cases.csv'
df = pd.read_csv(csv_file_path)

# Display raw data
st.subheader('Raw Data')
st.write(df)

# Aggregate data by state
state_summary = df.groupby('State').agg(
    Total_Users=pd.NamedAgg(column='State', aggfunc='count'),
    Positive_Cases=pd.NamedAgg(column='Malaria_diagnosis', aggfunc=lambda x: (x == 'The person is affected with Malaria 😷').sum()),
    Negative_Cases=pd.NamedAgg(column='Malaria_diagnosis', aggfunc=lambda x: (x == 'The person is not affected with Malaria 😊').sum())
).reset_index()

# Function to display data for each state
def display_state_data(state, total_users, positive_cases, negative_cases):
    st.subheader(f'{state}')
    st.write(f'Total Users Registered: {total_users}')
    st.write(f'Positive Cases: {positive_cases}')
    st.write(f'Negative Cases: {negative_cases}')
    st.write('---')

# List of states and union territories
state = "Andhra Pradesh"

# Loop through each state and display its data if present in the summary

state_data = state_summary[state_summary['State'] == "Andhra Pradesh"]
if not state_data.empty:
    display_state_data(
        state,
        state_data['Total_Users'].values[0],
        state_data['Positive_Cases'].values[0],
        state_data['Negative_Cases'].values[0]
    )
