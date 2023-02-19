-- @block
CREATE DATABASE recify;
-- @block
CREATE TABLE ingredients,
ingredient VARCHAR(255) NOT NULL UNIQUE,
category VARCHAR(255),
technique TEXT;
-- @block
INSERT INTO ingredients (ingredient, category, technique)
VALUES ("flour", "baking", "null"),
    ("yeast", "baking", "null"),
    ("eggs", "misc", "null"),
    ("milk", "misc", "null"),
    ("sugar", "baking", "null"),
    ("baking soda", "baking", "null"),
    ("baking powder", "baking", "null"),
    ("salt", "misc", "null"),
    ("brown sugar", "baking", "null"),
    ("cinnamon", "baking", "null"),
    ("butter", "misc", "null"),
    ("oil", "misc", "null"),
    ("vanilla extract", "baking", "null");
("chocolate", "sweets, null");
-- @block
SELECT *
FROM ingredients;