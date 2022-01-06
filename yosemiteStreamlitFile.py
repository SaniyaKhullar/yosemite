# loading in packages in this streamlit python file
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


# please note that this is the file we will use for our streamlit application

housePriceDF = pd.read_csv("housePriceData.csv")
strokeDF = pd.read_csv("healthcare-dataset-stroke-data.csv")
# importing data files

# https://docs.streamlit.io/library/api-reference

#################### Introduction: ###########################################################################################
st.title("House Prices and Strokes")
st.write("Please note some things about this app....")
# display the image of the class picture
st.write("This App Was Created By: Alexander, Ashwin, Andre, Gayu, Abhinav")
st.write("Instructor: Saniya Khullar")
st.write("Please note that the datasets we used were: [House Prices](https://www.kaggle.com/shree1992/housedata) and [Strokes](https://www.kaggle.com/fedesoriano/stroke-prediction-dataset)") # adding in hyperlinks. 
st.image('yoseMite.png')

#### House Prices ###########################################################################################
st.header("Predicting House Prices based On Given Data")
st.header("Houses In Seattle")
# kaggle website: https://www.kaggle.com/shree1992/housedata

st.dataframe(housePriceDF)
#housePricefig1 = fig = px.pie(housePriceDF, values="price", names="condition", title = "condition vs. prices of houses")
#st.plotly_chart(housePricefig1)
#colorVariable1 = st.selectbox(
    # 'How would you like the graph to be colored?',
    # ("yr_built","price", "floors", "waterfront", "yr_renovated","sqft_lot","sqft_living", "condition", "city", "sqft_basement", "statezip", "country"))
#housePricefig2 = px.scatter(housePriceDF, y="price", x="sqft_living",size = "price" ,color = colorVariable1, title = "Price Based On Square Feet of Living")
#st.plotly_chart(housePricefig2)

#housePricefig3 = px.scatter(housePriceDF, x="sqft_lot", y="sqft_living", color =colorVariable1, title = "Square Feet of Living as Compared To Square Feet of Lot")
#st.plotly_chart(housePricefig3)


unknownvariable1 = st.selectbox(
     'What do You Want The X-Axis of This Graph To Show?',
        numericHouseColumnsTuple)

unknownvariable2 = st.selectbox(
     'What do You Want The Y-Axis of This Graph To Show?',
           numericHouseColumnsTuple)
colorVariable1 = st.selectbox(
     'what would you like the graph to be colored based on?',
      ("price", "bedrooms", "bathrooms", "sqft_living", "sqft_lot",
       "floors", "waterfront", "view", "condition", "sqft_above",
       "sqft_basement", "yr_built", "yr_renovated", "street", "city",
       "statezip", "State of Renovation",
       "State/Condition of House", "House Size", "Type of Home", "Cost",
       "View Condition", "# Of Stories"))

titleMessage = "Scatterplot of " + unknownvariable2+" as compared to "+unknownvariable1
housePricefig1 = px.scatter(housePriceDF, x=unknownvariable1, y=unknownvariable2, color = colorVariable1,
                           title = titleMessage)
st.plotly_chart(housePricefig1)
#####################################################################################################################





#####################################################################################################################




#  Strokes ###########################################################################################
st.title("Stroke Prediction based on Variables")
st.header("Second most leading cause of deaths globally")

# #VERY IMPORTANT: ADDING NEW COLUMNS
# under = 'Young'
# middle = 'Middle-aged'
# over = 'Old'

# strokeDF.loc[(strokeDF['age'] <= 30, 'general_age')] = under
# strokeDF.loc[(((strokeDF['age'] > 30) & (strokeDF['age'] <= 60)), 'general_age')] = middle
# strokeDF.loc[(strokeDF['age'] > 60, 'general_age')] = over

# under2 = 'Underweight'
# middle2 = 'Normal'
# over2 = 'Overweight'
# moreover2 = 'Obese'
# moreoverag2 = 'Extremely Obese'

# strokeDF.loc[(strokeDF['bmi'] < 18.5, 'weight')] = under2
# strokeDF.loc[(((strokeDF['bmi'] >= 18.5) & (strokeDF['bmi'] < 25)), 'weight')] = middle2
# strokeDF.loc[(((strokeDF['bmi'] >= 25) & (strokeDF['bmi'] < 30)), 'weight')] = over2
# strokeDF.loc[(((strokeDF['bmi'] >= 30) & (strokeDF['bmi'] < 35)), 'weight')] = moreover2
# strokeDF.loc[(strokeDF['bmi'] > 35, 'weight')] = moreoverag2

# ex3 = 'Excellent'
# go3 = 'Good'
# po3 = 'Poor'

# strokeDF.loc[(strokeDF['avg_glucose_level'] <= 115, 'general_glucose_level')] = ex3
# strokeDF.loc[(((strokeDF['avg_glucose_level'] >= 115) & (strokeDF['avg_glucose_level'] <= 180)), 'general_glucose_level')] = go3
# strokeDF.loc[(strokeDF['avg_glucose_level'] > 180, 'general_glucose_level')] = po3

# strokeDF = strokeDF.fillna("Unknown")

# ################################### done adding new columns

st.dataframe(strokeDF)

# # https://docs.streamlit.io/library/api-reference/widgets/st.selectbox
# strkcolorVariable1 = st.selectbox(
#      'How would you like the bar graph to be colored?',
#      ("hypertension","smoking_status", "heart_disease", "work_type", "Residence_type", "ever_married","general_age","general_glucose_level", "weight"))


# strokefig1 = px.bar(strokeDF, x='stroke', y='smoking_status',color=strkcolorVariable1,labels = {"smoking_status":"Smoking Status","stroke":"Amount of People who had Strokes"},title="Strokes based on Smoking Status and Chosen Variable")

# st.plotly_chart(strokefig1)

knownBMI = strokeDF[strokeDF["bmi"] != "Unknown"] # known bmi
knownBMI

strkcolorVariable1 = st.selectbox(
     'How would you like the scatter plot to be colored?',
     ("hypertension","smoking_status", "heart_disease", "work_type", "Residence_type", "ever_married"))

figStrokeBMI = px.scatter(knownBMI, x='age', y='bmi', color = strkcolorVariable1)
st.plotly_chart(figStrokeBMI)


#strkcolorVariable2 = st.selectbox(
     #'What variable would you like to display?',
     #("hypertension","smoking_status", "heart_disease", "work_type", "Residence_type", "ever_married","weight","general_glucose_level","general_age","gender"))

#strokefig2 = px.pie(strokeDF, values='stroke', names=strkcolorVariable2,labels = {title="Strokes Pie Chart based on Chosen Variables"})

#st.plotly_chart(strokefig2)
