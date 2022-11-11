SELECT *
FROM (SELECT * FROM workout.Recipe_Video WHERE video_viewCount > 100000) AS rv NATURAL JOIN (SELECT * FROM workout.Channels WHERE subscriberCount > 1000000) AS ch
WHERE video_title LIKE "%vegan%"
ORDER BY likeCount DESC
LIMIT 15;