from wagtail.core import blocks

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



