from registro_financeiro.domain.entities import ControleFinanceiro
from infrastructure.repository import RepositorioFinanceiro
from datetime import date
from decimal import Decimal


class RegistrarGastoUser:
    def __init__(self, repository: RepositorioFinanceiro):
        self.repository = repository

    def executar(self, titulo: str, valor: Decimal, descricao: str, data: date):
        novo_registro = ControleFinanceiro(
            titulo=titulo, valor=valor, descricao=descricao, data=data
        )
        self.repository.salvar_registro(novo_registro)
        return novo_registro
