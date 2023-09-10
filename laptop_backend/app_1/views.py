from django.shortcuts import render
from datetime import datetime
from app_1.models import Input_data
from pickle import load
from pandas import DataFrame

with open('ml_models/laptop_model.pkl', 'rb') as file_obj:
    ML_model = load(file_obj)

# Create your views here.
def home(request):
    return render(request, 'home.html')

def predictor(request):
    return render(request, 'predictor.html')

def result(request):
    if request.method == 'POST':
        Company = request.POST.get('Company')
        TypeName = request.POST.get('TypeName')
        RAM = request.POST.get('RAM')
        OpSys = request.POST.get('OpSys')
        CPU_Brand = request.POST.get('CPU_Brand')
        CPU_Frequency = request.POST.get('CPU_Frequency')
        GPU = request.POST.get('GPU')
        Memory_SSD = request.POST.get('Memory_SSD')

        # to_predict = DataFrame([[Company, TypeName, RAM, OpSys, CPU_Brand, CPU_Frequency, GPU, Memory_SSD]])
        to_predict = DataFrame.from_dict({
            'Company' : [Company],
            'TypeName' : [TypeName],
            'RAM' : [RAM],
            'OpSys' : [OpSys],
            'CPU_Brand' : [CPU_Brand],
            'CPU_Frequency' : [CPU_Frequency],
            'GPU' : [GPU],
            'Memory_SSD' : [Memory_SSD]
        })

        predicted_price = ML_model.predict(to_predict) [0]
        predicted_price = round(predicted_price, 2)

        data = Input_data(Company=Company, TypeName=TypeName, RAM=RAM, OpSys=OpSys, CPU_Brand=CPU_Brand, CPU_Frequency=CPU_Frequency, GPU=GPU, Memory_SSD=Memory_SSD, Price=predicted_price, date_time=datetime.now())
        data.save()
    return render(request, 'result.html', {'predicted_price' : predicted_price})

def services(request):
    return render(request, 'services.html')

def about(request):
    return render(request, 'about.html')

def contact_email(request):
    return render(request, 'contact_email.html')

def contact_whatsapp(request):
    return render(request, 'contact_whatsapp.html')

def contact_other_options(request):
    return render(request, 'contact_other_options.html')

# Other functions
# def predict_price(to_predict):
#     file_obj = open('concrete_model.pkl', 'rb')
#     ML_model = load(file_obj)
#     file_obj.close()

#     predicted_price = ML_model.predict(to_predict)

#     return predicted_price