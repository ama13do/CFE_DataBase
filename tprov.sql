CREATE TABLE Proveedor_plutonio (
    id_proveedor NUMBER PRIMARY KEY,
    nombre_proveedor VARCHAR2(100 BYTE),
    pais_proveedor VARCHAR2(100 BYTE)
);

CREATE TABLE Transportista (
    id_transportista NUMBER PRIMARY KEY,
    nombre_transportista VARCHAR(100),
    matricula VARCHAR(20) UNIQUE
);

CREATE TABLE Productor_Proveedor (
    id_productor_proveedor NUMBER PRIMARY KEY,
    id_productor NUMBER,
    id_proveedor NUMBER,
    FOREIGN KEY (id_proveedor) REFERENCES Proveedor_plutonio (id_proveedor)
);

CREATE TABLE Productor_transportista (
    id_producttrans NUMBER PRIMARY KEY,
    id_productor NUMBER,
    id_transportista NUMBER,
    FOREIGN KEY (id_transportista) REFERENCES Transportista (id_transportista)
);
