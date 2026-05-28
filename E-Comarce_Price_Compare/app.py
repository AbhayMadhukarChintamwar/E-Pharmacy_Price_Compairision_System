import serpapi 
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def Compare(med_name):
    params ={
    "engine": "google_shopping",
    "q": med_name,
    "api_key": "4f5438def2f6d1aa1bcdd256cc72f1ea2909323f4c8aa00999a350c9d7607bcf",
    'gl':'in'
    }
    search = serpapi.search(params)
    results =search.as_dict()
    shopping_results = results["shopping_results"]
    return shopping_results

c1,c2 = st.columns(2)
c1.image("App_Logo.png",width = 200)
c2.header('E-Pharmacy Price Comparison System')


# <-------------------------------------------------------------------------->
st.sidebar.title('Enter Name of Medicine:')

med_name = st.sidebar.text_input('Enter Name Here:')
number = st.sidebar.number_input(
    'Enter number of options here:',
    min_value=2,
    step=1
)

if med_name:
    if st.sidebar.button('Price Compare'):

        shopping_results = Compare(med_name)
        lowest_Price = float(
        shopping_results[0].get('price').replace('₹', '').replace(',', ''))
        lowest_Price_Index = 0
        print(lowest_Price , " ", lowest_Price_Index)

        for i in range(min(number, len(shopping_results))):
            current_Price = float(shopping_results[i].get('price').replace('₹', '').replace(',', ''))

            item = shopping_results[i]

            st.subheader(f"Option {i+1}")

            c1, c2 = st.columns([1, 2])

            # Product Image
            with c1:
                st.image(
                    shopping_results[i].get("thumbnail", ""),
                    width=150
                )

            # Product Details
            with c2:
                st.write("###", shopping_results[i].get("title", "No Title"))
                st.write("💰 Price:", shopping_results[i].get("price", "N/A"))
                st.write("🏪 Company:", shopping_results[i].get("source", "N/A"))
                st.write("⭐ Rating:", shopping_results[i].get("rating", "N/A"))
                st.write("📝 Reviews:", shopping_results[i].get("reviews", "N/A"))

                st.link_button(
                    "Buy Now",
                    shopping_results[i].get("product_link", "#")
                )

            st.divider()
            if(current_Price<lowest_Price):
             lowest_Price = float(shopping_results[i].get('price').replace('₹', '').replace(',', ''))
             lowest_Price_Index = i



# <---- This is Best option --->
        st.subheader(" Best Option")

        c1, c2 = st.columns([1, 2])

            # Product Image
        with c1:
                st.image(
                    shopping_results[lowest_Price_Index].get("thumbnail"," "),
                    width=150
                )

            # Product Details
        with c2:
                st.write("###", shopping_results[lowest_Price_Index].get("title", "No Title"))
                st.write("💰 Price:", shopping_results[lowest_Price_Index].get("price", "N/A"))
                st.write("🏪 Company:", shopping_results[lowest_Price_Index].get("source", "N/A"))
                st.write("⭐ Rating:", shopping_results[lowest_Price_Index].get("rating", "N/A"))
                st.write("📝 Reviews:", shopping_results[lowest_Price_Index].get("reviews", "N/A"))

                st.link_button(
                    "Buy Now",
                    shopping_results[i].get("product_link", "#")
                )

        st.divider()
    