import requests

response = requests.get('https://covid19-api.org/api/status')
data = response.json()
country_list = []
last_update_list = []
cases_list = []
deaths_list = []
recovered_list = []
i = 0
while True:
    try:
        country = data[i]['country']
        last_update = data[i]['last_update']
        cases = data[i]['cases']
        deaths = data[i]['deaths']
        recovered = data[i]['recovered']
        country_list.append(country)
        last_update_list.append(last_update)
        cases_list.append(cases)
        deaths_list.append(deaths)
        recovered_list.append(recovered)
        i = i+1
    except IndexError:
        break


