import uuid

from django.db import models

from users.models import CustomUser

status = (
    ("PENDING", "Pending"),
    ("FROZEN", "Frozen"),
    ("CLOSED", "Closed"),
)



class Ticket(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None)
    content = models.TextField()
    created = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=status, max_length=155, default="PENDING")
    modified = models.DateTimeField(auto_now=True)
    answer = models.CharField(max_length=255, default="")

    def __str__(self):
        return "{} - {}".format(self.title, self.ticket_id)

    def save(self, *args, **kwargs):
        super(Ticket, self).save(*args, **kwargs) # Call the real   save() method

    class Meta:
        ordering = ["-created"]



class Discussion(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255, default=None, null=True)
    ticket = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created"]
