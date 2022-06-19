import streamlit
streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('omega 3 & blueberry oatmeal')
streamlit.text('Kale, spinach  & Rocket smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my+fruit_list.set-index('fruit')


# let's put a pick list here so they can pick the fruit they want to include
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
                     
#display the table on the page
streamlit.dataframe(my_fruit_list)
