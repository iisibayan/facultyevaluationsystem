from django.db import models


class Teacher(models.Model):
    name = models.CharField(verbose_name='Name of teacher',
                            max_length=255, unique=True)

    @property
    def avgFeedback(self):
        feedbacks = self.feedbackdata_set.all()
        l = len(feedbacks)
        avgFeedbacks = {
            'punctuality':0,
            'portion':0,
            'doubt':0,
            'interactive':0
            }
        if l:
            for feedback in feedbacks:
                avgFeedbacks['punctuality']+=int(feedback.punctuality)
                avgFeedbacks['portion'] += int(feedback.portion)
                avgFeedbacks['doubt']+= int(feedback.doubt)
                avgFeedbacks['interactive']+= int(feedback.interactive)
            avgFeedbacks['punctuality']/=l
            avgFeedbacks['portion']/=l
            avgFeedbacks['doubt']/=l
            avgFeedbacks['interactive']/=l
        return avgFeedbacks
    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

    def __str__(self):
        return self.name
