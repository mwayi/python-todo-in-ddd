CREATE TABLE todos (
    `id` integer primary key,
    `created` datetime NOT NULL,
    `description` varchar(60) NOT NULL,
    `uuid` varchar(36) NOT NULL,
    `status` varchar(10) DEFAULT NULL,
    `deleted` datetime(6) DEFAULT NULL
);