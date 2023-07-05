import pandas as pd


csvfile = pd.read_csv("BDPRojFinal\output.csv", nrows=1000).values.tolist()
ordem = ['codlegislatura','datemissao','idedocumento','idecadastro','indtipodocumento',
         'nucarteiraparlamentar','nudeputadoid','nulegislatura','numano','numespecificacaosubcota',
         'numlote','nummes','numparcela','numressarcimento','numsubcota','sgpartido','sguf',
         'txtnomeparlamentar','txtcnpjcpf','txtdescricao','txtdescricaoespecificacao',
         'txtfornecedor','txtnumero','txtpassageiro','txttrecho','vlrdocumento','vlrglosa','vlrliquido','vlrrestituicao']


sgpartido = ordem.index("sgpartido") + 1
txtcnpjcpf = ordem.index("txtcnpjcpf")+ 1
txtfornecedor = ordem.index("txtfornecedor")+ 1
codlegislatura = ordem.index("codlegislatura")+ 1
nulegislatura = ordem.index("nulegislatura")+ 1
lote = ordem.index("numlote")+ 1
nudeputadoid = ordem.index("nudeputadoid")+ 1
sguf = ordem.index("sguf")+ 1
txtnomeparlamentar = ordem.index("txtnomeparlamentar")+ 1
idecadastro = ordem.index("idecadastro")+ 1
nucarteiraparlamentar = ordem.index("nucarteiraparlamentar")+ 1
inddoc = ordem.index("indtipodocumento") + 1
txtnumero = ordem.index("txtnumero") + 1
numsubcota = ordem.index("numsubcota") + 1
txtdescricao = ordem.index("txtdescricao") + 1
datemissao = ordem.index("datemissao") + 1
vlrdocumento  = ordem.index("vlrdocumento") + 1                                         
vlrglosa = ordem.index("vlrglosa") + 1
numparcela = ordem.index("numparcela") + 1
numressarcimento = ordem.index("numressarcimento") + 1
vlrrestituicao = ordem.index("vlrrestituicao") + 1
nummes = ordem.index("nummes") + 1
numano = ordem.index("numano") + 1
txtpassageiro = ordem.index("txtpassageiro") + 1
txttrecho = ordem.index("txttrecho") + 1

'''
with open("BDPRojFinal\inserirPartido.sql", 'w') as insert:
    for linha in csvfile:
        insert.write(f"INSERT INTO Partido(sgPartido) VALUES ('{linha[sgpartido]}');\n")

with open("BDPRojFinal\inserirFornecedor.sql", 'w') as insert:
    for linha in csvfile:
        insert.write(f"INSERT INTO Fornecedor(txtcnpjcpg, txtfornecedor) VALUES ('{linha[txtcnpjcpf]}', '{linha[txtfornecedor]}');\n")

with open("BDPRojFinal\inserirLote.sql", 'w') as insert:
    for linha in csvfile:
        insert.write(f"INSERT INTO Lote(numLote) VALUES ({linha[lote]});\n")

with open("BDPRojFinal\inserirLegislatura.sql", 'w') as insert:
    for linha in csvfile:
        insert.write(f"INSERT INTO Legislatura(codLegislatura, nuLegislatura) VALUES ({linha[codlegislatura]}, {linha[nulegislatura]});\n")

with open("BDPRojFinal\inserirParlamentar.sql", 'w') as insert:
    for linha in csvfile:
        insert.write(f"INSERT INTO Parlamentar(nuDeputadoid, sgUF, txtnomeparlamentar, ideCadastro, nuCarteiraParlamentar, sgPartido, codLegislatura)\n" +
                     f"VALUES ({linha[nudeputadoid]}, '{linha[sguf]}', '{linha[txtnomeparlamentar]}', {linha[idecadastro]}, {linha[nucarteiraparlamentar]}, '{linha[sgpartido]}', {linha[codlegislatura]});\n")
'''
with open("BDPRojFinal\inserirSubcota.sql", 'w') as insert:
    for linha in csvfile:
        insert.write(f"INSERT INTO Subcota_Documento(txtNumero, numSubCota, txtDescricaoEspecificacao, datEmissao,"+
                         "vlrDocumento, vlrGlosa, numParcela, numRessarcimento, vlrRestituicao, numMes, numAno, txtPassageiro, txtTrecho, numEspecificacaoSubCota, indTipoDocumento, txtcnpjcpf, numLote, nuDeputadoid)\n"+
                         f"VALUES ('{linha[txtnumero]}', {linha[numsubcota]}, '{linha[txtdescricao]}', '{linha[datemissao]}', {linha[vlrdocumento]}, {linha[vlrglosa]}, {linha[numparcela]}, {linha[numressarcimento]}, {linha[vlrrestituicao]}, {linha[nummes]}, {linha[numano]}, '{linha[txtpassageiro]}', '{linha[txttrecho]}', {linha[numsubcota]}, {linha[inddoc]}, '{linha[txtcnpjcpf]}', {linha[lote]}, {linha[nudeputadoid]});\n\n")

                                                                                                                                                                                                                                                                
            
