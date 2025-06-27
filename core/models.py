from django.db import models
from django.contrib.auth.models import User

# Helper function to convert marks to grade points
def get_grade_point(mark):
    if mark >= 80:
        return 4.0
    elif mark >= 75:
        return 3.75
    elif mark >= 70:
        return 3.5
    elif mark >= 65:
        return 3.25
    elif mark >= 60:
        return 3.0
    elif mark >= 55:
        return 2.75
    elif mark >= 50:
        return 2.5
    elif mark >= 45:
        return 2.25
    elif mark >= 40:
        return 2.0
    else:
        return 0.0

class SemesterResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    semester_name = models.CharField(max_length=100)
    total_credits = models.FloatField(default=0.0)
    gpa = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)

    def calculate_gpa(self):
        subjects = self.subject_set.all()
        total_points = 0
        total_credits = 0

        for subject in subjects:
            grade_point = get_grade_point(subject.mark)
            total_points += grade_point * subject.credit
            total_credits += subject.credit

        if total_credits > 0:
            self.gpa = round(total_points / total_credits, 2)
            self.total_credits = total_credits
        else:
            self.gpa = 0.0
            self.total_credits = 0.0

        self.save()

    def __str__(self):
        return f"{self.user.username} - {self.semester_name}"

class Subject(models.Model):
    semester = models.ForeignKey(SemesterResult, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    mark = models.FloatField()
    credit = models.FloatField()

    def __str__(self):
        return f"{self.name} ({self.mark} marks)"
