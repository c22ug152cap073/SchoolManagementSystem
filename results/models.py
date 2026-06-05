from django.db import models
from students.models import Student
from subjects.models import Subject


class Result(models.Model):

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE
    )

    marks = models.IntegerField()

    grade = models.CharField(
        max_length=2,
        blank=True
    )

    status = models.CharField(
        max_length=10,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def save(self, *args, **kwargs):

        if self.marks >= 90:
            self.grade = "A+"
        elif self.marks >= 80:
            self.grade = "A"
        elif self.marks >= 70:
            self.grade = "B"
        elif self.marks >= 60:
            self.grade = "C"
        else:
            self.grade = "F"

        self.status = "Pass" if self.marks >= 35 else "Fail"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student.name} - {self.subject.name}"