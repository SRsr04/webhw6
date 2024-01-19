SELECT subjects.subject_name
FROM subjects
JOIN grades ON subjects.subject_id = grades.subject_id
WHERE grades.student_id = 'your_student_id' AND subjects.teacher_id = 'your_teacher_id';
