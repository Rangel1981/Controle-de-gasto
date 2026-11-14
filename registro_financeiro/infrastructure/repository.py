from pathlib import Path
import json
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

        self.arquivo.write_text(
            json.dumps(dados_atuais, indent=4, ensure_ascii=False), encoding="utf-8"
        )

    def _ler_arquivo(self) -> list[dict]:
        if not self.arquivo.exists():
            return []
        conteudo = self.arquivo.read_text(encoding="utf-8")
        return json.loads(conteudo) if conteudo else []
