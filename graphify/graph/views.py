from collections import OrderedDict
from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render
from .forms import GraphifyForm
import json
import string

# Create your views here.
class HomeView(View):
	form_class = GraphifyForm
	template_name = "home.html"

	def get(self, request, *args, **kwargs):
		form = self.form_class(None)
		context ={
			'form':form,
			'labels': None,
			'data': None
		}
		return render(request, self.template_name, context)

	def post(self, request):
		form = self.form_class(request.POST, request.FILES or None)
		error = None

		if form.is_valid():
			text_file = form.cleaned_data['file_input']
			display_num = int(form.cleaned_data['display_num'])
			word_count = {}

			# chck if this file is a text file
			if '.txt' in str(text_file)[-4:]:
				try:
					text_file_data = form.cleaned_data['file_input'].read().decode('utf-8')
					translator = text_file_data.maketrans('', '', string.punctuation)
					text_file_data = text_file_data.translate(translator).lower()

					for word in text_file_data.split():
						print(word)
						if word in word_count:
							word_count[word] += 1
						else:
							word_count[word] = 1

				except UnicodeDecodeError as u:
					error = 'The file you tried to parse has encountered \
					a unicode decoding error. Please fix the file and \
					resubmit.'
				except:
					error = 'An unknown error occured.'

			else:
				error = 'Please enter a text file please'

			# make sure the size of the list matches the
			# total number of bar you want to return
			# also put data in the right order 
			labels = []
			data = []
			count = len(word_count)
			word_count = OrderedDict(sorted(word_count.items(), key=lambda t: t[1]))
			word_count = list(word_count.items())
			word_count.reverse()

			if display_num > count:
				display_num = count

			for i in word_count[:display_num]:
			    data.append(str(i[0]))
			    labels.append(str(i[1]))

		context ={
			'form':form,
			'error': error,
			'labels': json.dumps(labels),
			'data': json.dumps(data)
		}
		return render(request, self.template_name, context)
