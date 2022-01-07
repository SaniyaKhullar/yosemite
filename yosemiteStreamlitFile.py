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
st.write("Please note some things about this streamlit web application")
# display the image of the class picture
st.write("This App Was Created By: Alexander, Ashwin, Andre, Gayu, Abhinav")
st.write("Instructor: Saniya Khullar")
st.write("Please note that the datasets we used were: [House Prices](https://www.kaggle.com/shree1992/housedata) and [Strokes](https://www.kaggle.com/fedesoriano/stroke-prediction-dataset)") # adding in hyperlinks. 
st.image('yoseMite.png')

#### House Prices #############################################################################################################
st.header("Predicting House Prices based On Given Data")
st.header("Houses In Seattle")
# kaggle website: https://www.kaggle.com/shree1992/housedata
st.write ("This dataset gave us the information to build the scatter plot. Although it is data from three years ago, it is useful information to get the general idea for the average pricing for houses")
# Gayu to please write about.
####  adding columns to the dataset
valueIfTrue = "Renovated"
valueIfFalse = "Not Renovated"

# country size is: large if population is greater than or equal to 100 mil
# country size is: small if less than 100 mil

housePriceDF['State of Renovation'] = np.where((housePriceDF.yr_renovated >= 1), valueIfTrue, valueIfFalse)
#\
valueIfTrue = "Good Condition"
valueIfFalse = "Average/Poor Condition"

# country size is: large if population is greater than or equal to 100 mil
# country size is: small if less than 100 mil
housePriceDF['State/Condition of House'] = np.where((housePriceDF.condition >= 4), valueIfTrue, valueIfFalse)
housePriceDF

valueIfTrue = "Large House"
valueIfFalse = "Average/Small House"

housePriceDF['House Size'] = np.where((housePriceDF.sqft_living >=2500), valueIfTrue, valueIfFalse)
#\
valueIfTrue = "Studio"
valueIfFalse = "House/Apartment"

housePriceDF['Type of Home'] = np.where((housePriceDF.bedrooms==0), valueIfTrue, valueIfFalse)
#\
valueIfTrue = "Expensive"
valueIfFalse = "Average/Cheap"

housePriceDF['Cost'] = np.where((housePriceDF.price>=1200000), valueIfTrue, valueIfFalse)
#]\
valueIfTrue = "Good View"
valueIfFalse = "Average/Poor View"

housePriceDF['View Condition'] = np.where((housePriceDF.view>=3), valueIfTrue, valueIfFalse)

valueIfTrue = "Multi Story House"
valueIfFalse = "One Story House"

housePriceDF['# Of Stories'] = np.where((housePriceDF.floors>=2), valueIfTrue, valueIfFalse)

valueIfTrue = "Haunted"
valueIfFalse = "Not Haunted"

housePriceDF['Haunt Status'] = np.where((housePriceDF.price==0), valueIfTrue, valueIfFalse)

co1 = 'Excellent Condition'
co2 = 'Good Condition'
co3 = 'Average Condition'
co4 = 'Poor Condition'
co5 = 'Terrible Condition'

housePriceDF.loc[(housePriceDF['condition'] == 5, 'State/Condition of House')] = co1
housePriceDF.loc[(housePriceDF['condition'] == 4, 'State/Condition of House')] = co2
housePriceDF.loc[(housePriceDF['condition'] == 3, 'State/Condition of House')] = co3
housePriceDF.loc[(housePriceDF['condition'] == 2, 'State/Condition of House')] = co4
housePriceDF.loc[(housePriceDF['condition'] == 1, 'State/Condition of House')] = co5

v1 = 'Excellent View'
v2 = 'Good View'
v3 = 'Average View'
v4 = 'Poor View'
v5 = 'Terrible View'


housePriceDF.loc[(housePriceDF['view'] == 4, 'View Condition')] = v1
housePriceDF.loc[(housePriceDF['view'] == 3, 'View Condition')] = v2
housePriceDF.loc[(housePriceDF['view'] == 2, 'View Condition')] = v3
housePriceDF.loc[(housePriceDF['view'] == 1, 'View Condition')] = v4
housePriceDF.loc[(housePriceDF['view'] == 0, 'View Condition')] = v5

c1 = 'Expensive'
c2 = 'Average'
c3 = 'Cheap'
housePriceDF.loc[(housePriceDF['price'] <= 300000, 'Cost')] = c3
housePriceDF.loc[(((housePriceDF['price'] > 300000) & (housePriceDF['price'] <= 899999)), 'Cost')] = c2
housePriceDF.loc[(housePriceDF['price'] > 900000, 'Cost')] = c1

