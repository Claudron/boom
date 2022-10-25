from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key
from django.db import models

from wagtail.admin.edit_handlers import (
    FieldPanel, PageChooserPanel, StreamFieldPanel
)
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.blocks import SnippetChooserBlock

from streams import blocks


# Pricing table default settings
NEW_TABLE_OPTIONS = {
    'minSpareRows': 0,
    'startRows': 4,
    'startCols': 4,
    'colHeaders': False,
    'rowHeaders': True,
    'contextMenu': [
        'row_above',
        'row_below',
        '---------',
        'col_left',
        'col_right',
        '---------',
        'remove_row',
        'remove_col',
        '---------',
        'undo',
        'redo'
    ],
    'editor': 'text',
    'stretchH': 'all',
    'renderer': 'text',
    'autoColumnSize': False,
}


class HomePage(Page):
    parent_page_types = ["wagtailcore.Page"]
    subpage_types = ["flex.FlexPage", "courses.CourseListPage"]
    max_count = 1
    lead_text = models.CharField(
        max_length=140,
        blank=True,
        help_text='Subheading text under the banner title',
    )
    button = models.ForeignKey(
        'wagtailcore.page',
        blank=True,
        null=True,
        related_name='+',
        help_text='select an optional page to link to',
        on_delete=models.SET_NULL,
    )
    button_text = models.CharField(
        max_length=50,
        default='read more',
        blank=True,
        help_text='Button text',
    )
    banner_background_image = models.ForeignKey(
        'wagtailimages.image',
        blank=False,
        null=True,
        related_name='+',
        help_text='Teh banner background image',
        on_delete=models.SET_NULL,
    )
    # Stream fields are stored in Jason format in the database
    body = StreamField([
        ("Title", blocks.TitleBlock()),
        ("cards", blocks.CardsBlock()),
        ("image_and_text", blocks.ImageAndTextBlock()),
        ("cta", blocks.CallToActionBlock()),
        ("testimonial", SnippetChooserBlock(
            target_model='testimonials.Testimonial',
            template="streams/testimonial_block.html",
        )),
        ("pricing_table", blocks.PricingTableBlock(table_options=NEW_TABLE_OPTIONS)),
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("lead_text"),
        PageChooserPanel("button"),
        FieldPanel("button_text"),
        ImageChooserPanel("banner_background_image"),
        StreamFieldPanel("body"),
    ]


