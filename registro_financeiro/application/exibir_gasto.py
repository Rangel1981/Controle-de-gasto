from registro_financeiro.infrastructure.repository import RepositorioFinanceiro


class ExibirGasto:
    def __init__(self, repository: RepositorioFinanceiro):
        self.repository = repository

    def executar(self) -> None:
        dados = self.repository.mostrar_registro()
        return dados
