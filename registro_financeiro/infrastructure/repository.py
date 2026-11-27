from decimal import Decimal
import json
from pathlib import Path
from registro_financeiro.domain.entities import ControleFinanceiro


class RepositorioFinanceiro:

    def __init__(self, caminho_arquivo: str = "financeiro.json"):
        self.arquivo = Path(caminho_arquivo)

    def salvar_registro(self, registro: ControleFinanceiro) -> None:
        dados_atuais = self._ler_arquivo()
        dados_atuais.append(
            {
                "titulo": registro.titulo,
                "valor": str(registro.valor),
                "descricao": registro.descricao,
                "data": registro.data.isoformat(),
            }
        )
        self._salvar_arquivo(dados_atuais)

    def _ler_arquivo(self) -> list[dict]:
        if not self.arquivo.exists():
            return []
        conteudo = self.arquivo.read_text(encoding="utf-8")
        return json.loads(conteudo) if conteudo else []

    def _salvar_arquivo(self, dados: list[dict]) -> None:
        self.arquivo.write_text(
            json.dumps(dados, indent=4, ensure_ascii=False), encoding="utf-8"
        )

    def mostrar_registro(self) -> list[dict]:
        return self._ler_arquivo()

    def remover_registro(self, titulo: str) -> bool:
        dados = self._ler_arquivo()

        if not dados:
            return False

        tamanho_original = len(dados)

        dados_atualizados = [item for item in dados if item.get("titulo") != titulo]

        if len(dados_atualizados) < tamanho_original:
            self._salvar_arquivo(dados_atualizados)
            return True

        return False
