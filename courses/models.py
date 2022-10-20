from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel

# # Use Wagtail Page classes or models.Model ?
#


class CourseListPage(Page):
    subtitle = models.TextField(
        blank=True,
        max_length=500,
    )

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
    ]


class CoursePage(Page):
    description = models.CharField(
        blank=True,
        max_length=500,
    )
    internal_page = models.ForeignKey(
        'wagtailcore.Page',
        blank=True,
        null=True,
        related_name='+',
        help_text='select an internal wagtail page',
        on_delete=models.SET_NULL,
    )

    external_page = models.URLField(blank=True)

    button_text = models.CharField(blank=True, max_length=50)

    course_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        help_text='This image will be used on the course listing page and will be cropped',
        related_name='+',
    )

    content_panels = Page.content_panels + [
        FieldPanel("description"),
        PageChooserPanel("internal_page"),
        FieldPanel("external_page"),
        FieldPanel("button_text"),
        ImageChooserPanel("course_image"),
    ]
# # The Course is made of Lessons
#     course_content = Lesson
#




# class LearnUnit(Page):
#     course_title = models.CharField(max_length=200)
#     unit_description = RichTextField
#
#
# class Lesson(Page):
#     lesson_title = models.CharField(max_length=200)
#     lesson_description = models.TextField()
# # a Lesson is made of individual LearnUnites
#     lesson_content = LearnUnit
#
#
