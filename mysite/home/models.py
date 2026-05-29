from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page


class HomePage(Page):
    #HERO

    # hero_title = models.CharField(max_length=100)
    # hero_subtitle = models.CharField(max_length=255)

    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    newrai_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
    # FieldPanel("hero_title"),
    # FieldPanel("hero_subtitle"),
    FieldPanel("hero_image"),
    FieldPanel("newrai_image"),
]

