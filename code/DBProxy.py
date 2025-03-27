import sqlite3

class DBProxy:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)

        self.connection.execute('''
                                CREATE TABLE IF NOT EXISTS dados(
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                score INTEGER NOT NULL,
                                date TEXT NOT NULL  
                                )''')
        self.connection.commit()

    def save(self, score_dict: dict):
        self.connection.execute('INSERT INTO dados (score, date) VALUES (:score, :date)', score_dict)
        self.connection.commit()

    def retrieve_top10(self) -> list:
        return self.connection.execute('SELECT * FROM dados ORDER BY score DESC LIMIT 3').fetchall()

    def close(self):
        return self.connection.close()