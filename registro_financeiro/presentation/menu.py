from registro_financeiro.application.registrar_gasto import RegistrarGastoUser
from registro_financeiro.application.exibir_gasto import ExibirGasto
from registro_financeiro.application.somar_gasto import SomarGastos
from registro_financeiro.application.delete_gasto import DeleteGasto


class MenuCLI:
    def __init__(
        self,
        resgistro_gasto_use: RegistrarGastoUser,
        exibir: ExibirGasto,
        somar: SomarGastos,
        delete: DeleteGasto,
    ):
        self.registro_gasto_use = resgistro_gasto_use
        self.exibir = exibir
        self.somar = somar
        self.delete = delete

    def iniciar(self) -> None:
        while True:
            print("\n--- REGISTRO DE GASTO ---")
            print("1. Registrar Gasto")
            print("2. Exibir Registros")
            print("3. Somar Gastos")
            print("4. Deletar Registro e Gasto")
            print("0. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.registro_gasto_use._fluxo_registro()
                print(f"o {self.registro_gasto_use} foi registrado com sucesso!")

            elif opcao == "2":
                self.exibir.executar()

            elif opcao == "3":
                total = self.somar.executar_soma()
                print(f"\nTotal de gastos: R$ {total:.2f}")

            elif opcao == "4":
                self.delete.deletar_registro()
                print(f"O registro {self.delete} foi deletado com sucesso!")

            elif opcao == "0":
                print("Saindo do programa...")
                break

            else:
                print("Opção inválida!")
