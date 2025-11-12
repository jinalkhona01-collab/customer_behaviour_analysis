# Loading the dataset using pandas

import pandas as pd

def clean_customer_data(filepath):
  df = pd.read_csv(r'D:\customer_shopping_behavior\customer_shopping_behavior.csv')
  print(df.head())
  print(df.info())
#Summarizing the dataset
  print(df.describe(include='all'))

# Checking for missing values
  missing_values = df.isnull().sum()
#print("Missing values in each column:\n", missing_values)

# Imputing missing values in Review Rating column with the median rating of the product category 
  df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))
#print("Missing values after imputation:\n", df.isnull().sum())

# Renaming columns according to snake casing for better readability and documentation
  df.columns = df.columns.str.lower()
  df.columns = df.columns.str.replace(' ', '_')
  df = df.rename(columns={'purchase_amount_(usd)': 'purchase_amount'})
  df.columns

# create a new column age_group
  labels = ['Young Adult', 'Adult', 'Middle Aged', 'Senior']
  df['age_group'] = pd.qcut(df['age'], q=4, labels=labels)
  df[['age','age_group']].head(10)

# create new column purchase_frequency_days
  frequency_mapping = {'Fortnightly': 14,
    'Weekly': 7,
    'Monthly': 30,
    'Quarterly': 90,
    'Bi-Weekly': 14,
    'Annually': 365,
    'Every 3 Months': 90}

  df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)
  df[['frequency_of_purchases', 'purchase_frequency_days']].head(10)

  df[['discount_applied','promo_code_used']].head(10)
  (df['discount_applied'] == df['promo_code_used']).all()

# Dropping promo code used column

  df = df.drop('promo_code_used', axis=1)
  df.columns
  print("✅ Data cleaning complete.")
  return df


