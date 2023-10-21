-- Init Line Table
DROP TABLE IF EXISTS `line`;
CREATE TABLE `line` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ledger_id` int NOT NULL,
  `line_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `amount` decimal(10,2) NOT NULL,
  `deb_cred` tinyint(1) DEFAULT NULL,
  `freq` tinyint NOT NULL,
  `date_begin` date NOT NULL,
  `date_end` date DEFAULT NULL,
  `line_dts` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `ledger_id` (`ledger_id`),
  CONSTRAINT `line_ibfk_1` FOREIGN KEY (`ledger_id`) REFERENCES `ledger` (`id`),
  CONSTRAINT `line_chk_1` CHECK ((`amount` > 0)),
  CONSTRAINT `line_chk_2` CHECK ((`freq` >= 0))) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
LOCK TABLES `line` WRITE;
UNLOCK TABLES;