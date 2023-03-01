from .models import Task, userInfo
from django.forms import ModelForm


class TaskForm(ModelForm):
    class Meta:

        model = Task
        fields = ['title','description', 'complete']

class userInfo(ModelForm):
    class Meta:
        model = userInfo
        fields ='__all__'