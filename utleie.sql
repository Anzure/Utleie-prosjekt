create database utleie;

use utleie;

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';


-- -----------------------------------------------------
-- Schema utleie
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema utleie
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `utleie` DEFAULT CHARACTER SET utf8 ;
USE `utleie` ;

-- -----------------------------------------------------
-- Table `utleie`.`Komponenter`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `utleie`.`komponent` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `navn` VARCHAR(45) NOT NULL,
  `beholdning` INT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `utleie`.`Bruker`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `utleie`.`bruker` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `navn` VARCHAR(45) NULL,
  `epost` VARCHAR(45) NOT NULL unique,
  `telefon` INT NULL unique,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `utleie`.`leie`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `utleie`.`leie` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `komponent_id` INT NOT NULL,
  `bruker_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  -- INDEX `fk_Lån_Komponenter_idx` (`Komponenter_Komponent ID` ASC) VISIBLE,
  -- INDEX `fk_Lån_Låner1_idx` (`Låner_Låner ID` ASC) VISIBLE,
  -- CONSTRAINT `fk_Lån_Komponenter`
    FOREIGN KEY (`komponent_id`)
    REFERENCES `utleie`.`komponent` (`id`),
   -- ON DELETE NO ACTION
   -- ON UPDATE NO ACTION,
  -- CONSTRAINT `fk_Lån_Låner1`
    FOREIGN KEY (`bruker_id`)
    REFERENCES `utleie`.`bruker` (`id`))
   -- ON DELETE NO ACTION
   -- ON UPDATE NO ACTION
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;