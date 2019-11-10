from django import forms
from  plants.models import Waterdata
#DataFlair
class WaterdataCreate(forms.ModelForm):
	class Meta:
	    model = Waterdata
	    fields = '__all__'