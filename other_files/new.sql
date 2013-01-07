-- MySQL dump 10.13  Distrib 5.5.28, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: new
-- ------------------------------------------------------
-- Server version	5.5.28-0ubuntu0.12.10.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_bda51c3c` (`group_id`),
  KEY `auth_group_permissions_1e014c8f` (`permission_id`),
  CONSTRAINT `group_id_refs_id_3cea63fe` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `permission_id_refs_id_a7792de1` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_e4470c6e` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_728de91f` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=127 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add site',6,'add_site'),(17,'Can change site',6,'change_site'),(18,'Can delete site',6,'delete_site'),(19,'Can add log entry',7,'add_logentry'),(20,'Can change log entry',7,'change_logentry'),(21,'Can delete log entry',7,'delete_logentry'),(22,'Can add registration profile',8,'add_registrationprofile'),(23,'Can change registration profile',8,'change_registrationprofile'),(24,'Can delete registration profile',8,'delete_registrationprofile'),(25,'Can add report',9,'add_report'),(26,'Can change report',9,'change_report'),(27,'Can delete report',9,'delete_report'),(28,'Can add user profile',10,'add_userprofile'),(29,'Can change user profile',10,'change_userprofile'),(30,'Can delete user profile',10,'delete_userprofile'),(31,'Can add auto_number',11,'add_auto_number'),(32,'Can change auto_number',11,'change_auto_number'),(33,'Can delete auto_number',11,'delete_auto_number'),(34,'Can add organisation',12,'add_organisation'),(35,'Can change organisation',12,'change_organisation'),(36,'Can delete organisation',12,'delete_organisation'),(37,'Can add department',13,'add_department'),(38,'Can change department',13,'change_department'),(39,'Can delete department',13,'delete_department'),(40,'Can add lab',14,'add_lab'),(41,'Can change lab',14,'change_lab'),(42,'Can delete lab',14,'delete_lab'),(43,'Can add material',15,'add_material'),(44,'Can change material',15,'change_material'),(45,'Can delete material',15,'delete_material'),(46,'Can add test',16,'add_test'),(47,'Can change test',16,'change_test'),(48,'Can delete test',16,'delete_test'),(49,'Can add clientadd',17,'add_clientadd'),(50,'Can change clientadd',17,'change_clientadd'),(51,'Can delete clientadd',17,'delete_clientadd'),(52,'Can add edit clientadd',18,'add_editclientadd'),(53,'Can change edit clientadd',18,'change_editclientadd'),(54,'Can delete edit clientadd',18,'delete_editclientadd'),(55,'Can add govt',19,'add_govt'),(56,'Can change govt',19,'change_govt'),(57,'Can delete govt',19,'delete_govt'),(58,'Can add payment',20,'add_payment'),(59,'Can change payment',20,'change_payment'),(60,'Can delete payment',20,'delete_payment'),(61,'Can add job',21,'add_job'),(62,'Can change job',21,'change_job'),(63,'Can delete job',21,'delete_job'),(64,'Can add edit job',22,'add_editjob'),(65,'Can change edit job',22,'change_editjob'),(66,'Can delete edit job',22,'delete_editjob'),(67,'Can add client job',23,'add_clientjob'),(68,'Can change client job',23,'change_clientjob'),(69,'Can delete client job',23,'delete_clientjob'),(70,'Can add client edit job',24,'add_clienteditjob'),(71,'Can change client edit job',24,'change_clienteditjob'),(72,'Can delete client edit job',24,'delete_clienteditjob'),(73,'Can add suspence job',25,'add_suspencejob'),(74,'Can change suspence job',25,'change_suspencejob'),(75,'Can delete suspence job',25,'delete_suspencejob'),(76,'Can add suspence edit job',26,'add_suspenceeditjob'),(77,'Can change suspence edit job',26,'change_suspenceeditjob'),(78,'Can delete suspence edit job',26,'delete_suspenceeditjob'),(79,'Can add test total',27,'add_testtotal'),(80,'Can change test total',27,'change_testtotal'),(81,'Can delete test total',27,'delete_testtotal'),(82,'Can add test total perf',28,'add_testtotalperf'),(83,'Can change test total perf',28,'change_testtotalperf'),(84,'Can delete test total perf',28,'delete_testtotalperf'),(85,'Can add bill',29,'add_bill'),(86,'Can change bill',29,'change_bill'),(87,'Can delete bill',29,'delete_bill'),(88,'Can add bill perf',30,'add_billperf'),(89,'Can change bill perf',30,'change_billperf'),(90,'Can delete bill perf',30,'delete_billperf'),(91,'Can add amount',31,'add_amount'),(92,'Can change amount',31,'change_amount'),(93,'Can delete amount',31,'delete_amount'),(94,'Can add cdf amount',32,'add_cdfamount'),(95,'Can change cdf amount',32,'change_cdfamount'),(96,'Can delete cdf amount',32,'delete_cdfamount'),(97,'Can add distance',33,'add_distance'),(98,'Can change distance',33,'change_distance'),(99,'Can delete distance',33,'delete_distance'),(100,'Can add suspence',34,'add_suspence'),(101,'Can change suspence',34,'change_suspence'),(102,'Can delete suspence',34,'delete_suspence'),(103,'Can add staff',35,'add_staff'),(104,'Can change staff',35,'change_staff'),(105,'Can delete staff',35,'delete_staff'),(106,'Can add profroma tax',36,'add_profromatax'),(107,'Can change profroma tax',36,'change_profromatax'),(108,'Can delete profroma tax',36,'delete_profromatax'),(109,'Can add ta da',37,'add_tada'),(110,'Can change ta da',37,'change_tada'),(111,'Can delete ta da',37,'delete_tada'),(112,'Can add transportation',38,'add_transportation'),(113,'Can change transportation',38,'change_transportation'),(114,'Can delete transportation',38,'delete_transportation'),(115,'Can add transport',39,'add_transport'),(116,'Can change transport',39,'change_transport'),(117,'Can delete transport',39,'delete_transport'),(118,'Can add bankdetails',40,'add_bankdetails'),(119,'Can change bankdetails',40,'change_bankdetails'),(120,'Can delete bankdetails',40,'delete_bankdetails'),(121,'Can add tag',41,'add_tag'),(122,'Can change tag',41,'change_tag'),(123,'Can delete tag',41,'delete_tag'),(124,'Can add tagged item',42,'add_taggeditem'),(125,'Can change tagged item',42,'change_taggeditem'),(126,'Can delete tagged item',42,'delete_taggeditem');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'admin','','','addmin@admin.com','pbkdf2_sha256$10000$EN0kP9EGMc7T$gcYSOecd6jRMshoxogIMVRDKqto39co0wvZB2S+U8wg=',1,1,1,'2013-01-06 19:28:05','2013-01-06 19:24:24');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_fbfc09f1` (`user_id`),
  KEY `auth_user_groups_bda51c3c` (`group_id`),
  CONSTRAINT `user_id_refs_id_831107f1` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `group_id_refs_id_f0ee9890` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_fbfc09f1` (`user_id`),
  KEY `auth_user_user_permissions_1e014c8f` (`permission_id`),
  CONSTRAINT `user_id_refs_id_f2045483` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `permission_id_refs_id_67e79cb` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_fbfc09f1` (`user_id`),
  KEY `django_admin_log_e4470c6e` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_288599e6` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `user_id_refs_id_c8665aa` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'permission','auth','permission'),(2,'group','auth','group'),(3,'user','auth','user'),(4,'content type','contenttypes','contenttype'),(5,'session','sessions','session'),(6,'site','sites','site'),(7,'log entry','admin','logentry'),(8,'registration profile','registration','registrationprofile'),(9,'report','tcc','report'),(10,'user profile','tcc','userprofile'),(11,'auto_number','tcc','auto_number'),(12,'organisation','tcc','organisation'),(13,'department','tcc','department'),(14,'lab','tcc','lab'),(15,'material','tcc','material'),(16,'test','tcc','test'),(17,'clientadd','tcc','clientadd'),(18,'edit clientadd','tcc','editclientadd'),(19,'govt','tcc','govt'),(20,'payment','tcc','payment'),(21,'job','tcc','job'),(22,'edit job','tcc','editjob'),(23,'client job','tcc','clientjob'),(24,'client edit job','tcc','clienteditjob'),(25,'suspence job','tcc','suspencejob'),(26,'suspence edit job','tcc','suspenceeditjob'),(27,'test total','tcc','testtotal'),(28,'test total perf','tcc','testtotalperf'),(29,'bill','tcc','bill'),(30,'bill perf','tcc','billperf'),(31,'amount','tcc','amount'),(32,'cdf amount','tcc','cdfamount'),(33,'distance','tcc','distance'),(34,'suspence','tcc','suspence'),(35,'staff','tcc','staff'),(36,'profroma tax','tcc','profromatax'),(37,'ta da','tcc','tada'),(38,'transportation','tcc','transportation'),(39,'transport','tcc','transport'),(40,'bankdetails','tcc','bankdetails'),(41,'tag','tagging','tag'),(42,'tagged item','tagging','taggeditem');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_c25c2c28` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('c367d30f4735f8daab1855172f71dc44','MjM5OTY0MDJiOTc2NjRhMjBlZDM0NzZlNmRkOTlhZWQyOGQ2YTA5MzqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n','2013-01-20 19:28:05');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_site`
--

DROP TABLE IF EXISTS `django_site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_site`
--

LOCK TABLES `django_site` WRITE;
/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
INSERT INTO `django_site` VALUES (1,'example.com','example.com');
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registration_registrationprofile`
--

