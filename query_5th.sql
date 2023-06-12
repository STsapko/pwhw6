SELECT instructor, subject
FROM subjects AS sb
INNER JOIN instructors AS i
ON sb.instructor_id = i.id
ORDER BY instructor, subject;
