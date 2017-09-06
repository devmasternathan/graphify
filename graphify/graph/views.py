from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render
from .forms import GraphifyForm
import string

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

	def post(self, request):
		form = self.form_class(request.POST, request.FILES or None)
		error = None

		if form.is_valid():
			text_file = form.cleaned_data['file_input']
			display_num = form.cleaned_data['display_num']
			word_count = {}

			# check if the fle is a text fil
			if '.txt' in str(text_file)[-4:]:
				print('text file')
				try:

					text_file_data = form.cleaned_data['file_input'].read().decode('utf-8')
					# remove all punctuations and make all words lower case
					translator = text_file_data.maketrans('', '', string.punctuation)
					text_file_data = text_file_data.translate(translator).lower()

					for word in text_file_data.split():
						if word in word_count:
							word_count[word] += 1
						else:
							word_count[word] = 1
				except UnicodeDecodeError as u:
					error = 'decoding error'
				except:
					error = 'an error  occured'

			else:
				error = 'Please enter a text file please'

			print(display_num)
			print(text_file)
			print(word_count)

		context ={
			'form':form,
			'error': error
		}
		return render(request, self.template_name, context)
