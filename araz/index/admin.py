from django.contrib import admin
from .models import (Slider,
    Address,
    Phone,
    Statistic,
    OpeningHour,
    SocialNetwork,
    Newsletter,
    )

admin.site.register(Slider)
admin.site.register(Address)
admin.site.register(Phone)
admin.site.register(Statistic)
admin.site.register(OpeningHour)
admin.site.register(SocialNetwork)
admin.site.register(Newsletter)
