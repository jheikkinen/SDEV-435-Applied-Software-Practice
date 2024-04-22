"""
URL configuration for WarrenBuffy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

# Create URL path for the views.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('registration/', views.registrationForm, name='registration'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('profilesettings', views.profile_settings, name='profilesettings'),
    path('updatecontactinfo', views.update_contact_info, name='updatecontactinfo'),
    path('passwordchange', views.update_user_password, name='passwordchange'),
    path('home/', views.home, name='home'),
    path('budgetManagement', views.budgetManagement, name='budgetManagement'),
    path('budgetManagementEdit', views.update_budget_item, name='budgetManagementEdit'),
    path('PDIT/', views.pdit, name='PDIT'),
    path('portfoliogrowth/', views.portfolioGrowth, name='PortfolioGrowth'),
    path('investmentrisk/', views.investmentRisk, name='InvestmentRisk'),
    path('mortgageCalculator/', views.mortgageCalculator, name='mortgageCalculator'),
]