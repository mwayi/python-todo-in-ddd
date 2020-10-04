
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
	(1, '2020-08-31 16:57:33', 'Make a todo list', '3ac66762-fb8e-11ea-adc1-0242ac120002', 'done', NULL),
	(2, '2020-09-21 13:35:04', 'Check off first thing on todo list', '55009123-9bb3-4992-87c1-f8bd4eff0b87', 'done', NULL),
	(3, '2020-09-21 13:35:28', 'Realise that I have already done two things', 'b356940e-9a30-481e-b62e-886c0dd75793', NULL, NULL),
	(5, '2020-09-21 13:51:22', 'Reward myself for the above accomplishments', '736e435d-00ea-484a-8823-55129a157161', NULL, NULL);
