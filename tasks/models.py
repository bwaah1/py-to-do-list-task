from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    choices = (
        ("DONE", "Done"),
        ("NOT DONE", "Not done"),
    )
    name = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=8, choices=choices)
    deadline = models.DateTimeField()
    tags = models.ManyToManyField(Tag, related_name="tags")

    def __str__(self):
        return f"{self.name} ({self.status}, {self.get_deadline_display()}, {self.get_tags_display()})"

    def get_deadline_display(self):
        return format(self.deadline, 'd.m.Y H:i')

    def get_tags_display(self):
        return ", ".join(tag.name for tag in self.tags.all())
