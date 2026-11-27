from registro_financeiro.infrastructure.repository import RepositorioFinanceiro


class DeleteGasto:
    def __init__(self, repository: RepositorioFinanceiro):
        self.repository = repository

    def deletar_registro(self, titulo: str) -> bool:
        return self.repository.remover_registro(titulo)
