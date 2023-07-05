create table Fornecedor(
    txtcnpjcpf varchar(14) primary key,
    txtfornecedor varchar(255)
);

create table Partido(
    nomePartido varchar(18) primary key
);

create table Legislatura(
	codLegislatura integer primary key not null,
  	nuLegislatura integer
);

create table Lote(
	numLote integer primary key not null
);

create table Parlamentar(
    nuDeputadoid integer primary key not null,
    sgUF varchar(63),
    txtnomeparlamentar varchar(63),
    ideCadastro integer,
    nuCarteiraParlamentar integer,
    sgPartido varchar(18) references Partido(sgPartido),
    codLegislatura integer references Legislatura(codLegislatura)
);

create table Subcota_Documento(
    txtNumero varchar(63) primary key not null,
    numSubCota integer unique not null,
    txtDescricaoEspecificacao varchar(31),
    datEmissao date,
    vlrDocumento decimal(8, 2),
    vlrGlosa decimal(8, 2),
    numParcela integer,
    numRessarcimento float,
    vlrRestituicao decimal(8, 2),
    numMes integer,
    numAno integer,
    txtPassageiro varchar(1270),
    txtTrecho varchar(127),
    numEspecificacaoSubCota integer,
    indTipoDocumento integer,
    txtcnpjcpf varchar(14) references Fornecerdor(txtcnpjcpf),
    numLote integer references Lote(numLote),
    nuDeputadoid integer references Parlamentar(nuDeputadoid)
);


