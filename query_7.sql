SELECT student_id, grade
FROM grades
WHERE subject_id = 'your_subject_id' AND student_id IN (SELECT student_id FROM students WHERE group_id = 'your_group_id');
