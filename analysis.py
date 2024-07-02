import pandas as pd 
import datetime 
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler


data=pd.read_csv("D:\walmart-sales-dataset-of-45stores.csv")
df=pd.DataFrame(data)
print(df.head())
print("\nSummary statistics of the dataset:")
print(df.describe())
print(df.isnull().sum())

#no Null values to handle
print(df.duplicated().sum())

#no duplicated values to handle
print(df.dtypes)

# Data Preprocessing


#change date col to Datetime data type
df['Date'] = pd.to_datetime(df['Date'], format="%d-%m-%Y")

#clear inconsistant dates if present
start_date = pd.to_datetime('05-02-2010', format="%d-%m-%Y")
end_date = pd.to_datetime('01-11-2012', format="%d-%m-%Y")
df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

#Check for negative sales values
df=df[df['Weekly_Sales'] >= 0]
columns_to_handle_outliers = ['Weekly_Sales', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment']

# Loop through the specified columns
df_filtered = df.copy()



# Loop through the specified columns
for column in columns_to_handle_outliers:
    # Create box plot
    sns.boxplot(data=df_filtered[column])
    plt.title("before Outlier Handling: " + column)
    plt.show()
    # Calculate the interquartile range (IQR)
    q1 = df_filtered[column].quantile(0.25)
    q3 = df_filtered[column].quantile(0.75)
    iqr = q3 - q1
    # Define the threshold for outliers
    threshold = 1.5 * iqr
    # Handle outliers and update the filtered DataFrame
    df_filtered = df_filtered[(df_filtered[column] >= q1 - threshold) & (df_filtered[column] <= q3 + threshold)]
    sns.boxplot(data=df_filtered[column])
    plt.title("After Outlier Handling: " + column)
    plt.show()

# Visualization


#visulaize qaunitative coloums
plt.figure(figsize=(12, 8))
plt.subplot(3, 2, 1)
sns.histplot(df_filtered['Weekly_Sales'], kde=True, color='blue')
plt.title('Distribution of Weekly Sales')

plt.subplot(3, 2, 2)
sns.histplot(df_filtered['Temperature'], kde=True, color='red')
plt.title('Distribution of Temperature')

plt.subplot(3, 2, 3)
sns.histplot(df_filtered['Fuel_Price'], kde=True, color='green')
plt.title('Distribution of Fuel Price')

plt.subplot(3, 2, 4)
sns.histplot(df_filtered['CPI'], kde=True, color='orange')
plt.title('Distribution of CPI')

plt.subplot(3, 2, 5)
sns.histplot(df_filtered['Unemployment'], kde=True, color='purple')
plt.title('Distribution of Unemployment')

plt.tight_layout()
plt.show()
   
   
   
   
#stores sales
stores_sales = df_filtered.groupby("Store")["Weekly_Sales"].sum()
print("\nstores sales :\n",stores_sales)

#print max store in sales
print("\nStore",stores_sales.idxmax(),"has the maximum sales of",stores_sales.max())

#store standard diviations
stores_std=df_filtered.groupby("Store")["Weekly_Sales"].std()
print("\nstores stds :\n",stores_std)

#max store that vary in sales
print("\nStore",stores_std.idxmax(),"has the maximum variation",stores_std.max())


#the mean sales in the non-holiday season for all stores together
non_holiday_sales_mean = df_filtered[df_filtered['Holiday_Flag'] == 0]['Weekly_Sales'].mean()

#Filter the dataset to include only holiday dates
holiday_data = df_filtered[df_filtered['Holiday_Flag'] == 1]

#Calculate the sales for each holiday
holiday_sales = holiday_data.groupby('Date')['Weekly_Sales'].sum()

#Compare holiday sales with the mean sales during non-holiday seasons and return the gretaer tahn mean dates
holidays_higher_sales = holiday_sales[holiday_sales > non_holiday_sales_mean]

print("Holidays with higher sales than the mean sales in non-holiday seasons:")
print(holidays_higher_sales)

#monthely view of sales
df_filtered['month']=df_filtered['Date'].dt.month
monthely_sales=df_filtered.groupby('month')['Weekly_Sales'].sum()
print("monthely sales : \n",monthely_sales)

#month have max sales
print("max sales in month : ",monthely_sales.idxmax()," with sales ",monthely_sales.max())

#month have min sales
print("min sales in month : ",monthely_sales.idxmin()," with sales ",monthely_sales.min())

#method to classify monthes to seasons
def date_to_season(date):
    z=[]
    
    for x in date:
        x= x.strftime('%d-%m-%Y')
        parts=x.split('-')
        d=int(parts[0])
        m=int(parts[1])
        y=int(parts[2])
        x=datetime.datetime(y, m, d)
        if datetime.datetime(y,3,20) <= x <= datetime.datetime(y, 6, 20):
            y="spring"
        elif datetime.datetime(y,6,21) <= x <= datetime.datetime(y, 9, 22):
            y="summer"
        elif datetime.datetime(y,9,23) <= x <= datetime.datetime(y, 12, 21):
            y="autumn"
        else:
            y="winter"
        z.append(y)
    return z


#make season col
df_filtered["season"]=date_to_season(df_filtered["Date"])

#show seasons
print(df_filtered[["season","Date"]])

#seasonly view of sales
season_sales=df_filtered.groupby('season')['Weekly_Sales'].sum()
print("seasonly sales : \n",season_sales)

#season have max sales
print("max sales in season : ",season_sales.idxmax()," with sales ",season_sales.max())

#season have min sales
print("min sales in season : ",season_sales.idxmin()," with sales ",season_sales.min())

#Plot the relations between weekly sales vs. other numeric features and give insights.
plt.figure(figsize=(12, 8))

# Scatter plot for 'Temperature' vs. 'Weekly_Sales'
plt.subplot(2, 2, 1)
sns.scatterplot(data=df_filtered, x='Temperature', y='Weekly_Sales', color='blue')
plt.title('Temperature vs. Weekly Sales')

# Scatter plot for 'Fuel_Price' vs. 'Weekly_Sales'
plt.subplot(2, 2, 2)
sns.scatterplot(data=df_filtered, x='Fuel_Price', y='Weekly_Sales', color='green')
plt.title('Fuel Price vs. Weekly Sales')

# Scatter plot for 'CPI' vs. 'Weekly_Sales'
plt.subplot(2, 2, 3)
sns.scatterplot(data=df_filtered, x='CPI', y='Weekly_Sales', color='orange')
plt.title('CPI vs. Weekly Sales')

# Scatter plot for 'Unemployment' vs. 'Weekly_Sales'
plt.subplot(2, 2, 4)
sns.scatterplot(data=df_filtered, x='Unemployment', y='Weekly_Sales', color='purple')
plt.title('Unemployment vs. Weekly Sales')

plt.tight_layout()
plt.show()
