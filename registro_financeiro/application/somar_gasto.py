from decimal import Decimal

from registro_financeiro.infrastructure.repository import RepositorioFinanceiro


class SomarGastos:
    def __init__(self, repository: RepositorioFinanceiro):
        self.repository = repository

    def executar_soma(self):
        registros = self.repository.mostar_registro()

        total = sum(Decimal(str(registro["valor"])) for registro in registros)
        return total
