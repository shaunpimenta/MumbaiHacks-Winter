#  i have created this file - GTA
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, logout

from django.contrib.auth.decorators import login_required



# from django.http import HttpResponse
# from .models import Product, Contact
# import random

chatList = ["hello"]


# Create your views here.
def index(request):
    # return HttpResponse('Teamzeffort    |      business Page')
    return render(request,'custwheels_app/welcome.html')

def select_model(request):
    return render(request,'custwheels_app/select_model.html')


def customemodel(request):
    return render(request,'custwheels_app/customemodel.html')

'''
def llm_MODEL(input_text):
    #model code...

    

    jsonData = {
        "item" : "spoiler",
        "color": "red", # / #hg34vvh
        "type" : "type_1",
        "chat_response" : "uysefj",
    }
    return jsonData

def test(request):

    return render(request,'custwheels_app/loadobjModel.html')
'''

# def help(request):
#     return render(request,'custwheels_app/help.html')


@csrf_exempt  # To disable CSRF protection (not recommended for production)
def chat_view(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text', '')  # Get the input field value
        print(f"Received input: {input_text}")  # Print the input in the terminal
          
        chatList.append(input_text)
        # params = {"chatList" : input_text}
        params = {
            "chatList" : chatList,
            # "light_diffuse" : light_diffuse
            }
    return render(request,'custwheels_app/customemodel.html', params)


# ------------------------------ Login Controls ------------------------------ 

def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        
        # Check if the username is unique
        if not User.objects.filter(username=username).exists():
            # Create a new user
            user = User.objects.create_user(username=username, password=password, email=email)
            return redirect('user_login')  # Redirect to your login view
        else:
            error_message = 'Username already exists'
    else:
        error_message = None

    return render(request, 'custwheels_app/register.html', {'error_message': error_message})



def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('select_model')  # Redirect to your dashboard view
        else:
            error_message = 'Invalid username or password'
    else:
        error_message = None

    return render(request, 'custwheels_app/login.html', {'error_message': error_message})



def user_logout(request):
    logout(request)
    return redirect('user_login')  # Redirect to your login view

# ------------------------------- Extra ------------------------------- 

# def index(request):
#     products = Product.objects.all()

#     all_prods = []
#     catProds = Product.objects.values('category', 'Product_id')
#     cats = {item['category'] for item in catProds}
#     for cat in cats:
#         prod = Product.objects.filter(category=cat)
#         n = len(products)
#         all_prods.append([prod, n]) 

#     params = {
#         'catproducts' : all_prods,
#         'allproducts' : products,
#               }

#     return render(request,'tze/index.html', params)


# def business(request):
#     # return HttpResponse('Teamzeffort    |      business Page')
#     return render(request,'tze/business.html')

# def about(request):
#     return render(request,'tze/about.html')

# def contact(request):
#     coreMem = Contact.objects.filter(mem_tag="core")
#     teamMem = Contact.objects.filter(mem_tag="team")
#     # print(f"coreMem: {coreMem} \n teamMem: {teamMem}")

#     return render(request, 'tze/contact.html', {'core':coreMem,'team':teamMem })

# def productView(request, myslug):
#     # Fetch the product using the id
#     product = Product.objects.filter(slug=myslug)
#     prodCat = product[0].category
#     # print(prodCat)
#     recproduct = Product.objects.filter(category=prodCat)
#     # print(recproduct)

#     # randomObjects = random.sample(recproduct, 2)
#     randomObjects = random.sample(list(recproduct), 2)


#     return render(request, 'tze/prodView.html', {'product':product[0],'recprod':randomObjects })

