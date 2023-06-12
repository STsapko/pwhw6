SELECT student, subject, MAX(grade) AS max_grade 
FROM grades AS g
INNER JOIN students AS s
ON g.student_id = s.id
INNER JOIN subjects AS sb
ON g.subject_id = sb.id
GROUP BY subject_id;
