(SELECT channel_title, COUNT(video_id) AS cnt
FROM workout.Workout_Video_Trainer NATURAL JOIN workout.Channels
WHERE video_viewCount > 1000000 AND publish_date LIKE "202%"
GROUP BY channel_id

UNION

SELECT channel_title, COUNT(video_id) AS cnt
FROM workout.Workout_Video_Type NATURAL JOIN workout.Channels
WHERE video_viewCount > 1000000 AND workout_type = "HIIT&crossfit"
GROUP BY channel_id

UNION

SELECT channel_title, COUNT(video_id) AS cnt
FROM workout.Recipe_Video NATURAL JOIN workout.Channels
WHERE video_viewCount > 1000000
GROUP BY channel_id)
ORDER BY cnt DESC
LIMIT 15;