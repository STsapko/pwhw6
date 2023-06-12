SELECT instructor, AVG(grade) AS avg_grade 
FROM grades AS g
INNER JOIN subjects AS sb
ON g.subject_id = sb.id
INNER JOIN instructors AS i
ON sb.instructor_id = i.id
GROUP BY i.id
ORDER BY instructor;
