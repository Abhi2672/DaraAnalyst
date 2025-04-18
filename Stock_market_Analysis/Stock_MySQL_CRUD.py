import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
import mysql.connector


DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'root'
DB_NAME = 'stock_data'

def get_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS stock_prices (
        id INT AUTO_INCREMENT PRIMARY KEY,
        ticker VARCHAR(10),
        date DATE,
        open FLOAT,
        high FLOAT,
        low FLOAT,
        close FLOAT,
        volume BIGINT
    )
    """)
    conn.commit()
    cursor.close()
    conn.close()
    print(" Table 'stock_prices' created.")

def fetch_and_store_data(ticker_symbol, start_date, end_date):
    df = yf.download(ticker_symbol, start=start_date, end=end_date, auto_adjust=False)
    df = df.reset_index()

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = ['_'.join(col).strip() if isinstance(col, tuple) else col for col in df.columns]

    column_map = {}
    for col in df.columns:
        if 'Date' in col:
            column_map[col] = 'Date'
        elif 'Open' in col:
            column_map[col] = 'Open'
        elif 'High' in col:
            column_map[col] = 'High'
        elif 'Low' in col:
            column_map[col] = 'Low'
        elif 'Close' in col and 'Adj' not in col:
            column_map[col] = 'Close'
        elif 'Volume' in col:
            column_map[col] = 'Volume'
    df.rename(columns=column_map, inplace=True)

    conn = get_connection()
    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute("""
        INSERT INTO stock_prices (ticker, date, open, high, low, close, volume)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            ticker_symbol,
            pd.to_datetime(row['Date']).date(),
            float(row['Open']),
            float(row['High']),
            float(row['Low']),
            float(row['Close']),
            int(row['Volume'])
        ))

    conn.commit()
    cursor.close()
    conn.close()
    print(f" Data for {ticker_symbol} inserted into MySQL.")

def read_stock_data(ticker_symbol):
    conn = get_connection()
    df = pd.read_sql(f"SELECT * FROM stock_prices WHERE ticker = %s ORDER BY date DESC", conn, params=(ticker_symbol,))
    conn.close()
    print(df)

def update_close_price(ticker_symbol, date, new_close):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    UPDATE stock_prices SET close = %s WHERE ticker = %s AND date = %s
    """, (new_close, ticker_symbol, date))
    conn.commit()
    cursor.close()
    conn.close()
    print(f" Close price updated for {ticker_symbol} on {date}.")

def delete_stock_data(ticker_symbol):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM stock_prices WHERE ticker = %s", (ticker_symbol,))
    conn.commit()
    cursor.close()
    conn.close()
    print(f" Data for {ticker_symbol} deleted.")

def plot_closing_price(ticker_symbol):
    conn = get_connection()
    df = pd.read_sql(f"SELECT date, close FROM stock_prices WHERE ticker = %s ORDER BY date", conn, params=(ticker_symbol,))
    conn.close()

    plt.figure(figsize=(10, 5))
    sns.lineplot(x='date', y='close', data=df, marker='o')
    plt.title(f"Closing Price of {ticker_symbol}")
    plt.xlabel("Date")
    plt.ylabel("Close Price")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    plt.close()

def plot_volume(ticker_symbol):
    conn = get_connection()
    df = pd.read_sql(f"SELECT date, volume FROM stock_prices WHERE ticker = %s ORDER BY date", conn, params=(ticker_symbol,))
    conn.close()

    plt.figure(figsize=(10, 5))
    sns.barplot(x='date', y='volume', data=df)
    plt.title(f"Volume Traded - {ticker_symbol}")
    plt.xlabel("Date")
    plt.ylabel("Volume")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    plt.close()

def plot_moving_average(ticker_symbol, window=5):
    conn = get_connection()
    df = pd.read_sql(f"SELECT date, close FROM stock_prices WHERE ticker = %s ORDER BY date", conn, params=(ticker_symbol,))
    conn.close()

    df['moving_avg'] = df['close'].rolling(window=window).mean()

    plt.figure(figsize=(10, 5))
    sns.lineplot(x='date', y='close', data=df, label='Close')
    sns.lineplot(x='date', y='moving_avg', data=df, label=f'{window}-Day MA')
    plt.title(f"{ticker_symbol} - Closing Price & {window}-Day Moving Average")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.grid(True)
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    plt.close()

def plot_daily_returns(ticker_symbol):
    conn = get_connection()
    df = pd.read_sql(f"SELECT date, close FROM stock_prices WHERE ticker = %s ORDER BY date", conn, params=(ticker_symbol,))
    conn.close()

    df['daily_return'] = df['close'].pct_change()

    plt.figure(figsize=(10, 5))
    sns.lineplot(x='date', y='daily_return', data=df)
    plt.title(f"{ticker_symbol} - Daily Returns")
    plt.xlabel("Date")
    plt.ylabel("Daily Return")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    plt.close()



def menu():
    while True:
        print("\n📊 Stock Market Menu")
        print("1. Fetch and Store Stock Data")
        print("2. Show Latest Stock Data")
        print("3. Update Close Price")
        print("4. Delete Stock Data")
        print("5. Plot Closing Price")
        print("6. Plot Volume")
        print("7. Plot Moving Average")
        print("8. Plot Daily Returns")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == "1":
            ticker = input("Enter Ticker Symbol (e.g., AAPL): ")
            start = input("Enter Start Date (YYYY-MM-DD): ")
            end = input("Enter End Date (YYYY-MM-DD): ")
            fetch_and_store_data(ticker, start, end)

        elif choice == "2":
            ticker = input("Enter Ticker Symbol: ")
            read_stock_data(ticker)

        elif choice == "3":
            ticker = input("Enter Ticker Symbol: ")
            date = input("Enter Date (YYYY-MM-DD): ")
            new_close = float(input("Enter New Close Price: "))
            update_close_price(ticker, date, new_close)

        elif choice == "4":
            ticker = input("Enter Ticker Symbol to Delete: ")
            delete_stock_data(ticker)

        elif choice == "5":
            ticker = input("Enter Ticker Symbol: ")
            plot_closing_price(ticker)

        elif choice == "6":
            ticker = input("Enter Ticker Symbol: ")
            plot_volume(ticker)

        elif choice == "7":
            ticker = input("Enter Ticker Symbol: ")
            window = int(input("Enter Moving Average Window (e.g., 5): "))
            plot_moving_average(ticker, window)

        elif choice == "8":
            ticker = input("Enter Ticker Symbol: ")
            plot_daily_returns(ticker)

        elif choice == "9":
            print("👋 Exiting. Goodbye!")
            break

        else:
            print(" Invalid option. Please try again.")

if __name__ == "__main__":
    create_table()
    menu()
