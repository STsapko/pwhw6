SELECT DISTINCT student, subject 
FROM grades AS g
INNER JOIN students AS s
ON g.student_id = s.id
INNER JOIN subjects AS sb
ON g.subject_id = sb.id
ORDER BY student, subject;
