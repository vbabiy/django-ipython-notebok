from django.views.generic.list import ListView

from .models import Poll


class PollListView(ListView):
    model = Poll

    def dispatch(self, request, *args, **kwargs):
        return super(PollListView, self).dispatch(request, *args, **kwargs)