from django.db import models
from django.contrib.auth.models import User


class Poll(models.Model):
    question = models.CharField(max_length=250)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="poll_user")
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question


class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="poll_choice")
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text


class Vote(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name="vote_choices")
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="vote_poll")
    voted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="voter")

    class Meta:
        unique_together = ('poll', 'voted_by')
