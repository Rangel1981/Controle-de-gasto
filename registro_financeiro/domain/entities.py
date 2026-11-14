from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass
class ControleFinanceiro:
    titulo: str
    valor: Decimal
    descricao: str
    data: date

    def __post_init__(self):
        if not self.titulo.strip():
            raise ValueError("O titulo não pode ser vazio.")
        if self.valor <= 0:
            raise ValueError("O gasto não pode ser menor ou igual a zero.")
