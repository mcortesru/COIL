-- Crear la base de datos PracticaVentas
create database PracticaVentas;
go

-- Usar la base de datos PracticaVentas
use PracticaVentas;
go

-- Tabla articulo
create table articulo (
       idarticulo integer primary key identity,
       codigo varchar(50) null,
       nombre varchar(100) not null unique,
       precio_venta decimal(11,2) not null,
       stock integer not null,
       descripcion varchar(256) null,
       estado bit default(1)
);

-- Tabla persona
create table persona (
       idpersona integer primary key identity,
       tipo_persona varchar(20) not null,
       nombre varchar(100) not null,
       tipo_documento varchar(20) null,
       num_documento varchar(20) null,
       direccion varchar(70) null,
       telefono varchar(20) null,
       email varchar(50) null
);

-- Tabla usuario
create table usuario (
       idusuario integer primary key identity,
       nombre varchar(100) not null,
       tipo_documento varchar(20) null,
       num_documento varchar(20) null,
       direccion varchar(70) null,
       telefono varchar(20) null,
       email varchar(50) not null,
       password varbinary not null,
       estado bit default(1)
);

-- Tabla venta
create table venta (
       idventa integer primary key identity,
       idcliente integer not null,
       idusuario integer not null,
       fecha_hora datetime not null,
       impuesto decimal(4,2) not null,
       total decimal(11,2) not null,
       estado varchar(20) not null,
       FOREIGN KEY (idcliente) REFERENCES persona(idpersona),
       FOREIGN KEY (idusuario) REFERENCES usuario(idusuario)
);

-- Tabla detalle_venta
create table detalle_venta (
       iddetalle_venta integer primary key identity,
       idventa integer not null,
       idarticulo integer not null,
       cantidad integer not null,
       precio decimal(11,2) not null,
       descuento decimal(11,2) not null,
       FOREIGN KEY (idventa) REFERENCES venta(idventa) ON DELETE CASCADE,
       FOREIGN KEY (idarticulo) REFERENCES articulo(idarticulo)
);
