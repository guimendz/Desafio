print("\n| Bem-vindo! Para iniciarmos seu cadastro, escolha uma das opções abaixo. |")

class Usuario:
    def __init__(self,nome, cpf, perfil, ativo=True):
        self.nome = nome
        self.cpf = cpf
        self.perfil = perfil
        self.ativo = ativo
        
class Empresa:
    def __init__(self, nome_fantasia, razao_social, cnpj, endereco, tipo_da_empresa, socios):
        self.nome_fantasia = nome_fantasia
        self.razao_social = razao_social
        self.cnpj = cnpj
        self.endereco = endereco
        self.tipo = tipo_da_empresa
        self.socios = socios
        self.usuarios = []
    
    def adicionar_usuario(self, usuario):
        if any(u.cpf == usuario.cpf for u in self.usuarios):
            print("Já existe um usuário com esse CPF nesta empresa.")
        else:
            self.usuarios.append(usuario)
            print(f"Usuário {usuario.nome} adicionado com sucesso como {usuario.perfil}.")

empresas = []

def escolher_empresa():
    if not empresas:
        print("Nenhuma empresa cadastrada.")
        return None
    print("\nEmpresas cadastradas:")
    for i, e in enumerate(empresas):
        print(f"{i + 1}. {e.nome_fantasia} (CNPJ: {e.cnpj})")
    try:
        indice = int(input("Escolha o número da empresa: ")) - 1
        return empresas[indice]
    except (IndexError, ValueError):
        print("Opção inválida.")
        return None

