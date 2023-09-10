import streamlit as st
import joblib
import pandas as pd
model_path=r'C:\Users\PC\Untitled Folder 2\model2.pkl'
model3 = joblib.load(model_path)
category_mapping = {
    'bed_bath_table': 0,
    'computers_accessories': 1,
    'consoles_games': 2,
    'cool_stuff': 3,
    'furniture_decor': 4,
    'garden_tools': 5,
     'health_beauty': 6,
    'perfumery': 7,
     'watches_gifts': 8,
}

month_mapping = {
    'Jan': 1,
    'Feb': 2,
    'Mar': 3,
    'Apr': 4,
    'May': 5,
    'Jun': 6,
    'Jul': 7,
    'Aug': 8,
    'Sep': 9,
    'Oct': 10,
    'Nov': 11,
    'Dec': 12,
}


st.title('Price Prediction App')

# Collect user inputs
quantity = st.number_input("Enter Quantity")
unit_price = st.number_input("Enter Unit Price")
comp_price = st.number_input("Enter Competitive Price")
product_score = st.number_input("Enter Product Score (1.0 to 4.9)")
lag_price = st.number_input("Enter Lag Price")
avg_compt_diff = st.number_input("Enter Average Competitive Difference")

product_category_label = st.selectbox("Select Product Category", options=['bed_bath_table', 'computers_accessories','consoles_games','cool_stuff','furniture_decor','garden_tools','health_beauty','perfumery','watches_gifts'])

# Convert product category using label encoding
product_category = category_mapping.get(product_category_label)

# Map month names to numeric values
month_name = st.selectbox("Select Month", options=list(month_mapping.keys()))
month = month_mapping.get(month_name)

year = st.selectbox("Select Year", options=[2017, 2018, 2019])

if None in [quantity, unit_price, comp_price, product_score, lag_price, avg_compt_diff, product_category, month, year]:
    st.warning("Please fill in all required input fields.")    
else:    
    # Prepare input data as a DataFrame
        input_data = pd.DataFrame({
        'qty': [quantity],
        'unit_price': [unit_price],
        'comp_1': [comp_price],
        'product_score': [product_score],
        'lag_price': [lag_price],
        'avg_comp_diff': [avg_compt_diff],
        'product_category_name': [product_category],
        'month':[month],
        'year':[year],
    })
    
    # Use your trained model to make predictions
predicted_price = model3.predict(input_data)
    
st.success(f'Predicted Total Price: ${predicted_price[0]:.2f}')
