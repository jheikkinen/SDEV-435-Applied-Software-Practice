from django import forms
from .userInfo import budgetItems
from django.core import validators

# Model to allow user to input budget data
class budgetItemsForm(forms.ModelForm):
    # Prevents automated form submissions from bots by creating a hidden field
    botstopper = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])
    
    # Clean input data for database and ensure the values are not negative
    def clean(self):
        cleaned_data = super().clean()
        # For each field value, check to see if the values are not negative
        for field_name in self.Meta.fields:
            field_value = cleaned_data.get(field_name)
            if field_value is not None and field_value < 0:
                self.add_error(field_name, f"{field_name.capitalize()} must be a non-negative value.")

    # Metadata to reference model and database fields. Labels are used for display in the form.
    class Meta:
        model = budgetItems # Work off of budgetItems model
        fields = ['id','income', 'mortgage', 'utility', 'homeMaintenance', 'auto', 'transportation', 'food', 'clothing',
                  'entertainment', 'childCare', 'living', 'insurance', 'medical', 'savings', 'debt']
        # Used to label the fields of the form
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