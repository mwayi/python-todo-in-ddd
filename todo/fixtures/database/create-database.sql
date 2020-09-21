CREATE TABLE todos (
    `id` int(11) NOT NULL,
    `created` datetime NOT NULL,
    `description` varchar(60) NOT NULL,
    `uuid` varchar(36) NOT NULL,
    `status` varchar(10) NOT NULL,
    `deleted` datetime(6) DEFAULT NULL,
    PRIMARY KEY (id)
);