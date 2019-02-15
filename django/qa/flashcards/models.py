from django.db import models

class Card(models.Model):
    question = models.CharField(max_length=400)
    answer = models.CharField(max_length=400)

    def __unicode__(self):
        return self.question
    __unicode__.allow_tags = True

    def question_tag(self):
        return self.question
    question_tag.allow_tags = True

    def answer_tag(self):
        return self.answer
        answer_tag.allow_tags = True

import random

random_idx = random.randint(0, Card.objects.count() - 1)
random_obj = Card.objects.all()[random_idx]