while True:
    print("\n1. Cadastrar empresa")
    print("2. Adicionar usuário")
    print("3. Editar a empresa")
    print("4. Editar o usuario")
    print("5. Excluir")
    print("6. Consultar")
    
    opcao = input("Escolha uma das opções disponíveis de 1 a 6: ")

    if opcao == "1":
        nome_fantasia = str(input("\nDigite o nome fantasia: "))
        razao_social = str(input("Digite a razão social: "))
        cnpj = str(input("Digite o CNPJ: "))
        endereco = str(input("Digite o endereço da empresa: "))
        socios = str(input("Informe possíveis sócios: "))

        tipo_validos = ["mei", "ei", "slu", "ltda", "s.a"]
        tipo_da_empresa = str(input("Informe o tipo da empresa (MEI, EI, SLU, LTDA, S.A): ")).lower()

        while tipo_da_empresa not in tipo_validos:
            print("A opção informada não existe. Escolha uma das alternativas válidas.")
            tipo_da_empresa = str(input("Informe novamente o tipo da empresa: ")).lower()

        empresa = Empresa(nome_fantasia, razao_social, cnpj, endereco, tipo_da_empresa, socios)
        empresas.append(empresa) 

        print("\nCadastro realizado com sucesso!\n")
        print(f"Nome Fantasia: {empresa.nome_fantasia}")
        print(f"Razão social: {razao_social}")
        print(f"Cnpj: {cnpj}")
        print(f"Endereço: {endereco}")
        print(f"Sócios: {socios}")
        print(f"Tipo da empresa: {empresa.tipo.upper()}\n")

    elif opcao == "2":
        empresa = escolher_empresa()
        if empresa is None:
            continue
        nome_usuario = input("Digite o nome do usuário: ")
        cpf_usuario = input("Digite o CPF do usuário: ")
        perfis_validos = ["agência", "parceiro", "colaborador", "administrador"]
        perfil_usuario = input("Digite o perfil do usuário (agência, parceiro, colaborador, administrador): ").lower()
        
        while perfil_usuario not in perfis_validos:
            print("Perfil inválido. Escolha uma das alternativas válidas.")
            perfil_usuario = input("Informe novamente o tipo de perfil: ").lower()

        usuario = Usuario(nome_usuario, cpf_usuario, perfil_usuario)
        empresa.adicionar_usuario(usuario)

        print("\nCadastro realizado com sucesso!\n")
        print(f"Nome do usuário: {nome_usuario}")
        print(f"Cpf do usuário: {cpf_usuario}")
        print(f"perfil do usuário: {perfil_usuario}\n")
            
    elif opcao == "3":
        empresa = escolher_empresa()
        if empresa is None:
            continue
        empresa.nome_fantasia = input("Informe o novo nome fantasia: ")
        empresa.razao_social = input("Informe a nova razão social: ")
        empresa.cnpj = input("Informe o novo CNPJ: ")
        empresa.endereco = input("Informe o novo endereço: ")
        empresa.socios = input("Informe os novos sócios: ")
        tipo_validos = ["mei", "ei", "slu", "ltda", "s.a"]
        novo_tipo = input("Informe o novo tipo da empresa (MEI, EI, SLU, LTDA, S.A): ").lower()
        
        while novo_tipo not in tipo_validos:
            print("Tipo inválido.")
            novo_tipo = input("Informe novamente o tipo: ").lower()
        empresa.tipo = novo_tipo

        print("\nDados da empresa atualizados com sucesso.")
        print("\nDados da empresa atualizados com sucesso!\n")
        print(f"Novo nome: {nome_fantasia}")
        print(f"Nova razão social: {razao_social}")
        print(f"Novo Cnpj: {cnpj}")
        print(f"Novo endereço: {endereco}")
        print(f"Novos(as) sócios(as): {socios}")
        print(f"Novo tipo da empresa: {novo_tipo}\n")

    elif opcao == "4": 
        empresa = escolher_empresa()
        if empresa is None or not empresa.usuarios:
            print("Essa empresa não possui usuários.")
            continue
        cpf = input("Informe o CPF do usuário que deseja editar: ")
        for u in empresa.usuarios:
            if u.cpf == cpf:
                u.nome = input("Novo nome: ")
                u.cpf = input("Novo CPF: ")
                perfis_validos = ["agência", "parceiro", "colaborador", "administrador"]
                novo_perfil = input("Digite o novo perfil: (agência, parceiro, colaborador, administrador): ").lower()

                while novo_perfil not in perfis_validos:
                    print("Perfil inválido. Escolha uma das alternativas válidas")
                    novo_perfil = input("Informe novamente o perfil: ").lower()
                u.perfil = novo_perfil
                print("Usuário atualizado com sucesso.")
                break
        else:
            print("Usuário não encontrado.")
            
    elif opcao == "5":
        empresa = escolher_empresa()
        if empresa is None or not empresa.usuarios:
            print("Essa empresa não possui usuários.")
            continue
        cpf = input("Informe o CPF do usuário a ser excluído: ")
        for u in empresa.usuarios:
            if u.cpf == cpf:
                empresa.usuarios.remove(u)
                print(f"Usuário {u.nome} foi removido com sucesso.")
                break
        else:
            print("Usuário não encontrado.")

    elif opcao == "6":
        print("1. Consultar empresa por tipo")
        print("2. Consultar usuários por perfil")
        escolha = input("Escolha uma opção entre 1 e 2: ")

        if escolha == "1":
            tipo = input("Digite o tipo da empresa (MEI, EI, SLU, LTDA, S.A): ").lower()
            encontradas = [e for e in empresas if e.tipo == tipo]
            if encontradas:
                for e in encontradas:
                    print(f"Empresa: {e.nome_fantasia}, Tipo: {e.tipo.upper()}")
            else:
                print("Nenhuma empresa cadastrada com esse tipo.")

        elif escolha == "2":
            perfil = input("Digite o perfil do usuário (agência, parceiro, colaborador, administrador): ").lower()
            encontrados = False
            for e in empresas:
                usuarios = [u for u in e.usuarios if u.perfil == perfil]
                if usuarios:
                    print(f"\nNa empresa {e.nome_fantasia}:")
                    for u in usuarios:
                        status = "Ativo" if u.ativo else "Inativo"
                        print(f"  {u.nome} ({u.cpf}) - {u.perfil} - {status}")
                    encontrados = True
            if not encontrados:
                print("Nenhum usuário com esse perfil.")

    sair = input("Deseja voltar ao menu de opções? (s/n): ").lower()

    if sair != "s":
        print("Encerrando o programa.")
        break