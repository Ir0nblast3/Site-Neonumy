from django.db import models
from wagtail.contrib.settings.models import BaseGenericSetting, register_setting
from wagtail.admin.panels import FieldPanel, MultiFieldPanel


@register_setting
class NavigationSettings(BaseGenericSetting):

    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel("logo"),
    ]


@register_setting
class FooterSettings(BaseGenericSetting):
    
    finaciamento_icon=models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
   
    facebook_url = models.URLField(verbose_name="Facebook URL", blank=True)
    facebook_icon= models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    instagram_url = models.URLField(verbose_name="Instagram URL", blank=True)
    instagram_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    linkedin_url = models.URLField(verbose_name="LinkedIn URL", blank=True)
    linkedin_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    whatsapp_url = models.URLField(verbose_name="WhatsApp URL", blank=True)
    whatsapp_icon = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("facebook_url"),
                FieldPanel("facebook_icon"),
                FieldPanel("instagram_url"),
                FieldPanel("instagram_icon"),
                FieldPanel("linkedin_url"),
                FieldPanel("linkedin_icon"),
                FieldPanel("whatsapp_url"),
                FieldPanel("whatsapp_icon"),
                FieldPanel("finaciamento_icon")
            ],
            "Social settings",
        )
    ]
