from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page


class HomePage(Page):
    #HERO

    hero_title = models.CharField(max_length=100, blank=True)
    hero_subtitle = models.CharField(max_length=255, blank=True)

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

    #OUR TECNOLOGIES
    
    django_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    django_text = models.CharField(max_length=255, blank=True)

    docker_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    docker_text = models.CharField(max_length=255, blank=True)

    flutter_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    flutter_text = models.CharField(max_length=255, blank=True)

    graphql_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    graphql_text = models.CharField(max_length=255, blank=True)

    hashi_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    hashi_text = models.CharField(max_length=255, blank=True)

    mongo_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    mongo_text = models.CharField(max_length=255, blank=True)

    postgre_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    postgre_text = models.CharField(max_length=255, blank=True)

    react_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    react_text = models.CharField(max_length=255, blank=True)

    #ABOUT US

    About_Us_Text_1 = models.CharField(max_length=255, blank=True)


    content_panels = Page.content_panels + [
    FieldPanel("hero_title"),
    FieldPanel("hero_subtitle"),
    FieldPanel("hero_image"),
    FieldPanel("newrai_image"),

    FieldPanel("django_image"),
    FieldPanel("django_text"),
    FieldPanel("docker_image"),
    FieldPanel("docker_text"),
    FieldPanel("flutter_image"),
    FieldPanel("flutter_text"),
    FieldPanel("graphql_image"),
    FieldPanel("graphql_text"),
    FieldPanel("hashi_image"),
    FieldPanel("hashi_text"),
    FieldPanel("mongo_image"),
    FieldPanel("mongo_text"),
    FieldPanel("postgre_image"),
    FieldPanel("postgre_text"),
    FieldPanel("react_image"),
    FieldPanel("react_text"),

    FieldPanel("About_Us_Text_1"),
]

