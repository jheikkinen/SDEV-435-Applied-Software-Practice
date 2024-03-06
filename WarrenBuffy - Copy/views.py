from django.shortcuts import render
from .models import MyModel


# Create your views here. Pulls html document based on the user's selection.
def index(request):
    users =   MyModel.objects.all()
    return render(request, 'index.html', {'users': users})

def home(request):
    return render(request, 'home.html')

def pfm(request):
    return render(request, 'PFM.html')

def pdit(request):
    return render(request, 'PDIT.html')

def portfolioGrowth(request):
    return render(request, 'PortfolioGrowth.html')

def investmentRisk(request):
    return render(request, 'InvestmentRisk.html')

def mortgageCalculator(request):
    return render(request, 'mortgageCalculator.html')
