SELECT teacher_id, AVG(grade) AS average_grade
FROM subjects
JOIN grades ON subjects.subject_id = grades.subject_id
GROUP BY teacher_id;
