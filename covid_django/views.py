from django.shortcuts import render
import requests
def corona(request):
    if request.method=="POST":
        city_name=request.POST.get("city").strip()
        url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"
        headers = {
            'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
            'x-rapidapi-key': "21cf14a192msh204f296e47aa397p15bd5djsn552202dd0a7d"
            }

        response = requests.request("GET", url, headers=headers).json()
        count = 0
        data = {}
        for each in response['state_wise']:
            if int(response['state_wise'][each]['active']) :
                for city in response['state_wise'][each]['district']:
                    if city.lower() == city_name.lower():
                        data = response['state_wise'][each]['district'][city]
                        count = 1
        context={"data":data, "count": count, "city_name": city_name.title()}
        return render(request,"covid_result.html",context)
    else:
        return render(request,"city_form.html")