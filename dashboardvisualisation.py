import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from wordcloud import WordCloud

# Mapping companies to their respective paths
company_paths = {
    'mining': [
        'AA', 'FCX', 'HL', 'NEM', 'SCCO'
    ],
    'oilandgas': [
        'COP', 'CVX', 'MPC', 'OXY', 'XOM'
    ],
    'utilities': [
        'D', 'DUK', 'ED', 'EXC', 'NEE'
    ]
}


# Function to load data
def load_data(category, company_name):
    # Incorporate the company name in the file name
    file_path = f'{company_name}_visualisation_preprocessed.csv'
    return pd.read_csv(file_path)

# Sidebar for category selection
category = st.selectbox('Select a Category', list(company_paths.keys()))

# Sidebar for company selection based on the category
selected_company = st.selectbox('Select a Company', company_paths[category])

# Load the data for the selected company
data = load_data(category, selected_company)

# Title of the dashboard
st.title(f'{selected_company} Dashboard')

# Bar Charts

# Commodity Distribution
st.subheader('Commodity Distribution')
commodity_counts = data['commodity'].value_counts()
fig = px.bar(commodity_counts, x=commodity_counts.index, y=commodity_counts.values, labels={'x':'Commodity', 'y':'Count'}, title='Commodity Distribution')
st.plotly_chart(fig)

# Ownership Distribution
st.subheader('Ownership Distribution')
ownership_counts = data['ownership'].value_counts()
fig = px.bar(ownership_counts, x=ownership_counts.index, y=ownership_counts.values, labels={'x':'Ownership', 'y':'Count'}, title='Ownership Distribution')
st.plotly_chart(fig)

# Countries Representation
st.subheader('Region Representation')
country_counts = data['Countries'].value_counts()
fig = px.bar(country_counts, x=country_counts.index, y=country_counts.values, labels={'x':'Region', 'y':'Number of Assets'}, title='Region Representation')
st.plotly_chart(fig)

# Pie Charts

# Commodity Share
st.subheader('Commodity Share')
fig = px.pie(commodity_counts, values=commodity_counts.values, names=commodity_counts.index, title='Commodity Share')
st.plotly_chart(fig)

# Ownership Share
st.subheader('Ownership Share')
fig = px.pie(ownership_counts, values=ownership_counts.values, names=ownership_counts.index, title='Ownership Share')
st.plotly_chart(fig)

# Histograms

# Asset Distribution by Country
st.subheader('Asset Distribution by Region')
fig = px.histogram(data, x='Countries', title='Asset Distribution by Region')
st.plotly_chart(fig)

# Remove square brackets and apostrophes from state names
def clean_state_names(state_name):
    return state_name.strip("[]'")

# USA States Asset Distribution
st.subheader('USA States Asset Distribution')
filtered_data_states = data.dropna(subset=['USA states'])
usa_states_counts = filtered_data_states['USA states'].str.split(',').explode().str.strip().apply(clean_state_names).value_counts()
fig = px.histogram(usa_states_counts, x=usa_states_counts.index, y=usa_states_counts.values, labels={'x': 'USA States', 'y': 'Count'}, title='USA States Asset Distribution')
st.plotly_chart(fig)

# Word Clouds

# Most Frequent Commodities
st.subheader('Most Frequent Commodities')
commodity_text = ' '.join(data['commodity'].dropna().unique())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(commodity_text)
fig, ax = plt.subplots()
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis('off')
st.pyplot(fig)

# Most Common Countries
st.subheader('Most Common Regions')
country_text = ' '.join(data['Countries'].dropna().unique())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(country_text)
fig, ax = plt.subplots()
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis('off')
st.pyplot(fig)

# Heatmaps

# Commodity vs. Countries
st.subheader('Commodity vs. Region Heatmap')
commodity_country_matrix = data.groupby(['Countries', 'commodity']).size().unstack(fill_value=0)
fig = px.imshow(commodity_country_matrix, labels=dict(x="Commodity", y="Region", color="Count"), title='Commodity vs. Region Heatmap')
st.plotly_chart(fig)

# Commodity vs. Ownership
st.subheader('Commodity vs. Ownership Heatmap')
commodity_ownership_matrix = data.groupby(['ownership', 'commodity']).size().unstack(fill_value=0)
fig = px.imshow(commodity_ownership_matrix, labels=dict(x="Commodity", y="Ownership", color="Count"), title='Commodity vs. Ownership Heatmap')
st.plotly_chart(fig)

# Stacked Bar Charts

# Commodities by Ownership
# Group data by ownership and commodity, then count the number of physical assets
grouped_data = data.groupby(['ownership', 'commodity']).size().reset_index(name='count')

st.subheader('Commodities by Ownership')
fig = px.bar(grouped_data, x='ownership', y='count', color='commodity', title='Commodities by Ownership', barmode='stack')
st.plotly_chart(fig)

# Assets by Country and Commodity
# Group data by country and commodity, then count the number of physical assets
grouped_data_country = data.groupby(['Countries', 'commodity']).size().reset_index(name='count')

# Plot the data
st.subheader('Commodities by Country')
fig = px.bar(grouped_data_country, x='Countries', y='count', color='commodity', title='Assets by Region and Commodity', barmode='stack')
st.plotly_chart(fig)


# Bubble Charts

# Ownership vs. Commodity vs. Countries
st.subheader('Ownership vs. Commodity vs. Countries Bubble Chart')
fig = px.scatter(data, x='Countries', y='commodity', color='ownership',
                 hover_name='physical asset', title='Ownership vs. Commodity vs. Countries')
st.plotly_chart(fig)

# Treemaps
data['Countries'].fillna('Unknown Country', inplace=True)
data['ownership'].fillna('Unknown Ownership', inplace=True)
data['physical asset'].fillna('Unknown Asset', inplace=True)

# Clean 'USA states' column
def clean_state_names(state_name):
    return state_name.strip("[]'")

# Asset Distribution by Country and Ownership
st.subheader('Asset Distribution by Country and Ownership Treemap')
fig = px.treemap(data, path=['Countries', 'ownership', 'physical asset'], title='Asset Distribution by Country and Ownership')
st.plotly_chart(fig)