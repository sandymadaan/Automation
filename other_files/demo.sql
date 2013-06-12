-- phpMyAdmin SQL Dump
-- version 3.4.11.1deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jun 11, 2013 at 02:01 PM
-- Server version: 5.5.29
-- PHP Version: 5.4.6-1ubuntu1.2

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `git_auto`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_bda51c3c` (`group_id`),
  KEY `auth_group_permissions_1e014c8f` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_e4470c6e` (`content_type_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=193 ;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add permission', 1, 'add_permission'),
(2, 'Can change permission', 1, 'change_permission'),
(3, 'Can delete permission', 1, 'delete_permission'),
(4, 'Can add group', 2, 'add_group'),
(5, 'Can change group', 2, 'change_group'),
(6, 'Can delete group', 2, 'delete_group'),
(7, 'Can add user', 3, 'add_user'),
(8, 'Can change user', 3, 'change_user'),
(9, 'Can delete user', 3, 'delete_user'),
(10, 'Can add content type', 4, 'add_contenttype'),
(11, 'Can change content type', 4, 'change_contenttype'),
(12, 'Can delete content type', 4, 'delete_contenttype'),
(13, 'Can add session', 5, 'add_session'),
(14, 'Can change session', 5, 'change_session'),
(15, 'Can delete session', 5, 'delete_session'),
(16, 'Can add site', 6, 'add_site'),
(17, 'Can change site', 6, 'change_site'),
(18, 'Can delete site', 6, 'delete_site'),
(19, 'Can add log entry', 7, 'add_logentry'),
(20, 'Can change log entry', 7, 'change_logentry'),
(21, 'Can delete log entry', 7, 'delete_logentry'),
(22, 'Can add registration profile', 8, 'add_registrationprofile'),
(23, 'Can change registration profile', 8, 'change_registrationprofile'),
(24, 'Can delete registration profile', 8, 'delete_registrationprofile'),
(25, 'Can add report', 9, 'add_report'),
(26, 'Can change report', 9, 'change_report'),
(27, 'Can delete report', 9, 'delete_report'),
(28, 'Can add user profile', 10, 'add_userprofile'),
(29, 'Can change user profile', 10, 'change_userprofile'),
(30, 'Can delete user profile', 10, 'delete_userprofile'),
(31, 'Can add organisation', 11, 'add_organisation'),
(32, 'Can change organisation', 11, 'change_organisation'),
(33, 'Can delete organisation', 11, 'delete_organisation'),
(34, 'Can add department', 12, 'add_department'),
(35, 'Can change department', 12, 'change_department'),
(36, 'Can delete department', 12, 'delete_department'),
(37, 'Can add distribution', 13, 'add_distribution'),
(38, 'Can change distribution', 13, 'change_distribution'),
(39, 'Can delete distribution', 13, 'delete_distribution'),
(40, 'Can add lab', 14, 'add_lab'),
(41, 'Can change lab', 14, 'change_lab'),
(42, 'Can delete lab', 14, 'delete_lab'),
(43, 'Can add material', 15, 'add_material'),
(44, 'Can change material', 15, 'change_material'),
(45, 'Can delete material', 15, 'delete_material'),
(46, 'Can add test', 16, 'add_test'),
(47, 'Can change test', 16, 'change_test'),
(48, 'Can delete test', 16, 'delete_test'),
(49, 'Can add clientadd', 17, 'add_clientadd'),
(50, 'Can change clientadd', 17, 'change_clientadd'),
(51, 'Can delete clientadd', 17, 'delete_clientadd'),
(52, 'Can add edit clientadd', 18, 'add_editclientadd'),
(53, 'Can change edit clientadd', 18, 'change_editclientadd'),
(54, 'Can delete edit clientadd', 18, 'delete_editclientadd'),
(55, 'Can add govt', 19, 'add_govt'),
(56, 'Can change govt', 19, 'change_govt'),
(57, 'Can delete govt', 19, 'delete_govt'),
(58, 'Can add payment', 20, 'add_payment'),
(59, 'Can change payment', 20, 'change_payment'),
(60, 'Can delete payment', 20, 'delete_payment'),
(61, 'Can add job', 21, 'add_job'),
(62, 'Can change job', 21, 'change_job'),
(63, 'Can delete job', 21, 'delete_job'),
(64, 'Can add edit job', 22, 'add_editjob'),
(65, 'Can change edit job', 22, 'change_editjob'),
(66, 'Can delete edit job', 22, 'delete_editjob'),
(67, 'Can add client job', 23, 'add_clientjob'),
(68, 'Can change client job', 23, 'change_clientjob'),
(69, 'Can delete client job', 23, 'delete_clientjob'),
(70, 'Can add client edit job', 24, 'add_clienteditjob'),
(71, 'Can change client edit job', 24, 'change_clienteditjob'),
(72, 'Can delete client edit job', 24, 'delete_clienteditjob'),
(73, 'Can add suspence job', 25, 'add_suspencejob'),
(74, 'Can change suspence job', 25, 'change_suspencejob'),
(75, 'Can delete suspence job', 25, 'delete_suspencejob'),
(76, 'Can add suspence edit job', 26, 'add_suspenceeditjob'),
(77, 'Can change suspence edit job', 26, 'change_suspenceeditjob'),
(78, 'Can delete suspence edit job', 26, 'delete_suspenceeditjob'),
(79, 'Can add test total', 27, 'add_testtotal'),
(80, 'Can change test total', 27, 'change_testtotal'),
(81, 'Can delete test total', 27, 'delete_testtotal'),
(82, 'Can add test total perf', 28, 'add_testtotalperf'),
(83, 'Can change test total perf', 28, 'change_testtotalperf'),
(84, 'Can delete test total perf', 28, 'delete_testtotalperf'),
(85, 'Can add bill', 29, 'add_bill'),
(86, 'Can change bill', 29, 'change_bill'),
(87, 'Can delete bill', 29, 'delete_bill'),
(88, 'Can add bill perf', 30, 'add_billperf'),
(89, 'Can change bill perf', 30, 'change_billperf'),
(90, 'Can delete bill perf', 30, 'delete_billperf'),
(91, 'Can add amount', 31, 'add_amount'),
(92, 'Can change amount', 31, 'change_amount'),
(93, 'Can delete amount', 31, 'delete_amount'),
(94, 'Can add cdf amount', 32, 'add_cdfamount'),
(95, 'Can change cdf amount', 32, 'change_cdfamount'),
(96, 'Can delete cdf amount', 32, 'delete_cdfamount'),
(97, 'Can add distance', 33, 'add_distance'),
(98, 'Can change distance', 33, 'change_distance'),
(99, 'Can delete distance', 33, 'delete_distance'),
(100, 'Can add suspence', 34, 'add_suspence'),
(101, 'Can change suspence', 34, 'change_suspence'),
(102, 'Can delete suspence', 34, 'delete_suspence'),
(103, 'Can add staff', 35, 'add_staff'),
(104, 'Can change staff', 35, 'change_staff'),
(105, 'Can delete staff', 35, 'delete_staff'),
(106, 'Can add profroma tax', 36, 'add_profromatax'),
(107, 'Can change profroma tax', 36, 'change_profromatax'),
(108, 'Can delete profroma tax', 36, 'delete_profromatax'),
(109, 'Can add ta da', 37, 'add_tada'),
(110, 'Can change ta da', 37, 'change_tada'),
(111, 'Can delete ta da', 37, 'delete_tada'),
(112, 'Can add transportation', 38, 'add_transportation'),
(113, 'Can change transportation', 38, 'change_transportation'),
(114, 'Can delete transportation', 38, 'delete_transportation'),
(115, 'Can add transport', 39, 'add_transport'),
(116, 'Can change transport', 39, 'change_transport'),
(117, 'Can delete transport', 39, 'delete_transport'),
(118, 'Can add bankdetails', 40, 'add_bankdetails'),
(119, 'Can change bankdetails', 40, 'change_bankdetails'),
(120, 'Can delete bankdetails', 40, 'delete_bankdetails'),
(121, 'Can add tag', 41, 'add_tag'),
(122, 'Can change tag', 41, 'change_tag'),
(123, 'Can delete tag', 41, 'delete_tag'),
(124, 'Can add tagged item', 42, 'add_taggeditem'),
(125, 'Can change tagged item', 42, 'change_taggeditem'),
(126, 'Can delete tagged item', 42, 'delete_taggeditem'),
(127, 'Can add search', 43, 'add_search'),
(128, 'Can change search', 43, 'change_search'),
(129, 'Can delete search', 43, 'delete_search'),
(130, 'Can add report', 44, 'add_report'),
(131, 'Can change report', 44, 'change_report'),
(132, 'Can delete report', 44, 'delete_report'),
(133, 'Can add cube', 45, 'add_cube'),
(134, 'Can change cube', 45, 'change_cube'),
(135, 'Can delete cube', 45, 'delete_cube'),
(136, 'Can add chem_analysis', 46, 'add_chem_analysis'),
(137, 'Can change chem_analysis', 46, 'change_chem_analysis'),
(138, 'Can delete chem_analysis', 46, 'delete_chem_analysis'),
(139, 'Can add steel', 47, 'add_steel'),
(140, 'Can change steel', 47, 'change_steel'),
(141, 'Can delete steel', 47, 'delete_steel'),
(142, 'Can add ground_ water', 48, 'add_ground_water'),
(143, 'Can change ground_ water', 48, 'change_ground_water'),
(144, 'Can delete ground_ water', 48, 'delete_ground_water'),
(145, 'Can add concrete_ paver', 49, 'add_concrete_paver'),
(146, 'Can change concrete_ paver', 49, 'change_concrete_paver'),
(147, 'Can delete concrete_ paver', 49, 'delete_concrete_paver'),
(148, 'Can add interlock_ tiles', 50, 'add_interlock_tiles'),
(149, 'Can change interlock_ tiles', 50, 'change_interlock_tiles'),
(150, 'Can delete interlock_ tiles', 50, 'delete_interlock_tiles'),
(151, 'Can add pc', 51, 'add_pc'),
(152, 'Can change pc', 51, 'change_pc'),
(153, 'Can delete pc', 51, 'delete_pc'),
(154, 'Can add rebound_ hammer_ testing', 52, 'add_rebound_hammer_testing'),
(155, 'Can change rebound_ hammer_ testing', 52, 'change_rebound_hammer_testing'),
(156, 'Can delete rebound_ hammer_ testing', 52, 'delete_rebound_hammer_testing'),
(157, 'Can add brick', 53, 'add_brick'),
(158, 'Can change brick', 53, 'change_brick'),
(159, 'Can delete brick', 53, 'delete_brick'),
(160, 'Can add water', 54, 'add_water'),
(161, 'Can change water', 54, 'change_water'),
(162, 'Can delete water', 54, 'delete_water'),
(163, 'Can add soil_ ohsr', 55, 'add_soil_ohsr'),
(164, 'Can change soil_ ohsr', 55, 'change_soil_ohsr'),
(165, 'Can delete soil_ ohsr', 55, 'delete_soil_ohsr'),
(166, 'Can add soil_ building', 56, 'add_soil_building'),
(167, 'Can change soil_ building', 56, 'change_soil_building'),
(168, 'Can delete soil_ building', 56, 'delete_soil_building'),
(169, 'Can add admixture', 57, 'add_admixture'),
(170, 'Can change admixture', 57, 'change_admixture'),
(171, 'Can delete admixture', 57, 'delete_admixture'),
(172, 'Can add cement_ppc', 58, 'add_cement_ppc'),
(173, 'Can change cement_ppc', 58, 'change_cement_ppc'),
(174, 'Can delete cement_ppc', 58, 'delete_cement_ppc'),
(175, 'Can add cement_op c_33', 59, 'add_cement_opc_33'),
(176, 'Can change cement_op c_33', 59, 'change_cement_opc_33'),
(177, 'Can delete cement_op c_33', 59, 'delete_cement_opc_33'),
(178, 'Can add cement_op c_43', 60, 'add_cement_opc_43'),
(179, 'Can change cement_op c_43', 60, 'change_cement_opc_43'),
(180, 'Can delete cement_op c_43', 60, 'delete_cement_opc_43'),
(181, 'Can add cement_op c_53', 61, 'add_cement_opc_53'),
(182, 'Can change cement_op c_53', 61, 'change_cement_opc_53'),
(183, 'Can delete cement_op c_53', 61, 'delete_cement_opc_53'),
(184, 'Can add non payment job', 62, 'add_nonpaymentjob'),
(185, 'Can change non payment job', 62, 'change_nonpaymentjob'),
(186, 'Can delete non payment job', 62, 'delete_nonpaymentjob'),
(187, 'Can add mat comment', 63, 'add_matcomment'),
(188, 'Can change mat comment', 63, 'change_matcomment'),
(189, 'Can delete mat comment', 63, 'delete_matcomment'),
(190, 'Can add distanceperf', 64, 'add_distanceperf'),
(191, 'Can change distanceperf', 64, 'change_distanceperf'),
(192, 'Can delete distanceperf', 64, 'delete_distanceperf');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
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
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=9 ;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `username`, `first_name`, `last_name`, `email`, `password`, `is_staff`, `is_active`, `is_superuser`, `last_login`, `date_joined`) VALUES
(1, 'sandy', '', '', 'mkaurkhalsa@gmail.com', 'pbkdf2_sha256$10000$gGbHtUOdxlcv$ziUbj/MdpoIJHDzINuJA1Z9pHPnN0htLh5Qkg/TNlqQ=', 1, 1, 1, '2013-06-11 14:01:10', '2013-03-30 17:27:38'),
(2, 'Bhagwant', '', '', 'mkaurkhalsa@gmail.com', 'pbkdf2_sha256$10000$YJZpkw8GYrgA$2kbyZGVSslrCZ3O+XV9JnZ1MEVinKrldlM4crjFgJGc=', 0, 1, 0, '2013-03-31 21:58:57', '2013-03-30 23:29:05'),
(3, 'dotorgdotcom', '', '', 'dotorgdotcom@gmail.com', 'pbkdf2_sha256$10000$qNk6NZDOGPv6$bbi0tOTwJ0oqtiMn5gU5HPephPhnM8IWqLr4GT4kqmU=', 0, 1, 0, '2013-03-31 19:46:55', '2013-03-31 11:26:05'),
(4, 'sandeep', '', '', 'mkaurkhalsa@gmail.com', 'pbkdf2_sha256$10000$OEFnKC9ToESb$r/1zXRgFriKg+Ipx//XxD2mxQN8Omy91a8K8woSawxg=', 0, 1, 0, '2013-03-31 17:26:32', '2013-03-31 17:25:55'),
(5, 'Mandeep', '', '', 'mandeep.kaur.jolly@gmail.com', 'pbkdf2_sha256$10000$Jdxe3UnV7Op1$avWn3E+ghf/v40Ul+ZzdofZGk9DFPuPURC/jrXcv7GU=', 0, 1, 0, '2013-04-01 13:54:20', '2013-04-01 13:52:04'),
(6, 'Taranjeet', '', '', 'taranjeetssidhu@gmail.com', 'pbkdf2_sha256$10000$BEq8NwXqsk3t$yFrOaDfVdNdut+SlDzARoeT3FIP6Sk38Qyx/bldTWlE=', 0, 1, 0, '2013-04-01 14:57:55', '2013-04-01 14:56:56'),
(7, 'Taranjeet_Singh', '', '', 'taranjeetssidhu@gmail.com', 'pbkdf2_sha256$10000$21VC1BnFtlMb$n2mTzN/hZ1alVT4sKwef5NUDgKLP5MTR6c1B8IHrIpc=', 0, 1, 0, '2013-04-01 14:59:38', '2013-04-01 14:59:38'),
(8, 'mandy', '', '', 'meghasimak@gmail.com', 'pbkdf2_sha256$10000$vtz6uBC40qQP$PcQlOr9MFrR0rLHW9MNlBUCXR5IivNYoEqALmv1fLoM=', 0, 1, 0, '2013-04-01 16:01:36', '2013-04-01 16:00:59');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_fbfc09f1` (`user_id`),
  KEY `auth_user_groups_bda51c3c` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_fbfc09f1` (`user_id`),
  KEY `auth_user_user_permissions_1e014c8f` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
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
  KEY `django_admin_log_e4470c6e` (`content_type_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=91 ;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `user_id`, `content_type_id`, `object_id`, `object_repr`, `action_flag`, `change_message`) VALUES
