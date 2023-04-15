import sqlite3

# Verbinding maken met de database
conn = sqlite3.connect('database.db')

# Cursor-object maken
cur = conn.cursor()

# SQL-queries uitvoeren om tabellen aan te maken
cur.execute('''
CREATE TABLE `users` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `email` TEXT NOT NULL UNIQUE,
    `password` TEXT NOT NULL
)
''')

cur.execute('''
CREATE TABLE `movies` (
    `id` INTEGER NOT NULL UNIQUE PRIMARY KEY,
    `title` TEXT NOT NULL,
    `director_id` TEXT NOT NULL,
    `year_released` INTEGER NOT NULL
)
''')

cur.execute('''
CREATE TABLE `actors` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `first_name` TEXT NOT NULL,
    `last_name` TEXT NOT NULL
)
''')

cur.execute('''
CREATE TABLE `role` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `movie_id` TEXT NOT NULL,
    `actor_id` TEXT NOT NULL,
    `character_name` TEXT NOT NULL
)
''')

cur.execute('''
CREATE TABLE `directors` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `first_name` TEXT NOT NULL,
    `last_name` TEXT NOT NULL
)
''')

# Wijzigingen opslaan en verbinding sluiten
conn.commit()
conn.close()
