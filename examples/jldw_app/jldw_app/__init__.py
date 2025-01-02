from importlib import metadata

__version__ = metadata.version(__name__)

from nautobot.apps import ConstanceConfigItem, nautobot_database_ready, NautobotAppConfig


class JldwAppConfig(NautobotAppConfig):
    name = "jldw_app"
    verbose_name = "JLDW App"
    author = "Nautobot development team"
    author_email = "nautobot@example.com"
    version = __version__
    description = "This is a test app for JLDW"
    installed_apps = ["nautobot.extras.tests.jldw_app_dependency"]
    middleware = ["jldw_app.middleware.JLDWMiddleware"]
    base_url = "jldw-app"

    home_view_name = "plugins:jldw_app:home"

config = JldwAppConfig
