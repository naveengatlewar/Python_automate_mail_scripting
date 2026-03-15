from load import load_data
from clean import clean_data
from load_to_sql import load_to_sql
from analysis import generate_revenue_chart
from send_email import send_report

df = load_data()

df = clean_data(df)

load_to_sql(df)

generate_revenue_chart()    

send_report()

print(df.head())