DROP TABLE Forum;
DROP TABLE User_Information;

CREATE TABLE User_Information(
	user_id INT NOT NULL,
	email VARCHAR(255) NOT NULL,
	phone_number VARCHAR(10) NOT NULL,
	password VARCHAR(255) NOT NULL,
	PRIMARY KEY (user_id));

CREATE TABLE Forum(
	post_id INT NOT NULL,
	user_id INT NOT NULL,
	post_timestamp VARCHAR(255) NOT NULL,
	post_title VARCHAR(255) NOT NULL,
	post_content VARCHAR(5000) NOT NULL,
	PRIMARY KEY (post_id , user_id),
	FOREIGN KEY(user_id) REFERENCES User_Information(user_id) ON DELETE CASCADE);

INSERT INTO workout.User_Information VALUES(1, "anderliu0216@gmail.com", "4479021648", "19990216");