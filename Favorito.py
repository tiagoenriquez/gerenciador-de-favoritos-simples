import webbrowser


class Favorito:
    def __init__(self, nome: str, url: str, id = 0) -> None:
        self.nome = nome
        self.url = url
        self.id = id
    
    def abrir(self) -> None:
        webbrowser.open(self.url)