from django.templatetags.static import static
from django.urls import path
from django.views.generic import RedirectView

from nautobot.apps.urls import NautobotUIViewSetRouter

from jldw_app import views

app_name = "jldw_app"
router = NautobotUIViewSetRouter()


urlpatterns = [
    path("", views.JLDWAppHomeView.as_view(), name="home"),
]
urlpatterns += router.urls
