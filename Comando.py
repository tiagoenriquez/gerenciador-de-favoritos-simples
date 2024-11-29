from Favorito import Favorito
import Controller


def inserir() -> None:
    print('\nInserir Favorito:\n')
    favorito = Favorito(input('Nome: '), input('URL: '))
    print('')
    Controller.inserir(favorito)

def listar(favoritos: list[Favorito]) -> None:
    print('\nFavoritos Registrados:\n')
    [print(f'  -> {favorito.nome}: {favorito.url}') for favorito in favoritos]
    print('')
    ler_comando()

def atualizar() -> None:
    print('\nAtualizar Favoritos:\n')
    favorito = Controller.procurar(input('Nome do favorito desatualizado: '))
    print('')
    Controller.atualizar(Favorito(input('Nome atualizado: '), input('URL atualizado: '), favorito.id))
    print('\n')
    ler_comando()

def excluir() -> None:
    print('\nExcluir Favoritos:\n')
    favorito = Controller.procurar(input('Nome do favorito a ser removido: '))
    print('')
    Controller.excluir(favorito.id)
    print('\n')
    ler_comando()

def abrir() -> None:
    print('\nAbrir Favoritos:\n')
    Controller.procurar(input('Nome do favorito: ')).abrir()
    sair()

def sair() -> None:
    print('\nEncerrando aplicação...\n')

def ajuda() -> None:
    print('\nComandos disponíveis:\n')
    print('inserir - insere favorito após informar nome e URL')
    print('listar - lista favoritos em ordem alfabética de nome')
    print('atualizar - atualiza/corrige favorito após informar nome salvo, nome correto e URL')
    print('excluir - exclui favorito após informar nome')
    print('abrir - abre favorito após informar nome')
    print('sair - sai da aplicação')
    print('ajuda - lista comandos disponíveis')
    print('\n')
    ler_comando()

def invalido() -> None:
    print('\nComando inválido\n')
    ler_comando()

def direcionar(comando: str) -> None:
    match comando:
        case 'inserir':
            inserir()
        case 'listar':
            Controller.listar()
        case 'atualizar':
            atualizar()
        case 'excluir':
            excluir()
        case 'abrir':
            abrir()
        case 'sair':
            sair()
        case 'ajuda':
            ajuda()
        case _:
            invalido()

def ler_comando() -> None:
    comando = input('Comando: ')
    direcionar(comando)