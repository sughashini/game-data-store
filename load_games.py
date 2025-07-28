import csv
import sqlite3

csv_file = "games_dataset.csv"
data = []

# Step 1: Read the CSV
with open(csv_file, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

# Step 2: Connect to SQLite
conn = sqlite3.connect("games.db")
cursor = conn.cursor()

# Step 3: Create Table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS games (
        game_name TEXT,
        genre TEXT,
        platform TEXT,
        release_year INTEGER,
        user_rating REAL
    )
''')

# Step 4: Insert Data
for row in data:
    try:
        cursor.execute('''
            INSERT INTO games (game_name, genre, platform, release_year, user_rating)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            row['Game Name'],
            row['Genre'],
            row['Platform'],
            int(float(row['Release Year'])),
            float(row['User Rating'])
        ))
    except Exception as e:
        print(f"Error in row: {row.get('Game Name')}, error: {e}")

conn.commit()
conn.close()
print("✅ Done! Data stored in games.db")
