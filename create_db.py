import sqlite3

# Connect to (or create) the database
conn = sqlite3.connect('fantasy.db')
cursor = conn.cursor()

# 1. Create 'players' table - Primary list for UI population
cursor.execute('''
CREATE TABLE IF NOT EXISTS players (
    player TEXT PRIMARY KEY,
    value INTEGER,
    ctg TEXT
)''')

# 2. Create 'stats' table - Historical performance data
cursor.execute('''
CREATE TABLE IF NOT EXISTS stats (
    player TEXT PRIMARY KEY,
    matches INTEGER,
    runs INTEGER,
    hundreds INTEGER,
    fifties INTEGER,
    value INTEGER,
    ctg TEXT,
    FOREIGN KEY (player) REFERENCES players (player)
)''')

# 3. Create 'match' table - Current match data for score calculation
cursor.execute('''
CREATE TABLE IF NOT EXISTS match (
    player TEXT PRIMARY KEY,
    scored INTEGER,
    faced INTEGER,
    fours INTEGER,
    sixes INTEGER,
    bowled INTEGER,
    maiden INTEGER,
    given INTEGER,
    wkts INTEGER,
    catches INTEGER,
    stumping INTEGER,
    ro INTEGER
)''')

# 4. Create 'teams' table - To save user-created teams
cursor.execute('''
CREATE TABLE IF NOT EXISTS teams (
    name TEXT,
    players TEXT,
    value INTEGER
)''')

# --- DATA INSERTION ---

# Data for players and stats (Extracted from document source: 463)
player_data = [
    ('Kohli', 120, 'BAT', 189, 8257, 28, 43),
    ('Yuvraj', 100, 'BAT', 86, 3589, 10, 21),
    ('Rahane', 100, 'BAT', 158, 5435, 11, 31),
    ('Dhawan', 85, 'BAT', 25, 565, 2, 1),
    ('Dhoni', 75, 'WK', 78, 2573, 3, 19),
    ('Axar', 100, 'BWL', 67, 208, 0, 0),
    ('Pandya', 75, 'AR', 70, 77, 0, 0),
    ('Jadeja', 85, 'AR', 16, 1, 0, 0),
    ('Kedar', 90, 'BAT', 111, 675, 0, 1),
    ('Ashwin', 100, 'AR', 136, 1914, 0, 10),
    ('Umesh', 110, 'BWL', 296, 9496, 10, 64),
    ('Bumrah', 60, 'BWL', 73, 1365, 0, 0),
    ('Bhuwaneshwar', 75, 'BWL', 17, 289, 0, 0),
    ('Rohit', 85, 'BAT', 304, 8701, 14, 40),
    ('Kartick', 75, 'WK', 11, 111, 0, 0)
]

for p in player_data:
    cursor.execute("INSERT OR REPLACE INTO players VALUES (?,?,?)", (p[0], p[1], p[2]))
    cursor.execute("INSERT OR REPLACE INTO stats VALUES (?,?,?,?,?,?,?)", (p[0], p[3], p[4], p[5], p[6], p[1], p[2]))

# Current Match Data for score calculation (Extracted from source: 463)
match_stats = [
    ('Kohli', 102, 98, 8, 2, 0, 0, 0, 0, 0, 0, 1),
    ('Yuvraj', 12, 20, 1, 0, 48, 0, 36, 1, 0, 0, 0),
    ('Rahane', 49, 75, 3, 0, 0, 0, 0, 0, 1, 0, 0),
    ('Dhawan', 32, 35, 4, 0, 0, 0, 0, 0, 0, 0, 0),
    ('Dhoni', 56, 45, 3, 1, 0, 0, 0, 0, 3, 2, 0),
    ('Axar', 8, 4, 2, 0, 48, 0, 35, 1, 0, 0, 0),
    ('Pandya', 42, 36, 3, 3, 30, 0, 25, 0, 1, 0, 0),
    ('Jadeja', 18, 10, 1, 1, 60, 0, 50, 2, 1, 0, 1),
    ('Kedar', 65, 60, 7, 0, 24, 0, 24, 0, 0, 0, 0),
    ('Ashwin', 23, 42, 3, 0, 60, 0, 45, 2, 0, 0, 0),
    ('Umesh', 0, 0, 0, 0, 54, 0, 50, 1, 1, 0, 0),
    ('Bumrah', 0, 0, 0, 0, 60, 0, 49, 1, 0, 0, 0),
    ('Bhuwaneshwar', 15, 12, 2, 0, 60, 0, 46, 2, 0, 0, 0),
    ('Rohit', 46, 65, 5, 0, 0, 0, 0, 0, 1, 0, 0),
    ('Kartick', 29, 42, 3, 0, 0, 0, 0, 0, 2, 0, 1)
]

cursor.executemany("INSERT OR REPLACE INTO match VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", match_stats)

conn.commit()
conn.close()
print("fantasy.db has been created and populated successfully!")