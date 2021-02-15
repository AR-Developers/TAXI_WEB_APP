from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
import json
import requests
from .models import VendorAccount

from .forms import RegistrationForm, AccountAuthenticationForm

def register_view(request, *args, **kwargs):
	user = request.user
	if user.is_authenticated: 
		return HttpResponse("You are already authenticated as " + str(user.email))

	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email').lower()
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(email=email, password=raw_password)
			# login(request, account)
			destination = kwargs.get("next")
			if destination:
				return redirect(destination)
			return redirect('login')
		else:
			context['registration_form'] = form

	else:
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'account/register.html', context)

@login_required(login_url='login')
def home(request):
    return render(request, 'dashboard/index.html')

def login_view(request, *args, **kwargs):
    context = {}
    user = request.user
    if user.is_authenticated: 
	    return redirect("home")

    destination = get_redirect_if_exists(request)
    print("destination: " + str(destination))

    if request.POST:
	    form = AccountAuthenticationForm(request.POST)
	    if form.is_valid():
		    email = request.POST['email']
		    password = request.POST['password']
		    user = authenticate(email=email, password=password)

		    if user:
			    login(request, user)
			    if destination:
				    return redirect(destination)
			    return redirect("home")

    else:
	    form = AccountAuthenticationForm()

    context['login_form'] = form

    return render(request, "account/login.html", context)

def get_redirect_if_exists(request):
    redirect = None
    if request.GET:
	    if request.GET.get("next"):
		    redirect = str(request.GET.get("next"))
    return redirect

def logout_view(request):
    logout(request)
    return redirect("home")



def details(request):
    ven = VendorAccount.objects.all()
    context = {
        'ven' :ven
    }
    return render(request, 'dashboard/details.html', context)

def vendor_reg(request):
    if request.method == "POST":
        send_url = "http://api.ipstack.com/check?access_key=f78b7a305665b6a034589df60c5b9ec1"
        geo_req = requests.get(send_url)
        geo_json = json.loads(geo_req.text)
        latitude = geo_json['latitude']
        longitude = geo_json['longitude']
        print(latitude, longitude)
        obj = VendorAccount()
        obj.org_name = request.POST.get('org_name')
        obj.per_name = request.POST.get('per_name')
        obj.org_email = request.POST.get('org_email')
        obj.org_phone = request.POST.get('org_phone')
        obj.add1 = request.POST.get('add1')
        obj.add2 = request.POST.get('add2')
        obj.state = request.POST.get('state')
        obj.city = request.POST.get('city')
        obj.pincode = request.POST.get('pincode')
        obj.lat = latitude
        obj.lon = longitude
        # obj.context = {
        #     'org_name': org_name,
        #     'per_name': per_name,
        #     'org_email': org_email,
        #     'org_phone': org_phone,
        #     'add1': add1,
        #     'add2': add2,
        #     'state': state,
        #     'city': city,
        #     'pincode': pincode,
        # }
        obj.save()
        # print(context)
        return render(request, 'dashboard/vendor_regestration.html')
    else:
        return render(request, 'dashboard/vendor_regestration.html')

def get_latlon(request):
    send_url = "http://api.ipstack.com/check?access_key=f78b7a305665b6a034589df60c5b9ec1"
    geo_req = requests.get(send_url)
    geo_json = json.loads(geo_req.text)
    latitude = geo_json['latitude']
    longitude = geo_json['longitude']
    print(latitude, longitude)
    return HttpResponse("Hello Welcome Home!!!!")