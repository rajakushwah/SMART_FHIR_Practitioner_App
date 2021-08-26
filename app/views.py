from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
import requests
from json import dumps

pid=''
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    lst=[]
    Resource = 'https://fhir-open.cerner.com/r4/ec2458f2-1e24-41c8-b71b-0e701af7583d'
    url = Resource + "/Patient?given=smith&_count=5"
    newHeaders = {'Content-type': 'application/json', 'Accept': 'application/json'}
    response = requests.get(url, headers=newHeaders, verify=False)
    data = response.json()
    lst = []
    key_to_lookup = 'entry'
    if key_to_lookup in data:
        entry = data['entry']
        for all_data in entry:
            if response.ok:
                l = []
                id = all_data['resource']['id']
                l.append(id)

                try:
                    gender = all_data['resource']['gender']
                except:
                    gender = "No data available"
                l.append(gender)

                try:
                    name = all_data['resource']['name'][0]['given'][0]
                except:
                    name = "No data available"
                l.append(name)
                lst.append(l)
                param = {'param': lst}
    return render(request, 'app/index.html',param)

def about(request):
    return render(request, 'app/about.html')

def info(request):
    if request.method == "POST":
        global pid
        pid = request.POST.get('ID', '')
    return render(request, 'app/info.html',{"Patient_id":pid})

@login_required(login_url='/login')
def patient(request):
    global identifier
    identifier=request.resolver_match.view_name
    return render(request, 'app/auth.html')

@login_required(login_url='/login')
def observation(request):
    global identifier
    identifier = request.resolver_match.view_name
    return render(request, 'app/auth.html')

@login_required(login_url='/login')
def practitioner(request):
    global identifier
    identifier = request.resolver_match.view_name
    return render(request, 'app/auth.html')

@login_required(login_url='/login')
def medication(request):
    global identifier
    identifier = request.resolver_match.view_name
    return render(request, 'app/auth.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

        else:
            # No backend authenticated the credentials
            return render(request, 'app/login.html')

    return render(request, 'app/login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")

@login_required(login_url='/login')
def result(request):
    if identifier =='patient':
        return render(request, 'app/jsonPatient.html', {'patient_id':pid})

    elif identifier == 'observation':
        return render(request, 'app/jsonObservation.html', {'patient_id': pid})

    elif identifier == 'practitioner':
        return render(request, 'app/jsonPractitioner.html', {'patient_id': pid})

    elif identifier == 'medication':
        return render(request, 'app/jsonMedication.html', {'patient_id': pid})

    return render(request,'app/info.html')

def auth(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'app/auth.html')