import pandas as pd

import streamlit as st
import plotly.express as px

from sklearn.datasets import load_iris

# Define columns to plot
features = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']

#Get datas
@st.cache(allow_output_mutation=True) # @st.cache são para colocar dados na mémoria sem precisar buscar eles toda vez.
def load_data():
    data = load_iris()
    df = pd.DataFrame(data=data['data'], columns = data['feature_names'])
    df['target'] = data['target']

    return df

def plotly_hist(df, features_select):

    fig = px.histogram(df, x=features_select)
    return fig


# Create a sidebar
barra_lateral = st.sidebar.empty() # Instantiate a object sidebar
features_select = st.sidebar.selectbox("Select a feature:", features)# Create a select box to get a columns name

# Checkbox for capture boolean type if you want show the dataset
load_datas = st.sidebar.checkbox('Load Data')

### Central elements from page
# You need instantiate a st.empty() before for insert grafics in web app page.
grafico_histplot = st.empty()

# Header streamlit page
st.title('Stock Monitor')

st.header('Data from sklearn.load_iris')

st.subheader('Grafic and data visualization')

# Call function for load data
df = load_data()

# Here your configre presentation to web page stremlit
try:
    
    # plotly_chart you can configure your plotly plot and show in web page
    fig = plotly_hist(df, features_select)
    grafico_histplot = st.plotly_chart(fig)

    # If want to show dataset
    if load_datas:
        st.subheader('Dados')
        dados = st.dataframe(df.head())
        stock_select = st.sidebar.selectbox
except Exception as e:
    st.error(e)
