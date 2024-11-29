from Favorito import Favorito
from connection import con


def inserir(favorito: Favorito) -> None:
    data = [favorito.nome, favorito.url]
    with con:
        con.execute('INSERT INTO favoritos (nome, url) VALUES (?, ?)', data)
        con.commit()

def listar() -> list[Favorito]:
    favoritos: list[Favorito] = []
    with con:
        cur = con.execute('SELECT * FROM favoritos ORDER BY nome')
        result = cur.fetchall()
        for row in result:
            favoritos.append(Favorito(row[1], row[2], row[0]))
    return favoritos

def procurar(nome: str) -> Favorito:
    data = [nome]
    with con:
        cur = con.execute('SELECT * FROM favoritos WHERE nome = ?', data)
        result = cur.fetchone()
        return Favorito(result[1], result[2], result[0])

def atualizar(favorito: Favorito) -> None:
    data = [favorito.nome, favorito.url, favorito.id]
    with con:
        con.execute('UPDATE favoritos SET nome = ?, url = ? WHERE id = ?', data)
        con.commit()

def excluir(id: int) -> None:
    data = [id]
    with con:
        con.execute('DELETE FROM favoritos WHERE id = ?', data)
        con.commit()