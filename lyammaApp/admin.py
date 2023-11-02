from django.contrib import admin
from .models import PartnerRequest,AllItems,launchPartner,Contact

# Register your models here.
admin.site.register(PartnerRequest)
admin.site.register(AllItems)
admin.site.register(launchPartner)
admin.site.register(Contact)