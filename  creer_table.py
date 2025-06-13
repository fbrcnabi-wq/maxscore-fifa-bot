import sqlite3

# Connexion à la base de données
conn = sqlite3.connect("scores.db")
cur = conn.cursor()

# Création de la table si elle n'existe pas déjà
cur.execute("""
    CREATE TABLE IF NOT EXISTS matchs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        equipe1 TEXT,
        equipe2 TEXT,
        score1 INTEGER,
        score2 INTEGER
    )
""")

conn.commit()
conn.close()

print("Table 'matchs' créée avec succès.")