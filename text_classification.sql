/*
Navicat MySQL Data Transfer

Source Server         : classification
Source Server Version : 50721
Source Host           : 47.98.96.189:3306
Source Database       : text_classification

Target Server Type    : MYSQL
Target Server Version : 50721
File Encoding         : 65001

Date:UTC+3 2020-05-11 09:01:19 
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for news_classify
-- ----------------------------
DROP TABLE IF EXISTS `news_classify`;
CREATE TABLE `news_classify` (
  `classify_id` int(11) NOT NULL AUTO_INCREMENT,
  `classify` varchar(10) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`classify_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

-- insert classified_dictionary
INSERT INTO `text_classification`.`news_classify` (`classify_id`, `classify`) VALUES ('1', '体育'),('2', '财经'),('3', '房产'),('4','家居'),('5','教育'),('6','科技'),('7','时尚'),('8','时政'),('9','游戏'),('10','娱乐'),('11','股票'),('12','彩票'),('13','社会')
    ,('14','星座');

-- ----------------------------
-- Table structure for wangyi_news
-- ----------------------------
DROP TABLE IF EXISTS `wangyi_news`;
CREATE TABLE `wangyi_news` (
  `news_id` int(11) NOT NULL AUTO_INCREMENT,
  `news_title` varchar(600) CHARACTER SET utf8 DEFAULT NULL,
  `news_url` varchar(600) DEFAULT NULL,
  `news_article` longtext CHARACTER SET utf8,
  `insert_time` varchar(11) DEFAULT NULL,
  PRIMARY KEY (`news_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2627 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for wangyi_news_classify
-- ----------------------------
DROP TABLE IF EXISTS `wangyi_news_classify`;
CREATE TABLE `wangyi_news_classify` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `news_id` int(11) DEFAULT NULL,
  `classify_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `wangyi_news_classify_ibfk_1` (`news_id`),
  KEY `wangyi_news_classify_ibfk_2` (`classify_id`),
  CONSTRAINT `wangyi_news_classify_ibfk_1` FOREIGN KEY (`news_id`) REFERENCES `wangyi_news` (`news_id`),
  CONSTRAINT `wangyi_news_classify_ibfk_2` FOREIGN KEY (`classify_id`) REFERENCES `news_classify` (`classify_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2776 DEFAULT CHARSET=latin1;

-- ----------------------------
-- View structure for view_news_classify
-- ----------------------------
DROP VIEW IF EXISTS `view_news_classify`;
CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`%` SQL SECURITY DEFINER VIEW `view_news_classify` AS select `wangyi_news_classify`.`news_id` AS `news_id`,`wangyi_news`.`news_title` AS `news_title`,`wangyi_news`.`news_url` AS `news_url`,`wangyi_news`.`insert_time` AS `insert_time`,`news_classify`.`classify` AS `classify` from ((`wangyi_news` join `news_classify`) join `wangyi_news_classify`) where ((`wangyi_news`.`news_id` = `wangyi_news_classify`.`news_id`) and (`news_classify`.`classify_id` = `wangyi_news_classify`.`classify_id`)) order by `wangyi_news`.`insert_time` desc ;