(1, '2013-04-01 12:04:46', 1, 15, '21', 'Tiles', 1, ''),
(2, '2013-04-02 14:34:27', 1, 16, '16', 'Comp. Strength  ', 2, 'Changed cost.'),
(3, '2013-04-02 14:35:12', 1, 16, '17', 'Water Absorption  ', 2, 'Changed cost.'),
(4, '2013-04-02 14:35:42', 1, 16, '18', 'Effloroscence  ', 2, 'Changed cost.'),
(5, '2013-04-02 15:07:49', 1, 15, '22', 'BM/PC', 1, ''),
(6, '2013-04-02 15:14:02', 1, 16, '53', 'BM', 1, ''),
(7, '2013-04-02 15:14:30', 1, 16, '54', 'PC', 1, ''),
(8, '2013-04-02 15:15:36', 1, 15, '23', 'BM & PC Mix', 1, ''),
(9, '2013-04-02 15:16:46', 1, 16, '55', 'Bitumen Content', 1, ''),
(10, '2013-04-02 15:32:47', 1, 15, '24', 'Coarse & Fine Aggregates', 1, ''),
(11, '2013-04-04 10:43:00', 1, 15, '25', 'Water for Construction', 1, ''),
(12, '2013-04-04 10:44:20', 1, 16, '56', 'Water for Construction', 1, ''),
(13, '2013-04-04 11:11:00', 1, 15, '26', 'Lab. MDD & OMC', 1, ''),
(14, '2013-04-04 11:12:11', 1, 15, '27', 'Plastic Limit/Liquid Limit', 1, ''),
(15, '2013-04-04 11:15:19', 1, 16, '57', 'Lab. MDD & OMC', 1, ''),
(16, '2013-04-04 11:17:50', 1, 16, '58', 'Plastic Limit/Liquid Limit', 1, ''),
(17, '2013-04-04 11:18:56', 1, 15, '28', 'Uniformity Coefficient (D60/D10) in Graph as per RDSO', 1, ''),
(18, '2013-04-04 11:19:47', 1, 15, '29', 'The Coefficient of Curvature', 1, ''),
(19, '2013-04-04 11:20:24', 1, 16, '59', 'Uniformity Coefficient (D60/D10) in Graph as per RDSO', 1, ''),
(20, '2013-04-04 11:20:45', 1, 16, '60', 'The Coefficient of Curvature', 1, ''),
(21, '2013-04-04 12:07:43', 1, 15, '10', 'Mix Design', 2, 'Changed distribution and image.'),
(22, '2013-04-04 14:21:41', 1, 15, '30', 'Blanketing Materials', 1, ''),
(23, '2013-04-04 14:22:25', 1, 16, '61', 'Lab. MDD & OMC', 1, ''),
(24, '2013-04-04 14:22:51', 1, 16, '62', 'Plastic Limit/Liquid Limit', 1, ''),
(25, '2013-04-04 14:23:19', 1, 16, '63', 'Uniformity Coefficient (D60/D10) in Graph as per RDSO', 1, ''),
(26, '2013-04-04 14:23:42', 1, 16, '64', 'The Coefficient of Curvature', 1, ''),
(27, '2013-04-04 17:10:55', 1, 15, '3', 'Pavers', 2, 'Changed name, tags and image.'),
(28, '2013-04-05 11:18:57', 1, 15, '31', 'BM', 1, ''),
(29, '2013-04-05 11:20:10', 1, 15, '32', 'SDBC', 1, ''),
(30, '2013-04-05 11:21:21', 1, 16, '65', 'BM', 1, ''),
(31, '2013-04-05 11:21:44', 1, 16, '66', 'SDBC', 1, ''),
(32, '2013-04-05 14:38:14', 1, 15, '33', 'Hammer', 1, ''),
(33, '2013-04-05 14:39:12', 1, 16, '67', ' Hammer', 1, ''),
(34, '2013-04-05 15:14:51', 1, 15, '34', 'M.S.Plate', 1, ''),
(35, '2013-04-05 15:17:32', 1, 16, '68', 'M.S.Plate', 1, ''),
(36, '2013-04-08 10:55:56', 1, 15, '35', 'PC', 1, ''),
(37, '2013-04-08 10:57:26', 1, 16, '69', 'PC', 1, ''),
(38, '2013-04-08 17:11:45', 1, 35, '14', 'Sh. Balraj Singh', 1, ''),
(39, '2013-04-08 18:02:45', 1, 35, '10', 'Sh. Nandan Singh', 2, 'Changed name.'),
(40, '2013-04-08 18:13:51', 1, 15, '36', 'DBM', 1, ''),
(41, '2013-04-08 18:15:14', 1, 16, '70', 'DBM', 1, ''),
(42, '2013-04-09 10:43:02', 1, 16, '71', 'Lab Density', 1, ''),
(43, '2013-04-09 10:43:48', 1, 16, '72', 'PI Value', 1, ''),
(44, '2013-04-09 10:46:51', 1, 15, '37', 'GSB Material', 1, ''),
(45, '2013-04-09 10:48:07', 1, 16, '73', 'CRB Value', 1, ''),
(46, '2013-04-09 10:48:30', 1, 16, '74', 'PI Value', 1, ''),
(47, '2013-04-09 14:25:19', 1, 16, '75', 'Flakiness Index', 1, ''),
(48, '2013-04-09 14:26:13', 1, 16, '76', 'Crushing Value', 1, ''),
(49, '2013-04-09 14:33:21', 1, 15, '38', 'Coarse Aggregates & Fine Aggregates (Delterious Material)', 1, ''),
(50, '2013-04-09 14:34:41', 1, 16, '77', 'Coarse Aggregates & Fine Aggregates (Delterious Material)', 1, ''),
(51, '2013-04-10 14:45:36', 1, 15, '39', 'Coarse Sand', 1, ''),
(52, '2013-04-10 14:46:42', 1, 16, '78', 'F.M', 1, ''),
(53, '2013-04-10 14:47:56', 1, 16, '79', 'Silt Content', 1, ''),
(54, '2013-04-10 16:04:57', 1, 15, '40', 'Wood', 1, ''),
(55, '2013-04-10 16:06:32', 1, 15, '40', 'Wood', 3, ''),
(56, '2013-04-10 16:09:43', 1, 16, '80', 'Moisture Content', 1, ''),
(57, '2013-04-10 16:10:35', 1, 16, '81', '24 Hour Water absorption', 1, ''),
(58, '2013-04-10 16:11:14', 1, 16, '82', '2 Hour Swelling in Water', 1, ''),
(59, '2013-04-10 16:12:08', 1, 16, '83', 'Cigarette Burn Resistance', 1, ''),
(60, '2013-04-10 16:14:38', 1, 15, '41', 'Laminated Particle Board Grade-I, Type-II', 1, ''),
(61, '2013-04-10 16:15:28', 1, 16, '84', 'Moisture Content', 1, ''),
(62, '2013-04-10 16:15:50', 1, 16, '85', '24 Hour Water absorption', 1, ''),
(63, '2013-04-10 16:16:23', 1, 16, '86', '2 Hour Swelling in Water', 1, ''),
(64, '2013-04-10 16:16:57', 1, 16, '87', 'Cigarette Burn Resistance', 1, ''),
(65, '2013-04-10 16:43:07', 1, 16, '80', 'Moisture Content', 3, ''),
(66, '2013-04-10 16:43:07', 1, 16, '81', '24 Hour Water absorption', 3, ''),
(67, '2013-04-10 16:43:07', 1, 16, '82', '2 Hour Swelling in Water', 3, ''),
(68, '2013-04-10 16:43:07', 1, 16, '83', 'Cigarette Burn Resistance', 3, ''),
(69, '2013-04-12 11:12:50', 1, 15, '42', 'Corase Aggregate (Deleterious Material)', 1, ''),
(70, '2013-04-12 11:13:34', 1, 15, '43', 'Fine Aggregates (Deleterious Material)', 1, ''),
(71, '2013-04-12 11:16:06', 1, 16, '88', 'Deleterious Material', 1, ''),
(72, '2013-04-12 11:16:27', 1, 16, '89', 'Deleterious Material', 1, ''),
(73, '2013-04-12 11:22:18', 1, 16, '90', 'Gradation/Determination of Particle size', 1, ''),
(74, '2013-04-12 11:48:28', 1, 15, '44', 'Checking of Revised Drawing', 1, ''),
(75, '2013-04-12 11:49:41', 1, 16, '91', 'Checking of Revised Drawing', 1, ''),
(76, '2013-04-12 16:29:50', 1, 12, '10', 'Electronics and Communication', 1, ''),
(77, '2013-04-12 16:30:21', 1, 14, '10', 'Electronics', 1, ''),
(78, '2013-04-12 16:34:30', 1, 15, '45', 'Six Week Training (Electronic Circuit Design using VHDL)', 1, ''),
(79, '2013-04-12 16:44:56', 1, 16, '92', 'Six Weeks Training', 1, ''),
(80, '2013-04-12 16:47:35', 1, 35, '15', 'Er. Nirmal Singh grewal', 1, ''),
(81, '2013-04-12 16:53:40', 1, 35, '16', 'Er. Narwant Singh grewal', 1, ''),
(82, '2013-04-12 16:55:15', 1, 35, '17', 'Er. Harminder Kaur', 1, ''),
(83, '2013-04-12 16:55:54', 1, 35, '18', 'Er. Gurjot Kaur Walia', 1, ''),
(84, '2013-04-12 16:56:46', 1, 35, '19', 'Er. Rohin Gupta', 1, ''),
(85, '2013-04-12 16:57:24', 1, 35, '20', 'Er. Navneet Kaur', 1, ''),
(86, '2013-04-12 16:57:58', 1, 35, '21', 'Ms. Gagandeep Kaur', 1, ''),
(87, '2013-04-12 16:58:27', 1, 35, '22', 'Mr. Jaspal Singh', 1, ''),
(88, '2013-04-27 18:58:07', 1, 63, '1', 'testing of', 1, ''),
(89, '2013-04-27 18:58:16', 1, 63, '2', 'preparation of', 1, ''),
(90, '2013-04-27 18:58:20', 1, 63, '3', ' ', 1, '');

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=65 ;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `name`, `app_label`, `model`) VALUES
(1, 'permission', 'auth', 'permission'),
(2, 'group', 'auth', 'group'),
(3, 'user', 'auth', 'user'),
(4, 'content type', 'contenttypes', 'contenttype'),
(5, 'session', 'sessions', 'session'),
(6, 'site', 'sites', 'site'),
(7, 'log entry', 'admin', 'logentry'),
(8, 'registration profile', 'registration', 'registrationprofile'),
(9, 'report', 'tcc', 'report'),
(10, 'user profile', 'tcc', 'userprofile'),
(11, 'organisation', 'tcc', 'organisation'),
(12, 'department', 'tcc', 'department'),
(13, 'distribution', 'tcc', 'distribution'),
(14, 'lab', 'tcc', 'lab'),
(15, 'material', 'tcc', 'material'),
(16, 'test', 'tcc', 'test'),
(17, 'clientadd', 'tcc', 'clientadd'),
(18, 'edit clientadd', 'tcc', 'editclientadd'),
(19, 'govt', 'tcc', 'govt'),
(20, 'payment', 'tcc', 'payment'),
(21, 'job', 'tcc', 'job'),
(22, 'edit job', 'tcc', 'editjob'),
(23, 'client job', 'tcc', 'clientjob'),
(24, 'client edit job', 'tcc', 'clienteditjob'),
(25, 'suspence job', 'tcc', 'suspencejob'),
(26, 'suspence edit job', 'tcc', 'suspenceeditjob'),
(27, 'test total', 'tcc', 'testtotal'),
(28, 'test total perf', 'tcc', 'testtotalperf'),
(29, 'bill', 'tcc', 'bill'),
(30, 'bill perf', 'tcc', 'billperf'),
(31, 'amount', 'tcc', 'amount'),
(32, 'cdf amount', 'tcc', 'cdfamount'),
(33, 'distance', 'tcc', 'distance'),
(34, 'suspence', 'tcc', 'suspence'),
(35, 'staff', 'tcc', 'staff'),
(36, 'profroma tax', 'tcc', 'profromatax'),
(37, 'ta da', 'tcc', 'tada'),
(38, 'transportation', 'tcc', 'transportation'),
(39, 'transport', 'tcc', 'transport'),
(40, 'bankdetails', 'tcc', 'bankdetails'),
(41, 'tag', 'tagging', 'tag'),
(42, 'tagged item', 'tagging', 'taggeditem'),
(43, 'search', 'report', 'search'),
(44, 'report', 'report', 'report'),
(45, 'cube', 'report', 'cube'),
(46, 'chem_analysis', 'report', 'chem_analysis'),
(47, 'steel', 'report', 'steel'),
(48, 'ground_ water', 'report', 'ground_water'),
(49, 'concrete_ paver', 'report', 'concrete_paver'),
(50, 'interlock_ tiles', 'report', 'interlock_tiles'),
(51, 'pc', 'report', 'pc'),
(52, 'rebound_ hammer_ testing', 'report', 'rebound_hammer_testing'),
(53, 'brick', 'report', 'brick'),
(54, 'water', 'report', 'water'),
(55, 'soil_ ohsr', 'report', 'soil_ohsr'),
(56, 'soil_ building', 'report', 'soil_building'),
(57, 'admixture', 'report', 'admixture'),
(58, 'cement_ppc', 'report', 'cement_ppc'),
(59, 'cement_op c_33', 'report', 'cement_opc_33'),
(60, 'cement_op c_43', 'report', 'cement_opc_43'),
(61, 'cement_op c_53', 'report', 'cement_opc_53'),
(62, 'non payment job', 'tcc', 'nonpaymentjob'),
(63, 'mat comment', 'tcc', 'matcomment'),
(64, 'distanceperf', 'tcc', 'distanceperf');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_c25c2c28` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('14522114b15f5d0cf2aa99109031138c', 'MjM5OTY0MDJiOTc2NjRhMjBlZDM0NzZlNmRkOTlhZWQyOGQ2YTA5MzqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n', '2013-04-18 11:53:15'),
('2d7dccc09e5c6a39d135ecad5edcfbe9', 'M2FiNTNhOGY5M2YxZGRkYjk2ZmQxMTZmYTc3ZmRmMjE4ODFlODI0NjqAAn1xAShVDV9hdXRoX3Vz\nZXJfaWSKAQFVEl9hdXRoX3VzZXJfYmFja2VuZFUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxAnUu\n', '2013-04-27 10:12:51'),
('38ed284863e7f168e957062f210f213c', 'MjM5OTY0MDJiOTc2NjRhMjBlZDM0NzZlNmRkOTlhZWQyOGQ2YTA5MzqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n', '2013-06-25 14:01:10'),
('3e1b917cd7998945d4e43d8f81195fc1', 'OGEwM2FlMTdmZWEwZDdhODBlN2JlYjVmNDgyNzMzNzliNzIwMTk1ODqAAn1xAVUKdGVzdGNvb2tp\nZXECVQZ3b3JrZWRxA3Mu\n', '2013-04-15 13:54:55'),
('4872f25507e6876a4c0f54b5ccf0b783', 'ODY1ODAyYjFlZjc3YTdiZTIyZmJhZDFhZTE5YjIxMTNjNDQ2NmYyYjqAAn1xAS4=\n', '2013-04-13 17:28:01'),
('4d8ef7e38c9f4f30e387eef5d505d708', 'MjM5OTY0MDJiOTc2NjRhMjBlZDM0NzZlNmRkOTlhZWQyOGQ2YTA5MzqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n', '2013-04-16 15:56:03'),
('62ccbd03127ded68a3d2c2fe3b2ae2ff', 'MjM5OTY0MDJiOTc2NjRhMjBlZDM0NzZlNmRkOTlhZWQyOGQ2YTA5MzqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n', '2013-04-15 09:44:42'),
('64da5f62e534e47e810890c36a5305c2', 'MjM5OTY0MDJiOTc2NjRhMjBlZDM0NzZlNmRkOTlhZWQyOGQ2YTA5MzqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n', '2013-06-18 16:15:34'),
('68205f56e4d5d03343ba2714afc23fba', 'MjM5OTY0MDJiOTc2NjRhMjBlZDM0NzZlNmRkOTlhZWQyOGQ2YTA5MzqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n', '2013-05-11 18:57:10'),
('7b1429fb11105c0d302a3bf953930922', 'MjM5OTY0MDJiOTc2NjRhMjBlZDM0NzZlNmRkOTlhZWQyOGQ2YTA5MzqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n', '2013-05-31 17:12:03'),
('800d0548242e7bba981b55b9c5c585da', 'M2FiNTNhOGY5M2YxZGRkYjk2ZmQxMTZmYTc3ZmRmMjE4ODFlODI0NjqAAn1xAShVDV9hdXRoX3Vz\nZXJfaWSKAQFVEl9hdXRoX3VzZXJfYmFja2VuZFUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxAnUu\n', '2013-05-26 21:17:39'),
('94dda919b970a3bccaad9471cdc911f8', 'OGEwM2FlMTdmZWEwZDdhODBlN2JlYjVmNDgyNzMzNzliNzIwMTk1ODqAAn1xAVUKdGVzdGNvb2tp\nZXECVQZ3b3JrZWRxA3Mu\n', '2013-04-25 12:10:51'),
('9aea1ec259cdd61d7e409970d2035be2', 'M2FiNTNhOGY5M2YxZGRkYjk2ZmQxMTZmYTc3ZmRmMjE4ODFlODI0NjqAAn1xAShVDV9hdXRoX3Vz\nZXJfaWSKAQFVEl9hdXRoX3VzZXJfYmFja2VuZFUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxAnUu\n', '2013-04-15 10:53:21'),
('a40dd143b8d122c1a3c085c88a640a12', 'N2RmMTBlMDNjYzgwNDI0YTQ5NDI1NTUyNGZmOTQxOWJiNzIzZjVkOTqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQN1Lg==\n', '2013-04-14 19:46:55'),
('ab608e8f14acc7692064723d5343f52a', 'MjM5OTY0MDJiOTc2NjRhMjBlZDM0NzZlNmRkOTlhZWQyOGQ2YTA5MzqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n', '2013-04-13 17:51:34'),
('aba455275ae6630f8731a53697f6c15f', 'MjM5OTY0MDJiOTc2NjRhMjBlZDM0NzZlNmRkOTlhZWQyOGQ2YTA5MzqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n', '2013-04-14 16:28:38'),
('c5370a4db22eefc30928ed8ca504c878', 'MjM5OTY0MDJiOTc2NjRhMjBlZDM0NzZlNmRkOTlhZWQyOGQ2YTA5MzqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n', '2013-04-24 14:55:16'),
('c57587144f7ce2995a638b3fe58694bd', 'ODY1ODAyYjFlZjc3YTdiZTIyZmJhZDFhZTE5YjIxMTNjNDQ2NmYyYjqAAn1xAS4=\n', '2013-04-15 14:58:39'),
('d5b0c16cd5c9e516e47a13fcadf09481', 'MjM5OTY0MDJiOTc2NjRhMjBlZDM0NzZlNmRkOTlhZWQyOGQ2YTA5MzqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n', '2013-06-11 00:58:48'),
('e51734507cbe4d1fb448b3748fe4a7fa', 'MjM5OTY0MDJiOTc2NjRhMjBlZDM0NzZlNmRkOTlhZWQyOGQ2YTA5MzqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n', '2013-04-22 15:11:14'),
('f45b49e3a2cf8483ea10922bdf048111', 'MjM5OTY0MDJiOTc2NjRhMjBlZDM0NzZlNmRkOTlhZWQyOGQ2YTA5MzqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n', '2013-04-15 11:14:36'),
('f86ab6a419ae8c6b6618f675c8c8d5d6', 'MjM5OTY0MDJiOTc2NjRhMjBlZDM0NzZlNmRkOTlhZWQyOGQ2YTA5MzqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n', '2013-04-26 16:27:21');

-- --------------------------------------------------------

--
-- Table structure for table `django_site`
--

CREATE TABLE IF NOT EXISTS `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `django_site`
--

