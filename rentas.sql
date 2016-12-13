create database Rentapeliculas;
use Rentapeliculas; 
CREATE TABLE Rentapeliculas.renta (
  id INT NOT NULL AUTO_INCREMENT,
  pelicula VARCHAR(100) NULL,
  formato VARCHAR(100) NULL,
  duracion varchar(100) null,
  nombreCliente VARCHAR(100) NULL,
  total VARCHAR(100) NOT NULL,
  PRIMARY KEY (id, total, duracion));