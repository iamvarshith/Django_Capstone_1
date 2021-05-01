from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import HttpResponse
from .models import Gym


# Create your views here.
class CreateView(View):
    template_name = 'gym/index.html'
    k = 'testing'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        name = request.POST['name']
        age = request.POST['age']
        slot = request.POST['slot']
        weight = request.POST['weight']
        cardio = request.POST['cardio']
        image = request.FILES['image']
        newgym = Gym(
            name=name,
            age=age,
            slot=slot,
            weight=weight,
            cardio=cardio,
            image=image
        )
        newgym.save()
        return render(request, self.template_name)


class ReadView(View):
    template_name = 'gym/read.html'

    def get(self, request):
        contex = {'gym_members': Gym.objects.all()}
        return render(request, self.template_name, context=contex)


class UpdateView(TemplateView):
    template_name = 'gym/update.html'


class DeleteView(TemplateView):
    template_name = 'gym/delete.html'
