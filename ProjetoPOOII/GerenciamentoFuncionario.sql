-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE database IF NOT EXISTS `GerenciamentoFuncionarios`;
USE `GerenciamentoFuncionarios` ;

-- -----------------------------------------------------
-- Table `mydb`.`Departamento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Departamento` (
  `IdDepartamento` INT NOT NULL,
  `Nome` VARCHAR(45) NOT NULL,
  `Descricao` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`IdDepartamento`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Funcionario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Funcionario` (
  `Cpf` INT NOT NULL,
  `Nome` VARCHAR(45) NOT NULL,
  `Endereco` VARCHAR(45) NOT NULL,
  `Telefone` VARCHAR(45) NOT NULL,
  `Sexo` VARCHAR(45) NOT NULL,
  `Salario` INT NOT NULL,
  `Departamento_IdDepartamento` INT NOT NULL,
  PRIMARY KEY (`Cpf`, `Departamento_IdDepartamento`),
  INDEX `fk_Funcionario_Departamento_idx` (`Departamento_IdDepartamento` ASC) VISIBLE,
  CONSTRAINT `fk_Funcionario_Departamento`
    FOREIGN KEY (`Departamento_IdDepartamento`)
    REFERENCES `mydb`.`Departamento` (`IdDepartamento`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Projeto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Projeto` (
  `IDProjeto` INT NOT NULL,
  `Nome` VARCHAR(45) NOT NULL,
  `Departamento_IdDepartamento` INT NOT NULL,
  PRIMARY KEY (`IDProjeto`, `Departamento_IdDepartamento`),
  INDEX `fk_Projeto_Departamento1_idx` (`Departamento_IdDepartamento` ASC) VISIBLE,
  CONSTRAINT `fk_Projeto_Departamento1`
    FOREIGN KEY (`Departamento_IdDepartamento`)
    REFERENCES `mydb`.`Departamento` (`IdDepartamento`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`TrabalhaEm`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `TrabalhaEm` (
  `Projeto_IDProjeto` INT NOT NULL,
  `Funcionario_Cpf` INT NOT NULL,
  `Funcionario_Departamento_IdDepartamento` INT NOT NULL,
  PRIMARY KEY (`Projeto_IDProjeto`, `Funcionario_Cpf`, `Funcionario_Departamento_IdDepartamento`),
  INDEX `fk_Projeto_has_Funcionario_Funcionario1_idx` (`Funcionario_Cpf` ASC, `Funcionario_Departamento_IdDepartamento` ASC) VISIBLE,
  INDEX `fk_Projeto_has_Funcionario_Projeto1_idx` (`Projeto_IDProjeto` ASC) VISIBLE,
  CONSTRAINT `fk_Projeto_has_Funcionario_Projeto1`
    FOREIGN KEY (`Projeto_IDProjeto`)
    REFERENCES `mydb`.`Projeto` (`IDProjeto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Projeto_has_Funcionario_Funcionario1`
    FOREIGN KEY (`Funcionario_Cpf` , `Funcionario_Departamento_IdDepartamento`)
    REFERENCES `mydb`.`Funcionario` (`Cpf` , `Departamento_IdDepartamento`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Gerente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Gerente` (
  `idGerente` INT NOT NULL,
  `Funcionario_Cpf` INT NOT NULL,
  `Funcionario_Departamento_IdDepartamento` INT NOT NULL,
  `Departamento_IdDepartamento` INT NOT NULL,
  PRIMARY KEY (`idGerente`, `Funcionario_Cpf`, `Funcionario_Departamento_IdDepartamento`, `Departamento_IdDepartamento`),
  INDEX `fk_Gerente_Funcionario1_idx` (`Funcionario_Cpf` ASC, `Funcionario_Departamento_IdDepartamento` ASC) VISIBLE,
  INDEX `fk_Gerente_Departamento1_idx` (`Departamento_IdDepartamento` ASC) VISIBLE,
  CONSTRAINT `fk_Gerente_Funcionario1`
    FOREIGN KEY (`Funcionario_Cpf` , `Funcionario_Departamento_IdDepartamento`)
    REFERENCES `mydb`.`Funcionario` (`Cpf` , `Departamento_IdDepartamento`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Gerente_Departamento1`
    FOREIGN KEY (`Departamento_IdDepartamento`)
    REFERENCES `mydb`.`Departamento` (`IdDepartamento`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`RegistroDePresenca`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `RegistroDePresenca` (
  `idRegistroDePresenca` INT NOT NULL,
  `Funcionario_Cpf` INT NOT NULL,
  `Funcionario_Departamento_IdDepartamento` INT NOT NULL,
  `Data` VARCHAR(45) NOT NULL,
  `HorarioEntrada` VARCHAR(45) NOT NULL,
  `HorarioSaida` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idRegistroDePresenca`, `Funcionario_Cpf`, `Funcionario_Departamento_IdDepartamento`),
  INDEX `fk_RegistroDePresenca_Funcionario1_idx` (`Funcionario_Cpf` ASC, `Funcionario_Departamento_IdDepartamento` ASC) VISIBLE,
  CONSTRAINT `fk_RegistroDePresenca_Funcionario1`
    FOREIGN KEY (`Funcionario_Cpf` , `Funcionario_Departamento_IdDepartamento`)
    REFERENCES `mydb`.`Funcionario` (`Cpf` , `Departamento_IdDepartamento`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- ----------------------------------------------------------------------------
Show databases
