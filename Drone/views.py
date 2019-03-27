from django.shortcuts import render, redirect
from .models import VictimDetails
import requests
from requests.auth import HTTPBasicAuth
from django.core import serializers
from django.http import JsonResponse


def index(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		latitude = request.POST.get('lat')
		longitude = request.POST.get('long')
		phoneno = request.POST.get('phone')
		image = request.FILES.get('image')
		print(name, phoneno)
		details = VictimDetails(name = name, phoneno = phoneno, latitude= latitude, longitude = longitude, image = image)
		details.save()
		return redirect('/home/')

	return render(request, "index.html")

def droneadmin(request):
	return render(request, "admin.html")

def admin_page_data(request):
	dronedetails = VictimDetails.objects.all().order_by('-published')
	data = serializers.serialize('json', dronedetails)
	# url = 'https://app.nanonets.com/api/v2/ImageCategorization/LabelFile/'
	# for drone in dronedetails:
	# 	imagepath = drone.image.path
	# 	print(imagepath)
	# 	data = {'file': open(imagepath, 'rb'), 'modelId': ('', 'deaea15e-1972-4b5d-9645-b514af09b3ca')}
	# 	response = requests.post(url, auth= requests.auth.HTTPBasicAuth('L8pFSWMtPqAXddoDCP1OV34npFqPk2RH', ''), files=data)
	# 	print(response)
	resJson={}
	resJson=[]
	for data in dronedetails:
		name = data.name
		latitude = data.latitude
		longitude = data.longitude
		phoneno = data.phoneno
		image = str('/media/'+str(data.image))
		resJson.append([name,latitude,longitude,phoneno,image])

	return JsonResponse(resJson, safe=False)