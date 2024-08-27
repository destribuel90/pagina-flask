use prueba_apirest;
create table user(
id int auto_increment primary key,
Nombre varchar(50) not null,
Edad int not null,
Especie varchar(50) not null,
fecha_ingreso TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);