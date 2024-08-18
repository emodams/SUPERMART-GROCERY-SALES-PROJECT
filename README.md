# SUPERMART-GROCERY-SALES-PROJECT


### PROBLEM STATEMENT
Supermart, a mid-sized grocery retail chain, is experiencing fluctuations in sales across various product categories and stores. The management aims to optimize inventory levels, improve sales forecasting, and enhance promotional strategies. However, they lack a clear understanding of the factors driving sales variability, such as seasonality, pricing, promotions, customer preferences, and regional differences.

The objective of the "SuperMart Grocery Sales Project" is to analyze historical sales data to identify key patterns and trends, forecast future sales, and provide actionable insights to optimize product assortment, pricing strategies, and promotional efforts. The ultimate goal is to enhance SuperMart's profitability by improving decision-making processes related to inventory management, customer targeting, and marketing initiatives.

### LIBRARY USED
- Matplotlib
- Pandas
- Numpy
- Seaborn

### STEPS
#### Loading DATA

- Grocery=pd.read_csv("Supermart Grocery Sales - Retail Analytics Dataset.csv", index_col="Order ID")
- Grocery

#### CHECKING FOR COLUMNS

- Grocery.columns

#### CHECKING THE COLUMN TYPES OF THE DATA
Grocery.info()

#### CHANGING THE "OREDER DATE" COLUMN TO A datetime TYPE

- Grocery["Order Date"]=pd.to_datetime(Grocery["Order Date"])
- Grocery.info()

#### CREATING A NEW COLUMN TO SPLIT DAY NAME

- Grocery["Day_Name"]=Grocery["Order Date"].dt.day_name()

#### GETTING THE SALES PER DAY

- Daysales=Grocery.groupby("Day_Name")["Sales"].sum()
- Daysales

#### ASSINGING VARIABLES TO THE SALES PER DAY TO PLOT CHART

- Name=Daysales.index
- Number=Daysales.values

#### PLOTTING SALES PER DAY CHART

- plt.bar(Name,Number,color="red")
- plt.title("SALES PER DAY",fontstyle="italic",fontweight="bold",fontsize=15,c="black")
- plt.xlabel("Days")
- plt.ylabel("Sales per day")
- plt.savefig("Sales Per Day.png")
- plt.show()

