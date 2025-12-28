from django.db import models

class Job(models.Model):
    '''Model definition for Job.'''
    task = models.CharField(max_length=100)
    status = models.CharField(max_length=500, blank=True, null=True)
    class Meta:
        '''Meta definition for Job.'''

        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'

    def __str__(self):
        pass