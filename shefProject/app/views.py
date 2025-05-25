from django.shortcuts import render, redirect
from django.views import View
from app.forms import RecipeForm
from app.langchainp import ask

class Home(View):

     def get(self, request):
          response=request.session.get('response','')
          form=RecipeForm()
          return render(request, 'app/home.html',
                        
               {'form':form, 'response':response}
                        )
     def post(self, request):
          form=RecipeForm(request.POST)
          if form.is_valid():
               recipe_message=form.cleaned_data['recipe_message']
               response=ask(recipe_message)
               request.session['response']=response
          form=RecipeForm()
          return redirect('/')
