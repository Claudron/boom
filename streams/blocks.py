from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

# this file is like a models.py file just with a different name


class TitleBlock(blocks.StructBlock):
    text = blocks.CharBlock(
        required=True,
        help_text='Text to display',
    )

    class Meta:
        template = "streams/title_blocks.html"
        icon = "edit"
        label = "Title"
        help_text = "Centered text to display on the page"


class Link(blocks.StructBlock):

    link_text = blocks.CharBlock(max_length=50,
                                 default='more details',
                                 )
    internal_page = blocks.PageChooserBlock(required=False,
                                            )
    external_link = blocks.URLBlock(required=False,
                                    )


class Card(blocks.StructBlock):

    title = blocks.CharBlock(max_length=100,
                             help_text="Bold title text for this card. Max length of 100 characters.",
                             )
    text = blocks.TextBlock(max_length=225,
                            required=False,
                            help_text="Optional text for this card. Max length is 255 characters",
                            )
    image = ImageChooserBlock(required=False,
                              help_text="image will be automatically cropped by 570px by 370px",
                              )
    link = Link(help_text="Enter a link or select a page",
                )



class CardsBlock(blocks.StructBlock):

    cards = blocks.ListBlock(
        Card()
    )

    class Meta:
        template = "streams/cards_block.html"
        image = "image"
        label = "Standard Cards"



