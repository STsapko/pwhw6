SELECT group_name, student
FROM students AS s
INNER JOIN groups AS gr
ON s.group_id = gr.id
ORDER BY group_name, student;
