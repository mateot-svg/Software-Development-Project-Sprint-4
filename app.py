import streamlit as st
import pandas as pd
import plotly.express as px

# Load data 
df = pd.read_csv('data/vehicles_us.csv')
df['manufacturer'] = df['model'].apply(lambda x: x.split()[0])


# Title for the entire app
st.title('Vehicle Data Analysis Dashboard')

# Create a text header above the data frame
st.header('Data viewer')
# Display the dataframe with streamlit
st.dataframe(df)

# Select a visualization type
viz_type = st.radio("Choose a visualization type:", ['Histogram of Vehicle Prices', 'Scatter Plot of Price vs Odometer', 'Custom Histogram'])

# Based on the choice, render appropriate interactive elements and visualizations
if viz_type == 'Histogram of Vehicle Prices':
    # Checkbox for showing the histogram of vehicle prices
    if st.checkbox('Show Histogram', value=True):
        fig_price = px.histogram(df, x='price', title='Histogram of Vehicle Prices', color='manufacturer', nbins=50)
        st.plotly_chart(fig_price, use_container_width=True)

elif viz_type == 'Scatter Plot of Price vs Odometer':
    # Checkbox for showing the scatter plot
    if st.checkbox('Show Scatter Plot', value=True):
        fig_scatter = px.scatter(df, x='odometer', y='price', color='condition', title='Price vs. Odometer by Condition', hover_data=['model'])
        st.plotly_chart(fig_scatter, use_container_width=True)

elif viz_type == 'Custom Histogram':
    # Dropdown to select the feature for a custom histogram
    selected_column = st.selectbox('Select a feature to display histogram:', 
                                   options=df.select_dtypes(include=['int64', 'float64', 'boolean']).columns.tolist())
    # Generate and display the histogram based on the selected feature
    if selected_column:
        fig = px.histogram(df, x=selected_column, title=f'Histogram of {selected_column}', 
                           color_discrete_sequence=px.colors.qualitative.T10)
        st.plotly_chart(fig)