INSERT INTO `django_site` (`id`, `domain`, `name`) VALUES
(1, '192.168.15.178', '192.168.15.178');

-- --------------------------------------------------------

--
-- Table structure for table `registration_registrationprofile`
--

CREATE TABLE IF NOT EXISTS `registration_registrationprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `activation_key` varchar(40) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;

--
-- Dumping data for table `registration_registrationprofile`
--

INSERT INTO `registration_registrationprofile` (`id`, `user_id`, `activation_key`) VALUES
(1, 2, 'ALREADY_ACTIVATED'),
(2, 3, 'ALREADY_ACTIVATED'),
(3, 4, 'ALREADY_ACTIVATED'),
(4, 5, 'ALREADY_ACTIVATED'),
(5, 6, 'ALREADY_ACTIVATED'),
(6, 7, 'ALREADY_ACTIVATED'),
(7, 8, 'ALREADY_ACTIVATED');

-- --------------------------------------------------------

--
-- Table structure for table `tagging_tag`
--

CREATE TABLE IF NOT EXISTS `tagging_tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=167 ;

--
-- Dumping data for table `tagging_tag`
--

INSERT INTO `tagging_tag` (`id`, `name`) VALUES
(88, '&'),
(122, '(D60/D10)'),
(158, '(Deleterious'),
(146, '(Delterious'),
(107, '(OHSR)'),
(109, '(Treatment'),
(20, '0'),
(28, '1.5laclitre'),
(21, '10'),
(27, '1laclitre'),
(92, '2'),
(106, '2 week training (IT'),
(30, '2.5laclitre'),
(32, '20'),
(150, '24'),
(68, '2500'),
(24, '25000litre'),
(29, '2laclitre'),
(33, '30'),
(31, '5laclitre'),
(95, '6'),
(103, '6 months training (IT'),
(105, '6 week training (IT'),
(25, '75000'),
(26, '75000litre'),
(71, 'above'),
(52, 'abrasion'),
(38, 'absorption'),
(42, 'aggregate'),
(8, 'aggregates'),
(50, 'analysis'),
(77, 'angle'),
(99, 'area'),
(127, 'as'),
(85, 'ash'),
(72, 'barbed'),
(13, 'bc'),
(10, 'beams'),
(69, 'below'),
(115, 'Bitumen'),
(133, 'Blanketing'),
(113, 'BM'),
(112, 'BM/PC'),
(2, 'bricks'),
(153, 'Burn'),
(60, 'CBR'),
(12, 'cement'),
(79, 'channel'),
(164, 'Checking'),
(7, 'chemical'),
(154, 'Cigarette'),
(58, 'coarse'),
(123, 'Coefficient'),
(36, 'comp.'),
(66, 'compaction'),
(89, 'Computer'),
(116, 'Construction'),
(16, 'content'),
(159, 'Corase'),
(43, 'course'),
(144, 'CRB'),
(53, 'crushing'),
(104, 'CSE)'),
(44, 'cube'),
(67, 'cubes'),
(130, 'Curvature'),
(138, 'DBM'),
(46, 'deign'),
(160, 'Deleterious'),
(139, 'Density'),
(22, 'depth'),
(82, 'design'),
(108, 'Design(Building)'),
(70, 'dia'),
(165, 'Drawing'),
(39, 'effloroscence'),
(1, 'environment'),
(149, 'F.M'),
(9, 'fine'),
(18, 'fineness'),
(62, 'fines'),
(54, 'flakiness'),
(78, 'flat'),
(40, 'flexural'),
(86, 'fly'),
(14, 'for'),
(161, 'Gradation/Determination'),
(124, 'Graph'),
(56, 'gravity'),
(143, 'GSB'),
(136, 'Hammer'),
(102, 'hilly'),
(74, 'hing'),
(151, 'Hour'),
(55, 'impact'),
(128, 'in'),
(145, 'Index'),
(90, 'IT'),
(140, 'Lab'),
(117, 'Lab.'),
(156, 'Laminated Particle Board Grade-I'),
(64, 'limit'),
(120, 'Limit/Liquid'),
(65, 'liquid'),
(81, 'M-30'),
(83, 'M-40'),
(137, 'M.S.Plate'),
(98, 'material'),
(147, 'Material)'),
(134, 'Materials'),
(91, 'mba'),
(118, 'MDD'),
(47, 'mix'),
(84, 'mix design M-35'),
(19, 'modulus'),
(63, 'moisture'),
(96, 'months'),
(34, 'more'),
(132, 'of'),
(15, 'ohsr'),
(119, 'OMC'),
(162, 'Particle'),
(11, 'pavers'),
(114, 'PC'),
(129, 'per'),
(141, 'PI'),
(100, 'plain'),
(110, 'Plant)'),
(121, 'Plastic'),
(125, 'RDSO'),
(155, 'Resistance'),
(166, 'Revised'),
(148, 'Sand'),
(135, 'SDBC'),
(101, 'semi-hilly'),
(51, 'sieve'),
(17, 'silt'),
(163, 'size'),
(4, 'soil'),
(3, 'som'),
(59, 'soundness'),
(57, 'specific'),
(45, 'steel'),
(37, 'strength'),
(76, 'structural'),
(97, 'survey'),
(152, 'Swelling'),
(80, 'tees'),
(75, 'tension'),
(49, 'test'),
(41, 'tests'),
(35, 'than'),
(131, 'The'),
(111, 'Tiles'),
(23, 'to'),
(93, 'training'),
(157, 'Type-I'),
(126, 'Uniformity'),
(61, 'unsoaked'),
(142, 'Value'),
(5, 'waste water'),
(6, 'water'),
(94, 'week'),
(73, 'wire'),
(87, 'with'),
(48, 'wood');