####################### finished adding new columns for the houses dataset
st.dataframe(housePriceDF)
#housePricefig1 = fig = px.pie(housePriceDF, values="price", names="condition", title = "condition vs. prices of houses")
#st.plotly_chart(housePricefig1)
#colorVariable1 = st.selectbox(
    # 'How would you like the graph to be colored?',
    # ("yr_built","price", "floors", "waterfront", "yr_renovated","sqft_lot","sqft_living", "condition", "city", "sqft_basement", "statezip", "country"))

numericHouseColumnsTuple = tuple(housePriceDF.select_dtypes(["int", "float"]).columns) # selecting all of the columns that have data types of ints or floats

HouseColumnsTuple = tuple(housePriceDF.columns)
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
txt = st.text_area('Analysis of the above Scatterplot Chart', '''This scatterplot for home pricing rate shows the pricing of houses based on the x and y 
co-ordinates. you can change the x and y choices using the drop down menu. the options range anywhere from bedrooms, views, to price and more! Just like you can change the x and y axis, you can also change the coloring factor.  ''')


choice = st.radio("Pick a View Type", ['Terrible View', 'Poor View', 'Average View', 'Good View', 'Excellent View'])
if choice == 'Terrible View':
    houseviewDF = housePriceDF[housePriceDF["View Condition"] == "Terrible View"]
elif choice == 'Poor View':
    houseviewDF = housePriceDF[housePriceDF["View Condition"] == "Poor View"]
elif choice == 'Average View':
    houseviewDF = housePriceDF[housePriceDF["View Condition"] == "Average View"]
elif choice == 'Good View':
    houseviewDF = housePriceDF[housePriceDF["View Condition"] == "Good View"]
else: # choice == 'Excellent View':
    houseviewDF = housePriceDF[housePriceDF["View Condition"] == "Excellent View"]
    
titleBoxPlot = "Boxplot of the Prices of the Homes for Various Conditions (1 to 5 Stars) with a " + choice + ":"
housePricefig2 = px.box(houseviewDF, x="condition", y="price", 
                           title = titleBoxPlot)
st.plotly_chart(housePricefig2)


categoryForBarChart1 = st.radio("Which feature do you want to learn more about in the bar chart?",  ('Type of Home', 'House Size', 'State/Condition of House', '# Of Stories'))
categoryForBarChart2 = st.radio("What other feature do you want to be shown in the bar chart?", numericHouseColumnTuple)
titleMessage3 = "Bar Graph of " + categoryForBarChart1 +" as compared to "+ categoryForBarChart2

housePricefig3 = px.bar(housePriceDF, x = categoryForBarChart2, y = categoryForBarChart1, title = titleMessage3)
st.plotly_chart(housePricefig3)
#####################################################################################################################





#####################################################################################################################


#  Strokes ###########################################################################################
st.title("Stroke Prediction based on Variables")
st.header("Second most leading cause of deaths globally")

# here, you can talk about the new variables you defined.
txt = st.text_area('Deriving additional categorical variables for strokes', '''The "general_age" column defines people <30 years old as young, >30 but <=60 as middle-aged, and >60 as old.   ||   "weight" column specifies people with a BMI <18.5 as underweight, >=18.5 but <25 as normal, >=25 but <30 as overweight, >=30 but <35 as obese, and >35 as extremely obese.   ||   "general_glucose_level" column assigns excellent to an average glucose level <=115, good if it is >=115 but <= 180, and poor if it is >180.''')

#VERY IMPORTANT: ADDING NEW COLUMNS
under = 'Young'
middle = 'Middle-aged'
over = 'Old'

strokeDF.loc[(strokeDF['age'] <= 30, 'general_age')] = under
strokeDF.loc[(((strokeDF['age'] > 30) & (strokeDF['age'] <= 60)), 'general_age')] = middle
strokeDF.loc[(strokeDF['age'] > 60, 'general_age')] = over

under2 = 'Underweight'
middle2 = 'Normal'
over2 = 'Overweight'
moreover2 = 'Obese'
moreoverag2 = 'Extremely Obese'

strokeDF.loc[(strokeDF['bmi'] < 18.5, 'weight')] = under2
strokeDF.loc[(((strokeDF['bmi'] >= 18.5) & (strokeDF['bmi'] < 25)), 'weight')] = middle2
strokeDF.loc[(((strokeDF['bmi'] >= 25) & (strokeDF['bmi'] < 30)), 'weight')] = over2
strokeDF.loc[(((strokeDF['bmi'] >= 30) & (strokeDF['bmi'] < 35)), 'weight')] = moreover2
strokeDF.loc[(strokeDF['bmi'] > 35, 'weight')] = moreoverag2

ex3 = 'Excellent'
go3 = 'Good'
po3 = 'Poor'

