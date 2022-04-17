from django.shortcuts import render
from django.views.generic import ListView

from beneficiaries.models import Donations,PickupStations
from NGO.models import NGOdonations
# Create your views here.
def index(request):

    donations_count=Donations.objects.all().count()
    pickup_stations=PickupStations.objects.all()
    beneficiaries_count=Donations.objects.all().count()
    causes_count=Donations.objects.all().count()+NGOdonations.objects.all().count()
    pickup_stations_count=PickupStations.objects.all().count()
    context = {
        'donations': Donations.objects.all().filter(delivered=False)[:3],
        'ngodonations':NGOdonations.objects.all().filter(delivered=False),
        'donations_count': donations_count,
        'pickup_stations': pickup_stations,
        'beneficiaries_count': beneficiaries_count,
        'causes_count': causes_count,
        'pickup_stations_count': pickup_stations_count,

    }

    return render(request, 'index2.html',context)

class CausesList(ListView):
    template_name = 'causes_list.html'
    model = Donations
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super(CausesList, self).get_context_data(**kwargs)
        context['pickup_stations'] = PickupStations.objects.all()
        context['ngodonations'] = NGOdonations.objects.all().filter(delivered=False)
        context['bendonations']=Donations.objects.all().filter(delivered=False)


        return context





