from django.db import models

class Club(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    founded_date = models.DateField()

    def __str__(self):
        return self.name

class Member(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=100)
    join_date = models.DateField()

    def __str__(self):
        return self.name

class Event(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title

class Announcement(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    message = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
