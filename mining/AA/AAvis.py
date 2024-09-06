import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from wordcloud import WordCloud
import networkx as nx

# Load the data
file_path = r'C:\Users\avani\Desktop\Thesis\mining\AA\visualisation_preprocessed.csv'  # Updated file path
data = pd.read_csv(file_path)



# Clean 'USA states' column
def clean_state_names(state_name):
    return state_name.strip("[]'")

# Title of the dashboard
st.title('Alcoa Corporation Dashboard')



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

### In-Depth Analysis Visualizations



# Stacked Bar Charts

# Commodities by Ownership
st.subheader('Commodities by Ownership')
fig = px.bar(data, x='ownership', y='physical asset', color='commodity', title='Commodities by Ownership', barmode='stack')
st.plotly_chart(fig)

# Assets by Country and Commodity
st.subheader('Assets by Region and Commodity')
fig = px.bar(data, x='Countries', y='physical asset', color='commodity', title='Assets by Region and Commodity', barmode='stack')
st.plotly_chart(fig)

# Sankey Diagrams

# Ownership to Commodity Flow
st.subheader('Ownership to Commodity Flow Sankey Diagram')
fig = px.parallel_categories(data, dimensions=['ownership', 'commodity'], title='Ownership to Commodity Flow')
st.plotly_chart(fig)

# Country to Commodity Flow
st.subheader('Country to Commodity Flow Sankey Diagram')
fig = px.parallel_categories(data, dimensions=['Countries', 'commodity'], title='Country to Commodity Flow')
st.plotly_chart(fig)

# Treemaps
# Replace NaN values in the relevant columns
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

# Bubble Charts

# Ownership vs. Commodity vs. Countries
st.subheader('Ownership vs. Commodity vs. Countries Bubble Chart')
fig = px.scatter(data, x='Countries', y='commodity', color='ownership',
                 hover_name='physical asset', title='Ownership vs. Commodity vs. Countries')
st.plotly_chart(fig)

'''
import streamlit as st
import pandas as pd
import plotly.express as px

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

base_paths = {
    'mining': 'C:/Users/avani/Desktop/Thesis/mining',
    'oilandgas': 'C:/Users/avani/Desktop/Thesis/oilandgas',
    'utilities': 'C:/Users/avani/Desktop/Thesis/utilities'
}

# Function to load data
def load_data(category, company_name):
    file_path = f'{base_paths[category]}/{company_name}/visualisation_preprocessed.csv'
    return pd.read_csv(file_path)

# Sidebar for category selection
category = st.selectbox('Select a Category', list(company_paths.keys()), key='category_selectbox')

# Load data for all companies in the selected category
all_data = []
for company in company_paths[category]:
    all_data.append(load_data(category, company))
data = pd.concat(all_data)

# Identify assets with multiple ownerships
asset_ownership_counts = data.groupby('physical asset')['ownership'].nunique()
multiple_ownership_assets = asset_ownership_counts[asset_ownership_counts > 1].index

# Filter data to include only these assets
multiple_ownership_data = data[data['physical asset'].isin(multiple_ownership_assets)]

# Display the table of assets and their ownerships
st.subheader('Assets with Multiple Ownerships')
st.write(multiple_ownership_data[['physical asset', 'ownership']].drop_duplicates().sort_values(by='physical asset'))

# Plot the number of assets with multiple ownerships
multiple_ownership_summary = multiple_ownership_data.groupby('physical asset')['ownership'].nunique().reset_index()
multiple_ownership_summary = multiple_ownership_summary['ownership'].value_counts().reset_index()
multiple_ownership_summary.columns = ['Number of Owners', 'Number of Assets']

fig = px.bar(multiple_ownership_summary, x='Number of Owners', y='Number of Assets', title='Assets with Multiple Ownerships')
st.plotly_chart(fig)
'''