-- --------------------------------------------------------

--
-- Table structure for table `tagging_taggeditem`
--

CREATE TABLE IF NOT EXISTS `tagging_taggeditem` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tag_id` int(11) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `object_id` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tag_id` (`tag_id`,`content_type_id`,`object_id`),
  KEY `tagging_taggeditem_3747b463` (`tag_id`),
  KEY `tagging_taggeditem_1bb8f392` (`content_type_id`),
  KEY `tagging_taggeditem_7d61c803` (`object_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=394 ;

--
-- Dumping data for table `tagging_taggeditem`
--

INSERT INTO `tagging_taggeditem` (`id`, `tag_id`, `content_type_id`, `object_id`) VALUES
(1, 1, 12, 1),
(8, 2, 13, 1),
(3, 3, 12, 2),
(4, 4, 12, 3),
(16, 4, 13, 5),
(5, 5, 12, 4),
(6, 6, 12, 4),
(80, 6, 13, 13),
(55, 6, 14, 17),
(68, 6, 14, 21),
(229, 6, 15, 25),
(213, 6, 16, 17),
(232, 6, 16, 56),
(344, 6, 16, 81),
(349, 6, 16, 82),
(360, 6, 16, 85),
(365, 6, 16, 86),
(7, 7, 12, 5),
(78, 7, 13, 12),
(9, 8, 13, 2),
(18, 8, 14, 1),
(225, 8, 15, 24),
(324, 8, 15, 38),
(375, 8, 15, 43),
(330, 8, 16, 77),
(10, 9, 13, 2),
(19, 9, 14, 1),
(116, 9, 14, 33),
(121, 9, 14, 34),
(123, 9, 14, 35),
(227, 9, 15, 24),
(326, 9, 15, 38),
(376, 9, 15, 43),
(332, 9, 16, 77),
(11, 10, 13, 3),
(12, 11, 13, 3),
(59, 11, 14, 19),
(63, 11, 14, 20),
(67, 11, 14, 21),
(295, 11, 15, 3),
(13, 12, 13, 4),
(69, 12, 14, 22),
(14, 13, 13, 5),
(15, 14, 13, 5),
(58, 14, 14, 19),
(62, 14, 14, 20),
(66, 14, 14, 21),
(179, 14, 14, 48),
(230, 14, 15, 25),
(233, 14, 16, 56),
(17, 15, 13, 6),
(27, 15, 14, 4),
(40, 15, 14, 13),
(45, 15, 14, 14),
(50, 15, 14, 15),
(20, 16, 14, 2),
(112, 16, 14, 32),
(223, 16, 16, 55),
(337, 16, 16, 79),
(340, 16, 16, 80),
(356, 16, 16, 84),
(21, 17, 14, 2),
(338, 17, 16, 79),
(22, 18, 14, 3),
(23, 19, 14, 3),
(24, 20, 14, 4),
(25, 21, 14, 4),
(37, 21, 14, 13),
(26, 22, 14, 4),
(39, 22, 14, 13),
(44, 22, 14, 14),
(48, 22, 14, 15),
(28, 23, 14, 4),
(41, 23, 14, 13),
(46, 23, 14, 14),
(29, 24, 14, 5),
(30, 25, 14, 6),
(31, 26, 14, 7),
(32, 27, 14, 8),
(33, 28, 14, 9),
(35, 30, 14, 11),
(36, 31, 14, 12),
(38, 32, 14, 13),
(42, 32, 14, 14),
(43, 33, 14, 14),
(47, 33, 14, 15),
(49, 34, 14, 15),
(51, 35, 14, 15),
(52, 36, 14, 16),
(57, 36, 14, 19),
(126, 36, 14, 36),
(210, 36, 16, 16),
(53, 37, 14, 16),
(60, 37, 14, 19),
(64, 37, 14, 20),
(128, 37, 14, 36),
(211, 37, 16, 16),
(54, 38, 14, 17),
(65, 38, 14, 21),
(212, 38, 16, 17),
(345, 38, 16, 81),
(361, 38, 16, 85),
(56, 39, 14, 18),
(214, 39, 16, 18),
(61, 40, 14, 20),
(70, 41, 14, 22),
(71, 42, 13, 7),
(85, 42, 14, 24),
(87, 42, 14, 25),
(90, 42, 14, 26),
(93, 42, 14, 27),
(96, 42, 14, 28),
(100, 42, 14, 29),
(105, 42, 14, 30),
(107, 42, 14, 31),
(111, 42, 14, 32),
(115, 42, 14, 33),
(119, 42, 14, 34),
(122, 42, 14, 35),
(371, 42, 15, 42),
(72, 43, 13, 7),
(82, 43, 14, 23),
(86, 43, 14, 24),
(88, 43, 14, 25),
(91, 43, 14, 26),
(94, 43, 14, 27),
(97, 43, 14, 28),
(73, 44, 13, 8),
(74, 45, 13, 9),
(132, 45, 14, 37),
(136, 45, 14, 38),
(138, 45, 14, 39),
(141, 45, 14, 40),
(143, 45, 14, 41),
(146, 45, 14, 42),
(148, 45, 14, 43),
(150, 45, 14, 44),
(75, 46, 13, 10),
(272, 46, 15, 10),
(76, 47, 13, 10),
(154, 47, 14, 45),
(160, 47, 14, 47),
(273, 47, 15, 10),
(220, 47, 15, 23),
(77, 48, 13, 11),
(339, 48, 15, 40),
(79, 49, 13, 12),
(103, 49, 14, 29),
(81, 50, 14, 23),
(110, 51, 14, 1),
(83, 51, 14, 23),
(84, 52, 14, 24),
(89, 53, 14, 25),
(320, 53, 16, 76),
(92, 54, 14, 26),
(318, 54, 16, 75),
(95, 55, 14, 27),
(98, 56, 14, 28),
(124, 56, 14, 35),
(99, 57, 14, 28),
(125, 57, 14, 35),
(101, 58, 14, 29),
(106, 58, 14, 30),
(108, 58, 14, 31),
(226, 58, 15, 24),
(325, 58, 15, 38),
(334, 58, 15, 39),
(331, 58, 16, 77),
(102, 59, 14, 29),
(104, 60, 14, 30),
(109, 61, 14, 31),
(113, 62, 14, 32),
(114, 63, 14, 32),
(341, 63, 16, 80),
(357, 63, 16, 84),
(117, 64, 14, 33),
(238, 64, 15, 27),
(245, 64, 16, 58),
(280, 64, 16, 62),
(118, 65, 14, 33),
(120, 66, 14, 34),
(127, 67, 14, 36),
(129, 68, 14, 37),
(133, 68, 14, 38),
(130, 69, 14, 37),
(131, 70, 14, 37),
(135, 70, 14, 38),
(134, 71, 14, 38),
(137, 72, 14, 39),
(139, 73, 14, 39),
(140, 74, 14, 40),
(142, 75, 14, 40),
(199, 76, 12, 9),
(202, 76, 13, 18),
(204, 76, 13, 19),
(208, 76, 13, 20),
(144, 76, 14, 41),
(145, 77, 14, 42),
(147, 78, 14, 43),
(149, 79, 14, 44),
(151, 80, 14, 44),
(152, 81, 14, 45),
(198, 82, 12, 9),
(201, 82, 13, 18),
(206, 82, 13, 20),
(153, 82, 14, 45),
(158, 82, 14, 47),
(155, 83, 14, 46),
(156, 84, 14, 46),
(157, 85, 14, 47),
(159, 86, 14, 47),
(161, 87, 14, 47),
(162, 88, 12, 6),
(218, 88, 15, 23),
(224, 88, 15, 24),
(234, 88, 15, 26),
(322, 88, 15, 38),
(241, 88, 16, 57),
(276, 88, 16, 61),
(328, 88, 16, 77),
(163, 89, 12, 6),
(164, 90, 12, 6),
(165, 91, 12, 7),
(346, 92, 16, 82),
(362, 92, 16, 86),
(175, 97, 12, 8),
(177, 97, 13, 17),
(181, 97, 14, 48),
(184, 97, 14, 49),
(187, 97, 14, 50),
(176, 98, 13, 17),
(313, 98, 15, 37),
(379, 98, 16, 88),
(381, 98, 16, 89),
(178, 99, 14, 48),
(182, 99, 14, 49),
(185, 99, 14, 50),
(180, 100, 14, 48),
(183, 101, 14, 49),
(186, 102, 14, 50),
(188, 103, 13, 16),
(194, 103, 14, 51),
(193, 104, 13, 14),
(191, 104, 13, 15),
(189, 104, 13, 16),
(195, 104, 14, 51),
(197, 104, 14, 52),
(190, 105, 13, 15),
(196, 105, 14, 52),
(192, 106, 13, 14),
(200, 107, 13, 18),
(203, 108, 13, 19),
(205, 109, 13, 20),
(207, 110, 13, 20),
(209, 111, 15, 21),
(215, 112, 15, 22),
(219, 113, 15, 23),
(296, 113, 15, 31),
(216, 113, 16, 53),
(298, 113, 16, 65),
(221, 114, 15, 23),
(304, 114, 15, 35),
(217, 114, 16, 54),
(305, 114, 16, 69),
(222, 115, 16, 55),
(228, 116, 15, 25),
(231, 116, 16, 56),
(235, 117, 15, 26),
(242, 117, 16, 57),
(277, 117, 16, 61),
(236, 118, 15, 26),
(243, 118, 16, 57),
(278, 118, 16, 61),
(237, 119, 15, 26),
(244, 119, 16, 57),
(279, 119, 16, 61),
(239, 120, 15, 27),
(246, 120, 16, 58),
(281, 120, 16, 62),
(240, 121, 15, 27),
(247, 121, 16, 58),
(282, 121, 16, 62),
(248, 122, 15, 28),
(260, 122, 16, 59),
(283, 122, 16, 63),
(249, 123, 15, 28),
(256, 123, 15, 29),
(261, 123, 16, 59),
(268, 123, 16, 60),
(284, 123, 16, 63),
(291, 123, 16, 64),
(250, 124, 15, 28),
(262, 124, 16, 59),
(285, 124, 16, 63),
(251, 125, 15, 28),
(263, 125, 16, 59),
(286, 125, 16, 63),
(252, 126, 15, 28),
(264, 126, 16, 59),
(287, 126, 16, 63),
(253, 127, 15, 28),
(265, 127, 16, 59),
(288, 127, 16, 63),
(254, 128, 15, 28),
(266, 128, 16, 59),
(289, 128, 16, 63),
(350, 128, 16, 82),
(366, 128, 16, 86),
(255, 129, 15, 28),
(267, 129, 16, 59),
(290, 129, 16, 63),
(257, 130, 15, 29),
(269, 130, 16, 60),
(292, 130, 16, 64),
(258, 131, 15, 29),
(270, 131, 16, 60),
(293, 131, 16, 64),
(259, 132, 15, 29),
(389, 132, 15, 44),
(271, 132, 16, 60),
(294, 132, 16, 64),
(384, 132, 16, 90),
(393, 132, 16, 91),
(274, 133, 15, 30),
(275, 134, 15, 30),
(297, 135, 15, 32),
(299, 135, 16, 66),
(300, 136, 15, 33),
(301, 136, 16, 67),
(302, 137, 15, 34),
(303, 137, 16, 68),
(306, 138, 15, 36),
(307, 138, 16, 70),
(308, 139, 16, 71),
(309, 140, 16, 71),
(310, 141, 16, 72),
(316, 141, 16, 74),
(311, 142, 16, 72),
(315, 142, 16, 73),
(317, 142, 16, 74),
(321, 142, 16, 76),
(312, 143, 15, 37),
(314, 144, 16, 73),
(319, 145, 16, 75),
(323, 146, 15, 38),
(329, 146, 16, 77),
(327, 147, 15, 38),
(373, 147, 15, 42),
(377, 147, 15, 43),
(333, 147, 16, 77),
(335, 148, 15, 39),
(336, 149, 16, 78),
(342, 150, 16, 81),
(358, 150, 16, 85),
(343, 151, 16, 81),
(347, 151, 16, 82),
(359, 151, 16, 85),
(363, 151, 16, 86),
(348, 152, 16, 82),
(364, 152, 16, 86),
(351, 153, 16, 83),
(367, 153, 16, 87),
(352, 154, 16, 83),
(368, 154, 16, 87),
(353, 155, 16, 83),
(369, 155, 16, 87),
(354, 156, 15, 41),
(355, 157, 15, 41),
(370, 158, 15, 42),
(374, 158, 15, 43),
(372, 159, 15, 42),
(378, 160, 16, 88),
(380, 160, 16, 89),
(382, 161, 16, 90),
(383, 162, 16, 90),
(385, 163, 16, 90),
(386, 164, 15, 44),
(390, 164, 16, 91),
(387, 165, 15, 44),
(391, 165, 16, 91),
(388, 166, 15, 44),
(392, 166, 16, 91);

-- --------------------------------------------------------

--
-- Table structure for table `tcc_amount`
--

CREATE TABLE IF NOT EXISTS `tcc_amount` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `job_id` int(11) NOT NULL,
  `college_income` int(11) DEFAULT NULL,
  `admin_charge` int(11) DEFAULT NULL,
  `consultancy_asst` int(11) DEFAULT NULL,
  `development_fund` int(11) DEFAULT NULL,
  `unit_price` int(11) DEFAULT NULL,
  `report_type` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tcc_amount_751f44ae` (`job_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `tcc_bankdetails`
--

CREATE TABLE IF NOT EXISTS `tcc_bankdetails` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `accname` varchar(50) NOT NULL,
  `accountno` int(11) NOT NULL,
  `accountcode` varchar(50) NOT NULL,
  `address` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `tcc_bill`
--

CREATE TABLE IF NOT EXISTS `tcc_bill` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `job_no` int(11) NOT NULL,
  `education_tax` int(11) DEFAULT NULL,
  `higher_education_tax` int(11) DEFAULT NULL,
  `service_tax` int(11) DEFAULT NULL,
  `net_total` int(11) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `discount_total` int(11) DEFAULT NULL,
  `trans_total` int(11) DEFAULT NULL,
  `trans_net_total` int(11) DEFAULT NULL,
  `balance` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `tcc_billperf`
--

CREATE TABLE IF NOT EXISTS `tcc_billperf` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `job_no` int(11) NOT NULL,
  `education_tax` int(11) DEFAULT NULL,
  `higher_education_tax` int(11) DEFAULT NULL,
  `service_tax` int(11) DEFAULT NULL,
  `net_total` int(11) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `discount_total` int(11) DEFAULT NULL,
  `trans_total` int(11) DEFAULT NULL,
  `trans_net_total` int(11) DEFAULT NULL,
  `balance` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `tcc_cdfamount`
--

CREATE TABLE IF NOT EXISTS `tcc_cdfamount` (
  `job_no` int(11) NOT NULL,
  `date` date NOT NULL,
  `lab` varchar(100) NOT NULL,
  `total` int(11) NOT NULL,
  `field` varchar(10) NOT NULL,
  `other_field` varchar(100) DEFAULT NULL,
  `report_type` varchar(20) NOT NULL,
  PRIMARY KEY (`job_no`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `tcc_clientadd`
--

CREATE TABLE IF NOT EXISTS `tcc_clientadd` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `client_id` int(11) NOT NULL,
  `job_no` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tcc_clientadd_fbfc09f1` (`user_id`),
  KEY `tcc_clientadd_4a4e8ffb` (`client_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `tcc_clienteditjob`
--

CREATE TABLE IF NOT EXISTS `tcc_clienteditjob` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `job_id` int(11) NOT NULL,
  `material_id` int(11) NOT NULL,
  `other_test` varchar(400) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tcc_clienteditjob_751f44ae` (`job_id`),
  KEY `tcc_clienteditjob_fab9ba43` (`material_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `tcc_clienteditjob_test`
--

CREATE TABLE IF NOT EXISTS `tcc_clienteditjob_test` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `clienteditjob_id` int(11) NOT NULL,
  `test_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `clienteditjob_id` (`clienteditjob_id`,`test_id`),
  KEY `tcc_clienteditjob_test_cbd9e9bb` (`clienteditjob_id`),
  KEY `tcc_clienteditjob_test_a88de8dc` (`test_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `tcc_clientjob`
--

CREATE TABLE IF NOT EXISTS `tcc_clientjob` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `job_id` int(11) NOT NULL,
  `material_id` int(11) NOT NULL,
  `other_test` varchar(400) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tcc_clientjob_751f44ae` (`job_id`),
  KEY `tcc_clientjob_fab9ba43` (`material_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `tcc_clientjob_test`
--

CREATE TABLE IF NOT EXISTS `tcc_clientjob_test` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `clientjob_id` int(11) NOT NULL,
  `test_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `clientjob_id` (`clientjob_id`,`test_id`),
  KEY `tcc_clientjob_test_244d514d` (`clientjob_id`),
  KEY `tcc_clientjob_test_a88de8dc` (`test_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `tcc_department`
--

CREATE TABLE IF NOT EXISTS `tcc_department` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `organisation_id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `address` varchar(150) NOT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `dean` varchar(50) DEFAULT NULL,
  `faxno` varchar(100) DEFAULT NULL,
  `email_1` varchar(75) NOT NULL,
  `email_2` varchar(75) NOT NULL,
  `url` varchar(50) NOT NULL,
  `about` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tcc_department_28b1ef86` (`organisation_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=11 ;

--
-- Dumping data for table `tcc_department`
--

INSERT INTO `tcc_department` (`id`, `organisation_id`, `name`, `address`, `phone`, `dean`, `faxno`, `email_1`, `email_2`, `url`, `about`) VALUES
(1, 1, 'Testing & Consultancy Cell', 'Gill Road, Gill Park, Ludhiana - 141006', '0161-2491193,5064509', 'Dr. Hardeep Singh Rai', '0161-5064742', 'tcc@gndec.ac.in', '', 'http//tcc.gndec.ac.in', 'Consultancy Services are being rendered by various Departments of the College to the industry, Sate Government Departments and Entrepreneurs and are extended in the form of expert advice in design, testing of materials & equipment, technical surveys, technical audit, caliberation of instruments, prepartion of technical feasibility reports etc.\\<br /\\>\\<br\\>\r\n\r\nThis consultancy cell of the college has given a new dimension to the development programmes of the College. Consultancy projects of over Rs. one crore are completed by the Consultancy cell during financial year 2009-10.<br><br>\r\n<a href="http://gndec.ac.in/~tcc/files/brochure.pdf">Brochure of TCC</a><br><br>\r\n<b>Courses</b><br><br>\r\nCurrent Session\r\n<ul>\r\n    \r\n</hr>\r\n    <li>AIEEE Crash Course View brochure March 26, 2012\r\n    <li>CAD course by Mechanical and Prod. Engineering Department April 30 - June 08, 2012\r\n    <li>Course on VHDL by Electronics and Comm. Engineering Department April 26 - June 06, 2012\r\n    <li>OOPs using C++ View brochure Register online Sept 12 - Nov 11, 2011\r\n</ul>\r\n\r\n   Previous Session<br>\r\n<ul>\r\n\r\n    <li>CAD course by Mechanical and Prod. Engineering Department June 13 - July 22, 2011\r\n    <li>Course on VHDL by Electronics and Comm. Engineering Department May 23 - July 01, 2011\r\n    <li>AIEEE Crash Course April 2011\r\n\r\n    <li>Course on Computer Aided Analysis and Design by Civil Engineering Department June 07 - June 18, 2010\r\n    <li>CAD course by Mechanical and Prod. Engineering Department June 07 - July 16, 2010\r\n    <li>Course by Electrical Engineering Department June 15 - July 25, 2010\r\n    <li>Course on Matlab by Electronics and Comm. Engineering Department June 07 - July 19, 2010\r\n    <li>Course on VHDL by Electronics and Comm. Engineering Department June 07 - July 19, 2010\r\n    <li>Course on PHP and MySQL by CSE and IT Department June 07 - July 19, 2010\r\n    <li>CET Crash Course April 2010\r\n</ul>'),
(2, 1, 'Civil Engineering', 'Gill Park, Gill Road, Ludhiana', '82347582', 'Dr. J.N. Jha', NULL, '', '', '', ''),
(5, 1, 'Mechanical Engineering', 'GNDEC,  Ludhiana', '', '', NULL, '', '', '', ''),
(6, 1, 'Computer Science Engineering & Information Technol', 'GNDEC,  Ludhiana', '', '', NULL, '', '', '', ''),
(7, 1, 'Electrical Engineering', 'GNDEC,  Ludhiana', '', '', NULL, '', '', '', ''),
(8, 1, 'Applied Sciences', 'GNDEC,  Ludhiana', '', '', NULL, '', '', '', ''),
(9, 1, 'MBA', 'GNDEC,  Ludhiana', '', '', NULL, '', '', '', ''),
(10, 1, 'Electronics and Communication', 'GNDEC, Ldh', '', 'Nirmal Singh Grewal', '', '', '', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `tcc_distance`
--

CREATE TABLE IF NOT EXISTS `tcc_distance` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `job` int(11) NOT NULL,
  `sandy` decimal(10,3) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `tcc_distanceperf`
--

CREATE TABLE IF NOT EXISTS `tcc_distanceperf` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `job` int(11) NOT NULL,
  `sandy` decimal(10,3) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `tcc_distribution`
--

CREATE TABLE IF NOT EXISTS `tcc_distribution` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `tcc_distribution`
--

INSERT INTO `tcc_distribution` (`id`, `name`) VALUES
(1, 'ROUTINE'),
(2, 'INSTITUTIONAL'),
(3, 'INDIVIDUAL');

-- --------------------------------------------------------

--
-- Table structure for table `tcc_editclientadd`
--

CREATE TABLE IF NOT EXISTS `tcc_editclientadd` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `client_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tcc_editclientadd_fbfc09f1` (`user_id`),
  KEY `tcc_editclientadd_4a4e8ffb` (`client_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `tcc_editjob`
--

CREATE TABLE IF NOT EXISTS `tcc_editjob` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `client_id` int(11) NOT NULL,
  `job_no` int(11) NOT NULL,
  `sample` varchar(11) NOT NULL,
  `ip` varchar(50) NOT NULL,
  `site` varchar(600) DEFAULT NULL,
  `type_of_work_id` int(11) NOT NULL,
  `report_type_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `letter_no` varchar(200) DEFAULT NULL,
  `letter_date` date DEFAULT NULL,
  `tds` int(11) NOT NULL,
  `discount` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tcc_editjob_4a4e8ffb` (`client_id`),
  KEY `tcc_editjob_ca5d2cd8` (`type_of_work_id`),
  KEY `tcc_editjob_3d4f9c7e` (`report_type_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `tcc_govt`
--

CREATE TABLE IF NOT EXISTS `tcc_govt` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(600) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `tcc_govt`
--

INSERT INTO `tcc_govt` (`id`, `name`) VALUES
(1, 'GOVERNMENT'),
(2, 'SEMI-GOVERNMENT'),
(3, 'PRIVATE');

-- --------------------------------------------------------

--
-- Table structure for table `tcc_job`
--

CREATE TABLE IF NOT EXISTS `tcc_job` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `client_id` int(11) NOT NULL,
  `job_no` int(11) NOT NULL,
  `sample` int(11) NOT NULL,
  `ip` varchar(50) NOT NULL,
  `site` varchar(5000) DEFAULT NULL,
  `type_of_work_id` int(11) NOT NULL,
  `report_type_id` int(11) NOT NULL,
  `pay` varchar(600) NOT NULL,
  `check_number` varchar(15) NOT NULL,
  `check_dd_date` varchar(15) NOT NULL,
  `date` date NOT NULL,
  `letter_no` varchar(400) NOT NULL,
  `letter_date` date DEFAULT NULL,
  `tds` int(11) NOT NULL,
  `discount` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tcc_job_4a4e8ffb` (`client_id`),
  KEY `tcc_job_ca5d2cd8` (`type_of_work_id`),
  KEY `tcc_job_3d4f9c7e` (`report_type_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `tcc_lab`
--

CREATE TABLE IF NOT EXISTS `tcc_lab` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(300) NOT NULL,
  `tags` varchar(255) NOT NULL,
  `department_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=11 ;

--
-- Dumping data for table `tcc_lab`
--

INSERT INTO `tcc_lab` (`id`, `name`, `tags`, `department_id`) VALUES
(1, 'ENVIRONMENT', 'environment', 2),
(2, 'SOM', 'som', 2),
(3, 'SOIL', 'soil', 2),
(4, 'WATER/WASTE WATER', 'water, waste water', 0),
(5, 'CHEMICAL', 'chemical', 0),
(6, 'IT & Computer', 'IT & Computer', 6),
(7, 'MBA ', 'mba', 9),
(8, 'Survey', 'survey', 2),
(9, 'Structural Design', 'Structural Design', 2),
(10, 'Electronics', '', 10);

-- --------------------------------------------------------

--
-- Table structure for table `tcc_matcomment`
--

CREATE TABLE IF NOT EXISTS `tcc_matcomment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(300) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `tcc_matcomment`
--

INSERT INTO `tcc_matcomment` (`id`, `name`) VALUES
(1, 'Testing of'),
(2, 'Preparation of'),
(3, ' ');

-- --------------------------------------------------------

--
-- Table structure for table `tcc_material`
--

CREATE TABLE IF NOT EXISTS `tcc_material` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lab_id` int(11) NOT NULL,
  `distribution_id` int(11) NOT NULL,
  `name` varchar(300) NOT NULL,
  `matcomment_id` int(11) NOT NULL,
  `tags` varchar(255) NOT NULL,
  `report_id` int(11) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tcc_material_4a1410c6` (`lab_id`),
  KEY `tcc_material_29fa1030` (`report_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=46 ;

--
-- Dumping data for table `tcc_material`
--

INSERT INTO `tcc_material` (`id`, `lab_id`, `distribution_id`, `name`, `matcomment_id`, `tags`, `report_id`, `image`) VALUES
(1, 2, 1, 'Bricks', 1, 'bricks', 1, ''),
(2, 3, 1, 'Fine Aggregate', 1, 'fine aggregates', 1, 'logo/fine.jpeg'),
(3, 2, 1, 'Pavers', 1, 'pavers', 1, 'logo/baka.png'),
(4, 2, 1, 'Cement', 1, 'cement', 1, ''),
(5, 3, 2, 'Soil for BC', 1, 'soil for bc', 2, ''),
(6, 3, 2, 'OHSR', 3, 'ohsr', 2, ''),
(7, 3, 1, 'Coarse Aggregate', 1, 'course aggregate', 1, 'logo/CAggregate.JPG'),
(8, 2, 1, 'Cubes', 1, 'cube', 1, ''),
(9, 2, 1, 'Steel', 1, 'steel', 1, ''),
(10, 2, 3, 'Mix Design', 2, 'mix deign', 1, 'logo/train.png'),
(11, 2, 2, 'Wood', 1, 'wood', 1, ''),
(12, 5, 2, 'Chemical testing', 3, 'chemical test', 1, ''),
(13, 1, 2, 'Water/Waster Water', 1, 'water', 1, ''),
(14, 6, 2, '2 week training (IT, CSE)', 3, '2 week training (IT, CSE)', 1, ''),
(15, 6, 2, '6 week training (IT, CSE)', 3, '6 week training (IT, CSE)', 1, ''),
(16, 6, 2, '6 months training (IT, CSE)', 3, '6 months training (IT, CSE)', 1, ''),
(17, 8, 2, 'Survey', 3, 'survey material', 2, ''),
(18, 9, 3, 'Structural Design (OHSR)', 2, 'Structural Design (OHSR)', 1, 'logo/Sunset-Ship1.jpg'),
(19, 9, 3, 'Structural Design(Building)', 2, 'Structural Design(Building)', 1, 'logo/ATT33506.jpg'),
(20, 9, 3, 'Structural Design (Treatment Plant)', 2, 'Structural Design (Treatment Plant)', 1, 'logo/failure.jpg'),
(21, 2, 1, 'Tiles', 1, 'Tiles', 1, 'logo/.png'),
(22, 3, 1, 'BM/PC', 1, 'BM/PC', 1, 'logo/SAM_0793.JPG'),
(23, 3, 1, 'BM & PC Mix', 1, 'BM & PC Mix', 1, 'logo/SAM_0793_1.JPG'),
(24, 3, 1, 'Coarse & Fine Aggregates', 1, 'Coarse & Fine Aggregates', 1, 'logo/SAM_0792.JPG'),
(25, 1, 2, 'Water for Construction', 1, 'Water for Construction', 1, 'logo/SAM_0795.JPG'),
(26, 3, 1, 'Soil Samples', 1, 'Soil Samples', 1, 'logo/SAM_0793_2.JPG'),
(27, 3, 1, 'Plastic Limit/Liquid Limit', 0, 'Plastic Limit/Liquid Limit', 1, 'logo/SAM_0795_1.JPG'),
(28, 3, 1, 'Uniformity Coefficient (D60/D10) in Graph as per RDSO', 0, 'Uniformity Coefficient (D60/D10) in Graph as per RDSO', 1, 'logo/SAM_0795_2.JPG'),
(29, 3, 1, 'The Coefficient of Curvature', 0, 'The Coefficient of Curvature', 1, 'logo/SAM_0795_3.JPG'),
(30, 3, 1, 'Blanketing Materials', 0, 'Blanketing Materials', 1, 'logo/SAM_0795_4.JPG'),
(31, 3, 1, 'BM', 0, 'BM', 1, 'logo/SAM_0795_5.JPG'),
(32, 3, 1, 'SDBC', 0, 'SDBC', 1, 'logo/SAM_0795_6.JPG'),
(33, 2, 2, 'Hammer', 0, 'Hammer', 2, 'logo/SAM_0795_7.JPG'),
(34, 2, 1, 'M.S.Plate', 0, 'M.S.Plate', 1, 'logo/SAM_0795_8.JPG'),
(35, 3, 1, 'PC', 0, 'PC', 1, 'logo/SAM_0795_9.JPG'),
(36, 3, 1, 'DBM', 0, 'DBM', 1, 'logo/skunkling-QUOTE.png'),
(37, 3, 1, 'GSB Material', 0, 'GSB Material', 1, 'logo/SAM_0795_10.JPG'),
(38, 1, 2, 'Coarse Aggregates & Fine Aggregates (Delterious Material)', 0, 'Coarse Aggregates & Fine Aggregates (Delterious Material)', 1, 'logo/1.JPG'),
(39, 3, 1, 'Coarse Sand', 0, 'Coarse Sand', 1, 'logo/1_1.JPG'),
(41, 2, 1, 'Laminated Particle Board Grade-I, Type-II', 0, 'Laminated Particle Board Grade-I, Type-I', 1, 'logo/1_3.JPG'),
(42, 1, 2, 'Corase Aggregate (Deleterious Material)', 0, 'Corase Aggregate (Deleterious Material)', 1, 'logo/SAM_0795_11.JPG'),
(43, 1, 2, 'Fine Aggregates (Deleterious Material)', 0, 'Fine Aggregates (Deleterious Material)', 1, 'logo/SAM_0795_12.JPG'),
(44, 9, 3, 'Checking of Revised Drawing', 0, 'Checking of Revised Drawing', 1, 'logo/SAM_0795_13.JPG'),
(45, 10, 2, 'Six Week Training (Electronic Circuit Design using VHDL)', 0, '', 1, 'logo/baka_1.png');

-- --------------------------------------------------------

--
-- Table structure for table `tcc_nonpaymentjob`
--

CREATE TABLE IF NOT EXISTS `tcc_nonpaymentjob` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `job_no` int(11) NOT NULL,
  `client_id` int(11) NOT NULL,
  `ref_no` varchar(400) NOT NULL,
  `dated` date DEFAULT NULL,
  `site` varchar(5000) DEFAULT NULL,
  `material_type` varchar(500) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tcc_nonpaymentjob_4a4e8ffb` (`client_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `tcc_organisation`
--

CREATE TABLE IF NOT EXISTS `tcc_organisation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `address` varchar(150) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `director` varchar(50) NOT NULL,
  `status` varchar(5000) NOT NULL,
  `logo_upload` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `tcc_organisation`
--

INSERT INTO `tcc_organisation` (`id`, `name`, `address`, `phone`, `director`, `status`, `logo_upload`) VALUES
(1, 'Guru Nanak Dev Engineering College', 'Gill Park, Gill Road, Ludhiana - 141006 ', '0161-2491193, 506450', 'Dr. M.S. Saini', 'Punjab Govt. Aided Status, NBA Accredited ISO-9001-2008 Certified', 'logo/gndeclogo.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `tcc_payment`
--

CREATE TABLE IF NOT EXISTS `tcc_payment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `tcc_payment`
--

INSERT INTO `tcc_payment` (`id`, `name`) VALUES
(1, 'CASH'),
(2, 'CHEQUE'),
(3, 'ONLINE'),
(4, 'DD');

-- --------------------------------------------------------

--
-- Table structure for table `tcc_profromatax`
--

CREATE TABLE IF NOT EXISTS `tcc_profromatax` (
  `pro_no` int(11) NOT NULL,
  `service_tax` int(11) NOT NULL,
  `higher_education_tax` int(11) NOT NULL,
  `education_tax` int(11) NOT NULL,
  `total` int(11) NOT NULL,
  PRIMARY KEY (`pro_no`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `tcc_report`
--

CREATE TABLE IF NOT EXISTS `tcc_report` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `tcc_report`
--

INSERT INTO `tcc_report` (`id`, `name`) VALUES
(1, 'LAB'),
(2, 'FIELD'),
(3, 'ADVANCE');

-- --------------------------------------------------------

--
-- Table structure for table `tcc_staff`
--

CREATE TABLE IF NOT EXISTS `tcc_staff` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `department_id` int(11) NOT NULL,
  `code` varchar(5) NOT NULL,
  `name` varchar(50) NOT NULL,
  `daily_income` int(11) NOT NULL,
  `position` varchar(100) NOT NULL,
  `lab_id` int(11) NOT NULL,
  `email` varchar(75) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tcc_staff_2ae7390` (`department_id`),
  KEY `tcc_staff_4a1410c6` (`lab_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=23 ;

--
-- Dumping data for table `tcc_staff`
--

INSERT INTO `tcc_staff` (`id`, `department_id`, `code`, `name`, `daily_income`, `position`, `lab_id`, `email`) VALUES
(1, 1, 'A', 'DR. J.N. Jha', 160, 'Prof.', 3, ''),
(2, 1, 'B', 'Prof. Kulbir Singh Gill', 120, 'A.P', 3, ''),
(3, 1, 'C', 'Dr. Jagbir Singh', 120, 'A.P', 2, ''),
(4, 1, 'D', 'Prof. Kanwaljit Singh Bedi', 120, 'A.P', 2, ''),
(5, 1, 'E', 'Dr. R.P.Singh', 100, 'A.P', 5, ''),
(6, 1, 'F', 'Prof.Puneet Pal  Singh', 100, 'AP', 1, ''),
(7, 2, 'G', 'Dr. Hardeep Singh Rai', 180, 'Prof.', 9, 'hsrai@gmail.com'),
(8, 2, '1', 'Sh. Amarjit Singh', 100, 'Mech.', 2, ''),
(9, 2, '2', 'Sh. Avtar Singh', 60, 'L.A', 2, ''),
(10, 2, '3', 'Sh. Nandan Singh', 60, 'L.A', 3, ''),
(11, 2, 'E', 'Dr. Harpal Singh', 120, 'Prof.', 9, ''),
(12, 2, 'G', 'Dr. HarvinderSingh', 120, 'Ass. Prof.', 9, ''),
(13, 2, 'H', 'Prof Prashant Garg', 120, 'Ass. Prof.', 9, ''),
(14, 2, '4', 'Sh. Balraj Singh', 60, 'Attendant ', 1, ''),
(15, 10, 'I', 'Er. Nirmal Singh grewal', 120, 'HOD', 10, ''),
(16, 10, 'J', 'Er. Narwant Singh grewal', 100, 'Coordinator & Lect.', 10, ''),
(17, 10, 'K', 'Er. Harminder Kaur', 100, 'Lect.', 10, ''),
(18, 10, 'L', 'Er. Gurjot Kaur Walia', 10, 'Lect.', 10, ''),
(19, 10, 'M', 'Er. Rohin Gupta', 100, 'Lect.', 10, ''),
(20, 10, 'N', 'Er. Navneet Kaur', 100, 'Lect.', 10, ''),
(21, 10, 'O', 'Ms. Gagandeep Kaur', 80, 'Lab Tech.', 10, ''),
(22, 10, 'P', 'Mr. Jaspal Singh', 80, 'Lab Attendent', 10, '');

-- --------------------------------------------------------

--
-- Table structure for table `tcc_suspence`
--

CREATE TABLE IF NOT EXISTS `tcc_suspence` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `job_id` int(11) NOT NULL,
  `rate` int(11) DEFAULT NULL,
  `sus_id` int(11) DEFAULT NULL,
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
  KEY `tcc_suspence_c13e1de8` (`sus_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `tcc_suspenceeditjob`
--

CREATE TABLE IF NOT EXISTS `tcc_suspenceeditjob` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `job_id` int(11) NOT NULL,
  `field_id` int(11) NOT NULL,
  `test_id` int(11) DEFAULT NULL,
  `other` varchar(600) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tcc_suspenceeditjob_751f44ae` (`job_id`),
  KEY `tcc_suspenceeditjob_b49f3317` (`field_id`),
  KEY `tcc_suspenceeditjob_a88de8dc` (`test_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `tcc_suspencejob`
--

CREATE TABLE IF NOT EXISTS `tcc_suspencejob` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `job_id` int(11) NOT NULL,
  `field_id` int(11) NOT NULL,
  `test_id` int(11) DEFAULT NULL,
  `other` varchar(600) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tcc_suspencejob_751f44ae` (`job_id`),
  KEY `tcc_suspencejob_b49f3317` (`field_id`),
  KEY `tcc_suspencejob_a88de8dc` (`test_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `tcc_tada`
--

CREATE TABLE IF NOT EXISTS `tcc_tada` (
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
  KEY `tcc_tada_751f44ae` (`job_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `tcc_test`
--

CREATE TABLE IF NOT EXISTS `tcc_test` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `material_id` int(11) NOT NULL,
  `name` varchar(300) NOT NULL,
  `quantity` int(11) DEFAULT NULL,
  `unit` varchar(15) NOT NULL,
  `cost` int(11) DEFAULT NULL,
  `tags` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tcc_test_54645bd` (`material_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=93 ;

--
-- Dumping data for table `tcc_test`
--

INSERT INTO `tcc_test` (`id`, `material_id`, `name`, `quantity`, `unit`, `cost`, `tags`) VALUES
(1, 2, 'Sieve Analysis  ', 3, 'kg', 800, 'fine aggregates sieve'),
(2, 2, 'SILT CONTENT', 3, 'kg', 800, 'silt content'),
(3, 2, 'FINENESS MODULUS', 3, 'kg', 800, 'fineness modulus'),
(4, 5, 'depth 0 to10', 6000, 'meter', 0, 'ohsr depth 0 to 10'),
(5, 6, ' 25000 Litre Capacity', 1, 'litre', 6000, '25000litre'),
(6, 6, '50000 Litres Capacity', 1, 'litre', 6000, '75000'),
(7, 6, '75000 Litre Capacity', 1, 'litre', 6000, '75000litre'),
(8, 6, '1.0 Lac Litres Capacity ', 1, 'litre', 8200, '1laclitre'),
(9, 6, '1.5 Lac Litres Capacity ', 1, 'litre', 8200, '1.5laclitre'),
(10, 6, '2.0 Lac Litres Capacity ', 1, 'litre', 8200, '2laclitre'),
(11, 6, '2.5 Lac Litres Capacity ', 1, 'litre', 8200, '2.5laclitre'),
(12, 6, '5.0 Lac Litres Capacity ', 1, 'litre', 10600, '5laclitre'),
(13, 5, 'depth 10 to 20 m', 6000, 'meter', 900, 'ohsr depth 10 to 20'),
(14, 5, 'depth 20 to 30 m', 6000, 'meter', 1200, 'ohsr depth 20 to 30'),
(15, 5, 'depth more than 30 m', 6000, 'meter', 1500, 'ohsr depth more than 30'),
(16, 1, 'Comp. Strength  ', 10, 'Bricks', 400, 'comp. strength'),
(17, 1, 'Water Absorption  ', 10, 'Bricks', 400, 'water absorption'),
(18, 1, 'Effloroscence  ', 10, 'Bricks', 400, 'effloroscence'),
(19, 3, 'Comp. Strength  ', 1, 'C.paver', 300, 'comp. strength for pavers'),
(20, 3, 'Flexural Strength  ', 1, 'C.paver', 300, 'flexural strength for pavers'),
(21, 3, 'Water Absorption  ', 1, 'C.paver', 300, 'water absorption for pavers'),
(22, 4, 'Initial & Final Setting time Comp. Strength (at 7 day’s  curing) , at 28 day’s curing, Soundness, Fineness, Consistency  ', 15, 'kg', 2500, 'cement tests'),
(23, 7, 'Sieve Analysis  ', 10, 'kg', 800, 'course sieve analysis'),
(24, 7, 'Abrasion Value  ', 10, 'kg', 800, 'course aggregate abrasion'),
(25, 7, 'Crushing Value/Strength', 10, 'kg', 800, 'course aggregate crushing'),
(26, 7, 'Flakiness Index  ', 10, 'kg', 800, 'course aggregate flakiness'),
(27, 7, 'Impact Value  ', 5, 'kg', 800, 'course aggregate impact'),
(28, 7, 'Specific Gravity  ', 5, 'kg', 800, 'course aggregate specific gravity'),
(29, 7, 'Soundness Tests  ', 5, 'kg', 800, 'coarse aggregate soundness test'),
(30, 7, 'C.B.R. Test  (Soaked)  ', 10, 'kg', 1800, 'coarse aggregate CBR '),
(31, 7, 'C.B.R. Test  (Unsoaked)  ', 10, 'kg', 1800, 'coarse aggregate unsoaked'),
(32, 2, 'Moisture  Content  ', 3, 'kg', 800, 'fines aggregate moisture content'),
(33, 2, 'Liquid Limit &  Plastic Limit  ', 3, 'kg', 800, 'fine aggregate liquid limit'),
(34, 2, 'Compaction Test  (Dry Bulk Density)  ', 5, 'kg', 1500, 'fine aggregate compaction'),
(35, 2, 'Specific Gravity  ', 5, 'kg', 800, 'fine aggregate specific gravity'),
(36, 8, 'Comp. Strength  ', 3, 'Cubes', 500, 'cubes comp. strength'),
(37, 9, 'a) Ultimate Tensile Strength, b) Percentage Elongation, c) Bend test,  d) 0.2 Proof Stress  below 25 mm dia  ', 2, 'feet', 1500, 'steel below 2500 dia'),
(38, 9, 'a) Ultimate Tensile Strength, b) Percentage Elongation, c) Bend test,  d) 0.2 Proof Stress 25 mm & above   ', 2, 'feet', 2500, 'steel above 2500 dia'),
(39, 9, 'Barbed Wire ', 2, 'feet', 2500, 'steel barbed wire'),
(40, 9, 'Hing Tension', 2, 'feet', 2500, 'steel hing tension'),
(41, 9, 'Structural', 2, 'feet', 2500, 'steel structural'),
(42, 9, 'Angle', 2, 'feet', 2500, 'steel angle'),
(43, 9, 'Flats ', 2, 'feet', 2500, 'steel flat'),
(44, 9, 'Tees Channel ', 2, 'feet', 2500, 'steel tees channel'),
(45, 10, 'Mix Design upto M-30', 1, 'Bag', 8000, 'mix design M-30'),
(46, 10, 'Mix Design M-35 & M-40', 2, 'Bag', 10000, 'mix design M-35, M-40'),
(47, 10, 'Mix Design with fly ash', 2, 'Bag', 15000, 'mix design with fly ash'),
(48, 17, 'Plain area ', 1, 'acre', 1000, 'survey for plain area'),
(49, 17, 'Semi-Hilly area ', 1, 'acre', 1500, 'survey semi-hilly area'),
(50, 17, 'Hilly area ', 1, 'acre', 2000, 'survey hilly area'),
(51, 16, '6 months training ', 6, 'months', 6000, '6 months training (IT, CSE)'),
(52, 15, '6 week training ', 6, 'week', 2000, '6 week training (IT, CSE)'),
(53, 22, 'BM', 10, 'Kg', 1500, 'BM'),
(54, 22, 'PC', 10, 'Kg', 1500, 'PC'),
(55, 23, 'Bitumen Content', 10, 'Kg', 1500, 'Bitumen Content'),
(56, 25, 'Water for Construction', 10, 'Litres', 1500, 'Water for Construction'),
(57, 26, 'Lab. MDD & OMC', 15, 'kg', 1800, 'Lab. MDD & OMC'),
(58, 27, 'Plastic Limit/Liquid Limit', 15, 'kg', 800, 'Plastic Limit/Liquid Limit'),
(59, 28, 'Uniformity Coefficient (D60/D10) in Graph as per RDSO', 15, 'Kg', 800, 'Uniformity Coefficient (D60/D10) in Graph as per RDSO'),
(60, 29, 'The Coefficient of Curvature', 15, 'kg', 800, 'The Coefficient of Curvature'),
(61, 30, 'Lab. MDD & OMC', 15, 'Kg', 1800, 'Lab. MDD & OMC'),
(62, 30, 'Plastic Limit/Liquid Limit', 15, 'kg', 800, 'Plastic Limit/Liquid Limit'),
(63, 30, 'Uniformity Coefficient (D60/D10) in Graph as per RDSO', 15, 'Kg', 800, 'Uniformity Coefficient (D60/D10) in Graph as per RDSO'),
(64, 30, 'The Coefficient of Curvature', 15, 'Kg', 800, 'The Coefficient of Curvature'),
(65, 31, 'BM', 15, 'Kg', 1500, 'BM'),
(66, 32, 'SDBC', 15, 'Kg', 1500, 'SDBC'),
(67, 33, ' Hammer', 0, 'o', 10000, 'Hammer'),
(68, 34, 'M.S.Plate', 1, 'm', 2500, 'M.S.Plate'),
(69, 35, 'PC', 15, 'Kg', 1500, 'PC'),
(70, 36, 'DBM', 15, 'kg', 1500, 'DBM'),
(71, 26, 'Lab Density', 15, 'Kg', 1800, 'Lab Density'),
(72, 26, 'PI Value', 15, 'Kg', 800, 'PI Value'),
(73, 37, 'CRB Value', 15, 'Kg', 1800, 'CRB Value'),
(74, 37, 'PI Value', 15, 'Kg', 800, 'PI Value'),
(75, 2, 'Flakiness Index', 15, 'Kg', 800, 'Flakiness Index'),
(76, 2, 'Crushing Value', 15, 'Kg', 800, 'Crushing Value'),
(77, 38, 'Coarse Aggregates & Fine Aggregates (Delterious Material)', 15, 'Kg', 1500, 'Coarse Aggregates & Fine Aggregates (Delterious Material)'),
(78, 39, 'F.M', 15, 'Kg', 800, 'F.M'),
(79, 39, 'Silt Content', 15, 'Kg', 800, 'Silt Content'),
(84, 41, 'Moisture Content', 1, 'Pc', 800, 'Moisture Content'),
(85, 41, '24 Hour Water absorption', 1, 'Pc', 800, '24 Hour Water absorption'),
(86, 41, '2 Hour Swelling in Water', 1, 'Pc', 800, '2 Hour Swelling in Water'),
(87, 41, 'Cigarette Burn Resistance', 1, 'Pc', 800, 'Cigarette Burn Resistance'),
(88, 42, 'Deleterious Material', 15, 'Kg', 1500, 'Deleterious Material'),
(89, 43, 'Deleterious Material', 15, 'Kg', 1500, 'Deleterious Material'),
(90, 2, 'Gradation/Determination of Particle size', 15, 'Kg', 800, 'Gradation/Determination of Particle size'),
(91, 44, 'Checking of Revised Drawing', 1, 'drawing', 15000, 'Checking of Revised Drawing'),
(92, 45, 'Six Weeks Training', 1, 'No.', 4450, '');

-- --------------------------------------------------------

--
-- Table structure for table `tcc_testtotal`
--

CREATE TABLE IF NOT EXISTS `tcc_testtotal` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `job_id` int(11) NOT NULL,
  `unit_price` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tcc_testtotal_751f44ae` (`job_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `tcc_testtotalperf`
--

CREATE TABLE IF NOT EXISTS `tcc_testtotalperf` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `job_id` int(11) NOT NULL,
  `unit_price` int(11) DEFAULT NULL,
  `rate` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tcc_testtotalperf_751f44ae` (`job_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `tcc_transport`
--

CREATE TABLE IF NOT EXISTS `tcc_transport` (
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
  KEY `tcc_transport_4bffff7` (`vehicle_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `tcc_transportation`
--

CREATE TABLE IF NOT EXISTS `tcc_transportation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `vehicleno` varchar(150) NOT NULL,
  `rate` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `tcc_userprofile`
--

CREATE TABLE IF NOT EXISTS `tcc_userprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `middle_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `company` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `pin_code` int(11) DEFAULT NULL,
  `state` varchar(30) NOT NULL,
  `website` varchar(200) DEFAULT NULL,
  `email_address` varchar(75) DEFAULT NULL,
  `contact_no` varchar(500) NOT NULL,
  `type_of_organisation` varchar(20) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tcc_userprofile_fbfc09f1` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `group_id_refs_id_3cea63fe` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `permission_id_refs_id_a7792de1` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `content_type_id_refs_id_728de91f` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `group_id_refs_id_f0ee9890` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `user_id_refs_id_831107f1` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `permission_id_refs_id_67e79cb` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `user_id_refs_id_f2045483` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `content_type_id_refs_id_288599e6` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `user_id_refs_id_c8665aa` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `registration_registrationprofile`
--
ALTER TABLE `registration_registrationprofile`
  ADD CONSTRAINT `user_id_refs_id_cecd7f3c` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `tcc_amount`
--
ALTER TABLE `tcc_amount`
  ADD CONSTRAINT `job_id_refs_id_6018e7df` FOREIGN KEY (`job_id`) REFERENCES `tcc_job` (`id`);

--
-- Constraints for table `tcc_clientadd`
--
ALTER TABLE `tcc_clientadd`
  ADD CONSTRAINT `user_id_refs_id_8335da6c` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `client_id_refs_id_7f3a75eb` FOREIGN KEY (`client_id`) REFERENCES `tcc_userprofile` (`id`);

--
-- Constraints for table `tcc_clienteditjob`
--
ALTER TABLE `tcc_clienteditjob`
  ADD CONSTRAINT `material_id_refs_id_cac842a5` FOREIGN KEY (`material_id`) REFERENCES `tcc_material` (`id`),
  ADD CONSTRAINT `job_id_refs_id_eea896a0` FOREIGN KEY (`job_id`) REFERENCES `tcc_editjob` (`id`);

--
-- Constraints for table `tcc_clienteditjob_test`
--
ALTER TABLE `tcc_clienteditjob_test`
  ADD CONSTRAINT `clienteditjob_id_refs_id_8826c265` FOREIGN KEY (`clienteditjob_id`) REFERENCES `tcc_clienteditjob` (`id`),
  ADD CONSTRAINT `test_id_refs_id_92a6bad2` FOREIGN KEY (`test_id`) REFERENCES `tcc_test` (`id`);

--
-- Constraints for table `tcc_clientjob`
--
ALTER TABLE `tcc_clientjob`
  ADD CONSTRAINT `material_id_refs_id_d47d0f5b` FOREIGN KEY (`material_id`) REFERENCES `tcc_material` (`id`),
  ADD CONSTRAINT `job_id_refs_id_cf851ff0` FOREIGN KEY (`job_id`) REFERENCES `tcc_job` (`id`);

--
-- Constraints for table `tcc_clientjob_test`
--
ALTER TABLE `tcc_clientjob_test`
  ADD CONSTRAINT `clientjob_id_refs_id_8691d49b` FOREIGN KEY (`clientjob_id`) REFERENCES `tcc_clientjob` (`id`),
  ADD CONSTRAINT `test_id_refs_id_fbfdbbd2` FOREIGN KEY (`test_id`) REFERENCES `tcc_test` (`id`);

--
-- Constraints for table `tcc_editclientadd`
--
ALTER TABLE `tcc_editclientadd`
  ADD CONSTRAINT `user_id_refs_id_277f0ac4` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `client_id_refs_id_fd489edd` FOREIGN KEY (`client_id`) REFERENCES `tcc_userprofile` (`id`);

--
-- Constraints for table `tcc_editjob`
--
ALTER TABLE `tcc_editjob`
  ADD CONSTRAINT `report_type_id_refs_id_715128a7` FOREIGN KEY (`report_type_id`) REFERENCES `tcc_report` (`id`),
  ADD CONSTRAINT `client_id_refs_id_475d7782` FOREIGN KEY (`client_id`) REFERENCES `tcc_editclientadd` (`id`),
  ADD CONSTRAINT `type_of_work_id_refs_id_3ff866ab` FOREIGN KEY (`type_of_work_id`) REFERENCES `tcc_govt` (`id`);

--
-- Constraints for table `tcc_job`
--
ALTER TABLE `tcc_job`
  ADD CONSTRAINT `client_id_refs_id_fd23af76` FOREIGN KEY (`client_id`) REFERENCES `tcc_clientadd` (`id`),
  ADD CONSTRAINT `report_type_id_refs_id_bd662a09` FOREIGN KEY (`report_type_id`) REFERENCES `tcc_report` (`id`),
  ADD CONSTRAINT `type_of_work_id_refs_id_4da5e95b` FOREIGN KEY (`type_of_work_id`) REFERENCES `tcc_govt` (`id`);

--
-- Constraints for table `tcc_nonpaymentjob`
--
ALTER TABLE `tcc_nonpaymentjob`
  ADD CONSTRAINT `client_id_refs_id_c048bcad` FOREIGN KEY (`client_id`) REFERENCES `tcc_userprofile` (`id`);

--
-- Constraints for table `tcc_suspence`
--
ALTER TABLE `tcc_suspence`
  ADD CONSTRAINT `sus_id_refs_id_4acb203f` FOREIGN KEY (`sus_id`) REFERENCES `tcc_suspencejob` (`id`),
  ADD CONSTRAINT `job_id_refs_id_25fd0307` FOREIGN KEY (`job_id`) REFERENCES `tcc_job` (`id`);

--
-- Constraints for table `tcc_suspenceeditjob`
--
ALTER TABLE `tcc_suspenceeditjob`
  ADD CONSTRAINT `field_id_refs_id_8efd9e88` FOREIGN KEY (`field_id`) REFERENCES `tcc_material` (`id`),
  ADD CONSTRAINT `job_id_refs_id_7e90c6bd` FOREIGN KEY (`job_id`) REFERENCES `tcc_editjob` (`id`),
  ADD CONSTRAINT `test_id_refs_id_84316b4f` FOREIGN KEY (`test_id`) REFERENCES `tcc_test` (`id`);

--
-- Constraints for table `tcc_suspencejob`
--
ALTER TABLE `tcc_suspencejob`
  ADD CONSTRAINT `field_id_refs_id_f9dd1268` FOREIGN KEY (`field_id`) REFERENCES `tcc_material` (`id`),
  ADD CONSTRAINT `job_id_refs_id_cafb41b3` FOREIGN KEY (`job_id`) REFERENCES `tcc_job` (`id`),
  ADD CONSTRAINT `test_id_refs_id_faa2f6f` FOREIGN KEY (`test_id`) REFERENCES `tcc_test` (`id`);

--
-- Constraints for table `tcc_tada`
--
ALTER TABLE `tcc_tada`
  ADD CONSTRAINT `job_id_refs_id_67cf5ad5` FOREIGN KEY (`job_id`) REFERENCES `tcc_job` (`id`);

--
-- Constraints for table `tcc_testtotal`
--
ALTER TABLE `tcc_testtotal`
  ADD CONSTRAINT `job_id_refs_id_4aaa37b8` FOREIGN KEY (`job_id`) REFERENCES `tcc_job` (`id`);

--
-- Constraints for table `tcc_testtotalperf`
--
ALTER TABLE `tcc_testtotalperf`
  ADD CONSTRAINT `job_id_refs_id_56adbb8d` FOREIGN KEY (`job_id`) REFERENCES `tcc_editjob` (`id`);

--
-- Constraints for table `tcc_transport`
--
ALTER TABLE `tcc_transport`
  ADD CONSTRAINT `vehicle_id_refs_id_b0f5c5` FOREIGN KEY (`vehicle_id`) REFERENCES `tcc_transportation` (`id`);

--
-- Constraints for table `tcc_userprofile`
--
ALTER TABLE `tcc_userprofile`
  ADD CONSTRAINT `user_id_refs_id_3f595074` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
