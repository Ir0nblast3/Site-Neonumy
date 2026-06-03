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

    Aboutus_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    About_Us_Text_2 = models.CharField(max_length=255, blank=True) 

    #OUR TEAM

    Image_1 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    Name_Text_1 = models.CharField(max_length=255, blank=True) 
    Role_Text_1 = models.CharField(max_length=255, blank=True)

    Image_2 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    Name_Text_2 = models.CharField(max_length=255, blank=True) 
    Role_Text_2 = models.CharField(max_length=255, blank=True)

    Image_3 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    Name_Text_3 = models.CharField(max_length=255, blank=True) 
    Role_Text_3 = models.CharField(max_length=255, blank=True)

    Image_4 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    Name_Text_4 = models.CharField(max_length=255, blank=True) 
    Role_Text_4 = models.CharField(max_length=255, blank=True)

    Image_5 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    Name_Text_5 = models.CharField(max_length=255, blank=True) 
    Role_Text_5 = models.CharField(max_length=255, blank=True)

    Image_6 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    Name_Text_6 = models.CharField(max_length=255, blank=True) 
    Role_Text_6 = models.CharField(max_length=255, blank=True)

    Image_7 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    Name_Text_7 = models.CharField(max_length=255, blank=True) 
    Role_Text_7 = models.CharField(max_length=255, blank=True)

    Image_8 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    Name_Text_8 = models.CharField(max_length=255, blank=True) 
    Role_Text_8 = models.CharField(max_length=255, blank=True)


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
    FieldPanel("Aboutus_image"),
    FieldPanel("About_Us_Text_2"),

    FieldPanel("Image_1"),
    FieldPanel("Name_Text_1"),
    FieldPanel("Role_Text_1"),
    FieldPanel("Image_2"),
    FieldPanel("Name_Text_2"),
    FieldPanel("Role_Text_2"),
    FieldPanel("Image_3"),
    FieldPanel("Name_Text_3"),
    FieldPanel("Role_Text_3"),
    FieldPanel("Image_4"),
    FieldPanel("Name_Text_4"),
    FieldPanel("Role_Text_4"),
    FieldPanel("Image_5"),
    FieldPanel("Name_Text_5"),
    FieldPanel("Role_Text_5"),
    FieldPanel("Image_6"),
    FieldPanel("Name_Text_6"),
    FieldPanel("Role_Text_6"),
    FieldPanel("Image_7"),
    FieldPanel("Name_Text_7"),
    FieldPanel("Role_Text_7"),
    FieldPanel("Image_8"),
    FieldPanel("Name_Text_8"),
    FieldPanel("Role_Text_8"),
]

