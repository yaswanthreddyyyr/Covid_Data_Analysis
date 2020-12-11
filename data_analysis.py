# import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

df = pd.read_csv("Dataset/covid_19_india.csv")
df.head()

print(" Number of row in the dataset are :", df.shape[0])
print(" Number of column in the dataset are :", df.shape[1])

# dataset info

df.info()

# dataset describe

df.describe()

df.isnull().sum()

print("Number of duplicate value in the dataset are :", sum(df.duplicated()))

df_new = df.drop(['ConfirmedIndianNational', 'ConfirmedForeignNational'], axis = 1)

df_new.head()

covid_new = df_new[df_new['Date'] == '10/07/20']

#Which state has most number of Confirmed Cases?

covid_new.sort_values(by='Confirmed', ascending=False)[:10]

covid_new.sort_values(by="Confirmed", ascending=False)[:10].plot(x='State/UnionTerritory',y='Confirmed',kind='bar',  color= 'tab:orange',figsize=(12,6))
covid_new.sort_values(by="Deaths", ascending=False)[:10]
# plot the bar graph of top 10 state with most number of Deaths cases on 10/07/20

covid_new.sort_values(by="Deaths", ascending=False)[:10].plot(x='State/UnionTerritory',y='Deaths',kind='bar', color= 'tab:red', figsize=(10,5))

# sort the dataset of top 10 state with most number of recovery on 10/07/20

covid_new.sort_values(by="Cured", ascending=False)[:10]

# plot the bar graph of top 10 state with most number of Confirmed cases on 10/07/20

covid_new.sort_values(by="Cured", ascending=False)[:10].plot(x='State/UnionTerritory',y='Cured',kind='bar', color= 'tab:green' ,figsize=(10,5))

labels=['Cured','Death','Confirmed']
values=[127259,9667,230599]
import matplotlib.pyplot as plt
explode=(0.20,0.20,0)

