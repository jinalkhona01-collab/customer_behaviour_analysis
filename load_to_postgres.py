from sqlalchemy import create_engine
from urllib.parse import quote_plus
from customer_shopping_behaviour import clean_customer_data  # ✅ import function from your other file

# Step 1: Clean and prepare data
filepath = r"D:\customer_shopping_behavior\customer_shopping_behavior.csv"
df = clean_customer_data(filepath)  # ✅ df is now defined

# Step 2: Connect to PostgreSQL
# Replace placeholders with your actual details
username = "postgres"      # default user
password = quote_plus("Jay@2703") # the password you set during installation
host = "localhost"         # if running locally
port = "5432"              # default PostgreSQL port
database = "customer_behaviour"    # the database you created in pgAdmin

# Create engine
engine = create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}")

# STep 3: Upload DataFrame
table_name = "customer"
df.to_sql(table_name, engine, if_exists="replace", index=False)

print(f"✅ Data successfully loaded into table '{table_name}' in database '{database}'.")


