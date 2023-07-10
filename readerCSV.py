import pandas as pd


ordem = ['codlegislatura','datemissao','idedocumento','idecadastro','indtipodocumento',
         'nucarteiraparlamentar','nudeputadoid','nulegislatura','numano','numespecificacaosubcota',
         'numlote','nummes','numparcela','numressarcimento','numsubcota','sgpartido','sguf',
         'txtnomeparlamentar','txtcnpjcpf','txtdescricao','txtdescricaoespecificacao',
         'txtfornecedor','txtnumero','txtpassageiro','txttrecho','vlrdocumento','vlrglosa','vlrliquido','vlrrestituicao']
controle = []
lotecontrole = []
partidocon = []
legcon = []
fornecedorcon = []

sgpartido = ordem.index("sgpartido") 
txtcnpjcpf = ordem.index("txtcnpjcpf")
txtfornecedor = ordem.index("txtfornecedor")
codlegislatura = ordem.index("codlegislatura")
nulegislatura = ordem.index("nulegislatura")
lote = ordem.index("numlote")
nudeputadoid = ordem.index("nudeputadoid")
sguf = ordem.index("sguf")
txtnomeparlamentar = ordem.index("txtnomeparlamentar")
idecadastro = ordem.index("idecadastro")
nucarteiraparlamentar = ordem.index("nucarteiraparlamentar")
inddoc = ordem.index("indtipodocumento") 
txtnumero = ordem.index("txtnumero") 
numsubcota = ordem.index("numsubcota") 
txtdescricao = ordem.index("txtdescricao") 
datemissao = ordem.index("datemissao") 
vlrdocumento  = ordem.index("vlrdocumento")                                          
vlrglosa = ordem.index("vlrglosa") 
numparcela = ordem.index("numparcela") 
numressarcimento = ordem.index("numressarcimento") 
vlrrestituicao = ordem.index("vlrrestituicao") 
nummes = ordem.index("nummes") 
numano = ordem.index("numano") 
txtpassageiro = ordem.index("txtpassageiro") 
txttrecho = ordem.index("txttrecho") 
id = -1

for i in range(100):
    csvfile = pd.read_csv("BDPRojFinal\cota-parlamentar.csv", skiprows=i*1000, nrows=1000).values.tolist()
    tam = len(csvfile[0])
    for linha in csvfile:
        '''
        #usar se necessário
        for i in range(tam):
            if isinstance(linha[i], str) and "'" in linha[i]:
                linha[i] = linha[i].replace("'", "")
        
        #usar se necessário
        '''
        
        #inserir subcota no arquivo
        with open("BDPRojFinal\inserirSubcotaAtualizado.sql", 'a') as insert:
            id += 1
            insert.write(f"INSERT INTO Subcota_Documento(idSubcota, txtNumero, numSubCota, txtDescricaoEspecificacao, datEmissao,"+
                        "vlrDocumento, vlrGlosa, numParcela, numRessarcimento, vlrRestituicao, numMes, numAno, txtPassageiro, txtTrecho, numEspecificacaoSubCota, indTipoDocumento, txtcnpjcpf, numLote, nuDeputadoid)\n"+
                            f"VALUES ({id},'{linha[txtnumero]}', {linha[numsubcota]}, '{linha[txtdescricao]}', '{linha[datemissao]}', {linha[vlrdocumento]}, {linha[vlrglosa]}, {linha[numparcela]}, {linha[numressarcimento]}, {linha[vlrrestituicao]}, {linha[nummes]}, {linha[numano]}, '{linha[txtpassageiro]}', '{linha[txttrecho]}', {linha[numsubcota]}, {linha[inddoc]}, '{linha[txtcnpjcpf]}', {linha[lote]}, {linha[nudeputadoid]});\n\n")

        #inserir fornecedores no arquivo
        with open("BDPRojFinal\inserirFornecedorAtualizado.sql", 'a') as insert:
            if linha[txtcnpjcpf] not in fornecedorcon:
                fornecedorcon.append(linha[txtcnpjcpf])
                insert.write(f"INSERT INTO Fornecedor(txtcnpjcpf, txtfornecedor) VALUES ('{linha[txtcnpjcpf]}', '{linha[txtfornecedor]}');\n")
        
        #inserir Lote no arquivo
        with open("BDPRojFinal\inserirLote.sql", 'a') as insert:
            insert.write(f"INSERT INTO Lote(numLote) VALUES ({linha[txtcnpjcpf]});\n")

        #inserir legislatura no arquivo
        with open("BDPRojFinal\inserirLegislatura.sql", 'a') as insert:
            if linha[codlegislatura] not in legcon:
                legcon.append(linha[codlegislatura])
                insert.write(f"INSERT INTO Legislatura(codLegislatura, nuLegislatura) VALUES ({linha[codlegislatura]}, {linha[nulegislatura]});\n")
        
        #inserir partidos no arquivo
        tempPartido = linha[sgpartido]
        if tempPartido not in partidocon:
            partidocon.append(tempPartido)
            with open("BDPRojFinal\inserirPartido.sql", 'a') as insert:
                insert.write(f"INSERT INTO Partido(sgPartido) VALUES ('{linha[sgpartido]}');\n")

        #inserir deputados no arquivo
        depid = linha[nudeputadoid]
        if depid not in controle:
            controle.append(depid)
            with open("BDPRojFinal\inserirParlamentar.sql", 'a') as insert:
                insert.write(f"INSERT INTO Parlamentar(nuDeputadoid, sgUF, txtnomeparlamentar, ideCadastro, nuCarteiraParlamentar, sgPartido, codLegislatura)\n" +
                            f"VALUES ({linha[nudeputadoid]}, '{linha[sguf]}', '{linha[txtnomeparlamentar]}', {linha[idecadastro]}, {linha[nucarteiraparlamentar]}, '{linha[sgpartido]}', {linha[codlegislatura]});\n")
                                                                                                                                                                                                                                                           
                