DROP TABLE IF EXISTS `registration_registrationprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `registration_registrationprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `activation_key` varchar(40) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `user_id_refs_id_cecd7f3c` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registration_registrationprofile`
--

LOCK TABLES `registration_registrationprofile` WRITE;
/*!40000 ALTER TABLE `registration_registrationprofile` DISABLE KEYS */;
/*!40000 ALTER TABLE `registration_registrationprofile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tagging_tag`
--

DROP TABLE IF EXISTS `tagging_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tagging_tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tagging_tag`
--

LOCK TABLES `tagging_tag` WRITE;
/*!40000 ALTER TABLE `tagging_tag` DISABLE KEYS */;
/*!40000 ALTER TABLE `tagging_tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tagging_taggeditem`
--

DROP TABLE IF EXISTS `tagging_taggeditem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tagging_taggeditem` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tag_id` int(11) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `object_id` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tag_id` (`tag_id`,`content_type_id`,`object_id`),
  KEY `tagging_taggeditem_3747b463` (`tag_id`),
  KEY `tagging_taggeditem_e4470c6e` (`content_type_id`),
  KEY `tagging_taggeditem_829e37fd` (`object_id`),
  CONSTRAINT `content_type_id_refs_id_f1f84eed` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `tag_id_refs_id_9f51000d` FOREIGN KEY (`tag_id`) REFERENCES `tagging_tag` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tagging_taggeditem`
