# Generated by Django 3.2.16 on 2022-10-22 13:58

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_homepage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('Title', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Text to display', required=True))])), ('cards', wagtail.core.blocks.StructBlock([('cards', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(help_text='Bold title text for this card. Max length of 100 characters.', max_length=100)), ('text', wagtail.core.blocks.TextBlock(help_text='Optional text for this card. Max length is 255 characters', max_length=225, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='image will be automatically cropped by 570px by 370px', required=False))])))]))], blank=True, null=True),
        ),
    ]
