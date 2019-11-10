from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import  UserForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from plants.models import Waterdata

from .forms import WaterdataCreate
from django.http import HttpResponse

from django.db.models import Q
from django.shortcuts import render, redirect

# Create your views here.

#@csrf_exempt
def login(request):
    print(request.POST, request.GET)
    print(12345)
    form = UserForm()
    #if request.user != None:
    #    return HttpResponseRedirect(reverse('plants:dashboard'))
    if request.POST.get('username') and request.POST.get('password') and request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user:
            print(user)
            auth_login(request, user)
            return HttpResponseRedirect(reverse('plants:dashboard'))
            #return render(request, 'userdashboard.html', context={'username': user.username})
    return render(request, 'index.html', context={'form': form})

def logout_view(request):
    print(741852963)
    logout(request)
    #print (request.user, "request.user")
    return HttpResponseRedirect(reverse('auth_part:login'))

#@csrf_exempt
def create_profile(request):
    error = ""
    if request.method == 'POST':
        print('yoyo')
        userform = UserForm(request.POST)
        #profileform = ProfileForm(request.POST)
        if userform.is_valid() and (len(User.objects.filter(email=request.POST.get('email')))==0):
            print('yoyo2')
            user = User.objects.create_user(**userform.cleaned_data)
            auth_login(request, user)
            return HttpResponseRedirect(reverse('plants:dashboard'))
            #return HttpResponse(status=200)
        else:
            error = "Username or email already in use."
            print(error)

            return render(request, 'register.html', context={'sign_up': True, 'error': error, 'tried': True})
            
    
    userform = UserForm()
    return render(request, 'register.html', context={'sign_up': True, 'error': error})
           
    

def addwaterdata(request):
    error = ""
    if request.method == 'POST':
        print('yoyo')
        district=request.POST.get('district', False)
        zone=request.POST.get('zone', False)
        settlement=request.POST.get('settlement', False)
        block=request.POST.get('block', False)
        cluster=request.POST.get('cluster', False)
        source=request.POST.get('source', False)
        dwdnum=request.POST.get('dwdnum', False)
        ycord=request.POST.get('ycord', False)
        xcord=request.POST.get('xcord', False)
        parameter=request.POST.get('parameter', False)
        freeresid=request.POST.get('freeresid', False)
        turbidity=request.POST.get('turbidity', False)
        ecol=request.POST.get('ecol', False)
        ph=request.POST.get('ph', False)

        print ("PH Data %s" % (ph))
      
        adddata = Waterdata(user=request.user, district=district,zone=zone,settlement=settlement,block=block,cluster=cluster,source=source,dwdnum=dwdnum,ycord=ycord,xcord=xcord,parameter=parameter,freeresid=freeresid,turbidity=turbidity,ecol=ecol,ph=ph)
        adddata.save()

        return render(request, 'addwaterdata.html', context={'sign_up': True, 'error': error, 'tried': True})
            
   
    return render(request, 'addwaterdata.html', context={'sign_up': True, 'error': error})
           





def search_result(request):
    query = request.GET.get('q')
    results =Waterdata.objects.filter(Q(district__icontains=query) | Q(zone__icontains=query) | Q(settlement__icontains=query) | Q(block__icontains=query) | Q(cluster__icontains=query) | Q(borehole__icontains=query))

    return render(request, 'view_waterdata.html', {'results': results})

def search_waterdata(request):
 
    return render(request, 'search_waterdata.html', {})



def all_waterdata(request):
 
    results =Waterdata.objects.all()
    return render(request, 'all_waterdata.html', {'results':results})


def update_result(request, result_id):
    result_id = int(result_id)
    results = None
    try:
        waterdata_sel = Waterdata.objects.get(id = result_id)
    except Waterdata.DoesNotExist:
        return redirect('/all_waterdata/')
    waterdata_form = WaterdataCreate(request.POST or None, instance = waterdata_sel)
    if waterdata_form.is_valid():
       waterdata_form.save()
       results =Waterdata.objects.all()
       return redirect('/all_waterdata/')
       
    return render(request, 'editwaterdata.html', {'waterdata_form':waterdata_form, 'result_id':result_id})





def delete_result(request, result_id):
    waterdata_id = int(result_id)
    try:
        waterdata_sel = Waterdata.objects.get(id = waterdata_id)
    except Waterdata.DoesNotExist:
        return redirect('/all_waterdata/')
    waterdata_sel.delete()
    return redirect('/all_waterdata/')




