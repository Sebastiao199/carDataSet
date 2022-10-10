import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

#st.title('Hello Wilders, welcome to my application! This is a application about cars!')

df_cars = pd.read_csv("https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv")
#st.write(df_cars)

st.write("Based on this graphics we can sum up that the Mpg have been increasing on Usa, Europe and Japan across the years. \
        By viewing the three regions we can easily see that Usa has a more consistent growth across the years and the other \
        two regions have some up and downs. We can also clearly say that Europe was the region with the most MPG on the last \
        year we have the data (1983). Below you will be able to see four different types of graphics so you can visualize \
        the data and the results in different ways.")

options = st.selectbox('Choose region:', df_cars['continent'].unique())
fig, axes = plt.subplots(figsize=(12,8))
sns.boxplot(data=df_cars[df_cars['continent']==options], x="year", y="mpg", color='blue').set(title='The Boxplot of the Mpg across the years on different continents.')
st.pyplot(fig)

fig2, axes2 = plt.subplots(figsize=(12,8))
sns.barplot(data=df_cars[df_cars['continent']==options], x="year", y="mpg", color='blue', ci=None).set(title='The Barplot of the Mpg across the years on different continents.')
st.pyplot(fig2)

fig3, axes3 = plt.subplots(figsize=(12,8))
sns.regplot(data=df_cars[df_cars['continent']==options], x="year", y="mpg", color='blue', ci=None).set(title='The Regplot of the Mpg across the years on different continents.')
st.pyplot(fig3)

fig4, axes4 = plt.subplots(figsize=(12,8))
sns.histplot(data=df_cars[df_cars['continent']==options], x="year", y="mpg", color='blue').set(title='The Histplot of the Mpg across the years on different continents.')
st.pyplot(fig4)




#continent = ('US.', 'Europe.', 'Japan.')
#dropdown = st.multiselect('Pick your continent: ', continent)




