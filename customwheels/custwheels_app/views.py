#  i have created this file - GTA
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, logout

from django.contrib.auth.decorators import login_required


# NER 
import spacy
nlp = spacy.load("en_core_web_sm")# Load the spaCy model with NER component

import os

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import re
# import nltk
# from nltk.stem import PorterStemmer


# from django.http import HttpResponse
# from .models import Product, Contact
# import random

chatList = []

tempMaterial = ""
tempColor = ""
tempMaterialType = ""

# Create your views here.
def index(request):
    # return HttpResponse('Teamzeffort    |      business Page')
    global chatList
    chatList = []
    return render(request,'custwheels_app/welcome.html')

def select_model(request):
    global chatList
    chatList = []
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

only_material = [
    "It looks like you've chosen the material for the body. Would you like to explore different material types or change the color?",

    "Great choice on the material for the body! Are you interested in checking out other material options or perhaps adjusting the color?",

    "You've selected a material for the body. Would you like to see more material types or experiment with different colors?",

    "The body material is set! Are you interested in exploring other material options or altering the color to see how it complements your design?",

    "You've made a selection for the body material. Do you want to continue with this choice or maybe try a different material type or color?",

    "The material for the body has been chosen. Would you like to review other material types or tweak the color to achieve your desired look?",

    "It seems you've settled on a material for the body. If you're interested, we can explore other material options or adjust the color to match your preferences.",

    "You've chosen a material for the body. Do you want to stick with this choice, or shall we explore different materials and colors to enhance your design?",

    "You've specified the material for the body. Would you like to experiment with different material types or modify the color to achieve the perfect aesthetic?",

    "The body material has been selected. Are you satisfied with your choice, or would you like to explore different materials and colors to fine-tune your design?",
]