![Sales Per Day](https://github.com/user-attachments/assets/7e5d2003-adcd-4ba1-bd60-66114e87a1b4)


### SOLUTION 2
#### GETTING THE TOP 5 SALES

- Top5=Grocery.sort_values("Sales",ascending=False).head(5)
- Top5

#### PLOTTING SALES BY CITY CHART SEABORN

- sns.barplot(x=Top5["City"],y=Top5["Sales"],data=Top5,palette="summer")
- plt.title("TOP 5 CITY BY SALES",fontsize=15,fontweight="bold",c="g")
- plt.xlabel("City")
- plt.ylabel("Sales")
- plt.savefig("T5 city by sales.png")
- plt.show()

![T5 city by sales](https://github.com/user-attachments/assets/42a12898-be20-4d97-82c9-60555cd60c45)


### SOLUTION 3

#### GROUPING THE REGION BY THEIR PROFITS

- RegDis=Grocery.groupby("Region")["Discount"].sum()
- RegDis

#### ASSIGNING A VARIABLE TO PLOT A CHART

- Name1=RegDis.index
- Number1=RegDis.values

#### PLOTTING A LINE CHART FOR DISCOUNT BY REGION

- plt.plot(Name1,Number1,marker="o")
- plt.title("DISCOUNT BY REGION", fontsize=15,fontweight="bold",c="violet")
- plt.xlabel("Region")
- plt.ylabel("Discount")
- plt.savefig("DisReg.png")
- plt.show()

![DisReg](https://github.com/user-attachments/assets/30869ee1-60f7-4230-a676-c8ed63e98325)

### SOLUTION 4

#### GETTING THE TOP 10 HIGHEST PROFIT

- Top10=Grocery.sort_values("Profit",ascending=False).head(10)
- Top10

#### GROUPING THE CUSTOMERS WITH THEIR PROFIT

- CustProfit=Top10.groupby("Customer Name")["Profit"].sum()
- CustProfit

#### ASSIGNING VARIABLES TO THE SALES PER DAY TO PLOT CHART

- Name2=CustProfit.index
- Number2=CustProfit.values

#### PLOTTING THE CHART FOR CUSTOMERS WITH THE HIGHEST PROFIT(TOP10)

- plt.barh(Name2,Number2,color="purple")
- plt.title("TOP 10 CUSTOMERS WITH THE HIGHEST PROFIT",fontsize=15,fontweight="bold",c="#FF0000")
- plt.savefig("T10 cust.png")
- plt.show()

![T10 cust](https://github.com/user-attachments/assets/ccbe8a4b-2a01-4e5d-971a-ece80371fb4f)

### SOLUTION 5

#### CREATING A NEW COLUMN TO SPLIT THE YEAR

- Grocery["Year"]=Grocery["Order Date"].dt.year

#### GETTING THE SALES PER YEAR

- Year=Grocery.groupby("Year")["Sales"].sum()
- Year

#### ASSIGNING A VARIABLE TO PLOT A CHART

- Name3=Year.index
- Number3=Year.values

#### PLOTTING A PIE CHART FOR THE CATEGORY BY YEAR

- plt.pie(Number3,labels=Name3,autopct="%1.0f%%",shadow=True,explode=[0,0.1,0,0.1])  # autopct is each pie percentage
- plt.title("SALES PER YEAR",fontsize=15,fontweight="bold",c="black")
- plt.savefig("SPY.png")
- plt.show()

![SPY](https://github.com/user-attachments/assets/3210b41b-e322-4ae5-96db-e1fe000f1b3c)


### SOLUTION 6
#### PLOTTING THE CHART OF CATEGORY BUY SALES USING SEABORN

- sns.boxplot(x=Grocery["Category"],y=Grocery["Sales"],data=Grocery,palette="coolwarm")
- plt.title("CATEGORY BY SALES",fontsize=15,fontweight="bold",fontstyle="italic",c="b")
- plt.xlabel("Category Name")
- plt.ylabel("Total Sales")
- plt.savefig("CatSales.png")
- plt.show()

![CatSales](https://github.com/user-attachments/assets/49fecf20-2757-41ac-8a75-473ca792a2a5)

### FINAL SOLUTION

#### PLOTTING THE CHARTS IN A SUBPLOTS

- fig,SuperMart=plt.subplots(nrows=3,ncols=2,figsize=(12,12))
- fig.suptitle("SUPERMART GROCERY SALES REPORT",fontweight="bold",c="#800080",fontsize=30)
- SuperMart[0,0].bar(Name,Number,color="red")
- sns.barplot(x=Top5["City"],y=Top5["Sales"],data=Top5,palette="summer",ax=SuperMart[0,1])
- SuperMart[1,0].plot(Name1,Number1,marker="o")
- SuperMart[1,1].barh(Name2,Number2,color="purple")
- SuperMart[2,0].pie(Number3,labels=Name3,autopct="%1.0f%%",shadow=True,explode=[0,0.1,0,0.1])
- sns.boxplot(x=Grocery["Category"],y=Grocery["Sales"],data=Grocery,palette="coolwarm",ax=SuperMart[2,1])
- SuperMart[0,0].set(title="SALES PER DAY")
- SuperMart[0,1].set(title="TOP 5 CITY BY SALES")
- SuperMart[1,0].set(title="DISCOUNT BY REGION")
- SuperMart[1,1].set(title="TOP 10 CUSTOMERS WITH THE HIGHEST PROFIT")
- SuperMart[2,0].set(title="SALES PER YEAR")
- SuperMart[2,1].set(title="CATEGORY BY SALES")
- plt.tight_layout()
- plt.savefig("SuperMart.png")
- plt.show()

![SuperMart](https://github.com/user-attachments/assets/cc31de95-3e16-416c-b3cc-55d8e5edffd3)
