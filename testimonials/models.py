from django.db import models
from wagtail.snippets.models import register_snippet


# This whole app is just an example of how I can get user data into the database and display
# it AND make it searchable in the admin area.


@register_snippet
class Testimonial(models.Model):
    """A testimonial class"""

    quote = models.TextField(
        max_length=500,
        blank=False,
        null=False,
    )
    attribution = models.CharField(
        max_length=500,
        blank=False,
        null=False,
    )

    def __str__(self):
        """The string representation of this class"""
        return f"{self.quote} by {self.attribution}"

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"
