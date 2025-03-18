from django.urls import path
from . import views

app_name = "store"

urlpatterns = [
    path("", views.index, name="storehome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("productview/", views.prod_view, name="ProductView"),
    path("checkout/", views.check_out, name="Checkout"),
]