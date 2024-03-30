from django import forms
from .userInfo import budgetItems
from django.core import validators

# Model to allow user to input budget data
class budgetItemsForm(forms.ModelForm):
    # Prevents automated form submissions from bots by creating a hidden field
    botstopper = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])
    
    # Clean input data for database
    def clean(self):
        all_clean_data = super().clean()

    # Metadata to reference model and database fields. Labels are used for display in the form.
    class Meta:
        model = budgetItems
        fields = ['id','income', 'mortgage', 'utility', 'homeMaintenance', 'auto', 'transportation', 'food', 'clothing',
                  'entertainment', 'childCare', 'living', 'insurance', 'medical', 'savings', 'debt']
        labels = {
            'id': 'ID',
            'income': 'Income',
            'mortgage': 'Mortgage',
            'utility': 'Utility',
            'homeMaintenance': 'Home Maintenance',
            'auto': 'Auto',
            'transportation': 'Transportation',
            'food': 'Food',
            'clothing': 'Clothing',
            'entertainment': 'Entertainment',
            'childCare': 'Child Care',
            'living': 'Living',
            'insurance': 'Insurance',
            'medical': 'Medical',
            'savings': 'Savings',
            'debt': 'Debt',
        }