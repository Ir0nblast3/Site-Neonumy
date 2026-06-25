from django.db import models
from wagtail.contrib.settings.models import BaseGenericSetting, register_setting
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.models import Orderable
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

class SocialsLogo(Orderable):
    footer = ParentalKey(
        'base.FooterSettings',
        on_delete=models.CASCADE,
        related_name='socials'
    )

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    url = models.URLField()

    panels = [
        FieldPanel('image'),
        FieldPanel("url"),
    ]

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
class FooterSettings(BaseGenericSetting, ClusterableModel):
    
    address = models.CharField("Address",max_length=255,blank=True)
    email = models.CharField("Email", max_length=255, blank=True)

    finaciamento_icon=models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    panels = [
        MultiFieldPanel(
            [
                InlinePanel("socials", label="Socials"),
                FieldPanel("address"),
                FieldPanel("email")
            ],
            "Social settings",
        )
    ]
