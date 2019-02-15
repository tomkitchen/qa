from django.db import models
# Create your models here.
class Card(models.Model):
    question = models.CharField(max_length=400)
    answer = models.CharField(max_length=400)
    station = models.CharField(max_length=100, choices=[
        ('1', 'Nursing Care 1 Fluid Therapy'),
        ('2', 'Nursing Care 3 IM Injection'),
        ('3', 'Nursing Care 4 Subcut Injection'),
        ('4', 'Nursing Care 11 IM Injection 2'),
        ('5', 'Nursing Care 12 IM Injection 3'),
        ('6', 'Nursing Care 16 Tube Feeding'),
        ('7', 'Nursing Care 17 Urinary Catheter Care'),
        ('8', 'Nursing Care 19 Dispensing Medication'),
        ('9', 'Supporting Anaesthesia 1 Ayres T Piece'),
        ('10', 'Supporting Anaesthesia 2 Bain'),
        ('11', 'Supporting Anaesthesia 3 Lack'),
        ('12', 'Supporting Anaesthesia 4 Mini Lack')])

    def __unicode__(self):
        return self.question
    __unicode__.allow_tags = True

    def question_tag(self):
        return self.question
    question_tag.allow_tags = True

    def answer_tag(self):
        return self.answer
    answer_tag.allow_tags = True
