import serpapi 
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image



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


# Page Config
st.set_page_config(
    page_title="E-Pharmacy Price Comparison System",
    page_icon="➕",
    layout="wide"
)

# Load thumbnail/logo image

# Header
st.markdown("""
<style>
.stApp {
    background-color: #000000;
    color:#0F766E;
}
</style>
""", unsafe_allow_html=True)

st.title("🏥 E-Pharmacy Price Comparison System")
st.write("Compare medicine prices from different platforms")
st.divider()

c1,c2 = st.columns(2)
with c1:
   
    c1.image("App_Logo.png",width = 200)
   
    
with c2:
        c2.header('E-Pharmacy Price Comparison System')


# <-------------------------------------------------------------------------->
st.sidebar.markdown(
    """
    <style>
    section[data-testid="stSidebar"] {
         background-color: #0F766E;

    }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.header("🏥 E-Pharmacy Price Comparison System")

st.sidebar.title('Enter Name of Medicine:')

med_name = st.sidebar.text_input('Enter Name Here:')
number = st.sidebar.number_input('Enter number of options here:',min_value=1,step=1)
medicine_comp = []
med_price =[]

if med_name:
    if st.sidebar.button('Price Compare'):

        shopping_results = Compare(med_name)
        lowest_Price = float(
        shopping_results[0].get('price').replace('₹', '').replace(',', ''))
        lowest_Price_Index = 0


        for i in range(min(number, len(shopping_results))):
            current_Price = float(shopping_results[i].get('price').replace('₹', '').replace(',', ''))
            medicine_comp.append(shopping_results[i].get("source", "N/A"))
            med_price.append(float(shopping_results[i].get('price').replace('₹', '').replace(',', '')))


 # <---------------------------------------------------------------------->

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

# <----------------------------------------------------------------->
        st.sidebar.subheader(" Best Option")


            # Product Image
        st.sidebar.image(
                    shopping_results[lowest_Price_Index].get("thumbnail"," "),
                    width=150
                )

            # Product Details
        st.sidebar.write("###", shopping_results[lowest_Price_Index].get("title", "No Title"))
        st.sidebar.write("💰 Price:", shopping_results[lowest_Price_Index].get("price", "N/A"))
        st.sidebar.write("🏪 Company:", shopping_results[lowest_Price_Index].get("source", "N/A"))
        st.sidebar.write("⭐ Rating:", shopping_results[lowest_Price_Index].get("rating", "N/A"))
        st.sidebar.write("📝 Reviews:", shopping_results[lowest_Price_Index].get("reviews", "N/A"))

        st.sidebar.link_button(
                    "Buy Now",
                    shopping_results[i].get("product_link", "#")
                )

        st.divider()


# <----------------------------------------------->
        # Graphs Compare 
        df = pd.DataFrame(med_price,medicine_comp)
        st.title('Chart Comparison :')
        st.bar_chart(df)

        fig,ax=plt.subplots(figsize=(12,5))
        ax.pie(med_price, labels = medicine_comp, shadow = True)
        ax.axis('equal')
        st.pyplot(fig)

st.markdown("---")
st.markdown(
    "<h5 style='text-align:center;'>Made with ❤️ by Abhay</h5>",
    unsafe_allow_html=True
)
    