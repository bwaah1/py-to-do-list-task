from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    STATUS_CHOICES = (
        ("DONE", "Done"),
        ("NOT DONE", "Not done"),
    )
    name = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)
    deadline = models.DateTimeField()
    tags = models.ForeignKey(Tag, blank=True, null=True, related_name="tasks", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.status}, {self.get_deadline_display()})"

    def get_deadline_display(self):
        return format(self.deadline, 'd.m.Y H:i')
