from django.shortcuts import render, redirect
#from django.http import HttpResponse
# since we want to use class based view, we need to import listview
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView , UpdateView, DeleteView, FormView
from .models import Task, userInfo
from .forms import userInfo
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
# Create your views here.


class loginPage(LoginView):
    template_name = 'first_app/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self) -> str:
        return reverse_lazy('tasks')
    
  
    
   
    
class registerPage(FormView):
    template_name= 'first_app/signup.html'
    form_class= UserCreationForm
    redirect_authenticated_user = True
    success_url  =reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(registerPage, self).form_valid(form)
    

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect ('tasks')
        return super(registerPage, self).get(*args, **kwargs)





class TaskList(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = 'tasks' # by default, the detailview looks for object.list but we can set that to whatever we want e.g 'tasks' in this example
    template_name = 'first_app/tasks.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['color'] = 'red'  // this is what we need to overwrite
        context['tasks'] = context['tasks'].filter(user = self.request.user)
        context['count'] = context['tasks'].filter(complete = False).count()

        search_input = self.request.GET.get('search') or ''

        if search_input :
            context['tasks'] = context['tasks'].filter(title__icontains= search_input)

        context['search_input'] = search_input

        return context

class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name = 'task'  # by default, the detailview looks for object but we can set that to whatever we want e.g 'task' in this example
    template_name = 'first_app/taskdetail.html'
       
class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task    #by default the createView works with the modelForm
    fields =['title', 'description', 'complete']
    success_url  = reverse_lazy('tasks')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)
        
    #template_name ='first_app/createTask.html'  # by default, this looks for a template with prefix of the referenced model_form.html

    #form_class = Our Model Form     // we can create our own form and appy using this command instead of using the default form.

class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    fields =['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')
    #template_name = 'first_app/createTask.html'


class DeleteTask(LoginRequiredMixin,DeleteView):
    model= Task
    context_object_name= 'task'
    success_url = reverse_lazy('tasks') 
    template_name= 'first_app/deleteTask.html'  #by default, this deleteView looks for modelprefix_confirm_delete.html

