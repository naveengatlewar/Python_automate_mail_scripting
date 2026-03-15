# import sqlite3
# import matplotlib.pyplot as plt
# import pandas as pd
# import os


# def generate_revenue_chart():

#     conn = sqlite3.connect("../database/subscriptions.db")

#     query = """
#     SELECT DATE(date_created) as date,
#     SUM(amount) as revenue
#     FROM subscriptions
#     WHERE status='CHARGED'
#     GROUP BY DATE(date_created)
#     """

#     revenue_df = pd.read_sql(query, conn)

#     plt.plot(revenue_df["date"], revenue_df["revenue"])
#     plt.title("Daily Revenue")
#     plt.xlabel("Date")
#     plt.ylabel("Revenue")
#     plt.xticks(rotation=45)

#     os.makedirs("../charts", exist_ok=True)

#     plt.savefig("../charts/revenue_chart.png")

#     conn.close()



import sqlite3
import matplotlib.pyplot as plt
import pandas as pd
import os

def generate_revenue_chart():
    # 1. Get the absolute path of the directory where this script lives
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # 2. Fix the database path
    db_path = os.path.join(base_dir, "..", "database", "subscriptions.db")
    
    # 3. Fix the chart output folder and file paths
    charts_dir = os.path.join(base_dir, "..", "charts")
    chart_file = os.path.join(charts_dir, "revenue_chart.png")

    # Use the absolute db_path
    conn = sqlite3.connect(db_path)

    query = """
    SELECT DATE(date_created) as date,
    SUM(amount) as revenue
    FROM subscriptions
    WHERE status='CHARGED'
    GROUP BY DATE(date_created)
    """

    revenue_df = pd.read_sql(query, conn)

    plt.figure(figsize=(10, 6)) # Good practice to set size
    plt.plot(revenue_df["date"], revenue_df["revenue"])
    plt.title("Daily Revenue")
    plt.xlabel("Date")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)
    plt.tight_layout() # Prevents labels from getting cut off

    # 4. Use absolute paths for making directory and saving
    os.makedirs(charts_dir, exist_ok=True)
    plt.savefig(chart_file)

    conn.close()
    print(f"Chart successfully saved to: {chart_file}")