import pandas as pd # for dataframes
import matplotlib.pyplot as plt # for plotting graphs
import seaborn as sns # for plotting graphs
import datetime as dt
data=pd.read_excel('D:\onilne_retail2.xlsx')#to read excel file 
data.info()
df=pd.DataFrame(data)
filtered_data=data[['CustomerID','Country']].drop_duplicates()#drop duplicates 
filtered_data.Country.value_counts()[:10].plot(kind="bar")#make a plot#study
#study
plt.title("Top 10 Countries")
plt.xlabel("Country")
plt.ylabel("Count")
plt.show()#display plot
uk_data=data[data.Country=='United Kingdom']#filtering data
#till here
uk_data.info()
print(uk_data.nunique())#show uniqness
print(uk_data.describe())
#study again
uk_data=uk_data[(uk_data['Quantity']>=0)&(uk_data['UnitPrice']>0)]#rem inconsistant data
uk_data.dropna()#drop null values coloums

#till here
uk_data.info()
#study
uk_data=uk_data[['InvoiceNo','Quantity','InvoiceDate','UnitPrice','CustomerID','Country']]
#end
uk_data['total_price']=uk_data['Quantity']*uk_data['UnitPrice']
present=dt.datetime(2024,12,3)
#study
uk_data['InvoiceDate']=pd.to_datetime(uk_data['InvoiceDate'],format='%m/%d/%y %H:%M')
df['InvoiceDate'] = uk_data['InvoiceDate'].dt.strftime('%Y/%-m/%-d')
#study
rfm=uk_data.groupby('CustomerID').agg({'InvoiceDate':lambda date:(present-date.max()).days,'InvoiceNo':lambda num:len(num),'total_price':lambda price:price.sum()})
#till here 
rfm.columns=['Recency','Frequency','Monetary']
#study
rfm['Recency']=rfm['Recency'].astype(int)
rfm['Monetary']=rfm['Monetary'].astype(int)
rfm['R_qurtil']=pd.qcut(rfm['Recency'],4,[1,2,3,4])
rfm['F_qurtil']=pd.qcut(rfm['Frequency'],4,[4,3,2,1])
rfm['M_qurtil']=pd.qcut(rfm['Monetary'],4,[4,3,2,1])
#till here
rfm['RFM_score']=rfm['R_qurtil'].astype(str)+rfm['F_qurtil'].astype(str)+rfm['M_qurtil'].astype(str)
print(rfm.head())
#study
print(rfm[rfm['RFM_score']=='111'].sort_values('Monetary',ascending=False).head())#display first 5 top customers

