DROP TABLE IF EXISTS Forum;
DROP TABLE IF EXISTS User_Information;

CREATE TABLE User_Information(
	user_id VARCHAR(255) NOT NULL,
	email VARCHAR(255) NOT NULL,
	phone_number VARCHAR(10) NOT NULL,
	password VARCHAR(255) NOT NULL,
	PRIMARY KEY (user_id));

CREATE TABLE Forum(
	post_id INT NOT NULL AUTO_INCREMENT,
	user_id VARCHAR(255) NOT NULL,
	post_title VARCHAR(255) NOT NULL,
	post_content VARCHAR(5000) NOT NULL,
	PRIMARY KEY (post_id),
	FOREIGN KEY(user_id) REFERENCES User_Information(user_id) ON DELETE CASCADE);

INSERT INTO workout.User_Information VALUES("anderliu", "anderliu0216@gmail.com", "4479021648", "19990216");
INSERT INTO workout.Forum VALUES(1, "anderliu", "Fisrt time trying workout", "feeling good");
INSERT INTO workout.Forum VALUES(2, "anderliu", "Hello world", "Hello world");