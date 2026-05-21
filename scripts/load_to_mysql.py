# load_to_mysql.py — Load supply chain data and results to MySQL

import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()

DB_URL = (
    f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}"
    f"@{os.getenv('MYSQL_HOST')}:{os.getenv('MYSQL_PORT')}/{os.getenv('MYSQL_DATABASE')}"
)

DATA_PATH = Path(__file__).parent.parent / 'data' / 'processed'

def create_database(engine):
    with engine.connect() as conn:
        conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {os.getenv('MYSQL_DATABASE')}"))
        conn.commit()
    print(f"✅ Database '{os.getenv('MYSQL_DATABASE')}' ready")

def load_table(df, table_name, engine):
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
    print(f"✅ {table_name:35s} → {len(df):>7,} rows loaded")

def main():
    print("Connecting to MySQL...")
    base_engine = create_engine(
        f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}"
        f"@{os.getenv('MYSQL_HOST')}:{os.getenv('MYSQL_PORT')}"
    )
    create_database(base_engine)

    engine = create_engine(DB_URL)
    print("Loading tables...\n")

    tables = {
        'supply_chain_clean'       : 'supply_chain_clean.csv',
        'market_summary'           : 'market_summary.csv',
        'category_summary'         : 'category_summary.csv',
        'shipping_summary'         : 'shipping_summary.csv',
        'segment_summary'          : 'segment_summary.csv',
        'delivery_risk_predictions': 'delivery_risk_predictions.csv',
        'delivery_risk_metrics'    : 'delivery_risk_metrics.csv',
        'category_profitability'   : 'category_profitability.csv',
        'loss_making_orders'       : 'loss_making_orders.csv',
        'inventory_plan'           : 'inventory_plan.csv',
        'forecast_metrics'         : 'forecast_metrics.csv',
        'demand_forecasts'         : 'demand_forecasts.csv',
    }

    for table_name, filename in tables.items():
        filepath = DATA_PATH / filename
        if filepath.exists():
            df = pd.read_csv(filepath)
            load_table(df, table_name, engine)
        else:
            print(f"⚠️  {filename} not found — skipping")

    print("\n✅ All tables loaded to MySQL")
    print(f"   Database: {os.getenv('MYSQL_DATABASE')}")
    print(f"   Host:     {os.getenv('MYSQL_HOST')}")

if __name__ == '__main__':
    main()