#!/usr/bin/env python
# coding: utf-8

# In[62]:


# Importing Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[63]:


#Laoding DATA

Grocery=pd.read_csv("Supermart Grocery Sales - Retail Analytics Dataset.csv", index_col="Order ID")
Grocery


# In[64]:


#CHECKING FOR COLUMNS

Grocery.columns


# In[65]:


# CHECKING THE COLUMN TYPES OFN THE DATA
Grocery.info()


# In[66]:


#CHANGING THE "OREDER DATE" COLUMN TO A datetime TYPE

Grocery["Order Date"]=pd.to_datetime(Grocery["Order Date"])


# In[67]:


Grocery.info()


# In[68]:


#CREATING A NEW COLUMN TO SPLIT DAY NAME

Grocery["Day_Name"]=Grocery["Order Date"].dt.day_name()


# In[69]:


#GETTING THE SALES PER DAY

Daysales=Grocery.groupby("Day_Name")["Sales"].sum()
Daysales


# In[70]:


#ASSINGING VARIABLES TO THE SALES PER DAY TO PLOT CHART

Name=Daysales.index
Number=Daysales.values


# In[71]:


#PLOTTING SALES PER DAY CHART

plt.bar(Name,Number,color="red")
plt.title("SALES PER DAY",fontstyle="italic",fontweight="bold",fontsize=15,c="black")
plt.xlabel("Days")
plt.ylabel("Sales per day")
plt.savefig("Sales Per Day.png")
plt.show()


# In[72]:


#GETTING THE TOP 5 SALES

Top5=Grocery.sort_values("Sales",ascending=False).head(5)
Top5


# In[73]:


#PLOTTING SALES BY CITY CHART SEABORN

sns.barplot(x=Top5["City"],y=Top5["Sales"],data=Top5,palette="summer")
plt.title("TOP 5 CITY BY SALES",fontsize=15,fontweight="bold",c="g")
plt.xlabel("City")
plt.ylabel("Sales")
plt.savefig("T5 city by sales.png")
plt.show()


# In[74]:


# GROUPING THE REGION BY THEIR PROFITS

RegDis=Grocery.groupby("Region")["Discount"].sum()
RegDis


# In[75]:


#ASSIGNING A VARIABLE TO PLOT A CHART

Name1=RegDis.index
Number1=RegDis.values


# In[76]:


#PLOTTING A LINE CHART FOR DISCOUNT BY REGION

plt.plot(Name1,Number1,marker="o")
plt.title("DISCOUNT BY REGION", fontsize=15,fontweight="bold",c="violet")
plt.xlabel("Region")
plt.ylabel("Discount")
plt.savefig("DisReg.png")
plt.show()


# In[77]:


#GETTING THE TOP 10 HIGHEST PROFIT

Top10=Grocery.sort_values("Profit",ascending=False).head(10)
Top10


# In[78]:


#GROUPING THE CUSTOMERS WITH THEIR PROFIT

CustProfit=Top10.groupby("Customer Name")["Profit"].sum()
CustProfit


# In[79]:


#ASSIGNING VARIABLES TO THE SALES PER DAY TO PLOT CHART

Name2=CustProfit.index
Number2=CustProfit.values


# In[80]:


#PLOTTING THE CHART FOR CUSTOMERS WITH THE HIGHEST PROFIT(TOP10)

plt.barh(Name2,Number2,color="purple")
plt.title("TOP 10 CUSTOMERS WITH THE HIGHEST PROFIT",fontsize=15,fontweight="bold",c="#FF0000")
plt.savefig("T10 cust.png")
plt.show()


# In[81]:


#CREATING A NEW COLUMN TO SPLIT THE YEAR

Grocery["Year"]=Grocery["Order Date"].dt.year


# In[82]:


#GETTING THE SALES PER YEAR

Year=Grocery.groupby("Year")["Sales"].sum()
Year


# In[83]:


#ASSIGNING A VARIABLE TO PLOT A CHART

Name3=Year.index
Number3=Year.values


# In[84]:


#PLOTTING A PIE CHART FOR THE CATEGORY BY YEAR

plt.pie(Number3,labels=Name3,autopct="%1.0f%%",shadow=True,explode=[0,0.1,0,0.1])  # autopct is each pie percentage
plt.title("SALES PER YEAR",fontsize=15,fontweight="bold",c="black")
plt.savefig("SPY.png")
plt.show()


# In[88]:


#PLOTTING THE CHART OF CATEGORY BUY SALES USING SEABORN

sns.boxplot(x=Grocery["Category"],y=Grocery["Sales"],data=Grocery,palette="coolwarm")
plt.title("CATEGORY BY SALES",fontsize=15,fontweight="bold",fontstyle="italic",c="b")
plt.xlabel("Category Name")
plt.ylabel("Total Sales")
plt.savefig("CatSales.png")
plt.show()


# In[87]:


#PLOTTING THE CHARTS IN A SUBPLOTS

fig,SuperMart=plt.subplots(nrows=3,ncols=2,figsize=(12,12))
fig.suptitle("SUPERMART GROCERY SALES REPORT",fontweight="bold",c="#800080",fontsize=30)
SuperMart[0,0].bar(Name,Number,color="red")
sns.barplot(x=Top5["City"],y=Top5["Sales"],data=Top5,palette="summer",ax=SuperMart[0,1])
SuperMart[1,0].plot(Name1,Number1,marker="o")
SuperMart[1,1].barh(Name2,Number2,color="purple")
SuperMart[2,0].pie(Number3,labels=Name3,autopct="%1.0f%%",shadow=True,explode=[0,0.1,0,0.1])
sns.boxplot(x=Grocery["Category"],y=Grocery["Sales"],data=Grocery,palette="coolwarm",ax=SuperMart[2,1])
SuperMart[0,0].set(title="SALES PER DAY")
SuperMart[0,1].set(title="TOP 5 CITY BY SALES")
SuperMart[1,0].set(title="DISCOUNT BY REGION")
SuperMart[1,1].set(title="TOP 10 CUSTOMERS WITH THE HIGHEST PROFIT")
SuperMart[2,0].set(title="SALES PER YEAR")
SuperMart[2,1].set(title="CATEGORY BY SALES")
plt.tight_layout()
plt.savefig("SuperMart.png")
plt.show()


# In[ ]:





# In[ ]:




