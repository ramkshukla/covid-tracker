from django.shortcuts import render
from track.models import APIdata
from . import api_test


def search(request):
        api = APIdata.objects.all()
        api.delete()
        # newly tracked data
        country_val = api_test.country_list
        last_update_val = api_test.last_update_list
        cases_val = api_test.cases_list
        deaths_val = api_test.deaths_list
        recovered_val = api_test.recovered_list
        for i in range(api_test.i):
                value = APIdata(
                        country=country_val[i],
                        last_update=last_update_val[i],
                        cases=cases_val[i],
                        deaths=deaths_val[i],
                        recovered=recovered_val[i]
                )
                value.save()
        data = APIdata.objects.all()

        return render(request, 'index.html', {'data': data})