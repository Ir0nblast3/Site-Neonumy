from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.models import Page, Orderable
from wagtail.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock
from modelcluster.fields import ParentalKey

class TechnologyItem(Orderable):
    page = ParentalKey(
        'HomePage',
        on_delete=models.CASCADE,
        related_name='technologies'
    )

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    text = models.CharField(max_length=255, blank=True)

    panels = [
        FieldPanel('image'),
        FieldPanel('text'),
    ]

class TeamMembers(Orderable):
    page = ParentalKey(
        'HomePage',
        on_delete=models.CASCADE,
        related_name='teammembers'
    )

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    name = models.CharField(max_length=255, blank=True)
    role = models.CharField(max_length=255, blank=True)

    panels = [
        FieldPanel('image'),
        FieldPanel('name'),
        FieldPanel('role'),
    ]

class PrivacyPolicyPage(Page):

    last_update = models.CharField(max_length=100, blank=True)
    text_1 = models.TextField(blank=True)

    subtitle_1 = models.CharField(max_length=255, blank=True)
    subtext_1 = models.TextField(blank=True)

    subtitle_2 = models.CharField(max_length=255, blank=True)
    subtext_2 = models.TextField(blank=True)

    subtitle_3 = models.CharField(max_length=255, blank=True)
    subtext_3 = models.TextField(blank=True)
    
    subtitle_4 = models.CharField(max_length=255, blank=True)
    subtext_4 = models.TextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("last_update"),
        FieldPanel("text_1"),
        FieldPanel("subtitle_1"),
        FieldPanel("subtext_1"),
        FieldPanel("subtitle_2"),
        FieldPanel("subtext_2"),
        FieldPanel("subtitle_3"),
        FieldPanel("subtext_3"),
        FieldPanel("subtitle_4"),
        FieldPanel("subtext_4"),
    ]



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

    aboutus_gallery = StreamField([
        ('image', ImageChooserBlock()),
    ], use_json_field=True, blank=True)

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
    MultiFieldPanel([
        FieldPanel("hero_title"),
        FieldPanel("hero_subtitle"),
        FieldPanel("hero_image"),
        FieldPanel("newrai_image"),

    ], heading="Hero"),

    InlinePanel('technologies', label='Technologies'),

    FieldPanel("About_Us_Text_1"),
    FieldPanel("Aboutus_image"),
    FieldPanel("About_Us_Text_2"),
    FieldPanel("aboutus_gallery"),

    InlinePanel('teammembers', label='Members'),
]

