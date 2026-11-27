import json

from registro_financeiro.domain.entities import ControleFinanceiro
from registro_financeiro.infrastructure.repository import RepositorioFinanceiro
from datetime import date, datetime
from decimal import Decimal, InvalidOperation


class RegistrarGastoUser:
    def __init__(self, repository: RepositorioFinanceiro):
        self.repository = repository

    def executar(self, titulo: str, valor: Decimal, descricao: str, data: date):
        novo_registro = ControleFinanceiro(
            titulo=titulo, valor=valor, descricao=descricao, data=data
        )
        self.repository.salvar_registro(novo_registro)
        return novo_registro

    def _fluxo_registro(self) -> None:
        titulo = input("Digite o titulo do gasto: ")
        try:
            try:
                valor = Decimal(input("Valor gastado: ").replace(",", "."))
                descricao = input("Descreva o que gastou: ")
                texto = input("Digite uma data (dd/mm/aaaa): ")
                data = datetime.strptime(texto, "%d/%m/%Y").date()
                gasto_salvo = self.registro_gasto_use.executar(
                    titulo, valor, descricao, data
                )
                print(
                    f"Sucesso! o {gasto_salvo.titulo} foi registrado com os seguintes valores: {gasto_salvo.valor} | {gasto_salvo.descricao} | {gasto_salvo.data}"
                )
            except ValueError as erro:
                print(f"Erro ao registrar {erro}")
        except InvalidOperation as erro:
            print(f"Erro ao registrar {erro}")

    def _exibir_registro(self):
        with open("financeiro.json", "r", encoding="utf-8") as f:
            dados = json.load(f)
            print(dados)

    def _exibir_soma_gasto(self):
        with open("financeiro.json", "r", encoding="utf-8") as f:
            total = sum(Decimal(linha.strip()) for linha in f if linha.strip())
            print(total)