--

LOCK TABLES `tagging_taggeditem` WRITE;
/*!40000 ALTER TABLE `tagging_taggeditem` DISABLE KEYS */;
/*!40000 ALTER TABLE `tagging_taggeditem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tcc_amount`
--

DROP TABLE IF EXISTS `tcc_amount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tcc_amount` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `job_id` int(11) NOT NULL,
  `college_income` int(11) DEFAULT NULL,
  `admin_charge` int(11) DEFAULT NULL,
  `consultancy_asst` int(11) DEFAULT NULL,
  `development_fund` int(11) DEFAULT NULL,
  `unit_price` int(11) DEFAULT NULL,
  `report_type` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tcc_amount_751f44ae` (`job_id`),
  CONSTRAINT `job_id_refs_id_6018e7df` FOREIGN KEY (`job_id`) REFERENCES `tcc_job` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tcc_amount`
--

LOCK TABLES `tcc_amount` WRITE;
/*!40000 ALTER TABLE `tcc_amount` DISABLE KEYS */;
/*!40000 ALTER TABLE `tcc_amount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tcc_auto_number`
--

DROP TABLE IF EXISTS `tcc_auto_number`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tcc_auto_number` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `job_no` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `job_no` (`job_no`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tcc_auto_number`
--

LOCK TABLES `tcc_auto_number` WRITE;
/*!40000 ALTER TABLE `tcc_auto_number` DISABLE KEYS */;
/*!40000 ALTER TABLE `tcc_auto_number` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tcc_bankdetails`
--

DROP TABLE IF EXISTS `tcc_bankdetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tcc_bankdetails` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `accname` varchar(50) NOT NULL,
  `accountno` int(11) NOT NULL,
  `accountcode` varchar(50) NOT NULL,
  `address` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tcc_bankdetails`
--

LOCK TABLES `tcc_bankdetails` WRITE;
/*!40000 ALTER TABLE `tcc_bankdetails` DISABLE KEYS */;
/*!40000 ALTER TABLE `tcc_bankdetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tcc_bill`
--

DROP TABLE IF EXISTS `tcc_bill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tcc_bill` (
  `job_no` int(11) NOT NULL,
  `education_tax` int(11) DEFAULT NULL,
  `higher_education_tax` int(11) DEFAULT NULL,
  `service_tax` int(11) DEFAULT NULL,
  `net_total` int(11) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  PRIMARY KEY (`job_no`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tcc_bill`
--

LOCK TABLES `tcc_bill` WRITE;
/*!40000 ALTER TABLE `tcc_bill` DISABLE KEYS */;
/*!40000 ALTER TABLE `tcc_bill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tcc_billperf`
--

DROP TABLE IF EXISTS `tcc_billperf`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tcc_billperf` (
  `job_no` int(11) NOT NULL,
  `education_tax` int(11) DEFAULT NULL,
  `higher_education_tax` int(11) DEFAULT NULL,
  `service_tax` int(11) DEFAULT NULL,
  `net_total` int(11) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  PRIMARY KEY (`job_no`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tcc_billperf`
--

LOCK TABLES `tcc_billperf` WRITE;
/*!40000 ALTER TABLE `tcc_billperf` DISABLE KEYS */;
/*!40000 ALTER TABLE `tcc_billperf` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tcc_cdfamount`
--

DROP TABLE IF EXISTS `tcc_cdfamount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tcc_cdfamount` (
  `job_no` int(11) NOT NULL,
  `date` date NOT NULL,
  `lab` varchar(100) NOT NULL,
  `total` int(11) NOT NULL,
  `field` varchar(10) NOT NULL,
  `other_field` varchar(100) DEFAULT NULL,
  `report_type` varchar(20) NOT NULL,
  PRIMARY KEY (`job_no`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tcc_cdfamount`
--

LOCK TABLES `tcc_cdfamount` WRITE;
/*!40000 ALTER TABLE `tcc_cdfamount` DISABLE KEYS */;
/*!40000 ALTER TABLE `tcc_cdfamount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tcc_clientadd`
--

DROP TABLE IF EXISTS `tcc_clientadd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tcc_clientadd` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `client_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tcc_clientadd_fbfc09f1` (`user_id`),
  KEY `tcc_clientadd_4a4e8ffb` (`client_id`),
  CONSTRAINT `user_id_refs_id_8335da6c` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `client_id_refs_id_7f3a75eb` FOREIGN KEY (`client_id`) REFERENCES `tcc_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tcc_clientadd`
--

LOCK TABLES `tcc_clientadd` WRITE;
/*!40000 ALTER TABLE `tcc_clientadd` DISABLE KEYS */;
/*!40000 ALTER TABLE `tcc_clientadd` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tcc_clienteditjob`
--

DROP TABLE IF EXISTS `tcc_clienteditjob`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tcc_clienteditjob` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `job_id` int(11) NOT NULL,
  `material_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tcc_clienteditjob_751f44ae` (`job_id`),
  KEY `tcc_clienteditjob_fab9ba43` (`material_id`),
  CONSTRAINT `job_id_refs_id_eea896a0` FOREIGN KEY (`job_id`) REFERENCES `tcc_editjob` (`id`),
  CONSTRAINT `material_id_refs_id_cac842a5` FOREIGN KEY (`material_id`) REFERENCES `tcc_material` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tcc_clienteditjob`
--

LOCK TABLES `tcc_clienteditjob` WRITE;
/*!40000 ALTER TABLE `tcc_clienteditjob` DISABLE KEYS */;
/*!40000 ALTER TABLE `tcc_clienteditjob` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tcc_clienteditjob_test`
--

DROP TABLE IF EXISTS `tcc_clienteditjob_test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tcc_clienteditjob_test` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `clienteditjob_id` int(11) NOT NULL,
  `test_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `clienteditjob_id` (`clienteditjob_id`,`test_id`),
  KEY `tcc_clienteditjob_test_cbd9e9bb` (`clienteditjob_id`),
  KEY `tcc_clienteditjob_test_a88de8dc` (`test_id`),
  CONSTRAINT `clienteditjob_id_refs_id_8826c265` FOREIGN KEY (`clienteditjob_id`) REFERENCES `tcc_clienteditjob` (`id`),
  CONSTRAINT `test_id_refs_id_92a6bad2` FOREIGN KEY (`test_id`) REFERENCES `tcc_test` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tcc_clienteditjob_test`
--

LOCK TABLES `tcc_clienteditjob_test` WRITE;
/*!40000 ALTER TABLE `tcc_clienteditjob_test` DISABLE KEYS */;
/*!40000 ALTER TABLE `tcc_clienteditjob_test` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tcc_clientjob`
--

DROP TABLE IF EXISTS `tcc_clientjob`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tcc_clientjob` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `job_id` int(11) NOT NULL,
  `material_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tcc_clientjob_751f44ae` (`job_id`),
  KEY `tcc_clientjob_fab9ba43` (`material_id`),
  CONSTRAINT `material_id_refs_id_d47d0f5b` FOREIGN KEY (`material_id`) REFERENCES `tcc_material` (`id`),
  CONSTRAINT `job_id_refs_id_cf851ff0` FOREIGN KEY (`job_id`) REFERENCES `tcc_job` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tcc_clientjob`
--

LOCK TABLES `tcc_clientjob` WRITE;
/*!40000 ALTER TABLE `tcc_clientjob` DISABLE KEYS */;
/*!40000 ALTER TABLE `tcc_clientjob` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tcc_clientjob_test`
--

DROP TABLE IF EXISTS `tcc_clientjob_test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tcc_clientjob_test` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `clientjob_id` int(11) NOT NULL,
  `test_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `clientjob_id` (`clientjob_id`,`test_id`),
  KEY `tcc_clientjob_test_244d514d` (`clientjob_id`),
  KEY `tcc_clientjob_test_a88de8dc` (`test_id`),
  CONSTRAINT `clientjob_id_refs_id_8691d49b` FOREIGN KEY (`clientjob_id`) REFERENCES `tcc_clientjob` (`id`),
  CONSTRAINT `test_id_refs_id_fbfdbbd2` FOREIGN KEY (`test_id`) REFERENCES `tcc_test` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tcc_clientjob_test`
--

LOCK TABLES `tcc_clientjob_test` WRITE;
/*!40000 ALTER TABLE `tcc_clientjob_test` DISABLE KEYS */;
/*!40000 ALTER TABLE `tcc_clientjob_test` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tcc_department`
--

DROP TABLE IF EXISTS `tcc_department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tcc_department` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `organisation_id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `address` varchar(150) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `dean` varchar(50) NOT NULL,
  `faxno` int(11) DEFAULT NULL,
  `email_1` varchar(75) NOT NULL,
  `email_2` varchar(75) NOT NULL,
  `url` varchar(50) NOT NULL,
  `about` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tcc_department_28b1ef86` (`organisation_id`),
  CONSTRAINT `organisation_id_refs_id_52a18e23` FOREIGN KEY (`organisation_id`) REFERENCES `tcc_organisation` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tcc_department`
--

LOCK TABLES `tcc_department` WRITE;
/*!40000 ALTER TABLE `tcc_department` DISABLE KEYS */;
INSERT INTO `tcc_department` VALUES (1,1,'test_Department','','1234567890','admin',12,'','','','');
/*!40000 ALTER TABLE `tcc_department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tcc_distance`
--

DROP TABLE IF EXISTS `tcc_distance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tcc_distance` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `job` int(11) NOT NULL,
  `sandy` decimal(10,3) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tcc_distance`
--

LOCK TABLES `tcc_distance` WRITE;
/*!40000 ALTER TABLE `tcc_distance` DISABLE KEYS */;
/*!40000 ALTER TABLE `tcc_distance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tcc_editclientadd`
--

DROP TABLE IF EXISTS `tcc_editclientadd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tcc_editclientadd` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `client_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tcc_editclientadd_fbfc09f1` (`user_id`),
  KEY `tcc_editclientadd_4a4e8ffb` (`client_id`),
  CONSTRAINT `user_id_refs_id_277f0ac4` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `client_id_refs_id_fd489edd` FOREIGN KEY (`client_id`) REFERENCES `tcc_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tcc_editclientadd`
--

LOCK TABLES `tcc_editclientadd` WRITE;
/*!40000 ALTER TABLE `tcc_editclientadd` DISABLE KEYS */;
/*!40000 ALTER TABLE `tcc_editclientadd` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tcc_editjob`
--

DROP TABLE IF EXISTS `tcc_editjob`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tcc_editjob` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `client_id` int(11) NOT NULL,
  `job_no` int(11) NOT NULL,
  `sample` varchar(11) NOT NULL,
  `ip` varchar(50) NOT NULL,
  `site` varchar(600) NOT NULL,
  `type_of_work_id` int(11) NOT NULL,
  `report_type_id` int(11) NOT NULL,
  `pay` varchar(600) NOT NULL,
  `date` date NOT NULL,
  `check_number` varchar(15) NOT NULL,
  `check_dd_date` varchar(15) NOT NULL,
  `letter_no` int(11) DEFAULT NULL,
  `letter_date` date DEFAULT NULL,
  `tds` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tcc_editjob_4a4e8ffb` (`client_id`),
  KEY `tcc_editjob_ca5d2cd8` (`type_of_work_id`),
  KEY `tcc_editjob_3d4f9c7e` (`report_type_id`),
  CONSTRAINT `client_id_refs_id_475d7782` FOREIGN KEY (`client_id`) REFERENCES `tcc_editclientadd` (`id`),
  CONSTRAINT `report_type_id_refs_id_715128a7` FOREIGN KEY (`report_type_id`) REFERENCES `tcc_report` (`id`),
  CONSTRAINT `type_of_work_id_refs_id_3ff866ab` FOREIGN KEY (`type_of_work_id`) REFERENCES `tcc_govt` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tcc_editjob`
--

LOCK TABLES `tcc_editjob` WRITE;
/*!40000 ALTER TABLE `tcc_editjob` DISABLE KEYS */;
/*!40000 ALTER TABLE `tcc_editjob` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tcc_govt`
--

DROP TABLE IF EXISTS `tcc_govt`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tcc_govt` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(600) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tcc_govt`
--

LOCK TABLES `tcc_govt` WRITE;
/*!40000 ALTER TABLE `tcc_govt` DISABLE KEYS */;
/*!40000 ALTER TABLE `tcc_govt` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tcc_job`
--

DROP TABLE IF EXISTS `tcc_job`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tcc_job` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `client_id` int(11) NOT NULL,
  `job_no` int(11) NOT NULL,
  `sample` int(11) NOT NULL,
  `ip` varchar(50) NOT NULL,
  `site` varchar(50) NOT NULL,
  `type_of_work_id` int(11) NOT NULL,
  `report_type_id` int(11) NOT NULL,
  `pay` varchar(600) NOT NULL,
  `check_number` varchar(15) NOT NULL,
  `check_dd_date` varchar(15) NOT NULL,
  `date` date NOT NULL,
  `letter_no` int(11) DEFAULT NULL,
  `letter_date` date DEFAULT NULL,
  `tds` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tcc_job_4a4e8ffb` (`client_id`),
  KEY `tcc_job_ca5d2cd8` (`type_of_work_id`),
  KEY `tcc_job_3d4f9c7e` (`report_type_id`),
  CONSTRAINT `report_type_id_refs_id_bd662a09` FOREIGN KEY (`report_type_id`) REFERENCES `tcc_report` (`id`),
  CONSTRAINT `client_id_refs_id_fd23af76` FOREIGN KEY (`client_id`) REFERENCES `tcc_clientadd` (`id`),
  CONSTRAINT `type_of_work_id_refs_id_4da5e95b` FOREIGN KEY (`type_of_work_id`) REFERENCES `tcc_govt` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tcc_job`
--

LOCK TABLES `tcc_job` WRITE;
/*!40000 ALTER TABLE `tcc_job` DISABLE KEYS */;
/*!40000 ALTER TABLE `tcc_job` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tcc_lab`
--

DROP TABLE IF EXISTS `tcc_lab`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tcc_lab` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(5) NOT NULL,
  `name` varchar(300) NOT NULL,
  `department_id` int(11) NOT NULL,
  `tags` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tcc_lab_2ae7390` (`department_id`),
  CONSTRAINT `department_id_refs_id_e7636d4d` FOREIGN KEY (`department_id`) REFERENCES `tcc_department` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tcc_lab`
--

LOCK TABLES `tcc_lab` WRITE;
/*!40000 ALTER TABLE `tcc_lab` DISABLE KEYS */;
/*!40000 ALTER TABLE `tcc_lab` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tcc_material`
--

DROP TABLE IF EXISTS `tcc_material`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tcc_material` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lab_id` int(11) NOT NULL,
  `code` varchar(5) NOT NULL,
  `name` varchar(300) NOT NULL,
  `tags` varchar(255) NOT NULL,
  `report_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tcc_material_b5ebef3a` (`lab_id`),
  KEY `tcc_material_29fa1030` (`report_id`),
  CONSTRAINT `lab_id_refs_id_a847ac02` FOREIGN KEY (`lab_id`) REFERENCES `tcc_lab` (`id`),
  CONSTRAINT `report_id_refs_id_378be35e` FOREIGN KEY (`report_id`) REFERENCES `tcc_report` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tcc_material`
--

LOCK TABLES `tcc_material` WRITE;
/*!40000 ALTER TABLE `tcc_material` DISABLE KEYS */;
/*!40000 ALTER TABLE `tcc_material` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tcc_organisation`
--

DROP TABLE IF EXISTS `tcc_organisation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tcc_organisation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `address` varchar(150) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `director` varchar(50) NOT NULL,
  `logo_upload` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tcc_organisation`
--

LOCK TABLES `tcc_organisation` WRITE;
/*!40000 ALTER TABLE `tcc_organisation` DISABLE KEYS */;
INSERT INTO `tcc_organisation` VALUES (1,'test_Organisation','','1234567890','admin','');
/*!40000 ALTER TABLE `tcc_organisation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tcc_payment`
--

DROP TABLE IF EXISTS `tcc_payment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tcc_payment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tcc_payment`
--

LOCK TABLES `tcc_payment` WRITE;
/*!40000 ALTER TABLE `tcc_payment` DISABLE KEYS */;
/*!40000 ALTER TABLE `tcc_payment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tcc_profromatax`
--

DROP TABLE IF EXISTS `tcc_profromatax`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tcc_profromatax` (
  `pro_no` int(11) NOT NULL,
  `service_tax` int(11) NOT NULL,
  `higher_education_tax` int(11) NOT NULL,
  `education_tax` int(11) NOT NULL,
  `total` int(11) NOT NULL,
  PRIMARY KEY (`pro_no`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tcc_profromatax`
--

LOCK TABLES `tcc_profromatax` WRITE;
/*!40000 ALTER TABLE `tcc_profromatax` DISABLE KEYS */;
/*!40000 ALTER TABLE `tcc_profromatax` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tcc_report`
--

DROP TABLE IF EXISTS `tcc_report`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tcc_report` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tcc_report`
--

LOCK TABLES `tcc_report` WRITE;
/*!40000 ALTER TABLE `tcc_report` DISABLE KEYS */;
/*!40000 ALTER TABLE `tcc_report` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tcc_staff`
--

DROP TABLE IF EXISTS `tcc_staff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tcc_staff` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `department_id` int(11) NOT NULL,
  `code` varchar(5) NOT NULL,
  `name` varchar(50) NOT NULL,
  `daily_income` int(11) NOT NULL,
  `position` varchar(15) NOT NULL,
  `lab_id` int(11) NOT NULL,
  `email` varchar(75) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tcc_staff_2ae7390` (`department_id`),
  KEY `tcc_staff_b5ebef3a` (`lab_id`),
  CONSTRAINT `lab_id_refs_id_67a3244` FOREIGN KEY (`lab_id`) REFERENCES `tcc_lab` (`id`),
  CONSTRAINT `department_id_refs_id_6f4e591c` FOREIGN KEY (`department_id`) REFERENCES `tcc_department` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tcc_staff`
--

LOCK TABLES `tcc_staff` WRITE;
/*!40000 ALTER TABLE `tcc_staff` DISABLE KEYS */;
/*!40000 ALTER TABLE `tcc_staff` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tcc_suspence`
--

DROP TABLE IF EXISTS `tcc_suspence`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tcc_suspence` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `job_id` int(11) NOT NULL,
  `rate` int(11) DEFAULT NULL,
  `sus_id` int(11) NOT NULL,
  `work_charge` int(11) DEFAULT NULL,
  `labour_charge` int(11) DEFAULT NULL,
  `boring_charge_external` int(11) DEFAULT NULL,
  `boring_charge_internal` int(11) DEFAULT NULL,
  `car_taxi_charge` int(11) DEFAULT NULL,
  `lab_testing_staff` varchar(90) NOT NULL,
  `field_testing_staff` varchar(90) NOT NULL,
  `test_date` date DEFAULT NULL,
  `suspence_bill_no` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tcc_suspence_751f44ae` (`job_id`),
  KEY `tcc_suspence_c13e1de8` (`sus_id`),
  CONSTRAINT `job_id_refs_id_25fd0307` FOREIGN KEY (`job_id`) REFERENCES `tcc_job` (`id`),
  CONSTRAINT `sus_id_refs_id_4acb203f` FOREIGN KEY (`sus_id`) REFERENCES `tcc_suspencejob` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tcc_suspence`
--

LOCK TABLES `tcc_suspence` WRITE;
/*!40000 ALTER TABLE `tcc_suspence` DISABLE KEYS */;
/*!40000 ALTER TABLE `tcc_suspence` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tcc_suspenceeditjob`
--

DROP TABLE IF EXISTS `tcc_suspenceeditjob`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tcc_suspenceeditjob` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `job_id` int(11) NOT NULL,
  `field_id` int(11) NOT NULL,
  `test_id` int(11) NOT NULL,
  `other` varchar(600) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tcc_suspenceeditjob_751f44ae` (`job_id`),
  KEY `tcc_suspenceeditjob_b49f3317` (`field_id`),
  KEY `tcc_suspenceeditjob_a88de8dc` (`test_id`),
  CONSTRAINT `job_id_refs_id_7e90c6bd` FOREIGN KEY (`job_id`) REFERENCES `tcc_editjob` (`id`),
  CONSTRAINT `field_id_refs_id_8efd9e88` FOREIGN KEY (`field_id`) REFERENCES `tcc_material` (`id`),
  CONSTRAINT `test_id_refs_id_84316b4f` FOREIGN KEY (`test_id`) REFERENCES `tcc_test` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tcc_suspenceeditjob`
--

LOCK TABLES `tcc_suspenceeditjob` WRITE;
/*!40000 ALTER TABLE `tcc_suspenceeditjob` DISABLE KEYS */;
/*!40000 ALTER TABLE `tcc_suspenceeditjob` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tcc_suspencejob`
--

DROP TABLE IF EXISTS `tcc_suspencejob`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tcc_suspencejob` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `job_id` int(11) NOT NULL,
  `field_id` int(11) NOT NULL,
  `test_id` int(11) NOT NULL,
  `other` varchar(600) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tcc_suspencejob_751f44ae` (`job_id`),
  KEY `tcc_suspencejob_b49f3317` (`field_id`),
  KEY `tcc_suspencejob_a88de8dc` (`test_id`),
  CONSTRAINT `field_id_refs_id_f9dd1268` FOREIGN KEY (`field_id`) REFERENCES `tcc_material` (`id`),
  CONSTRAINT `job_id_refs_id_cafb41b3` FOREIGN KEY (`job_id`) REFERENCES `tcc_job` (`id`),
  CONSTRAINT `test_id_refs_id_faa2f6f` FOREIGN KEY (`test_id`) REFERENCES `tcc_test` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tcc_suspencejob`
--

LOCK TABLES `tcc_suspencejob` WRITE;
/*!40000 ALTER TABLE `tcc_suspencejob` DISABLE KEYS */;
/*!40000 ALTER TABLE `tcc_suspencejob` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tcc_tada`
--

DROP TABLE IF EXISTS `tcc_tada`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tcc_tada` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `job_id` int(11) NOT NULL,
  `departure_time_up` time NOT NULL,
  `arrival_time_up` time NOT NULL,
  `departure_time_down` time NOT NULL,
  `arrival_time_down` time NOT NULL,
  `tada_amount` int(11) DEFAULT NULL,
  `reach_site` varchar(60) NOT NULL,
  `test_date` varchar(15) NOT NULL,
  `end_date` varchar(15) NOT NULL,
  `testing_staff_code` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tcc_tada_751f44ae` (`job_id`),
  CONSTRAINT `job_id_refs_id_67cf5ad5` FOREIGN KEY (`job_id`) REFERENCES `tcc_job` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tcc_tada`
--

LOCK TABLES `tcc_tada` WRITE;
/*!40000 ALTER TABLE `tcc_tada` DISABLE KEYS */;
/*!40000 ALTER TABLE `tcc_tada` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tcc_test`
--

DROP TABLE IF EXISTS `tcc_test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tcc_test` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `material_id` int(11) NOT NULL,
  `code` varchar(5) NOT NULL,
  `name` varchar(300) NOT NULL,
  `quantity` int(11) DEFAULT NULL,
  `unit` varchar(15) NOT NULL,
  `cost` int(11) DEFAULT NULL,
  `tags` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tcc_test_fab9ba43` (`material_id`),
  CONSTRAINT `material_id_refs_id_ec75c33c` FOREIGN KEY (`material_id`) REFERENCES `tcc_material` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tcc_test`
--

LOCK TABLES `tcc_test` WRITE;
/*!40000 ALTER TABLE `tcc_test` DISABLE KEYS */;
/*!40000 ALTER TABLE `tcc_test` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tcc_testtotal`
--

DROP TABLE IF EXISTS `tcc_testtotal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tcc_testtotal` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `job_no` int(11) NOT NULL,
  `job_id` int(11) NOT NULL,
  `mat` int(11) DEFAULT NULL,
  `unit_price` int(11) DEFAULT NULL,
  `balance` int(11) DEFAULT NULL,
  `type` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tcc_testtotal_751f44ae` (`job_id`),
  CONSTRAINT `job_id_refs_id_4aaa37b8` FOREIGN KEY (`job_id`) REFERENCES `tcc_job` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tcc_testtotal`
--

LOCK TABLES `tcc_testtotal` WRITE;
/*!40000 ALTER TABLE `tcc_testtotal` DISABLE KEYS */;
/*!40000 ALTER TABLE `tcc_testtotal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tcc_testtotalperf`
--

DROP TABLE IF EXISTS `tcc_testtotalperf`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tcc_testtotalperf` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `job_no` int(11) NOT NULL,
  `job_id` int(11) NOT NULL,
  `mat` int(11) DEFAULT NULL,
  `unit_price` int(11) DEFAULT NULL,
  `balance` int(11) DEFAULT NULL,
  `type` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tcc_testtotalperf_751f44ae` (`job_id`),
  CONSTRAINT `job_id_refs_id_56adbb8d` FOREIGN KEY (`job_id`) REFERENCES `tcc_editjob` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tcc_testtotalperf`
--

LOCK TABLES `tcc_testtotalperf` WRITE;
/*!40000 ALTER TABLE `tcc_testtotalperf` DISABLE KEYS */;
/*!40000 ALTER TABLE `tcc_testtotalperf` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tcc_transport`
--

DROP TABLE IF EXISTS `tcc_transport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tcc_transport` (
  `vehicle_id` int(11) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `job_no` int(11) NOT NULL,
  `bill_no` int(11) DEFAULT NULL,
  `kilometer` varchar(150) NOT NULL,
  `amounts` varchar(180) NOT NULL,
  `total` int(11) DEFAULT NULL,
  `date` date NOT NULL,
  `test_date` varchar(300) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tcc_transport_4bffff7` (`vehicle_id`),
  CONSTRAINT `vehicle_id_refs_id_b0f5c5` FOREIGN KEY (`vehicle_id`) REFERENCES `tcc_transportation` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tcc_transport`
--

LOCK TABLES `tcc_transport` WRITE;
/*!40000 ALTER TABLE `tcc_transport` DISABLE KEYS */;
/*!40000 ALTER TABLE `tcc_transport` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tcc_transportation`
--

DROP TABLE IF EXISTS `tcc_transportation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tcc_transportation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `vehicleno` varchar(150) NOT NULL,
  `rate` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tcc_transportation`
--

LOCK TABLES `tcc_transportation` WRITE;
/*!40000 ALTER TABLE `tcc_transportation` DISABLE KEYS */;
/*!40000 ALTER TABLE `tcc_transportation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tcc_userprofile`
--

DROP TABLE IF EXISTS `tcc_userprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tcc_userprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `address_1` varchar(255) NOT NULL,
  `address_2` varchar(255) NOT NULL,
  `city` varchar(255) NOT NULL,
  `pin_code` int(11) DEFAULT NULL,
  `state` varchar(30) NOT NULL,
  `website` varchar(200) DEFAULT NULL,
  `contact_no` varchar(25) NOT NULL,
  `type_of_organisation` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tcc_userprofile_fbfc09f1` (`user_id`),
  CONSTRAINT `user_id_refs_id_3f595074` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tcc_userprofile`
--

LOCK TABLES `tcc_userprofile` WRITE;
/*!40000 ALTER TABLE `tcc_userprofile` DISABLE KEYS */;
/*!40000 ALTER TABLE `tcc_userprofile` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2013-01-06 19:48:40