fig1, ax1 = plt.subplots()
ax1.pie(values, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()

# Mortality rate of maharastra
print("Mortality rate of maharasthra:-")

(covid_new['Deaths'].max()/covid_new['Confirmed'].max())*100
# recovery rate of Maharastra
print("Recovery Rate of Maharastra:-")

(covid_new['Cured'].max()/covid_new['Confirmed'].max())*100
#------------------------------------------------------------------------------------------------------------#

# read the csv

df_age = pd.read_csv('Dataset/AgeGroupDetails.csv')
df_age.head()

# dataset info

df_age.info()

# dataset describe

df_age.describe()

# check weather dataset contain any null values

print("The number of value dataset contain are :",df_age.isnull().sum())

df_age.sort_values(by="TotalCases", ascending=False)

#Q3) Which Age group has heigher chance of getting infected?

# check weather the dataset contain null value or not

print("The number of nulll value in the dataset are :", df_age.isnull().sum())

df_age.sort_values(by="TotalCases", ascending=False)
# plot the graph between TotalCases and AgeGroups

df_age.sort_values(by="TotalCases", ascending=False).plot(x = 'AgeGroup', y='TotalCases', kind = 'bar', color= 'tab:red', figsize=(10,5))

#From the above data Age group between 20-29 has heigher chance of getting infected
#-------------------------------------------------------------------------------------------------------------------#
# read the dataset

df_hospital = pd.read_csv("Dataset/HospitalBedsIndia.csv")

df_hospital.head()
# dataset info

df_hospital.info()
# sort the value of dataset Total health care facilities


#Q4) Which state has better Public Health care facilities?

df_hospital.sort_values(by='TotalPublicHealthFacilities_HMIS', ascending=False)[1:10]

# plot the graph for total public health care facilites

df_hospital.sort_values(by="TotalPublicHealthFacilities_HMIS", ascending=False)[1:36].plot(x='State/UT',y='TotalPublicHealthFacilities_HMIS',kind='bar', color= 'tab:red', figsize=(12,5))
#From the data Uttar Pradesh is top in terms of Total Public Health Care has 4122
# sort the dataset which state has heigher number of public beds

df_hospital.sort_values(by="NumPublicBeds_HMIS", ascending=False)[1:10]
# plot the graph for number of public beds avilable

df_hospital.sort_values(by="NumPublicBeds_HMIS", ascending=False)[1:36].plot(x='State/UT',y='NumPublicBeds_HMIS',kind='bar', color= 'tab:orange' ,figsize=(12,5))

# sort the dateset by number of beds avilable

df_hospital.sort_values(by="NumUrbanBeds_NHP18", ascending=False)[1:10]

# plot the graph for number of Urban beds avilable

df_hospital.sort_values(by="NumUrbanBeds_NHP18", ascending=False)[1:36].plot(x='State/UT',y='NumUrbanBeds_NHP18',kind='bar', color= 'tab:green', figsize=(12,5))
# sort the dateset by number of Rural beds avilable

df_hospital.sort_values(by="NumRuralBeds_NHP18", ascending=False)[1:10]

# plot the graph for number of Rural beds avilable

df_hospital.sort_values(by="NumRuralBeds_NHP18", ascending=False)[1:36].plot(x='State/UT',y='NumRuralBeds_NHP18',kind='bar', color= 'tab:red', figsize=(12,5))





#-------------------------------------------------------------------------------------------------------------#
# read the datset

df_testing = pd.read_csv("Dataset/StatewiseTestingDetails.csv")
# df_testing

# dataset Info

df_testing.info()

# coverte the negative column from string to float


df_testing_details = pd.DataFrame(df_testing)

df_testing_details['Negative'] = pd.to_numeric(df_testing_details['Negative'], errors='coerce')

df_testing_details.info()

# Check weather the Negative column converted from string to float or not

print("Datatype of Negative column are :", df_testing_details['Negative'].dtype)
# check weather dataset contain any null values

print("The number of value dtaset contain are :",df_testing_details.isnull().sum())

# remove the null values

df_test = df_testing_details.dropna(subset=['Negative', 'Positive'])
# Check the null values are droped or not

print("The number of null value dataset contains are :",df_test.isnull().sum())

# sort the dataset by number of total cases

df_test.sort_values(by='TotalSamples', ascending = False)[:10]
# plot the graph for total number of sample

df_test.sort_values(by="TotalSamples", ascending=False)[1:36].plot(x='State',y='TotalSamples',kind='bar', color= 'tab:orange', figsize=(14,9))
# sort the dataset by number of positive cases

df_test.sort_values(by='Positive', ascending = False)[:10]
# plot the graph for total number of positive sample

df_test.sort_values(by="Positive", ascending=False)[1:36].plot(x='State',y='Positive',kind='bar', color= 'tab:red', figsize=(14,9))

# sort the dataset by number of Negative cases

df_test.sort_values(by='Negative', ascending = False)[:10]
# plot the graph for total number of negative sample

df_test.sort_values(by="Negative", ascending=False)[1:36].plot(x='State',y='Negative',kind='bar', color= 'tab:green', figsize=(14,9))

#we are going to analyis the Maharastra cases.
# Maharastra has max total Sample on 12/07/2020
# consider for date 12/07/2020

df_test_date = df_test[df_test['Date'] == '2020-07-12']
# Maximum total sample for Maharastra on date 12/07/2020
# make a df for state Maharastra for date 12/07/2020

df_test_maha = df_test_date[df_test_date["State"]=='Maharashtra']
df_test_maha['TotalSamples'].max()
# Maximum total Positive sample for Maharastra on date 12/07/2020

df_test_maha['Positive'].max()
# Maximum total Negative sample for Maharastra on date 12/07/2020

df_test_maha['Negative'].max()
labels=['Total Sample','Positive','Negative']
values=[1321715.0,259037.0, 1062678.0]
import matplotlib.pyplot as plt
explode=(0.20,0.20,0)

fig1, ax1 = plt.subplots()
ax1.pie(values, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
