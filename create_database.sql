CREATE TABLE `users` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `email` TEXT NOT NULL UNIQUE,
    `password` TEXT NOT NULL
);

CREATE TABLE `movies` (
    `id` INTEGER NOT NULL UNIQUE PRIMARY KEY,
    `title` TEXT NOT NULL,
    `director_id` TEXT NOT NULL,
    `year_released` INTEGER NOT NULL
);

CREATE TABLE `actors` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `first_name` TEXT NOT NULL,
    `last_name` TEXT NOT NULL
);

CREATE TABLE `role` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `movie_id` TEXT NOT NULL,
    `actor_id` TEXT NOT NULL,
    `character_name` TEXT NOT NULL
);

CREATE TABLE `directors` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `first_name` TEXT NOT NULL,
    `last_name` TEXT NOT NULL
);