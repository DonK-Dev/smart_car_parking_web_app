/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.7.9 : Database - smart_car_parking
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`smart_car_parking` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `smart_car_parking`;

/*Table structure for table `booking` */

DROP TABLE IF EXISTS `booking`;

CREATE TABLE `booking` (
  `book_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `starting_date` varchar(50) DEFAULT NULL,
  `starting_time` varchar(50) DEFAULT NULL,
  `ending_date` varchar(50) DEFAULT NULL,
  `ending_time` varchar(50) DEFAULT NULL,
  `slot_id` int(11) DEFAULT NULL,
  `amount` int(11) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`book_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `booking` */

insert  into `booking`(`book_id`,`user_id`,`starting_date`,`starting_time`,`ending_date`,`ending_time`,`slot_id`,`amount`,`status`) values (1,3,'28-02-2020','16:00','01-03-2020','2:00',2,80,'Payed'),(2,3,'01-03-2020','6:00','01-03-2020','17:00',1,40,'Reserved');

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `solution` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`complaint_id`,`user_id`,`description`,`date`,`status`,`solution`) values (1,3,'your system is not satisfied','2020-02-28','Pending','why'),(2,3,'You should improve the system','2020-02-28','Pending','NA');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `log_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`log_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`log_id`,`username`,`password`,`type`) values (1,'admin','admin','admin'),(2,'jissa','jissa','user'),(3,'jaya','jaya','user'),(4,'shan','shan','user');

/*Table structure for table `parking_locations` */

DROP TABLE IF EXISTS `parking_locations`;

CREATE TABLE `parking_locations` (
  `loc_id` int(11) NOT NULL AUTO_INCREMENT,
  `loc_name` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `latitude` varchar(50) DEFAULT NULL,
  `longitude` varchar(50) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`loc_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `parking_locations` */

insert  into `parking_locations`(`loc_id`,`loc_name`,`place`,`latitude`,`longitude`,`description`) values (1,'bus stand','nedumkandam','9.996999486326816','76.31094932556152','more space'),(3,'kaloor','ernakulam','9.987464083025962','76.32674116961671','large space'),(4,'Ammankovil','ernakulam','9.991310174671526','76.30330939166261','wide area'),(5,'boat jetty','ernakulam','9.976094601282911','76.27713103167726','large space'),(6,'marine drive','ernakulam','9.97693992957209','76.27970595233155','less space'),(7,'marine drive','ernakulam','9.97693992957209','76.27970595233155','less space');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `pay_id` int(11) NOT NULL AUTO_INCREMENT,
  `book_id` int(11) DEFAULT NULL,
  `amount` int(11) DEFAULT NULL,
  `mode_of_payment` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`pay_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

insert  into `payment`(`pay_id`,`book_id`,`amount`,`mode_of_payment`,`date`,`status`) values (1,1,80,'online','2020-02-28','Done'),(2,2,40,'online','2020-02-28','NA');

/*Table structure for table `slots` */

DROP TABLE IF EXISTS `slots`;

CREATE TABLE `slots` (
  `slot_id` int(11) NOT NULL AUTO_INCREMENT,
  `slot_description` varchar(50) DEFAULT NULL,
  `slot_status` varchar(50) DEFAULT NULL,
  `loc_id` int(11) DEFAULT NULL,
  `amount` int(11) DEFAULT NULL,
  `qr_code` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`slot_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `slots` */

insert  into `slots`(`slot_id`,`slot_description`,`slot_status`,`loc_id`,`amount`,`qr_code`) values (1,'bike','Reserved',7,40,'static/qrcode/2640bcd2-8828-41dd-bfbe-0e48c4e8e2a1.png'),(2,'bike','Occupied',7,40,'static/qrcode/ef42cb9a-1164-44cf-b9ba-fcc0f12042d7.png'),(3,'jeep','free',3,50,'static/qrcode/bdb2b241-6408-4150-a917-8be103880757.png'),(4,'car','free',3,90,'static/qrcode/708f3b7d-b33f-40ef-8acd-9ca517050bac.png'),(5,'jeep','free',5,20,'static/qrcode/add8d7d5-5d77-4dcd-843b-7a687733ec89.png'),(6,'jeep','free',4,30,'static/qrcode/c1a8376e-6615-48e4-bb91-fe39d18cba3b.png'),(7,'car','free',5,30,'static/qrcode/1710d4d0-5772-4591-8022-54dc4ee920b7.png'),(8,'jeep','free',4,25,'static/qrcode/25a9caeb-baec-4b8a-ac5b-91da7d4f9b42.png'),(9,'car','free',4,35,'static/qrcode/d1e17b8a-742f-460e-9522-468c18357ee9.png');

/*Table structure for table `users` */

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `log_id` int(11) DEFAULT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `house_name` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `pincode` varchar(10) DEFAULT NULL,
  `latitude` varchar(50) DEFAULT NULL,
  `longitude` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `users` */

insert  into `users`(`user_id`,`log_id`,`first_name`,`last_name`,`house_name`,`place`,`pincode`,`latitude`,`longitude`,`phone`,`email`) values (1,2,'Jissa','Mathew','Urumbithadathil','chembalam','685553','9.97713','76.2879162','6238826164','jisssa398@gmail.com'),(2,3,'Jayalakshmi','Jolly','Jolly Hut','Nedumkandam','688553','9.9760613','76.2868303','9863504528','jaya@gmail.com'),(3,4,'shan','shaji','pullanikavil','nedumkandam','685553','9.978078','76.2861063','6958437988','shan@gmail.com');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
