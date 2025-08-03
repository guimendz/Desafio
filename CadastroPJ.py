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
        if not 'empresa' in globals():
            print("\nÉ necessário que uma empresa seja cadastrada.\n")
        else:
            nome_usuario = input("Digite o nome do usuário: ")
            cpf_usuario = input("Digite o CPF do usuário: ")
            perfis_validos = ["agência", "parceiro", "colaborador", "administrador"]
            perfil_usuario = input("Digite o perfil do usuário (agência, parceiro, colaborador, administrador): ").lower()
            
            while perfil_usuario not in perfis_validos:
                print("A opção informada não existe. Escolha uma das alternativas válidas.")
                perfil_usuario = input ("informe novamente o tipo de perfil: ")
            
            usuario = Usuario(nome_usuario, cpf_usuario, perfil_usuario)
            
            empresa.adicionar_usuario(usuario)

            print("\nCadastro realizado com sucesso!\n")
            print(f"Nome do usuário: {nome_usuario}")
            print(f"Cpf do usuário: {cpf_usuario}")
            print(f"perfil do usuário: {perfil_usuario}\n")
            
    elif opcao == "3":
        if not 'empresa' in globals():
            print("\nÉ necessário que uma empresa seja cadastrada.\n")
        else:
            novo_nome = str(input("Informe o novo nome: "))
            empresa.nome_fantasia = novo_nome

            nova_razao = str(input("Informe a nova razão social: "))
            empresa.razao_social = nova_razao

            novo_cnpj = str(input("Informe o novo Cnpj: "))
            empresa.cnpj = novo_cnpj

            novo_endereco = str(input("Informe o novo endereço: "))
            empresa.endereco = novo_endereco

            novos_socios = str(input("Informe os novos sócios: "))
            empresa.socios = novos_socios

            tipo_validos = ["mei", "ei", "slu", "ltda", "s.a"]
            novo_tipo = str(input("Informe o novo tipo da empresa (MEI, EI, SLU, LTDA, S.A): ")).lower()
            
            while novo_tipo not in tipo_validos:
                print("A opção informada não existe. Escolha uma das alternativas válidas.")
                novo_tipo = str(input("Informe o novo tipo da empresa: ")).lower()
                empresa.tipo = novo_tipo

            print("\nDados da empresa atualizados com sucesso!\n")
            print(f"Novo nome: {novo_nome}")
            print(f"Nova razão social: {nova_razao}")
            print(f"Novo Cnpj: {novo_cnpj}")
            print(f"Novo endereço: {novo_endereco}")
            print(f"Novos(as) sócios(as): {novos_socios}")
            print(f"Novo tipo da empresa: {novo_tipo}\n")

    elif opcao == "4": 
        if not 'empresa' in globals():
            print("\nÉ necessário que um usuário seja cadastrado.\n")
        else:
            novo_usuario = str(input("Informe o novo nome: "))
            empresa.nome_usuario = novo_usuario

            novo_cpf = str(input("Informe o novo Cpf: "))
            empresa.cpf_usuario = novo_cpf

            perfis_validos = ["agência", "parceiro", "colaborador", "administrador"]
            novo_perfil = input("Digite o novo perfil do usuário (agência, parceiro, colaborador, administrador): ").lower()
            
            while novo_perfil not in perfis_validos:
                print("A opção informada não existe. Escolha uma das alternativas válidas.")
                novo_perfil = input ("informe novamente o tipo de perfil: ")
                empresa.perfil = novo_perfil
   
            print("\nDados da empresa atualizados com sucesso!\n")
            print(f"Novo usuario: {novo_usuario}")
            print(f"Nov Cpf: {novo_cpf}")
            print(f"Novo Perfil: {novo_perfil}")
            
    elif opcao == "5":
        if not 'empresa' in globals() or len(empresa.usuarios) == 0:
            print("\nÉ necessário que exista um usuário cadastrado.\n")
        else:
            cpf = input("Informe o CPF do usuário a ser excluído: ")
            for u in empresa.usuarios:
                if u.cpf == cpf:
                    empresa.usuarios.remove(u)
                    print(f"\nUsuário {u.nome} foi removido com sucesso.\n")
                break
            else:
                    print("Usuário não encontrado na empresa.")

    elif opcao == "6":
        print("1. Consultar empresa por tipo")
        print("2. Consultar usuários por perfil")
        escolha = input("Escolha uma opção entre 1 e 2: ")

        if escolha == "1":
            tipo = input("Digite o tipo da empresa: ").lower()
            if empresa.tipo == tipo:
                print(f"Empresa: {empresa.nome_fantasia}, Tipo: {empresa.tipo.upper()}")
            else:
                print("Nenhuma empresa cadastrada com esse tipo.")

        elif escolha == "2":
            perfil = input("Digite o perfil do usuário: ").lower()
            encontrados = [u for u in empresa.usuarios if u.perfil == perfil]
            if encontrados:
                for u in encontrados:
                    status = "Ativo" if u.ativo else "Inativo"
                    print(f"{u.nome} ({u.cpf}) - {u.perfil} - {status}")
            else:
                print("Nenhum usuário com esse perfil.")

    sair = input("Deseja voltar ao menu de opções? (s/n): ").lower()

    if sair != "s":
        print("Encerrando o programa.")
        break