strokeDF.loc[(strokeDF['avg_glucose_level'] <= 115, 'general_glucose_level')] = ex3
strokeDF.loc[(((strokeDF['avg_glucose_level'] >= 115) & (strokeDF['avg_glucose_level'] <= 180)), 'general_glucose_level')] = go3
strokeDF.loc[(strokeDF['avg_glucose_level'] > 180, 'general_glucose_level')] = po3

yesStroke = 'Stroke'
noStroke = 'No Stroke'

strokeDF.loc[(strokeDF['stroke'] == 1, 'HadStroke')] = yesStroke
strokeDF.loc[(strokeDF['stroke'] == 0, 'HadStroke')] = noStroke

# ################################### done adding new columns

st.dataframe(strokeDF)

# # https://docs.streamlit.io/library/api-reference/widgets/st.selectbox


strokeDF["people"] = 1

yesStroke = 'Stroke'
noStroke = 'No Stroke'

strokeDF.loc[(strokeDF['stroke'] == 1, 'HadStroke')] = yesStroke
strokeDF.loc[(strokeDF['stroke'] == 0, 'HadStroke')] = noStroke

categoryForBarChart = st.radio("Which feature do you want to learn more about in the bar chart?",  ('smoking_status', 'general_age', 'gender', 'HadStroke',  'ever_married'))

strokefig1 = px.bar(strokeDF, x='people', y= categoryForBarChart,color="HadStroke",
            labels = {"smoking_status":"Smoking Status","noStroke":"Amount of People who had no Strokes"},
                    title="Strokes based on Smoking Status and Chosen Variable")
st.plotly_chart(strokefig1)

# strkcolorVariable1 = st.selectbox(
#      'How would you like the bar graph to be colored?',
#      ("hypertension","smoking_status", "heart_disease", "work_type", "Residence_type", "ever_married","general_age","general_glucose_level", "weight"))


# strokefig1 = px.bar(strokeDF, x='stroke', y='smoking_status',color=strkcolorVariable1,labels = {"smoking_status":"Smoking Status","stroke":"Amount of People who had Strokes"},title="Strokes based on Smoking Status and Chosen Variable")



######################################################################################################
numericStrokeColumnsTuple = tuple(strokeDF.select_dtypes(["int", "float"]).columns) # selecting all of the columns that have data types of ints or floats
numericStrokeColumnsTuple
StrokeColumnsTuple = tuple(strokeDF.columns)

unknownvariable3 = st.selectbox('What do You Want The X-Axis of This Graph To Show?',
        numericStrokeColumnsTuple)
unknownvariable4 = st.selectbox('What do You Want The Y-Axis of This Graph To Show?',
        numericStrokeColumnsTuple)
strkcolorVariable1 = st.selectbox(
     'How would you like the scatter plot to be colored?',
    (StrokeColumnsTuple))
     #("hypertension","smoking_status", "heart_disease", "work_type", "Residence_type", "ever_married"))
knownBMI = strokeDF[strokeDF["bmi"] != "Unknown"] # known bmi
titleMessage1 = "Scatterplot of " + unknownvariable4 +" as compared to "+ unknownvariable3
figStrokeBMI = px.scatter(knownBMI, x=unknownvariable3, y=unknownvariable4, color = strkcolorVariable1, title = titleMessage1)
st.plotly_chart(figStrokeBMI)



#PIE CHART BELOW, no bmi or age options because it may crash the website#####################
strkcolorVariable2 = st.selectbox(
     'What variable would you like to visualize stroke metrics for?',
     ("smoking_status","hypertension", "heart_disease", "work_type", "Residence_type", "ever_married","weight","general_glucose_level","general_age","gender"))

# for people without strokes
peopleNoStrokesDF = strokeDF[strokeDF["stroke"] != 1] # dataframe with everyone who does not have a stroke (where stroke == 0)
peopleNoStrokesDF["noStroke"] = 1 # creates a new column called "noStroke" where every row has the value 1
# strokeDF[strokeDF["stroke"] == 0]

titleMessage = "Pie Chart of the 249 Individuals WITH Strokes :( based on: "+ strkcolorVariable2
strokefig2 = px.pie(strokeDF, values='stroke', names=strkcolorVariable2, title = titleMessage)
st.plotly_chart(strokefig2)

titleMessage2 = "Pie Chart of the 4,861 Individuals WITHOUT Strokes :] based on: "+strkcolorVariable2
strokefig3 = px.pie(peopleNoStrokesDF, values='noStroke', names=strkcolorVariable2, title = titleMessage2)
st.plotly_chart(strokefig3)

txt = st.text_area('Analysis of the above Pie Charts for Strokes', '''The two pie charts above compare the percentages of people who have a custom attribute that make up the total of those who had or did not have strokes.''')

######################################################################################################