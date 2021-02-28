from django.shortcuts import render
from django.http import HttpResponse
import joblib
import pandas as pd


reloadModel = joblib.load('model.pkl')

# Create your views here.


def index(request):
    context = {'a':"Tata Consultancy Services"}
    return render(request,'index.html',context)
    #return HttpResponse({'a':1}) 

def Predict_stock(request):
    if request.method == 'POST':
        temp={}
        temp['Open']=request.POST.get('Open')
        temp['High']=request.POST.get('High')
        temp['Low']=request.POST.get('Low')
    
    test_data = pd.DataFrame({"x":temp}).transpose()

    Closeprice = round(reloadModel.predict(test_data)[0],2)
    context = {'Closeprice': Closeprice }
    return render(request ,'index.html', context)