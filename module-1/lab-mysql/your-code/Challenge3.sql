-- MySQL dump 10.13  Distrib 8.0.12, for macos10.13 (x86_64)
--
-- Host: localhost    Database: mydb
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Car`
--

DROP TABLE IF EXISTS `Car`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Car` (
  `idCar` int NOT NULL AUTO_INCREMENT,
  `VIN` varchar(45) NOT NULL,
  `Manufacturer` varchar(45) NOT NULL,
  `Model` varchar(45) NOT NULL,
  `Year` year NOT NULL,
  `Color` varchar(45) NOT NULL,
  PRIMARY KEY (`idCar`),
  UNIQUE KEY `idCar_UNIQUE` (`idCar`),
  UNIQUE KEY `VIN_UNIQUE` (`VIN`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Car`
--

LOCK TABLES `Car` WRITE;
/*!40000 ALTER TABLE `Car` DISABLE KEYS */;
INSERT INTO `Car` VALUES (0,'3K096I98581DHSNUP','Volkswagen','Tiguan',2019,'Blue'),(1,'ZM8G7BEUQZ97IH46V','Peugeot','Rifter',2019,'Red'),(2,'RKXVNNIHLVVZOUB4M','Ford','Fusion',2018,'White'),(3,'HKNDGS7CU31E9Z7JW','Toyota','RAV4',2018,'Silver'),(4,'DAM41UDN3CHU2WVF7','Volvo','V60',2019,'Gray'),(5,'DAM41UDN3CHU2WVF6','Volvo','V60 Cross Country',2019,'Gray');
/*!40000 ALTER TABLE `Car` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Customer`
--

DROP TABLE IF EXISTS `Customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Customer` (
  `idCustomer` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(45) NOT NULL,
  `Phone_Number` int NOT NULL,
  `E-mail` varchar(45) NOT NULL,
  `Adress` varchar(45) NOT NULL,
  `City` varchar(45) NOT NULL,
  `State/Province` varchar(45) NOT NULL,
  `Country` varchar(45) NOT NULL,
  `Postal_Code` int NOT NULL,
  PRIMARY KEY (`idCustomer`),
  UNIQUE KEY `idCustomer_UNIQUE` (`idCustomer`)
) ENGINE=InnoDB AUTO_INCREMENT=30002 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Customer`
--

LOCK TABLES `Customer` WRITE;
/*!40000 ALTER TABLE `Customer` DISABLE KEYS */;
INSERT INTO `Customer` VALUES (0,'Pablo Picasso',837298762,'-','Paseo de la Chopera, 14','Madrid','Madrid','Spain',28045),(1,'Abraham Lincoln',789256374,'-','120 SW 8th St','Miami','Florida','United States',33130),(2,'Napoléon Bonaparte',179754000,'-','40 Rue du Colisée','Paris','Île-de-France','France',75008);
/*!40000 ALTER TABLE `Customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Invoices`
--

DROP TABLE IF EXISTS `Invoices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Invoices` (
  `idInvoices` int NOT NULL AUTO_INCREMENT,
  `Invoice_Numbers` int NOT NULL,
  `Date` datetime NOT NULL,
  `Car` int NOT NULL,
  `Customer` int NOT NULL,
  `Salesperson` int NOT NULL,
  PRIMARY KEY (`idInvoices`),
  UNIQUE KEY `idInvoices_UNIQUE` (`idInvoices`),
  UNIQUE KEY `Invoice_Numbers_UNIQUE` (`Invoice_Numbers`),
  KEY `Car_idx` (`Car`),
  KEY `Customer_idx` (`Customer`),
  KEY `Salesperson_idx` (`Salesperson`),
  CONSTRAINT `Car` FOREIGN KEY (`Car`) REFERENCES `Car` (`idCar`),
  CONSTRAINT `Customer` FOREIGN KEY (`Customer`) REFERENCES `Customer` (`idCustomer`),
  CONSTRAINT `Salesperson` FOREIGN KEY (`Salesperson`) REFERENCES `Salespersons` (`idSalespersons`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Invoices`
--

LOCK TABLES `Invoices` WRITE;
/*!40000 ALTER TABLE `Invoices` DISABLE KEYS */;
INSERT INTO `Invoices` VALUES (1,731166526,'2018-12-31 00:00:00',3,0,5),(2,271135104,'2019-01-22 00:00:00',2,2,7),(13,852399038,'2018-08-22 00:00:00',0,1,3);
/*!40000 ALTER TABLE `Invoices` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Salespersons`
--

DROP TABLE IF EXISTS `Salespersons`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `Salespersons` (
  `idSalespersons` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(45) NOT NULL,
  `Store` varchar(45) NOT NULL,
  PRIMARY KEY (`idSalespersons`),
  UNIQUE KEY `idSalespersons_UNIQUE` (`idSalespersons`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Salespersons`
--

LOCK TABLES `Salespersons` WRITE;
/*!40000 ALTER TABLE `Salespersons` DISABLE KEYS */;
INSERT INTO `Salespersons` VALUES (1,'Petey Cruiser','Madrid'),(2,'Anna Sthesia','Barcelona'),(3,'Paul Molive','Berlin'),(4,'Gail Forcewind','Paris'),(5,'Paige Turner','Mimia'),(6,'Bob Frapples','Mexico City'),(7,'Walter Melon','Amsterdam'),(8,'Shonda Leer','São Paulo');
/*!40000 ALTER TABLE `Salespersons` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-08-25 18:33:23
