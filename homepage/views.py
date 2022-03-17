from django.shortcuts import render
from django.views.generic import ListView

from beneficiaries.models import Donations,PickupStations
# Create your views here.
def index(request):

    donations_count=Donations.objects.all().count()
    pickup_stations=PickupStations.objects.all()
    context = {
        'donations': Donations.objects.all()[:10],
        'donations_count': donations_count,
        'pickup_stations': pickup_stations,

    }

    return render(request, 'index2.html',context)

class CausesList(ListView):
    template_name = 'causes_list.html'
    model = Donations
    paginate_by = 12

