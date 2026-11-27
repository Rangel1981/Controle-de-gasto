from registro_financeiro.application.delete_gasto import DeleteGasto
from registro_financeiro.application.exibir_gasto import ExibirGasto
from registro_financeiro.application.registrar_gasto import RegistrarGastoUser
from registro_financeiro.application.somar_gasto import SomarGastos
from registro_financeiro.infrastructure.repository import RepositorioFinanceiro
from registro_financeiro.presentation.menu import MenuCLI


def main() -> None:

    repositorio = RepositorioFinanceiro("financeiro.json")

    registro_gasto = RegistrarGastoUser(repositorio)
    exibir_gasto = ExibirGasto(repositorio)
    somar_gastos = SomarGastos(repositorio)
    delete_gasto = DeleteGasto(repositorio)

    menu = MenuCLI(
        resgistro_gasto_use=registro_gasto,
        exibir=exibir_gasto,
        somar=somar_gastos,
        delete=delete_gasto,
    )

    menu.iniciar()


if __name__ == "__main__":
    main()
