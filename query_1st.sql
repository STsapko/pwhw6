SELECT student, AVG(grade) AS avg_grade 
FROM grades AS g
INNER JOIN students AS s
ON g.student_id = s.id
GROUP BY student_id
ORDER BY avg_grade DESC
LIMIT 5;