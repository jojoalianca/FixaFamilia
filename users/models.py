from django.db import models
from custom.models import *
from django.contrib.auth.models import User, Group,AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
 
class AdminSuku(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE, null=True, verbose_name="Munisipiu")
    administrativepost = models.ForeignKey(AdministrativePost, on_delete=models.CASCADE, null=True, verbose_name="Postu Administrativu")
    village = models.ForeignKey(Village, on_delete=models.CASCADE, null=True, verbose_name="Suku")
    aldeia = models.ForeignKey(Aldeia, on_delete=models.CASCADE, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    groups = models.ManyToManyField(Group, verbose_name="Grupu", blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.village.name if self.village else ''}"

    class Meta:
        verbose_name = "Admin Suku"
        verbose_name_plural = "Admin Suku"

# Signal untuk otomatis menambahkan ke group 'Admin Suku' ketika dibuat
@receiver(post_save, sender=AdminSuku)
def add_to_admin_suku_group(sender, instance, created, **kwargs):
    if created:
        group, _ = Group.objects.get_or_create(name='Admin Suku')
        instance.user.groups.add(group)
        instance.user.save()