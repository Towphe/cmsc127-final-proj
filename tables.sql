-- create database
CREATE DATABASE IF NOT EXISTS food;

-- use database
USE food;

-- define tables
CREATE TABLE user (
    username VARCHAR(50) NOT NULL UNIQUE PRIMARY KEY, 
    password VARCHAR(50) NOT NULL, 
    type VARCHAR(5) NOT NULL -- Admin or User only
); 

CREATE TABLE establishment (
    establishment_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY, 
    added_by VARCHAR(50) NOT NULL, 
    establishment_name VARCHAR(50) NOT NULL, 
    average_rating DECIMAL(3,2) DEFAULT 0, -- Ratings range from 1-5; Average would always be one digit + 2 decimal points
    CONSTRAINT fk_estab_user FOREIGN KEY(added_by) REFERENCES user(username)
);

CREATE TABLE food_item (
    food_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY, 
    establishment_id INT NOT NULL,  -- FK
    food_name VARCHAR(50) NOT NULL,
    price DECIMAL (10,2) NOT NULL,
    category VARCHAR(100),
    average_rating DECIMAL(3,2) DEFAULT 0, -- Ratings range from 1-5; Average would always be one digit + 2 decimal points
    CONSTRAINT fk_item_estab FOREIGN KEY(establishment_id) REFERENCES establishment(establishment_id) 
);

CREATE TABLE food_review (
    review_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    food_id INT NOT NULL, -- FK
    reviewer_username VARCHAR(50) NOT NULL, -- FK
    content TEXT NOT NULL,
    rating INT NOT NULL,
    date_created DATE NOT NULL DEFAULT CURDATE(),
    CONSTRAINT fk_frev_user FOREIGN KEY(reviewer_username) REFERENCES user(username),
    CONSTRAINT fk_frev_estab FOREIGN KEY(establishment_id) REFERENCES establishment(establishment_id),
    CONSTRAINT fk_frev_item FOREIGN KEY(food_id) REFERENCES food_item(food_id)
);


CREATE TABLE establishment_review (
    review_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    establishment_id INT NOT NULL, -- FK
    reviewer_username VARCHAR(50) NOT NULL, -- FK
    content TEXT NOT NULL,
    rating INT NOT NULL,
    date_created DATE NOT NULL DEFAULT CURDATE(),
    CONSTRAINT fk_erev_user FOREIGN KEY(reviewer_username) REFERENCES user(username),
    CONSTRAINT fk_erev_estab FOREIGN KEY(establishment_id) REFERENCES establishment(establishment_id)
);