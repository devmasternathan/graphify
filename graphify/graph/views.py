from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render
from .forms import GraphifyForm
# Create your views here.
class HomeView(View):
	form_class = GraphifyForm
	template_name = "home.html"

	def get(self, request, *args, **kwargs):
		form = self.form_class(None)
		context ={
			'form':form
		}
		return render(request, self.template_name, context)

	def post(self, request, *args, **kwargs):
		form = self.form_class(None)
		context ={
			'form':form
		}
		return render(request, self.template_name, context)