@login_required
@csrf_exempt  # To disable CSRF protection (not recommended for production)
def chat_view(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text', '')  # Get the input field value
        print(f"Received input: {input_text}")  # Print the input in the terminal

        if input_text == "-h" or input_text == "help" or input_text == "--help":
            print("Help: Your help message here")
            __Reply = help_info()
        
        else:
            __Reply = filtertext(input_text)
            if __Reply['__part_name_check']:
                tempMaterial = __Reply['Part_Names']

            if __Reply['__color_name_check']:
                tempColor = __Reply['Color_Names']

            

        global chatList
        chatList.append(input_text)
        chatList.append(__Reply)

        # params = {"chatList" : input_text}
        params = {
            "chatList" : chatList,
            # "light_diffuse" : light_diffuse
            }
    return render(request,'custwheels_app/customemodel.html', params)
'''
you have selected material body do you want to change material type or color 

    data = {
        "Input_Text" : input_text,

        "__part_name_check" : checks_value['__part_name'],
        "__color_name_check" : checks_value['__color_name'],
        
        "Part_Names" : parts_found,
        "Color_Names" : colors_found,

        "color_value" : color_value,
    }
'''

# ---------------------------------------------------------------------------
# Custom Funtions
# ---------------------------------------------------------------------------

def help_info():
    value = """
        Display help information for types of materials and available colors.<br>

        Types of Materials:<br>
        - tire: "__type1", "__type2"<br>
        - tire_color: "black", "white", "gray"<br>
        - bonnet: "__type1"<br>
        - spoiler: "__type1"<br>

        Available Colors:<br>
        "red", "black", "blue", "green", "white",<br>
        "silver", "yellow", "purple", "orange",<br>
        "gray", "pink", "brown", "turquoise",<br> 
        "gold", "maroon", "lavender", "teal", "cyan",<br>
        "indigo", "violet"<br>
    """
    return value

# red, black, blue, green, white, silver, yellow, purple, orange, gray, pink, brown, turquoise, gold, maroon, lavender, teal, cyan, indigo, violet

typesMaterials = ["tire", "bonnet", "spoiler"]

typesMaterials = {
    "tire": ["__type1", "__type2"],
    "tire_color": ["black", "white", "gray"],

    "bonnet": ["__type1"],
    
    "spoiler": ["__type1"],

    # "bonnet": "spoiler"
    }

part_names = ["wheels", "wheel", "tires", "tire", "light", "exhaust","glass", "dashboard", "body", "spoiler", "spoilers", "wing", "lighting", "lights"]

colors = ["red", "black", "blue", "green", "white", "silver", "yellow", "purple", "orange", "gray", "pink", "brown", "turquoise", "gold", "maroon", "lavender", "teal", "cyan", "indigo", "violet"]


def filtertext(input_text):
    # Function to remove stop words from a chat
    def remove_stop_words(chat):
        doc = nlp(chat)
        filtered_words = [token.text for token in doc if not token.is_stop]
        return " ".join(filtered_words)

    # Function to perform lemmatization on a chat
    def lemmatize_chat(chat):
        doc = nlp(chat)
        lemmatized_words = [token.lemma_ for token in doc]
        return " ".join(lemmatized_words)

    # Function to make every word in a chat lowercase
    def make_chat_lowercase(chat):
        return chat.lower()

    # Function to remove symbols from a chat
    def remove_symbols(chat):
        chat_without_symbols = re.sub(r'[,.\'";?@-]', '', chat)
        return chat_without_symbols
    
    def checkActions(processed_text):
        print("checkActions: ", processed_text)
        __part_name = False
        __color_name = False
        for item in part_names:
            print("checks_value: ", item, processed_text)
            if item in processed_text:
                __part_name = True
            
        for item in colors:
            print("checks_value: ", item, processed_text)
            if item in processed_text:
                __color_name = True
            
        retValue = {
            "__color_name" : __color_name,
            "__part_name" : __part_name,
        }
        
        return retValue


    # input_text = "I'm thinking about customizing my car with black Wheels."

    # Apply all text processing steps to the input_text
    processed_text = remove_stop_words(input_text)
    print("remove_stop_words: ", processed_text)

    processed_text = lemmatize_chat(processed_text)
    print("lemmatize_chat: ", processed_text)
    processed_text = make_chat_lowercase(processed_text)
    print("make_chat_lowercase: ", processed_text)
    processed_text = remove_symbols(processed_text)
    print("remove_symbols: ", processed_text)

    checks_value = checkActions(processed_text)
    print("checks_value: ", checks_value)

    # Extract color and part name from the input_text
    colors_found, parts_found = extract_color_and_part_from_text(processed_text, checks_value) 

    if "none" != colors_found:
        color_value = map_color_to_mtl(colors_found)
    else:
        color_value = "none"

    data = {
        "Input_Text" : input_text,

        "__part_name_check" : checks_value['__part_name'],
        "__color_name_check" : checks_value['__color_name'],
        
        "Part_Names" : parts_found,
        "Colors" : colors_found,

        "color_value" : color_value,
    }
    # print(f"Input Text: {input_text} \t\t\t Colors: {colors_found} \t\t\t Part Names: {parts_found}")
    return data



def extract_color_and_part_from_text(input_text, checks_value):

    if checks_value['__part_name']:
        part_matches = re.findall(r'\b(?:' + '|'.join(part_names) + r')\b', input_text, flags=re.IGNORECASE)
        __part_matches = part_matches[0] if part_matches else None

    else:
        __part_matches = 'none'

    if checks_value['__color_name']:
        color_matches = re.findall(r'\b(?:' + '|'.join(colors) + r')\b', input_text, flags=re.IGNORECASE)
        __color_matches = color_matches[0] if color_matches else None

    else:
        __color_matches = 'none'
    
    return __color_matches, __part_matches


def map_color_to_mtl(color_name):
    # Define the list of colors and their corresponding RGB values
    colors = {
        "red": [1.0, 0.0, 0.0, 1.0],
        "black": [0.0, 0.0, 0.0, 1.0],
        "blue": [0.0, 0.0, 1.0, 1.0],
        "green": [0.0, 1.0, 0.0, 1.0],
        "white": [1.0, 1.0, 1.0, 1.0],
        "silver": [0.75, 0.75, 0.75, 1.0],
        "yellow": [1.0, 1.0, 0.0, 1.0],
        "purple": [0.5, 0.0, 0.5, 1.0],
        "orange": [1.0, 0.65, 0.0, 1.0],
        "gray": [0.5, 0.5, 0.5, 1.0],
        "pink": [1.0, 0.75, 0.8, 1.0],
        "brown": [0.65, 0.16, 0.16, 1.0],
        "turquoise": [0.25, 0.88, 0.82, 1.0],
        "gold": [1.0, 0.84, 0.0, 1.0],
        "maroon": [0.5, 0.0, 0.0, 1.0],
        "lavender": [0.71, 0.49, 0.86, 1.0],
        "teal": [0.0, 0.5, 0.5, 1.0],
        "cyan": [0.0, 1.0, 1.0, 1.0],
        "indigo": [0.29, 0.0, 0.51, 1.0],
        "violet": [0.93, 0.51, 0.93, 1.0]
    }

    if color_name in colors:
        color_values = colors[color_name]
        print("mtl - color_name : ", color_name)
        return color_values
    else:
        default = [0.0, 0.0, 0.0, 1.0]
        return default

'''
Material List:

["Mt_Abs_Black_Gloss", "Mt_ABS_Black_Mat", "Mt_AlloyWheels", "Mt_AventadorAtlas", "Mt_Body", "Mt_BrakeCaliper", "Mt_Chrome", "Mt_Glass_Translucent", "Mt_Interior_Black", "Mt_Light_Emissive", "Mt_Metal_Black_Glossy", "Mt_Metal_Brushed", "Mt_Mirror", "Mt_MirrorCover", "Mt_Reflector_BL", "Mt_Reflector_RL", "Mt_Reflector_TL", "Mt_Reflector_RL", "Mt_TurnLights", "Mt_Tyres", "Mt_WindScreens", "skyBox"]

'''

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

