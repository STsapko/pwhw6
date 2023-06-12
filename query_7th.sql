SELECT group_name, student, subject, grade 
FROM grades AS g
INNER JOIN students AS s
ON g.student_id = s.id
INNER JOIN groups AS gr
ON s.group_id = gr.id
INNER JOIN subjects AS sb
ON g.subject_id = sb.id
GROUP BY gr.id, sb.id, s.id
ORDER BY group_name, student, subject, grade DESC;
