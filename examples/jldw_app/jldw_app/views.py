"""Views for example_app_with_view_override."""

from django.shortcuts import render
from django.conf import settings
from django.core.paginator import Paginator
from jldw_app.api_call import make_api_call

from nautobot.apps.views import GenericView
from nautobot.apps import views


class JLDWAppHomeView(views.GenericView):
    def get(self, request):
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Token {settings.NAUTOBOT_API_TOKEN}"
        }

        # Get search parameters from query parameters
        position = request.GET.get('position', '').strip()
        name = request.GET.get('name', '').strip()

        # Build params dictionary with non-empty parameters
        params = {
            'limit': 250  # Get maximum results per API call
        }

        if name:
            params['name__ic'] = name

        # Handle position search
        if position:
            if position.lower() == 'none':
                params['position__isnull'] = True
            else:
                try:
                    int(position)
                    params['position'] = position
                except ValueError:
                    params['position__ic'] = position

        # Make the initial API call
        result = make_api_call(settings.NAUTOBOT_API_URL, params=params, headers=headers, verify=False)
        devices = []
        if result:
            devices.extend(result.get('results', []))
            # Keep fetching next page while it exists
            next_url = result.get('next')
            while next_url:
                result = make_api_call(next_url, headers=headers, verify=False)
                if result:
                    devices.extend(result.get('results', []))
                    next_url = result.get('next')
                else:
                    break

        # Set up pagination
        page_number = request.GET.get('page', 1)
        paginator = Paginator(devices, 25)  # Show 25 devices per page
        page_obj = paginator.get_page(page_number)
        context = {
            'page_obj': page_obj,
            'total_devices': len(devices),
        }
        return render(request, "jldw_app/home.html", context)




