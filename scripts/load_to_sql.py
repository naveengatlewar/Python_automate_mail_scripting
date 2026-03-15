# import sqlite3
# import pandas as pd

# def load_to_sql(df):
#     conn = sqlite3.connect("../database/subscriptions.db")
#     df.to_sql("subscriptions", conn, if_exists="replace", index=False)
#     conn.close()


import sqlite3
import pandas as pd
import os

def load_to_sql(df):
    # 1. Get the directory where THIS script (load_to_sql.py) is stored
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 2. Build the path: Go up one level (..) then into the 'database' folder
    db_path = os.path.join(base_dir, "..", "database", "subscriptions.db")
    
    # 3. Connect using the full path
    conn = sqlite3.connect(db_path)
    df.to_sql("subscriptions", conn, if_exists="replace", index=False)
    conn.close()
    print(f"Successfully loaded data to {db_path}")