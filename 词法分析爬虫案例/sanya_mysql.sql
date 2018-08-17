CREATE TABLE `illegal_ad` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `illegalID` int(50) DEFAULT NULL,
  `siteName` tinytext COMMENT '网站名称',
  `illegalContent` varchar(10000) DEFAULT NULL COMMENT '违规内容',
  `adUrl` varchar(45) DEFAULT NULL COMMENT '违规广告链接',
  `title` varchar(255) DEFAULT NULL COMMENT '标题',
  `illegalKeyWord_before` varchar(500) DEFAULT NULL,
  `illegalKeyWord` varchar(500) DEFAULT NULL COMMENT '违规关键字',
  `isCut` int(4) DEFAULT NULL COMMENT '是否分词采集（1是，0否）',
  `cutWord` varchar(10000) DEFAULT NULL COMMENT '分词（方便查询是否正确）',
  `screenshot` varchar(100) DEFAULT NULL COMMENT '截图',
  `modifyTime` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '修改时间',
  `createTime` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '采集时间',
  `isError` int(4) DEFAULT '0' COMMENT '是否有误',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3288 DEFAULT CHARSET=utf8 COMMENT='违规广告';




CREATE TABLE `illegal_jieba_userdict` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `errorWord` varchar(255) CHARACTER SET utf8mb4 DEFAULT NULL COMMENT '错误词',
  `remark` varchar(255) DEFAULT NULL COMMENT '备注',
  `is_cut_error` int(255) DEFAULT '1' COMMENT '1是分词错误、0是分词忽略',
  `is_force_keyWord` int(255) DEFAULT '0' COMMENT '是否强制添加关键字（1是强制，0不是）',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=83 DEFAULT CHARSET=utf8;

