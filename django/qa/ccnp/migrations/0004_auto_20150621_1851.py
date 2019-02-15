# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ccnp', '0003_auto_20150621_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='chapter',
            field=models.CharField(max_length=100, choices=[(b'1', b'Chapter 1: Enterprise Campus Network Design'), (b'2', b'Chapter 2: Switch Operation'), (b'3', b'Chapter 3: Switch Port Configuration'), (b'4', b'Chapter 4: VLANs and Trunks'), (b'5', b'Chapter 5: VLAN Trunking Protocol'), (b'6', b'Chapter 6: Traditional Spanning Tree Protocol'), (b'7', b'Chapter 7: Spanning Tree Configuration'), (b'8', b'Chapter 8: Protecting the Spanning Tree Protocol Topology'), (b'9', b'Chapter 9: Advanced Spanning Tree Protocol'), (b'10', b'Chapter 10: Aggregating Switch Links'), (b'11', b'Chapter 11: Multilayer Switching'), (b'12', b'Chapter 12: Configuring DHCP'), (b'13', b'Chapter 13: Logging Switch Activity'), (b'14', b'Chapter 14: Managing Switches with SNMP'), (b'15', b'Chapter 15: Monitoring Performance with IP SLA'), (b'16', b'Chapter 16: Using Port Mirroring to Monitor Traffic'), (b'17', b'Chapter 17: Understanding High Availability'), (b'18', b'Chapter 18: Layer 3 High Availability'), (b'19', b'Chapter 19: Securing Switch Access'), (b'20', b'Chapter 20: Securing VLANs'), (b'21', b'Chapter 21: Preventing Spoofing Attacks'), (b'22', b'Chapter 22: Managing Switch Users')]),
            preserve_default=True,
        ),
    ]
