import pandas as pd

df = pd.read_excel("project18.xlsx")
print(df.head())

print(df.info())
print(df.isnull().sum())

df["Review Rating"] = df.groupby("Category")["Review Rating"].transform(
    lambda x: x.fillna(x.median())
)
print(df.isnull().sum())

df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(" ", "_")
print(df.columns)


# create new column age_group
labels = ['young_adult','adult','middle_aged','senior']
df['age_group']=pd.qcut(df['age'],q=4,labels=labels)
print(df[['age','age_group']])

#create_column_purchase_frequency_days

frequency_mapping = {
    'Fortnightly': 14,
    'Weekly': 7,
    'Monthly': 30,
    'Quarterly': 90,
    'Bi-Weekly': 14,
    'Annually': 365,
    'Every 3 Months': 90
}

df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)

print(df[['purchase_frequency_days','frequency_of_purchases']].head(10))

print(df[['discount_applied','promo_code_used']].head(10))

print(df['discount_applied']==df['promo_code_used'].all())

df=df.drop('promo_code_used',axis=1)

print(df.columns)


from sqlalchemy import create_engine
import pandas as pd

# Database connection string
db_string = (
    "postgresql://postgres:7876612895@localhost:5432/customer_behavior"
)
engine = create_engine(db_string)



# Load data into SQL table
df.to_sql("sales_data", engine, if_exists="replace", index=False)