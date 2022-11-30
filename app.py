import streamlit as st
import pandas as pd

st.header('Videogames sales dashboard')
st.markdown('Dataframe')

df = pd.read_csv('vgsales.csv')

df = df.drop(columns=['Rank'], axis=1)

st.dataframe(df)

st.text('Select the graphics you wanna see')

col1, col2, col3, col4 = st.columns(4)

with col1:
  global_sales = st.checkbox('Global Sales per Year', False)
  
with col2:
  platforms_sales = st.checkbox('Total Sales per Platform', False)
  
with col3:
  genre_sales = st.checkbox('Total Sales per Genre', False)
  
with col4:
  japan_sales = st.checkbox('Total 10 games sales in Japan', False)
  
if global_sales:
  global_sales_df = pd.DataFrame(df, columns=['Year', 'Global_Sales'])
  global_sales_df = global_sales_df.groupby(['Year']).sum()
  st.line_chart(global_sales_df)
  
if platforms_sales:
  platforms_sales = pd.DataFrame(df, columns=['Global_Sales', 'Platform'])
  platforms_sales = platforms_sales.groupby(['Platform']).sum()
  st.bar_chart(platforms_sales)
  
if genre_sales:
  genre_sales = pd.DataFrame(df, columns=['Global_Sales', 'Genre'])
  genre_sales = genre_sales.groupby(['Genre']).sum()
  st.bar_chart(genre_sales)
  
if japan_sales:
  japan_sales = pd.DataFrame(df, columns=['JP_Sales', 'Name'])
  japan_sales = japan_sales.groupby(['Name']).sum()
  ordered_japan_sales = japan_sales.sort_values(ascending=False, by='JP_Sales')
  top10_japan_sales = ordered_japan_sales.head(10)
  st.bar_chart(top10_japan_sales)
  