from django.db.models.signals import post_save

from django.contrib.auth.models import Group, User

from django.dispatch import receiver

from user.models import userProfile


@receiver(post_save,sender=User)
def add_user_to_group(sender, instance,created,**kwargs):
    if created:
        default_group = Group.objects.get(name = '普通用户')
        instance.groups.add(default_group)