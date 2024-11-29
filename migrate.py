from connection import con


def migrate() -> None:
    with con:
        query = 'CREATE TABLE IF NOT EXISTS favoritos ('
        query += 'id INTEGER PRIMARY KEY AUTOINCREMENT, '
        query += 'nome VARCHAR (31) NOT NULL UNIQUE, '
        query += 'url VARCHAR (255) NOT NULL UNIQUE'
        query += ')'
        con.execute(query)