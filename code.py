import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets
customers = pd.read_csv('/content/Customers.csv')
products = pd.read_csv('/content/Products.csv')
transactions = pd.read_csv('/content/Transactions.csv')

# Explore Customers.csv
def explore_customers(customers):
    print("Customers Dataset Info:")
    print(customers.info())
    print("\nBasic Statistics:")
    print(customers.describe(include='all'))
    print("\nNull Values:")
    print(customers.isnull().sum())
    
    # Visualize Region Distribution
    plt.figure(figsize=(8, 5))
    sns.countplot(x='Region', data=customers, palette='viridis')
    plt.title('Customer Count by Region')
    plt.xticks(rotation=45)
    plt.show()

# Explore Products.csv
def explore_products(products):
    print("Products Dataset Info:")
    print(products.info())
    print("\nBasic Statistics:")
    print(products.describe(include='all'))
    print("\nNull Values:")
    print(products.isnull().sum())
    
    # Visualize Price Distribution
    plt.figure(figsize=(8, 5))
    sns.histplot(products['Price'], kde=True, bins=30, color='blue')
    plt.title('Product Price Distribution')
    plt.xlabel('Price')
    plt.show()

# Explore Transactions.csv
def explore_transactions(transactions):
    print("Transactions Dataset Info:")
    print(transactions.info())
    print("\nBasic Statistics:")
    print(transactions.describe(include='all'))
    print("\nNull Values:")
    print(transactions.isnull().sum())

    # Visualize Total Value Distribution
    plt.figure(figsize=(8, 5))
    sns.histplot(transactions['TotalValue'], kde=True, bins=30, color='green')
    plt.title('Transaction Total Value Distribution')
    plt.xlabel('Total Value')
    plt.show()

# Combine and Analyze Data
def combined_analysis(customers, products, transactions):
    # Merge datasets
    transactions_merged = transactions.merge(customers, on='CustomerID').merge(products, on='ProductID')
    
    # Top 10 Products by Sales
    top_products = transactions_merged.groupby('ProductName')['TotalValue'].sum().nlargest(10)
    print("Top 10 Products by Sales:\n", top_products)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_products.values, y=top_products.index, palette='mako')
    plt.title('Top 10 Products by Sales')
    plt.xlabel('Total Sales Value')
    plt.show()

    # Sales by Region
    region_sales = transactions_merged.groupby('Region')['TotalValue'].sum()
    print("Sales by Region:\n", region_sales)

    plt.figure(figsize=(8, 5))
    sns.barplot(x=region_sales.index, y=region_sales.values, palette='cool')
    plt.title('Sales by Region')
    plt.ylabel('Total Sales Value')
    plt.xticks(rotation=45)
    plt.show()

# Call Functions
explore_customers(customers)
explore_products(products)
explore_transactions(transactions)
combined_analysis(customers, products, transactions)
