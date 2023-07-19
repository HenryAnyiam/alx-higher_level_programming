-- creates a new database hbtn_0d_usa if it doesn't exist
-- creates tge table states in the hbtn_0d_usa database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
	PRIMARY KEY(id),
	id INT AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL);
