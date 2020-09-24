
-- DROP DATABASE todo IF EXISTS;
-- CREATE DATABASE todo;

CREATE TABLE `todos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created` datetime NOT NULL,
  `description` varchar(60) NOT NULL,
  `uuid` varchar(36) NOT NULL,
  `status` varchar(10) DEFAULT '',
  `deleted` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

INSERT INTO `todos` (`id`, `created`, `description`, `uuid`, `status`, `deleted`)
VALUES
	(1, '2020-08-31 16:57:33', 'Take out the milk', '3ac66762-fb8e-11ea-adc1-0242ac120002', '', NULL);
