from django.db import models
from django.urls import reverse
from Home.models import Teacher


class FeedbackData(models.Model):
    class Choice(models.IntegerChoices):
        Strongly_Disagree = 1
        Disagree = 2
        Sometimes = 3
        Agree = 4
        Strongly_Agree = 5
    date_submitted = models.DateTimeField(auto_now=True)

    teacher_name = models.ForeignKey(Teacher, verbose_name='Name of Teacher',
                                     on_delete=models.CASCADE)

    punctuality = models.IntegerField(verbose_name='The teacher is punctual in coming to class',choices=Choice.choices)

    portion = models.IntegerField(verbose_name='The teacher completes portions at the appropriate time',choices=Choice.choices)
                               
                               

    doubt = models.IntegerField(verbose_name='The teacher takes in effort to clear your doubts',choices=Choice.choices)

    interactive = models.IntegerField(verbose_name='The teacher makes the class interactive',choices=Choice.choices)

    comments = models.TextField(verbose_name='Any other feedback (your comments)',
                                blank=True)

    class Meta:
        verbose_name = 'Feedback Data'
        verbose_name_plural = 'Feedback Data'

    def __str__(self):
        return self.teacher_name.name

    def get_absolute_url(self):
        return reverse('SuccessView')
