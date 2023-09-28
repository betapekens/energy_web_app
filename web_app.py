import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



plt.style.use('dark_background')
# Title
st.title("Indicative price creator")

# Sliders for variables
st.subheader("Rapina brick")
rapina = st.slider("", min_value=0, max_value=20, value=10)
st.subheader("brick daily modulation")
brick = st.slider("", min_value=0, max_value=20, value=7)

# Brick total
tot_brick = rapina + brick
st.write(f"Brick totale: {tot_brick}")

# Gas Price
st.subheader("Latest gas price per maturity")
input = eval(st.text_input("Input future month prices", "[43, 41, 42, 40, 35, 33, 32, 31, 30, 32, 34, 34]"))

if input != "":
    prices  = input
else:
    prices = [43, 41, 42, 40, 35, 33, 32, 31, 30, 32, 34, 34]

gas_price = pd.DataFrame({"Price":prices,
                                   "Month":["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]})
fig, ax = plt.subplots()
ax.plot(gas_price["Month"], gas_price["Price"], color = "#048494")
ax.legend("Price")
st.pyplot(fig)



st.title("")
st.title("")
show_subheader = False

modulation_values = [6, 12, 23, 15, 5, 6, 8, 7, 6, 4, 5, 4]
# Create a button to toggle the subheader
st.subheader("Gas Modulation over month")
if st.checkbox("Gas Modulation"):
    modulation = eval(st.text_input("Input your own modulation if you want to change it",
                                 "[6, 12, 23, 15, 5, 6, 8, 7, 6, 4, 5, 4]"))
    if input != "":
        modulation_values  = modulation
    else :
        modulation_values = [6, 12, 23, 15, 5, 6, 8, 7, 6, 4, 5, 4]
    monthly_modulation = pd.DataFrame({"Price":modulation_values,
                                   "Month":["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]})
    fig, ax = plt.subplots()
    ax.plot(monthly_modulation["Month"], monthly_modulation["Price"], color = "r", alpha=0.7)
    ax.spines['top'].set_visible(False)    
    ax.spines['right'].set_visible(False)  
    ax.spines['bottom'].set_visible(False) 
    ax.spines['left'].set_visible(False)   
    st.pyplot(fig)



st.title("")
st.title("")
# Calculate transfer price
st.subheader ("Transfer Price Calculation")

sum_of_perc = sum(modulation_values)
modulation_perc = [n/sum_of_perc for n in modulation_values]
weighted_price = [modulation_perc[n]*prices[n] for n in range(len(modulation_perc))]
print(modulation_perc)
print(prices)
print(weighted_price)

weighted_dataframe = pd.DataFrame({"Price":weighted_price,
                                   "Month":["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]})

st.text("Weighted price per month")
fig, ax = plt.subplots()
ax.plot(weighted_dataframe["Month"], weighted_dataframe["Price"], color = "r", alpha=0.7)
st.pyplot(fig)


transfer_price = round(sum(weighted_price), 2)
with st.sidebar:
    st.title(f"The transfer price will be {transfer_price + tot_brick}")