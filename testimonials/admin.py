from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register
)

from .models import Testimonial

# This whole app is just an example of how I can get user data into the database and display
# it AND make it searchable in the admin area.


@modeladmin_register
class TestimonialAdmin(ModelAdmin):
    """Testimonial admin"""

    model = Testimonial
    menu_label = "Testimonials"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("quote", "attribution")
    search_fields = ("quote", "attribution")

