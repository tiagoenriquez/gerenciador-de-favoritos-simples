from Favorito import Favorito
import Dao


def ler_comando() -> None:
    from Comando import ler_comando
    ler_comando()

def inserir(favorito: Favorito) -> None:
    from Comando import ler_comando
    Dao.inserir(favorito)
    ler_comando()

def listar() -> list[Favorito]:
    from Comando import listar
    listar(Dao.listar())

def procurar(nome: str) -> Favorito:
    return Dao.procurar(nome)

def atualizar(favorito: Favorito) -> None:
    from Comando import ler_comando
    Dao.atualizar(favorito)
    ler_comando()

def excluir(id: int) -> None:
    from Comando import ler_comando
    Dao.excluir(id)
    ler_comando()