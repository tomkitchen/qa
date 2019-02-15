from django.db import models

class Card(models.Model):
    question = models.CharField(max_length=400)
    answer = models.CharField(max_length=400)
    chapter = models.CharField(max_length=100, choices=[
        ('1', 'Chapter 1: Enterprise Campus Network Design'),
        ('2', 'Chapter 2: Switch Operation'),
        ('3', 'Chapter 3: Switch Port Configuration'),
        ('4', 'Chapter 4: VLANs and Trunks'),
        ('5', 'Chapter 5: VLAN Trunking Protocol'),
        ('6', 'Chapter 6: Traditional Spanning Tree Protocol'),
        ('7', 'Chapter 7: Spanning Tree Configuration'),
        ('8', 'Chapter 8: Protecting the Spanning Tree Protocol Topology'),
        ('9', 'Chapter 9: Advanced Spanning Tree Protocol'),
        ('10', 'Chapter 10: Aggregating Switch Links'),
        ('11', 'Chapter 11: Multilayer Switching'),
        ('12', 'Chapter 12: Configuring DHCP'),
        ('13', 'Chapter 13: Logging Switch Activity'),
        ('14', 'Chapter 14: Managing Switches with SNMP'),
        ('15', 'Chapter 15: Monitoring Performance with IP SLA'),
        ('16', 'Chapter 16: Using Port Mirroring to Monitor Traffic'),
        ('17', 'Chapter 17: Understanding High Availability'),
        ('18', 'Chapter 18: Layer 3 High Availability'),
        ('19', 'Chapter 19: Securing Switch Access'),
        ('20', 'Chapter 20: Securing VLANs'),
        ('21', 'Chapter 21: Preventing Spoofing Attacks'),
        ('22', 'Chapter 22: Managing Switch Users')])

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

#random_idx = random.randint(0, Card.objects.count() - 1)
#random_obj = Card.objects.all()[random_idx]
