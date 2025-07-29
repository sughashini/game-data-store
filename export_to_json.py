import sqlite3
import json

# Step 1: Connect to your database
conn = sqlite3.connect("games.db")
cursor = conn.cursor()

# Step 2: Run SQL query to filter games released after 2014
cursor.execute('''
    SELECT game_name, genre, platform, release_year, user_rating
    FROM games
    WHERE release_year > 2014
''')

# Step 3: Fetch results
rows = cursor.fetchall()
columns = [description[0] for description in cursor.description]

# Step 4: Convert to list of dictionaries
filtered_games = [dict(zip(columns, row)) for row in rows]

# Step 5: Save to a JSON file
with open("filtered_games.json", "w", encoding="utf-8") as f:
    json.dump(filtered_games, f, indent=4)

# Step 6: Close the database connection
conn.close()

print("✅ Games released after 2014 have been saved to filtered_games.json")
