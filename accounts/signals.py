from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from .models import User,UserProfile

@receiver(post_save,sender=User)    #decorator to define sender and receiver function
def post_save_create_profile_receiver(sender, instance, created,**kwargs):
    print(created)
    if created:
        UserProfile.objects.create(user=instance)   # call korle profile hobe
        print("user profile is created")
    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()      #new create na hoye update hole
        except:
            UserProfile.objects.create(user=instance)
            print("Profile was not exist, but I created one ")
        print("User is Updated")

@receiver(pre_save,sender=User)
def pre_save_profile_receiver(sender,instance,**kwargs):
    print(instance.username, "The user is saved")