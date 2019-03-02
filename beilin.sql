/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 80012
Source Host           : localhost:3306
Source Database       : beilinpc

Target Server Type    : MYSQL
Target Server Version : 80012
File Encoding         : 65001

Date: 2018-12-20 11:48:17
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------
INSERT INTO `auth_group` VALUES ('1', 'external_recorder');
INSERT INTO `auth_group` VALUES ('2', 'baseline_admin');

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------
INSERT INTO `auth_group_permissions` VALUES ('1', '1', '1');
INSERT INTO `auth_group_permissions` VALUES ('2', '1', '4');
INSERT INTO `auth_group_permissions` VALUES ('3', '2', '1');
INSERT INTO `auth_group_permissions` VALUES ('4', '2', '2');
INSERT INTO `auth_group_permissions` VALUES ('5', '2', '3');
INSERT INTO `auth_group_permissions` VALUES ('6', '2', '4');

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=33 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can view log entry', '1', 'view_logentry');
INSERT INTO `auth_permission` VALUES ('5', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('8', 'Can view permission', '2', 'view_permission');
INSERT INTO `auth_permission` VALUES ('9', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('11', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('12', 'Can view group', '3', 'view_group');
INSERT INTO `auth_permission` VALUES ('13', 'Can add user', '4', 'add_user');
INSERT INTO `auth_permission` VALUES ('14', 'Can change user', '4', 'change_user');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete user', '4', 'delete_user');
INSERT INTO `auth_permission` VALUES ('16', 'Can view user', '4', 'view_user');
INSERT INTO `auth_permission` VALUES ('17', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('18', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('19', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('20', 'Can view content type', '5', 'view_contenttype');
INSERT INTO `auth_permission` VALUES ('21', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('22', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('23', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('24', 'Can view session', '6', 'view_session');
INSERT INTO `auth_permission` VALUES ('25', 'Can add 单位基本情况', '7', 'add_companies');
INSERT INTO `auth_permission` VALUES ('26', 'Can change 单位基本情况', '7', 'change_companies');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete 单位基本情况', '7', 'delete_companies');
INSERT INTO `auth_permission` VALUES ('28', 'Can view 单位基本情况', '7', 'view_companies');
INSERT INTO `auth_permission` VALUES ('29', 'Can add 人工录入单位基本情况', '8', 'add_companyinfo');
INSERT INTO `auth_permission` VALUES ('30', 'Can change 人工录入单位基本情况', '8', 'change_companyinfo');
INSERT INTO `auth_permission` VALUES ('31', 'Can delete 人工录入单位基本情况', '8', 'delete_companyinfo');
INSERT INTO `auth_permission` VALUES ('32', 'Can view 人工录入单位基本情况', '8', 'view_companyinfo');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  `last_name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=30 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$120000$lOC0vgNAzk1B$lDSNrr1NSSUmxZilf89NaLUDqynmPi+WlQ5bJxFWHMU=', '2018-12-20 03:46:57', '1', 'wenshi', '', 'ws@gmail.com', '1', '1', '2018-12-10 03:53:28', '');
INSERT INTO `auth_user` VALUES ('2', 'pbkdf2_sha256$120000$3r3RIyFuaM0I$FhIIJoO5Z/tMuk9E6d1fSUz1DIGTsK39mx3SjHmhad0=', '2018-12-11 06:56:36', '0', 'external_recorder_1', '', '', '1', '1', '2018-12-10 06:37:00', '');
INSERT INTO `auth_user` VALUES ('3', 'pbkdf2_sha256$120000$wn8g40Ad6Y6J$VXE0UbvJ4fDn+CYGw4vgmmIBTgnVirus3OqIQLjAJKg=', '2018-12-11 06:56:33', '0', 'external_recorder_2', '', '', '1', '1', '2018-12-10 06:38:00', '');
INSERT INTO `auth_user` VALUES ('4', 'pbkdf2_sha256$120000$hLsmLt9LMfst$hBPR4/YjShyrf8b2L8p5jczcx/FpPh2FlT5dwgH97xs=', '2018-12-11 06:55:54', '0', 'wangying', '', '', '1', '1', '2018-12-10 06:50:00', '');
INSERT INTO `auth_user` VALUES ('5', 'pbkdf2_sha256$120000$QQUsHluQ8hCM$ukYMwVpV6j8IjLMJhrDQiQbyLVH/dvDreVR6tfLjzz4=', '2018-12-11 06:56:00', '0', 'zhangyu', '', '', '1', '1', '2018-12-10 06:51:00', '');
INSERT INTO `auth_user` VALUES ('6', 'pbkdf2_sha256$120000$u9snnUuC0xOA$ccq9bSSB1aswxZMy9CAnq6ovwNat4xdUbdvdxM9DhyI=', '2018-12-16 02:54:00', '0', 'laqiuying', '', '', '1', '1', '2018-12-10 06:51:00', '');
INSERT INTO `auth_user` VALUES ('7', 'pbkdf2_sha256$120000$OYmjJ5TdwtiF$YgOfGIoXS6Qu/25lyR7Gv4HDkAks4PI5RgXo4QftD6A=', '2018-12-11 07:04:46', '0', 'zhangchengyu', '', '', '1', '1', '2018-12-10 06:52:00', '');
INSERT INTO `auth_user` VALUES ('8', 'pbkdf2_sha256$120000$alYSGFfafbUy$lorPt43ddqRrV0F5aUhRLJG0qL4rWmANPqXdirUIkII=', '2018-12-12 01:50:17', '0', 'qiaoyan', '', '', '1', '1', '2018-12-10 06:52:00', '');
INSERT INTO `auth_user` VALUES ('9', 'pbkdf2_sha256$120000$Nge2xdUYImX2$dQepQ5P45L00qT3Rytxl0mRr+ioU7aMHx0F4th23pDQ=', '2018-12-16 01:35:45', '0', 'liuluyu', '', '', '1', '1', '2018-12-11 04:57:00', '');
INSERT INTO `auth_user` VALUES ('10', 'pbkdf2_sha256$120000$8wbCF8QuTrqr$1nNFegiuK8N32ZiIHETiyHJ82NDQzY+oLc6Oj2Jf7oI=', '2018-12-14 06:30:33', '0', 'limei', '', '', '1', '1', '2018-12-12 01:18:00', '');
INSERT INTO `auth_user` VALUES ('11', 'pbkdf2_sha256$120000$RCbFUZBb5puw$CucQUVLwcwSEn3EEWpkrfaSoDJh7/AKsNiEYwbXinu8=', '2018-12-14 10:10:20', '0', 'external_recorder_3', '', '', '1', '1', '2018-12-12 01:19:00', '');
INSERT INTO `auth_user` VALUES ('12', 'pbkdf2_sha256$120000$jvxPsSM9jgIf$cBWj8N/kJXjiZXT/0wq8QX5lRYi2f+Hpki4rYEO3UCA=', '2018-12-16 05:06:27', '0', 'external_recorder_4', '', '', '1', '1', '2018-12-12 01:19:00', '');
INSERT INTO `auth_user` VALUES ('13', 'pbkdf2_sha256$120000$MvyVp7lKwt0G$hq6NpOMY1sUVsp61aCu8N9Uz6fgx1RlSZFzr1Dpcdok=', '2018-12-15 03:53:21', '0', 'external_recorder_5', '', '', '1', '1', '2018-12-12 01:19:00', '');
INSERT INTO `auth_user` VALUES ('14', 'pbkdf2_sha256$120000$dtB9cJ4ZxLgn$1SoIrS4We82bKfUCxMNUi6VpJZkT/7cm7YxAhP9N+14=', '2018-12-15 02:28:23', '1', 'mapanpan', '', '', '1', '1', '2018-12-12 06:05:00', '');
INSERT INTO `auth_user` VALUES ('15', 'pbkdf2_sha256$120000$CqEcGl07YS7j$Hk9DFvfykcAozEsKh0ypGwo2StPLNckrFwA4aRXCtlE=', '2018-12-13 05:32:50', '0', 'external_recorder_6', '', '', '1', '1', '2018-12-13 05:17:00', '');
INSERT INTO `auth_user` VALUES ('16', 'pbkdf2_sha256$120000$YBqmW4xbJ1Bo$nzsxDOlO4R72k5Img7QxxMsumKZNClXHc6KRXP3iFbE=', '2018-12-16 07:26:18', '0', 'external_recorder_7', '', '', '1', '1', '2018-12-13 05:19:00', '');
INSERT INTO `auth_user` VALUES ('17', 'pbkdf2_sha256$120000$mRIBr7VB4zla$23FbI9TInr58f/VxBiznMvrhCumB8QhU51BwZ5CiKO8=', '2018-12-14 02:35:03', '0', 'external_recorder_8', '', '', '1', '1', '2018-12-14 02:23:00', '');
INSERT INTO `auth_user` VALUES ('18', 'pbkdf2_sha256$120000$MbZcBtaWIOTl$pzlw+tGKO9pr2OoHpyJzOUE+HTjaA5Bk0YfoZywEkZE=', '2018-12-14 02:34:51', '0', 'external_recorder_9', '', '', '1', '1', '2018-12-14 02:23:00', '');
INSERT INTO `auth_user` VALUES ('19', 'pbkdf2_sha256$120000$uc1lzg0BMF4O$/4kfWtgaEokvZ9Tj0xlKK/Wq2gg2OyVp9RKFm6IVhrw=', '2018-12-14 02:38:35', '0', 'external_recorder_10', '', '', '1', '1', '2018-12-14 02:24:00', '');
INSERT INTO `auth_user` VALUES ('20', 'pbkdf2_sha256$120000$ZLWCQ0Gp6WWz$M/G8YOb9QMUSFUHXRE5suTi0Sw3FTTkn+YBEWm4h7yI=', '2018-12-14 02:43:56', '0', 'external_recorder_11', '', '', '1', '1', '2018-12-14 02:24:00', '');
INSERT INTO `auth_user` VALUES ('21', 'pbkdf2_sha256$120000$rO0vCNic3wmA$Ww5XKePt0Tnprf4csXpxgS18CFrf3BIt9PLmReYLXss=', '2018-12-14 02:40:00', '0', 'external_recorder_12', '', '', '1', '1', '2018-12-14 02:25:00', '');
INSERT INTO `auth_user` VALUES ('22', 'pbkdf2_sha256$120000$wEUgrgJEkHCZ$AeEALId6qvmAMZo/IB/gVDsRrERbs29z9fr50ybPoqU=', '2018-12-14 06:28:58', '0', 'wanghuan', '', '', '1', '1', '2018-12-14 02:38:00', '');
INSERT INTO `auth_user` VALUES ('23', 'pbkdf2_sha256$120000$N5kViqB4JIX3$22a1vfc6GD82ZCFxbf+OwmM2CMIFJEwXsh67BeSME2s=', '2018-12-14 06:31:04', '0', 'zhangmiaoxia', '', '', '1', '1', '2018-12-14 02:38:00', '');
INSERT INTO `auth_user` VALUES ('24', 'pbkdf2_sha256$120000$YlOyupYnykAe$WaYGkL4khmCrjSR/07aXaXJ1CvFttS/1atSOdV1sxhk=', '2018-12-14 06:31:37', '0', 'wangyujie', '', '', '1', '1', '2018-12-14 06:22:00', '');
INSERT INTO `auth_user` VALUES ('25', 'pbkdf2_sha256$120000$1KMP1RPAa9c0$+J3modl9ZObmK3nH06AFax4+yJ/+W3p+OUCh3pBzH2Q=', '2018-12-14 06:39:40', '0', 'zhangdi', '', '', '1', '1', '2018-12-14 06:22:00', '');
INSERT INTO `auth_user` VALUES ('26', 'pbkdf2_sha256$120000$ozblIR8wGmP4$+4JvLd75NPrKxXKdNk2HPbdd979WUg4XhsCAbbBOiR4=', '2018-12-14 06:29:03', '0', 'chenxupeng', '', '', '1', '1', '2018-12-14 06:23:00', '');
INSERT INTO `auth_user` VALUES ('27', 'pbkdf2_sha256$120000$vUgqsxTE8cu4$DO5T+ZqPe0f48XPyXr8za+JMsY7TqedvsXuHnC+Xhb4=', '2018-12-14 06:28:10', '1', 'hujiajie', '', '', '1', '1', '2018-12-14 06:24:00', '');
INSERT INTO `auth_user` VALUES ('28', 'pbkdf2_sha256$120000$mLw8W2h2aWUM$k9F/VrEXP5EWx0RRIXMIauPeFDVag7JvjrNvrh7NLms=', '2018-12-14 06:37:34', '0', 'gaorui', '', '', '1', '1', '2018-12-14 06:36:00', '');
INSERT INTO `auth_user` VALUES ('29', 'pbkdf2_sha256$120000$PLZ8WgIu969k$KsIMwsl8TUzMp3qh4nRUFPwVJGJUZurSVHkp5u8J7K8=', '2018-12-14 08:16:33', '0', 'wangweiyi', '', '', '1', '1', '2018-12-14 07:57:00', '');

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM AUTO_INCREMENT=29 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------
INSERT INTO `auth_user_groups` VALUES ('1', '2', '1');
INSERT INTO `auth_user_groups` VALUES ('2', '3', '1');
INSERT INTO `auth_user_groups` VALUES ('3', '4', '1');
INSERT INTO `auth_user_groups` VALUES ('4', '5', '1');
INSERT INTO `auth_user_groups` VALUES ('5', '6', '1');
INSERT INTO `auth_user_groups` VALUES ('6', '7', '1');
INSERT INTO `auth_user_groups` VALUES ('7', '8', '2');
INSERT INTO `auth_user_groups` VALUES ('9', '9', '1');
INSERT INTO `auth_user_groups` VALUES ('10', '10', '1');
INSERT INTO `auth_user_groups` VALUES ('11', '11', '1');
INSERT INTO `auth_user_groups` VALUES ('12', '12', '1');
INSERT INTO `auth_user_groups` VALUES ('13', '13', '1');
INSERT INTO `auth_user_groups` VALUES ('14', '15', '1');
INSERT INTO `auth_user_groups` VALUES ('15', '16', '1');
INSERT INTO `auth_user_groups` VALUES ('16', '17', '1');
INSERT INTO `auth_user_groups` VALUES ('17', '18', '1');
INSERT INTO `auth_user_groups` VALUES ('18', '19', '1');
INSERT INTO `auth_user_groups` VALUES ('19', '21', '1');
INSERT INTO `auth_user_groups` VALUES ('20', '22', '1');
INSERT INTO `auth_user_groups` VALUES ('21', '23', '1');
INSERT INTO `auth_user_groups` VALUES ('22', '20', '1');
INSERT INTO `auth_user_groups` VALUES ('23', '24', '1');
INSERT INTO `auth_user_groups` VALUES ('24', '25', '1');
INSERT INTO `auth_user_groups` VALUES ('25', '26', '1');
INSERT INTO `auth_user_groups` VALUES ('26', '27', '2');
INSERT INTO `auth_user_groups` VALUES ('27', '28', '1');
INSERT INTO `auth_user_groups` VALUES ('28', '29', '1');

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for baseline_companies
-- ----------------------------
DROP TABLE IF EXISTS `baseline_companies`;
CREATE TABLE `baseline_companies` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(128) DEFAULT NULL,
  `social_num` varchar(64) DEFAULT NULL,
  `org_num` varchar(64) DEFAULT NULL,
  `legal_person` varchar(32) DEFAULT NULL,
  `data_process_place` varchar(32) DEFAULT NULL,
  `province` varchar(32) NOT NULL,
  `city` varchar(32) NOT NULL,
  `district` varchar(32) NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `community` varchar(32) DEFAULT NULL,
  `district_code` varchar(32) DEFAULT NULL,
  `survey_area_code` varchar(32) DEFAULT NULL,
  `building_area_code` varchar(32) DEFAULT NULL,
  `building_unique_code` varchar(32) DEFAULT NULL,
  `park_name` varchar(32) DEFAULT NULL,
  `park_code` varchar(32) DEFAULT NULL,
  `register_province` varchar(32) DEFAULT NULL,
  `register_city` varchar(32) DEFAULT NULL,
  `register_district` varchar(32) DEFAULT NULL,
  `register_address` varchar(255) DEFAULT NULL,
  `register_street_district` varchar(32) DEFAULT NULL,
  `register_community` varchar(32) DEFAULT NULL,
  `register_district_code` varchar(32) DEFAULT NULL,
  `register_survey_area_code` varchar(32) DEFAULT NULL,
  `register_building_area_code` varchar(32) DEFAULT NULL,
  `register_park_name` varchar(32) DEFAULT NULL,
  `register_park_code` varchar(32) DEFAULT NULL,
  `landline_area_code` varchar(12) DEFAULT NULL,
  `landline_num` varchar(32) DEFAULT NULL,
  `landline_branch_num` varchar(32) DEFAULT NULL,
  `mobile` varchar(32) DEFAULT NULL,
  `main_activity_1` varchar(128) DEFAULT NULL,
  `main_activity_2` varchar(128) DEFAULT NULL,
  `main_activity_3` varchar(128) DEFAULT NULL,
  `industry_code` varchar(128) NOT NULL,
  `industry_name` varchar(128) DEFAULT NULL,
  `economic_code` varchar(128) DEFAULT NULL,
  `economic_name` varchar(128) DEFAULT NULL,
  `is_culture` varchar(12) DEFAULT NULL,
  `org_type` varchar(12) DEFAULT NULL,
  `register_type` varchar(12) DEFAULT NULL,
  `est_year` varchar(12) DEFAULT NULL,
  `est_month` varchar(12) DEFAULT NULL,
  `operate_status` varchar(12) DEFAULT NULL,
  `comp_type` varchar(12) DEFAULT NULL,
  `as_legal_person` tinyint(1) NOT NULL,
  `accounting_rule` varchar(12) DEFAULT NULL,
  `accounting_rule_note` varchar(32) DEFAULT NULL,
  `produce_energy` tinyint(1) NOT NULL,
  `sell_energy` tinyint(1) NOT NULL,
  `involved_military` tinyint(1) NOT NULL,
  `has_branch` tinyint(1) NOT NULL,
  `branch_cnt` varchar(12) DEFAULT NULL,
  `branch_type` varchar(12) DEFAULT NULL,
  `branch_comp_social_num` varchar(32) DEFAULT NULL,
  `branch_comp_org_num` varchar(32) DEFAULT NULL,
  `branch_comp_name` varchar(128) DEFAULT NULL,
  `branch_comp_address` varchar(255) DEFAULT NULL,
  `branch_comp_district_code` varchar(255) DEFAULT NULL,
  `parent_type` varchar(12) DEFAULT NULL,
  `parent_comp_social_num` varchar(32) DEFAULT NULL,
  `parent_comp_org_num` varchar(32) DEFAULT NULL,
  `parent_comp_name` varchar(128) DEFAULT NULL,
  `parent_comp_address` varchar(255) DEFAULT NULL,
  `parent_comp_district_code` varchar(255) DEFAULT NULL,
  `is_orphan` tinyint(1) NOT NULL,
  `unique_code` varchar(64) DEFAULT NULL,
  `data_source` varchar(64) DEFAULT NULL,
  `interviewee` varchar(32) DEFAULT NULL,
  `interviewee_contact` varchar(32) DEFAULT NULL,
  `recorded_date` date DEFAULT NULL,
  `added_date` date NOT NULL,
  `modified_date` date NOT NULL,
  `record_type` varchar(12) DEFAULT NULL,
  `added_by_id` int(11) DEFAULT NULL,
  `modified_by_id` int(11) DEFAULT NULL,
  `branch_comp_count_obtainemploy` varchar(255) DEFAULT NULL,
  `branch_comp_count_obtainemploy_female` varchar(255) DEFAULT NULL,
  `branch_comp_house_nosale_area` varchar(255) DEFAULT NULL,
  `branch_comp_house_sale_area` varchar(255) DEFAULT NULL,
  `branch_comp_nooperate_defray` varchar(255) DEFAULT NULL,
  `branch_comp_operate_income` varchar(255) DEFAULT NULL,
  `email` varchar(32) DEFAULT NULL,
  `fax_code` varchar(32) DEFAULT NULL,
  `is_notice` tinyint(1) NOT NULL,
  `is_write_661_1` tinyint(1) NOT NULL,
  `is_write_661_3` tinyint(1) NOT NULL,
  `is_write_661_5` tinyint(1) NOT NULL,
  `is_write_661_6` tinyint(1) NOT NULL,
  `legal_unite_accounting_standard` varchar(12) DEFAULT NULL,
  `legal_unite_company_size` varchar(12) DEFAULT NULL,
  `legal_unite_hkmatai` varchar(32) DEFAULT NULL,
  `legal_unite_hypotaxis` varchar(12) DEFAULT NULL,
  `legal_unite_nonperson_assets` varchar(255) DEFAULT NULL,
  `legal_unite_nonperson_defray` varchar(255) DEFAULT NULL,
  `legal_unite_obtainemploy` varchar(255) DEFAULT NULL,
  `legal_unite_obtainemploy_female` varchar(255) DEFAULT NULL,
  `legal_unite_person_assets` varchar(255) DEFAULT NULL,
  `legal_unite_person_income` varchar(255) DEFAULT NULL,
  `legal_unite_person_taxes` varchar(255) DEFAULT NULL,
  `legal_unite_stake` varchar(12) DEFAULT NULL,
  `postalcode` varchar(32) DEFAULT NULL,
  `profess_category` varchar(64) DEFAULT NULL,
  `retail_business_area` varchar(12) DEFAULT NULL,
  `retail_hotel_diet_area` varchar(12) DEFAULT NULL,
  `retail_hotel_diet_star` varchar(12) DEFAULT NULL,
  `retail_management_brand` varchar(255) DEFAULT NULL,
  `retail_management_form` varchar(12) DEFAULT NULL,
  `retail_opetrate_type` varchar(32) DEFAULT NULL,
  `website` varchar(32) DEFAULT NULL,
  `street_district` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `baseline_companies_added_by_id_a73c07b7` (`added_by_id`),
  KEY `baseline_companies_modified_by_id_1d39ff64` (`modified_by_id`)
) ENGINE=MyISAM AUTO_INCREMENT=26474 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of baseline_companies
-- ----------------------------
INSERT INTO `baseline_companies` VALUES ('3', '西安聪明豆广告文化传播有限公司', '916101030653225290', null, '陈哲', null, '陕西省', '西安市', '碑林区', '陕西省西安市碑林区南院门大车家巷小区2号楼20601室', '大车家巷', null, null, null, null, null, null, '陕西省', '西安市', '碑林区', null, null, null, null, null, null, null, null, null, null, null, '18509283093', '其他广告服务', null, null, '7259', null, null, null, null, '10', '173', '2013', '5', '1', '1', '0', '1', null, '0', '0', '0', '0', null, null, null, null, null, null, null, '1', null, null, null, null, null, '0', null, null, '陈哲', '18509283093', null, '2018-12-10', '2018-12-10', 'phase2', '3', null, null, null, null, null, null, null, null, null, '0', '0', '0', '0', '0', '1', '1', null, '10', null, null, null, null, null, null, null, '1', null, 'A', null, null, null, null, '1', null, null, '南院门');
INSERT INTO `baseline_companies` VALUES ('4', '西安豪游旅游文化传播有限责任公司', '91610103333723602T', null, '王振海', null, '陕西省', '西安市', '碑林区', '陕西省西安市碑林区粉巷3号1栋1082', '德福巷', null, null, null, null, null, null, '陕西省', '西安市', '碑林区', null, null, null, null, null, null, null, null, null, null, null, '13992892959', '旅游文化项目开发', null, null, '7291', null, null, null, null, '10', '173', '2015', '5', '1', '1', '0', '1', null, '0', '0', '0', '0', null, null, null, null, null, null, null, '1', null, null, null, null, null, '0', null, null, '王振海', '13519188567', null, '2018-12-10', '2018-12-10', 'phase2', '2', null, null, null, null, null, null, null, null, null, '0', '0', '0', '0', '0', '1', '1', null, '10', null, null, null, null, null, null, null, '1', null, 'A', null, null, null, null, '1', null, null, '南院门');
INSERT INTO `baseline_companies` VALUES ('5', '西安宇群电子科技有限公司', '91610103MA6TYXLG44', null, '孟新峰', null, '陕西省', '西安市', '碑林区', '陕西省西安市碑林区德福巷D东21号楼3-704室', '德福巷', null, null, null, null, null, null, '陕西省', '西安市', '碑林区', null, null, null, null, null, null, null, null, null, null, null, '18092777086', '计算机网络工程、楼宇智能化工程', null, null, '6490', null, null, null, null, '10', '173', '2016', '10', '1', '1', '0', '1', null, '0', '0', '0', '0', null, null, null, null, null, null, null, '1', null, null, null, null, null, '0', null, null, '孟新峰', '18092777086', null, '2018-12-10', '2018-12-10', 'phase2', '2', null, null, null, null, null, null, null, null, null, '0', '0', '0', '0', '0', '1', '1', null, '10', null, null, null, null, null, null, null, '1', null, 'A', null, null, null, null, '1', null, null, '南院门');
INSERT INTO `baseline_companies` VALUES ('6', '西安初见雨欣餐饮管理有限公司', '91610103MA6UUAJK0H', null, '仇雨馨', null, '陕西省', '西安市', '碑林区', '陕西省西安市碑林区南院门大车家巷17号院5号楼1单元1楼1号', '大车家巷', null, null, null, null, null, null, '陕西省', '西安市', '碑林区', null, null, null, null, null, null, null, null, null, null, null, '15389458830', '小吃服务', null, null, '6291', null, null, null, null, '10', '173', '2018', '4', '1', '1', '0', '1', null, '0', '0', '0', '0', null, null, null, null, null, null, null, '1', null, null, null, null, null, '0', null, null, '仇雨馨', '15389458830', null, '2018-12-10', '2018-12-10', 'phase2', '3', null, null, null, null, null, null, null, null, null, '0', '0', '0', '0', '0', '1', '1', null, '10', null, null, null, null, null, null, null, '1', null, 'A', null, null, null, null, '1', null, null, '南院门');
INSERT INTO `baseline_companies` VALUES ('7', '陕西今非昔比美容服务有限公司', '91610103MA6W12XN65', null, '任娟', null, '陕西省', '西安市', '碑林区', '陕西省西安市碑林区南大街真爱粉巷里四楼南户', '德福巷', null, null, null, null, null, null, '陕西省', '西安市', '碑林区', null, null, null, null, null, null, null, null, null, null, null, '13389211358', '美容服务', null, null, '804002', null, null, null, null, '10', '173', '2018', '7', '1', '1', '0', '1', null, '0', '0', '0', '0', null, null, null, null, null, null, null, '1', null, null, null, null, null, '0', null, null, '屈花', '13609266520', null, '2018-12-10', '2018-12-10', 'phase2', '2', null, null, null, null, null, null, null, null, null, '0', '0', '0', '0', '0', '1', '1', null, '10', null, null, null, null, null, null, null, '1', null, 'A', null, null, null, null, '1', null, null, '南院门');
INSERT INTO `baseline_companies` VALUES ('8', '西安市煤炭运销有限责任公司', '91610103724914078Q', null, '郭峰', null, '陕西省', '西安市', '碑林区', '西安市碑林区湘子庙街东口6号有色金属宾馆617号', '德福巷', null, null, null, null, null, null, '陕西省', '西安市', '碑林区', null, null, null, null, null, null, null, null, null, null, null, '15829550065', '煤炭批发', null, null, '5161', null, null, null, null, '10', '173', '2000', '9', '1', '1', '0', '1', null, '0', '0', '0', '0', null, null, null, null, null, null, null, '1', null, null, null, null, null, '0', null, null, '李林', '15829550065', null, '2018-12-10', '2018-12-10', 'phase2', '2', null, null, null, null, null, null, null, null, null, '0', '0', '0', '0', '0', '1', '1', null, '10', null, null, null, null, null, null, null, '1', null, 'A', null, null, null, null, '1', null, null, '南院门');
INSERT INTO `baseline_companies` VALUES ('9', '中共西安市碑林区委政法委员会', '1161010374284654x6', null, '陈哲', null, '陕西省', '西安市', '碑林区', '西安市碑林区南院门27号', '南院门社区', null, null, null, null, null, null, '陕西省', '西安市', '碑林区', null, null, null, null, null, null, null, null, null, '029-89625166', null, null, '综合事务管理', null, null, '9221', null, null, null, null, '30', '110', '2016年', '12月', '1', '1', '0', '3', null, '0', '0', '0', '0', null, null, null, null, null, null, null, '1', null, null, null, null, null, '0', null, null, '赵雪', '89625166', null, '2018-12-10', '2018-12-10', 'phase2', '5', '8', null, null, null, null, null, null, null, null, '0', '0', '0', '0', '0', '1', '1', null, '10', null, null, null, null, null, null, null, '1', null, 'A', null, null, null, null, '1', null, null, '南院门');
INSERT INTO `baseline_companies` VALUES ('10', '西安贞庆聚财务心理咨询有限责任公司', '91610103MA6U6HB04J', null, '郭莉莉', null, '陕西省', '西安市', '碑林区', '陕西省西安市碑林区荣民国际10629', '南广济街', null, null, null, null, null, null, '陕西省', '西安市', '碑林区', null, null, null, null, null, null, null, null, null, null, null, '18991803869', '二手房销售', null, null, '7030', null, null, null, null, '10', '173', '2018', '3', '3', '1', '0', '1', null, '0', '0', '0', '0', null, null, null, null, null, null, null, '1', null, null, null, null, null, '0', null, null, '郭莉莉', '18991803869', null, '2018-12-10', '2018-12-10', 'phase2', '7', null, null, null, null, null, null, null, null, null, '0', '0', '0', '0', '0', '1', '1', null, '10', null, null, null, null, null, null, null, '1', null, 'A', null, null, null, null, '1', null, null, '南院门');
INSERT INTO `baseline_companies` VALUES ('11', '西安存天阁艺术品有限公司', '91610103678609856A', null, '安今尧', null, '陕西省', '西安市', '碑林区', '陕西省西安市碑林区南院门湘子庙街58号1栋10102', '大车家巷', null, null, null, null, null, null, '陕西省', '西安市', '碑林区', null, null, null, null, null, null, null, null, null, null, null, '18292995464', '工艺美术品零售', null, null, '5246', null, null, null, null, '10', '173', '2008', '6', '1', '1', '0', '1', null, '0', '0', '0', '0', null, null, null, null, null, null, null, '1', null, null, null, null, null, '0', null, null, '安今尧', '18292995464', null, '2018-12-10', '2018-12-10', 'phase2', '3', null, null, null, null, null, null, null, null, null, '0', '0', '0', '0', '0', '1', '1', null, '10', null, null, null, null, null, null, null, '1', null, 'A', null, null, null, null, '1', null, null, '南院门');
INSERT INTO `baseline_companies` VALUES ('12', '西安吴中皮影王工艺品开发有限责任公司', '91610703668681416H', null, '王世清', null, '陕西省', '西安市', '碑林区', '陕西省西安市碑林区书院门商住户D30201室', '书院门', null, null, null, null, null, null, '陕西省', '西安市', '碑林区', null, null, null, null, null, null, null, null, null, null, null, '13299112000', '皮影加工零售', null, null, '5246', null, null, null, null, '10', '173', '2008', '1', '1', '1', '0', '1', null, '0', '0', '0', '0', null, null, null, null, null, null, null, '1', null, null, null, null, null, '0', null, null, '何姣', '15929294617', null, '2018-12-10', '2018-12-10', 'phase2', '4', null, null, null, null, null, null, null, null, null, '0', '0', '0', '0', '0', '1', '1', null, '10', null, null, null, null, null, null, null, '1', null, 'A', null, null, null, null, '1', null, null, '南院门');
INSERT INTO `baseline_companies` VALUES ('13', '西安信诚房地产评估有限公司', '916101035963473462', null, '王宁', null, '陕西省', '西安市', '碑林区', '西安市碑林区南大街粉巷22号7幢402室', '德福巷', null, null, null, null, null, null, '陕西省', '西安市', '碑林区', null, null, null, null, null, null, null, null, null, null, null, '18392157777', '房地产价格评估', null, null, '7030', null, null, null, null, '10', '173', '2012', '7', '1', '1', '0', '1', null, '0', '0', '0', '0', null, null, null, null, null, null, null, '1', null, null, null, null, null, '0', null, null, '曹婧', '18802977717', null, '2018-12-10', '2018-12-10', 'phase2', '2', null, null, null, null, null, null, null, null, null, '0', '0', '0', '0', '0', '1', '1', null, '10', null, null, null, null, null, null, null, '1', null, 'A', null, null, null, null, '1', null, null, '南院门');
INSERT INTO `baseline_companies` VALUES ('14', '西安臻达工程机械有限公司', '91610103678629355A', null, '张玥', null, '陕西省', '西安市', '碑林区', '陕西省西安市碑林区荣民国际19522', '南广济街', null, null, null, null, null, null, '陕西省', '西安市', '碑林区', null, null, null, null, null, null, null, null, null, null, null, '15091440062', '机械设备租赁', null, null, '7119', null, null, null, null, '10', '173', '2008', '11', '1', '1', '0', '1', null, '0', '0', '0', '0', null, null, null, null, null, null, null, '1', null, null, null, null, null, '0', null, null, '张玥', '15091440062', null, '2018-12-10', '2018-12-10', 'phase2', '7', null, null, null, null, null, null, null, null, null, '0', '0', '0', '0', '0', '1', '1', null, '10', null, null, null, null, null, null, null, '1', null, 'A', null, null, null, null, '1', null, null, '南院门');
INSERT INTO `baseline_companies` VALUES ('15', '西安恒奕商贸有限公司', '91610103583167848A', null, '王清莲', null, '陕西省', '西安市', '碑林区', '陕西省西安市碑林区南院门湘子庙街39号北楼101', '大车家巷', null, null, null, null, null, null, '陕西省', '西安市', '碑林区', null, null, null, null, null, null, null, null, null, null, null, '13379516033', '厨具卫具及日用杂品零售', null, null, '5235', null, null, null, null, '10', '159', '2011', '10', '1', '1', '0', '1', null, '0', '0', '0', '0', null, null, null, null, null, null, null, '1', null, null, null, null, null, '0', null, null, '王清莲', '13379516033', null, '2018-12-10', '2018-12-10', 'phase2', '3', null, null, null, null, null, null, null, null, null, '0', '0', '0', '0', '0', '1', '1', null, '10', null, null, null, null, null, null, null, '1', null, 'A', null, null, null, null, '1', null, null, '南院门');
INSERT INTO `baseline_companies` VALUES ('16', '中国有色金属西安供销运输公司', '916100002205214495', null, '刘富平', null, '陕西省', '西安市', '碑林区', '陕西省西安市碑林区湘子庙街3号副3号', '德福巷', null, null, null, null, null, null, '陕西省', '西安市', '碑林区', null, null, null, null, null, null, null, null, null, null, null, '13609265308', '有色金属材料、建筑材料的批发', null, null, '5165', null, null, null, null, '10', '110', '1995', '4', '1', '1', '0', '1', null, '0', '0', '0', '0', null, null, null, null, null, null, null, '1', null, null, null, null, null, '0', null, null, '韩莉', '13709256317', null, '2018-12-10', '2018-12-10', 'phase2', '2', null, null, null, null, null, null, null, null, null, '0', '0', '0', '0', '0', '1', '1', null, '10', null, null, null, null, null, null, null, '1', null, 'A', null, null, null, null, '1', null, null, '南院门');
INSERT INTO `baseline_companies` VALUES ('17', '陕西增栋商贸有限公司', '91610103MA6W1DYC2K', null, '马丽', null, '陕西省', '西安市', '碑林区', '陕西省西安市碑林区唐宁国际5号楼511', '南广济街', null, null, null, null, null, null, '陕西省', '西安市', '碑林区', null, null, null, null, null, null, null, null, null, null, null, '13669140258', '建材批发', null, null, '5165', null, null, null, null, '10', '173', '2018', '8', '1', '1', '0', '1', null, '0', '0', '0', '0', null, null, null, null, null, null, null, '1', null, null, null, null, null, '0', null, null, '马丽', '13669140258', null, '2018-12-10', '2018-12-10', 'phase2', '7', null, null, null, null, null, null, null, null, null, '0', '0', '0', '0', '0', '1', '1', null, '10', null, null, null, null, null, null, null, '1', null, 'A', null, null, null, null, '1', null, null, '南院门');
INSERT INTO `baseline_companies` VALUES ('18', '西安格江工贸有限公司', '91610104783590616R', null, '杨文富', null, '陕西省', '西安市', '碑林区', '书院门3幢3单元30303室', '书院门', null, null, null, null, null, null, '陕西省', '西安市', '碑林区', null, null, null, null, null, null, null, null, null, null, null, '15319998080', '成品油批发', null, null, '5162', null, null, null, null, '10', '173', '2006', '6', '1', '1', '0', '1', null, '0', '1', '0', '0', null, null, null, null, null, null, null, '1', null, null, null, null, null, '0', null, null, '张涛', '15319998080', null, '2018-12-10', '2018-12-10', 'phase2', '4', null, null, null, null, null, null, null, null, null, '0', '0', '0', '0', '0', '1', '1', null, '10', null, null, null, null, null, null, null, '1', null, 'A', null, null, null, null, '1', null, null, '南院门');
INSERT INTO `baseline_companies` VALUES ('19', '西安云顶资产管理有限公司', '91610103321958404P', null, '郭炜', null, '陕西省', '西安市', '碑林区', '西安市碑林区南大街粉巷3号真爱·粉巷里5层505号', '德福巷', null, null, null, null, null, null, '陕西省', '西安市', '碑林区', null, null, null, null, null, null, null, null, null, null, null, '15029000033', '投资管理，企业投资咨询', null, null, '7243', null, null, null, null, '10', '173', '2015', '1', '1', '1', '0', '1', null, '0', '0', '0', '0', null, null, null, null, null, null, null, '1', null, null, null, null, null, '0', null, null, '孙卓伟', '18699401521', null, '2018-12-10', '2018-12-10', 'phase2', '2', null, null, null, null, null, null, null, null, null, '0', '0', '0', '0', '0', '1', '1', null, '10', null, null, null, null, null, null, null, '1', null, 'A', null, null, null, null, '1', null, null, '南院门');
INSERT INTO `baseline_companies` VALUES ('20', '西安华义凯诚商贸有限公司', '91610103MA6U1AK99F', null, '张亚敏', null, '陕西省', '西安市', '碑林区', '陕西省西安市碑林区南院门横巷市委家属院13栋4单元40302', '大车家巷', null, null, null, null, null, null, '陕西省', '西安市', '碑林区', null, null, null, null, null, null, null, null, null, null, null, '18049297050', '保健品零售', null, null, '5225', null, null, null, null, '10', '173', '2017', '1', '1', '1', '0', '1', null, '0', '0', '0', '0', null, null, null, null, null, null, null, '1', null, null, null, null, null, '0', null, null, '张亚敏', '18049297050', null, '2018-12-10', '2018-12-10', 'phase2', '3', null, null, null, null, null, null, null, null, null, '0', '0', '0', '0', '0', '1', '1', null, '10', null, null, null, null, null, null, null, '1', null, 'A', null, null, null, null, '1', null, null, '南院门');
INSERT INTO `baseline_companies` VALUES ('21', '西安市碑林区基层工会建设指导服务中心', '12610103H16424741K', null, '柳萍', null, '陕西省', '西安市', '碑林区', '陕西省西安市碑林区南院门27号', '南院门社区', null, null, null, null, null, null, '陕西省', '西安市', '碑林区', null, null, null, null, null, null, null, null, null, '029-89625205', null, null, '工会', null, null, '9511', null, null, null, null, '20', '110', '2003年', '10月', '1', '1', '0', '2', null, '0', '0', '0', '0', null, null, null, null, null, null, null, '1', null, null, null, null, null, '0', null, null, '侯晓兰', '89625205', null, '2018-12-10', '2018-12-10', 'phase2', '5', '8', null, null, null, null, null, null, null, null, '0', '0', '0', '0', '0', '1', '1', null, '10', null, null, null, null, null, null, null, '1', null, 'A', null, null, null, null, '1', null, null, '南院门');
INSERT INTO `baseline_companies` VALUES ('22', '西安佰佳安商贸有限公司', '91610103MA6U22KK7K', null, '顾强', null, '陕西省', '西安市', '碑林区', '陕西省西安市碑林区盐店街128号第一栋一单元5层10517号', '南广济街', null, null, null, null, null, null, '陕西省', '西安市', '碑林区', null, null, null, null, null, null, null, null, null, '029-81021572', null, '15339081766', '工业自动化设备、机电设备安装', null, null, '4910', null, null, null, null, '10', '173', '2017', '3', '1', '1', '0', '1', null, '0', '0', '0', '0', null, null, null, null, null, null, null, '1', null, null, null, null, null, '0', null, null, '李杨', '15339081766', null, '2018-12-10', '2018-12-10', 'phase2', '7', null, null, null, null, null, null, null, null, null, '0', '0', '0', '0', '0', '1', '1', null, '10', null, null, null, null, null, null, null, '1', null, 'A', null, null, null, null, '1', null, null, '南院门');
INSERT INTO `baseline_companies` VALUES ('23', '陕西紫宸古建工程有限公司', '9161000D727379488M', null, '王顺利', null, '陕西省', '西安市', '碑林区', '陕西省西安市碑林区书院门1号', '书院门', null, null, null, null, null, null, '陕西省', '西安市', '碑林区', null, null, null, null, null, null, null, null, null, null, null, '15829330800', '古建修缮工程的施工', null, null, '5090', null, null, null, null, '10', '173', '2001', '6', '1', '1', '0', '1', null, '0', '0', '0', '0', null, null, null, null, null, null, null, '1', null, null, null, null, null, '0', null, null, '郭小艳', '13572921269', null, '2018-12-10', '2018-12-10', 'phase2', '4', null, null, null, null, null, null, null, null, null, '0', '0', '0', '0', '0', '1', '1', null, '10', null, null, null, null, null, null, null, '1', null, 'A', null, null, null, null, '1', null, null, '南院门');
INSERT INTO `baseline_companies` VALUES ('24', '陕西领创大数据科技有限公司', '916101003337753653', null, '周宙', null, '陕西省', '西安市', '碑林区', '西安市碑林区粉巷3号王子大厦9层912室', '德福巷', null, null, null, null, null, null, '陕西省', '西安市', '碑林区', null, null, null, null, null, null, null, null, null, null, null, '13802213003', '互联网数据服务', null, null, '6450', null, null, null, null, '10', '159', '2015', '6', '1', '1', '0', '1', null, '0', '0', '0', '0', null, null, null, null, null, null, null, '1', null, null, null, null, null, '0', null, null, '秦谅', '13619268432', null, '2018-12-10', '2018-12-10', 'phase2', '2', null, null, null, null, null, null, null, null, null, '0', '0', '0', '0', '0', '1', '1', null, '10', null, null, null, null, null, null, null, '1', null, 'A', null, null, null, null, '1', null, null, '南院门');
INSERT INTO `baseline_companies` VALUES ('25', '西安艾卡盟商贸有限公司', '91610103MA6UTE9GXA', null, '张敏鹏', null, '陕西省', '西安市', '碑林区', '陕西省西安市碑林区南院门大车家巷小区2号楼6层20603', '大车家巷', null, null, null, null, null, null, '陕西省', '西安市', '碑林区', null, null, null, null, null, null, null, null, null, null, null, '18189131388', '文具用品零售', null, null, '5241', null, null, null, null, '10', '173', null, null, '1', '1', '0', '1', null, '0', '0', '0', '0', null, null, null, null, null, null, null, '1', null, null, null, null, null, '0', null, null, '张敏鹏', '18189131388', null, '2018-12-10', '2018-12-10', 'phase2', '3', null, null, null, null, null, null, null, null, null, '0', '0', '0', '0', '0', '1', '1', null, '10', null, null, null, null, null, null, null, '1', null, 'A', null, null, null, null, '1', null, null, '南院门');
INSERT INTO `baseline_companies` VALUES ('27', '西安朗道能源科技有限公司', '916101035702203719', null, '王琪', null, '陕西省', '西安市', '碑林区', '陕西省西安市碑林区南院门伟业大厦A座1202号', '南院门社区', null, null, null, null, null, null, '陕西省', '西安市', '碑林区', null, null, null, null, null, null, null, null, null, '029-89388791', null, null, '能源技术开发', null, null, '7515', null, null, null, null, '10', '173', '2011年', '4月', '1', '1', '0', '1', null, '0', '0', '0', '0', null, null, null, null, null, null, null, '1', null, null, null, null, null, '0', null, null, '周梦', '13679280723', null, '2018-12-10', '2018-12-10', 'phase2', '5', '8', null, null, null, null, null, null, null, null, '0', '0', '0', '0', '0', '1', '1', null, '10', null, null, null, null, null, null, null, '1', null, 'A', null, null, null, null, '1', null, null, '南院门');
INSERT INTO `baseline_companies` VALUES ('28', '陕西京铁宏达建筑劳务有限公司', '91610103MA6URBXC0G', null, '马新伟', null, '陕西省', '西安市', '碑林区', '陕西省西安市碑林区德福巷D东5号楼3幢2单元20402室', '德福巷', null, null, null, null, null, null, '陕西省', '西安市', '碑林区', null, null, null, null, null, null, null, null, null, null, null, '18700039139', '劳务派遣服务', null, null, '726302', null, null, null, null, '10', '173', '2018', '3', '1', '1', '0', '1', null, '0', '0', '0', '0', null, null, null, null, null, null, null, '1', null, null, null, null, null, '0', null, null, '郝康红', '18909232017', null, '2018-12-10', '2018-12-10', 'phase2', '2', null, null, null, null, null, null, null, null, null, '0', '0', '0', '0', '0', '1', '1', null, '10', null, null, null, null, null, null, null, '1', null, 'A', null, null, null, null, '1', null, null, '南院门');
INSERT INTO `baseline_companies` VALUES ('29', '陕西天都绿业有限公司', '91610000732673737X', null, '王顺利', null, '陕西省', '西安市', '碑林区', '陕西省西安市碑林区书院门1号', '书院门', null, null, null, null, null, null, '陕西省', '西安市', '碑林区', null, null, null, null, null, null, null, null, null, null, null, '15829330800', '苗禾种柜批发', null, null, '5115', null, null, null, null, '10', '173', '2001', '12', '1', '1', '0', '1', null, '0', '0', '0', '0', null, null, null, null, null, null, null, '1', null, null, null, null, null, '0', null, null, '郭小艳', '13572921269', null, '2018-12-10', '2018-12-10', 'phase2', '4', null, null, null, null, null, null, null, null, null, '0', '0', '0', '0', '0', '1', '1', null, '10', null, null, null, null, null, null, null, '1', null, 'A', null, null, null, null, '1', null, null, '南院门');
INSERT INTO `baseline_companies` VALUES ('30', '西安朝禧羽歌商贸有限责任公司', '91610103MA6UYFYY6Y', null, '王朝阳', null, '陕西省', '西安市', '碑林区', '陕西省西安市碑林区南院门大车家巷5-7-101号', '大车家巷', null, null, null, null, null, null, '陕西省', '西安市', '碑林区', null, null, null, null, null, null, null, null, null, null, null, '15319450460', '服装零售', null, null, '5232', null, null, null, null, '10', '173', null, null, '1', '1', '0', '1', null, '0', '0', '0', '0', null, null, null, null, null, null, null, '1', null, null, null, null, null, '0', null, null, '王朝阳', '13700227085', null, '2018-12-10', '2018-12-10', 'phase2', '3', null, null, null, null, null, null, null, null, null, '0', '0', '0', '0', '0', '1', '1', null, '10', null, null, null, null, null, null, null, '1', null, 'A', null, null, null, null, '1', null, null, '南院门');
INSERT INTO `baseline_companies` VALUES ('31', '西安万旗企业文化传播有限公司', '91610100570212048L', null, '章红侠', null, '陕西省', '西安市', '碑林区', '陕西省西安市碑林区荣民国际大厦1幢1单元10602', '南广济街', null, null, null, null, null, null, '陕西省', '西安市', '碑林区', null, null, null, null, null, null, null, null, null, null, null, '13649231085', '广告设计；展览展示服务', null, null, '7259', null, null, null, null, '10', '173', '2011', '3', '1', '1', '0', '1', null, '0', '0', '0', '0', null, null, null, null, null, null, null, '1', null, null, null, null, null, '0', null, null, '章红侠', '13649231085', null, '2018-12-10', '2018-12-10', 'phase2', '7', null, null, null, null, null, null, null, null, null, '0', '0', '0', '0', '0', '1', '1', null, '10', null, null, null, null, null, null, null, '1', null, 'A', null, null, null, null, '1', null, null, '南院门');
INSERT INTO `baseline_companies` VALUES ('32', '西安市碑林区宏远针织服装厂', '916101037428214144', null, '高福军', null, '陕西省', '西安市', '碑林区', '西安市碑林区湘子庙街9号', '德福巷', null, null, null, null, null, null, '陕西省', '西安市', '碑林区', null, null, null, null, null, null, null, null, '029', '87260005', null, null, '服装', null, null, '5132', null, null, null, null, '10', '120', '2018', '1', '1', '1', '0', '1', null, '0', '0', '0', '0', null, null, null, null, null, null, null, '1', null, null, null, null, null, '0', null, null, '高福军', '87260005', null, '2018-12-10', '2018-12-10', 'phase2', '2', null, null, null, null, null, null, null, null, null, '0', '0', '0', '0', '0', '1', '1', null, '10', null, null, null, null, null, null, null, '1', null, 'A', null, null, null, null, '1', null, null, '南院门');
INSERT INTO `baseline_companies` VALUES ('33', '陕西中地非开挖技术有限公司', '91610000794102112Q', null, '李燕', null, '陕西省', '西安市', '碑林区', '陕西省西安市碑林区南院门大车家巷1号院', '大车家巷', null, null, null, null, null, null, '陕西省', '西安市', '碑林区', null, null, null, null, null, null, null, null, null, null, null, '13309200385', '管道施工', null, null, '4899', null, null, null, null, '10', '173', '2006', '9', '1', '1', '0', '1', null, '0', '0', '0', '0', null, null, null, null, null, null, null, '1', null, null, null, null, null, '0', null, null, '李燕', '13309200385', null, '2018-12-10', '2018-12-10', 'phase2', '3', null, null, null, null, null, null, null, null, null, '0', '0', '0', '0', '0', '1', '1', null, '10', null, null, null, null, null, null, null, '1', null, 'A', null, null, null, null, '1', null, null, '南院门');
INSERT INTO `baseline_companies` VALUES ('34', '西安市碑林区财政局', '1161010301338316XE', null, '闫丹杰', null, '陕西省', '西安市', '碑林区', '陕西省西安市碑林区南院门27号', '南院门社区', null, null, null, null, null, null, '陕西省', '西安市', '碑林区', null, null, null, null, null, null, null, null, null, '209-89625309', null, null, '综合事务管理', null, null, '9221', null, null, null, null, '30', '110', '1978年', '5月', '1', '1', '0', '3', null, '0', '0', '0', '0', null, null, null, null, null, null, null, '1', null, null, null, null, null, '0', null, null, '闫丹杰', '029-89625309', null, '2018-12-10', '2018-12-10', 'phase2', '5', '8', null, null, null, null, null, null, null, null, '0', '0', '0', '0', '0', '1', '1', null, '10', null, null, null, null, null, null, null, '1', null, 'A', null, null, null, null, '1', null, null, '南院门');
INSERT INTO `baseline_companies` VALUES ('35', '福建省南安市立丰微晶石材发展有限公司西安分公司', '91610103MA6TX1X74U', null, '丘启辉', null, '陕西省', '西安市', '碑林区', '西安市碑林区粉巷3号真爱粉巷里5层505室', '德福巷', null, null, null, null, null, null, '陕西省', '西安市', '碑林区', null, null, null, null, null, null, null, null, null, null, null, '13679216180', '石材、石材工艺品、人造石、微晶石的销售', null, null, '5287', null, null, null, null, '10', '159', '2015', '10', '1', '2', '0', '1', null, '0', '0', '0', '0', null, null, null, null, null, null, null, '1', null, null, null, null, null, '0', null, null, '李雪梅', '13679216180', null, '2018-12-10', '2018-12-10', 'phase2', '2', null, null, null, null, null, null, null, null, null, '0', '0', '0', '0', '0', '1', '1', null, '10', null, null, null, null, null, null, null, '1', null, 'A', null, null, null, null, '1', null, null, '南院门');
INSERT INTO `baseline_companies` VALUES ('36', '西安鹏森网络科技有限公司', '91610103081014171U', null, '任建鹏', null, '陕西省', '西安市', '碑林区', '陕西省西安市碑林区书院门古玩艺术城3幢4单元40302室', '书院门', null, null, null, null, null, null, '陕西省', '西安市', '碑林区', null, null, null, null, null, null, null, null, null, null, null, '18821720771', '互联网店广告服务', null, null, '7251', null, null, null, null, '10', '173', '2013', '12', '2', '1', '0', '1', null, '0', '0', '0', '0', null, null, null, null, null, null, null, '1', null, null, null, null, null, '0', null, null, '任建鹏', '18821720771', null, '2018-12-10', '2018-12-10', 'phase2', '4', null, null, null, null, null, null, null, null, null, '0', '0', '0', '0', '0', '1', '1', null, '10', null, null, null, null, null, null, null, '1', null, 'A', null, null, null, null, '1', null, null, '南院门');
INSERT INTO `baseline_companies` VALUES ('37', '陕西千景建设工程有限责任公司', '91610000681558172B', null, '陈友强', null, '陕西省', '西安市', '碑林区', '陕西省西安市碑林区荣民国际公寓11118', '南广济街', null, null, null, null, null, null, '陕西省', '西安市', '碑林区', null, null, null, null, null, null, null, null, null, null, null, '18984548888', '地下管廊和隧道施工', null, null, '4853', null, null, null, null, '10', '173', '2008', '10', '1', '1', '0', '1', null, '0', '0', '0', '0', null, null, null, null, null, null, null, '1', null, null, null, null, null, '0', null, null, '李晨', '13772177258', null, '2018-12-10', '2018-12-10', 'phase2', '7', null, null, null, null, null, null, null, null, null, '0', '0', '0', '0', '0', '1', '1', null, '10', null, null, null, null, null, null, null, '1', null, 'A', null, null, null, null, '1', null, null, '南院门');
INSERT INTO `baseline_companies` VALUES ('38', '西安市碑林区科学技术局', '11610103013383100E', null, '何明', null, '陕西省', '西安市', '碑林区', '陕西省西安市碑林区南院门27号', '南院门社区', null, null, null, null, null, null, '陕西省', '西安市', '碑林区', null, null, null, null, null, null, null, null, null, '029-89625256', null, null, '综合事务管理', null, null, '9221', null, null, null, null, '30', '110', '1978年', '2月', '1', '1', '0', '3', null, '0', '0', '0', '0', null, null, null, null, null, null, null, '1', null, null, null, null, null, '0', null, null, '吴静', '89625256', null, '2018-12-10', '2018-12-10', 'phase2', '5', '8', null, null, null, null, null, null, null, null, '0', '0', '0', '0', '0', '1', '1', null, '10', null, null, null, null, null, null, null, '1', null, 'A', null, null, null, null, '1', null, null, '南院门');
INSERT INTO `baseline_companies` VALUES ('39', '西安饮食股份有限公司永宁美术馆', '91610103321964126R', null, '王罡', null, '陕西省', '西安市', '碑林区', '西安市碑林区南大街2号', '德福巷', null, null, null, null, null, null, '陕西省', '西安市', '碑林区', null, null, null, null, null, null, null, null, null, null, null, '13609299852', '房屋租赁；物业管理', null, null, '7020', null, null, null, null, '10', '160', '2015', '1', '1', '2', '0', '1', null, '0', '0', '0', '0', null, null, null, null, null, null, null, '1', null, null, null, null, null, '0', null, null, '王罡', '13609299852', null, '2018-12-10', '2018-12-10', 'phase2', '2', null, null, null, null, null, null, null, null, null, '0', '0', '0', '0', '0', '1', '1', null, '10', null, null, null, null, null, null, null, '1', null, 'A', null, null, null, null, '1', null, null, '南院门');
INSERT INTO `baseline_companies` VALUES ('40', '西安三秦物业管理有限公司', '91610103MA6V6A7D6W', null, '董超', null, '陕西省', '西安市', '碑林区', '陕西省西安市碑林区南院门横巷13栋4单元4030室', '大车家巷', null, null, null, null, null, null, '陕西省', '西安市', '碑林区', null, null, null, null, null, null, null, null, null, null, null, '13038587368', '物业管理', null, null, '7020', null, null, null, null, '10', '173', '2017', '7', '1', '1', '0', '1', null, '0', '0', '0', '0', null, null, null, null, null, null, null, '1', null, null, null, null, null, '0', null, null, '董超', '13038587368', null, '2018-12-10', '2018-12-10', 'phase2', '3', null, null, null, null, null, null, null, null, null, '0', '0', '0', '0', '0', '1', '1', null, '10', null, null, null, null, null, null, null, '1', null, 'A', null, null, null, null, '1', null, null, '南院门');
INSERT INTO `baseline_companies` VALUES ('41', '西安利兰物业管理', '91610103MA6UT56D1E', null, '吴剑', null, '陕西省', '西安市', '碑林区', '陕西省西安市碑林区书院门24号', '书院门', null, null, null, null, null, null, '陕西省', '西安市', '碑林区', null, null, null, null, null, null, null, null, null, null, null, '15389291911', '物业管理', null, null, '7020', null, null, null, null, '10', '173', '2018', '4', '1', '1', '0', '1', null, '0', '0', '0', '0', null, null, null, null, null, null, null, '1', null, null, null, null, null, '0', null, null, '吴剑', '15389291911', null, '2018-12-10', '2018-12-10', 'phase2', '4', null, null, null, null, null, null, null, null, null, '0', '0', '0', '0', '0', '1', '1', null, '10', null, null, null, null, null, null, null, '1', null, 'A', null, null, null, null, '1', null, null, '南院门');
INSERT INTO `baseline_companies` VALUES ('26473', '华联咖世家（北京）餐饮管理有限公司西安第四分店', '91610103MA6UTY3T2J', 'MA6UTY3T2', '毕思波', '610103007006', '陕西省', '西安市', '碑林区', '陕西省西安市碑林区长安北路261号3层B3014-1号', '仁义社区居委会', '610103007006', '003', '996', 'YZ_610103007006003_996', '', '610103', '陕西省', '西安市', '碑林区', '陕西省西安市碑林区长安北路261号3层B3014-1号', '', '', '610103', null, null, '', '', '029', '83698702', '', '', '预包装食品零售', '自制饮品零售', '', '5229', '其他食品零售', '', '', '', '10', '340', '2018', '4', '1', '2', '0', '', '', '0', '0', '0', '0', '', null, null, null, null, null, null, '1', null, null, null, null, null, '0', null, null, null, null, null, '2018-12-17', '2018-12-17', 'phase1', null, null, null, null, null, null, null, null, null, null, '0', '0', '0', '0', '0', '1', '1', null, '10', null, null, null, null, null, null, null, '1', null, 'A', null, null, null, null, '1', null, null, '长安路街道办事处');

-- ----------------------------
-- Table structure for baseline_companyinfo
-- ----------------------------
DROP TABLE IF EXISTS `baseline_companyinfo`;
CREATE TABLE `baseline_companyinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) DEFAULT NULL,
  `social_num` varchar(64) DEFAULT NULL,
  `org_num` varchar(64) DEFAULT NULL,
  `legal_person` varchar(32) DEFAULT NULL,
  `est_year` varchar(12) DEFAULT NULL,
  `est_month` varchar(12) DEFAULT NULL,
  `landline_area_code` varchar(12) DEFAULT NULL,
  `landline_num` varchar(32) DEFAULT NULL,
  `landline_branch_num` varchar(32) DEFAULT NULL,
  `mobile` varchar(32) DEFAULT NULL,
  `fax_code` varchar(32) DEFAULT NULL,
  `postalcode` varchar(32) DEFAULT NULL,
  `email` varchar(32) DEFAULT NULL,
  `website` varchar(32) DEFAULT NULL,
  `province` varchar(32) NOT NULL,
  `city` varchar(32) NOT NULL,
  `district` varchar(32) NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `street_district` varchar(32) DEFAULT NULL,
  `community` varchar(32) DEFAULT NULL,
  `district_code` varchar(32) DEFAULT NULL,
  `survey_area_code` varchar(32) DEFAULT NULL,
  `building_area_code` varchar(32) DEFAULT NULL,
  `building_unique_code` varchar(50) DEFAULT NULL,
  `park_name` varchar(32) DEFAULT NULL,
  `park_code` varchar(32) DEFAULT NULL,
  `register_province` varchar(32) DEFAULT NULL,
  `register_city` varchar(32) DEFAULT NULL,
  `register_district` varchar(32) DEFAULT NULL,
  `register_address` varchar(255) DEFAULT NULL,
  `register_street_district` varchar(32) DEFAULT NULL,
  `register_community` varchar(32) DEFAULT NULL,
  `register_district_code` varchar(32) DEFAULT NULL,
  `register_survey_area_code` varchar(32) DEFAULT NULL,
  `register_building_area_code` varchar(32) DEFAULT NULL,
  `register_park_name` varchar(32) DEFAULT NULL,
  `register_park_code` varchar(32) DEFAULT NULL,
  `operate_status` varchar(12) DEFAULT NULL,
  `main_activity_1` varchar(128) DEFAULT NULL,
  `main_activity_2` varchar(128) DEFAULT NULL,
  `main_activity_3` varchar(128) DEFAULT NULL,
  `industry_code` varchar(128) NOT NULL,
  `industry_name` varchar(128) DEFAULT NULL,
  `economic_code` varchar(128) DEFAULT NULL,
  `economic_name` varchar(128) DEFAULT NULL,
  `is_culture` varchar(12) DEFAULT NULL,
  `org_type` varchar(12) DEFAULT NULL,
  `register_type` varchar(12) DEFAULT NULL,
  `comp_type` varchar(12) DEFAULT NULL,
  `retail_management_form` varchar(12) DEFAULT NULL,
  `retail_management_brand` varchar(255) DEFAULT NULL,
  `retail_opetrate_type` varchar(32) DEFAULT NULL,
  `retail_business_area` varchar(12) DEFAULT NULL,
  `retail_hotel_diet_star` varchar(12) DEFAULT NULL,
  `retail_hotel_diet_area` varchar(12) DEFAULT NULL,
  `legal_unite_hkmatai` varchar(32) DEFAULT NULL,
  `legal_unite_hypotaxis` varchar(12) DEFAULT NULL,
  `legal_unite_stake` varchar(12) DEFAULT NULL,
  `accounting_rule` varchar(12) DEFAULT NULL,
  `accounting_rule_note` varchar(32) DEFAULT NULL,
  `legal_unite_accounting_standard` varchar(12) DEFAULT NULL,
  `legal_unite_company_size` varchar(12) DEFAULT NULL,
  `legal_unite_obtainemploy` varchar(255) DEFAULT NULL,
  `legal_unite_obtainemploy_female` varchar(255) DEFAULT NULL,
  `legal_unite_person_income` varchar(255) DEFAULT NULL,
  `legal_unite_person_assets` varchar(255) DEFAULT NULL,
  `legal_unite_person_taxes` varchar(255) DEFAULT NULL,
  `legal_unite_nonperson_defray` varchar(255) DEFAULT NULL,
  `legal_unite_nonperson_assets` varchar(255) DEFAULT NULL,
  `has_branch` tinyint(1) NOT NULL,
  `branch_cnt` varchar(12) DEFAULT NULL,
  `branch_type` varchar(12) DEFAULT NULL,
  `parent_type` varchar(12) DEFAULT NULL,
  `parent_comp_social_num` varchar(32) DEFAULT NULL,
  `parent_comp_org_num` varchar(32) DEFAULT NULL,
  `parent_comp_name` varchar(128) DEFAULT NULL,
  `parent_comp_address` varchar(255) DEFAULT NULL,
  `parent_comp_district_code` varchar(255) DEFAULT NULL,
  `branch_comp_social_num` varchar(32) DEFAULT NULL,
  `branch_comp_org_num` varchar(32) DEFAULT NULL,
  `branch_comp_name` varchar(128) DEFAULT NULL,
  `branch_comp_address` varchar(255) DEFAULT NULL,
  `branch_comp_district_code` varchar(255) DEFAULT NULL,
  `branch_comp_count_obtainemploy` varchar(255) DEFAULT NULL,
  `branch_comp_count_obtainemploy_female` varchar(255) DEFAULT NULL,
  `branch_comp_operate_income` varchar(255) DEFAULT NULL,
  `branch_comp_nooperate_defray` varchar(255) DEFAULT NULL,
  `branch_comp_house_sale_area` varchar(255) DEFAULT NULL,
  `branch_comp_house_nosale_area` varchar(255) DEFAULT NULL,
  `is_notice` tinyint(1) NOT NULL,
  `is_write_661_1` tinyint(1) NOT NULL,
  `is_write_661_3` tinyint(1) NOT NULL,
  `is_write_661_5` tinyint(1) NOT NULL,
  `is_write_661_6` tinyint(1) NOT NULL,
  `data_process_place` varchar(32) DEFAULT NULL,
  `as_legal_person` tinyint(1) NOT NULL,
  `produce_energy` tinyint(1) NOT NULL,
  `sell_energy` tinyint(1) NOT NULL,
  `involved_military` tinyint(1) NOT NULL,
  `is_orphan` tinyint(1) NOT NULL,
  `unique_code` varchar(64) DEFAULT NULL,
  `profess_category` varchar(64) DEFAULT NULL,
  `data_source` varchar(64) DEFAULT NULL,
  `interviewee` varchar(32) DEFAULT NULL,
  `interviewee_contact` varchar(32) DEFAULT NULL,
  `recorded_date` date DEFAULT NULL,
  `added_date` date NOT NULL,
  `modified_date` date NOT NULL,
  `record_type` varchar(12) DEFAULT NULL,
  `add_by_id` int(11) DEFAULT NULL,
  `modified_by_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `baseline_companyinfo_add_by_user_id_05b2647e` (`add_by_id`),
  KEY `baseline_companyinfo_modified_by_id_a301db28` (`modified_by_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of baseline_companyinfo
-- ----------------------------

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('4', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('6', 'sessions', 'session');
INSERT INTO `django_content_type` VALUES ('7', 'baseline', 'companies');
INSERT INTO `django_content_type` VALUES ('8', 'baseline', 'companyinfo');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2018-12-20 03:28:31.638863');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2018-12-20 03:28:33.186641');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2018-12-20 03:28:33.395154');
INSERT INTO `django_migrations` VALUES ('4', 'admin', '0002_logentry_remove_auto_add', '2018-12-20 03:28:33.407526');
INSERT INTO `django_migrations` VALUES ('5', 'admin', '0003_logentry_add_action_flag_choices', '2018-12-20 03:28:33.416968');
INSERT INTO `django_migrations` VALUES ('6', 'contenttypes', '0002_remove_content_type_name', '2018-12-20 03:28:33.515534');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0002_alter_permission_name_max_length', '2018-12-20 03:28:33.570094');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0003_alter_user_email_max_length', '2018-12-20 03:28:33.623230');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0004_alter_user_username_opts', '2018-12-20 03:28:33.633646');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0005_alter_user_last_login_null', '2018-12-20 03:28:33.685935');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0006_require_contenttypes_0002', '2018-12-20 03:28:33.689408');
INSERT INTO `django_migrations` VALUES ('12', 'auth', '0007_alter_validators_add_error_messages', '2018-12-20 03:28:33.698832');
INSERT INTO `django_migrations` VALUES ('13', 'auth', '0008_alter_user_username_max_length', '2018-12-20 03:28:33.771966');
INSERT INTO `django_migrations` VALUES ('14', 'auth', '0009_alter_user_last_name_max_length', '2018-12-20 03:28:33.872632');
INSERT INTO `django_migrations` VALUES ('15', 'baseline', '0001_initial', '2018-12-20 03:28:34.666716');
INSERT INTO `django_migrations` VALUES ('16', 'baseline', '0002_auto_20181220_1128', '2018-12-20 03:28:34.758019');
INSERT INTO `django_migrations` VALUES ('17', 'sessions', '0001_initial', '2018-12-20 03:28:34.831032');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('22neeovtto5x1feqbgii054dellcb1b7', 'NTJmMTEwM2M4Zjg4ODcxMjk5NWM4NmNlMWMyY2I2MGZhYWEzZTFlZjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJjZTc1ZDdhMDFhZDYzYjI5MTA3YTQ4N2IzYTFjZjAyOGI1NjJkMmZiIn0=', '2019-01-03 03:46:56.720334');
