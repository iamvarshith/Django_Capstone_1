from django.shortcuts import render, redirect
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
        context = {'gym_members': Gym.objects.all()}
        return render(request, self.template_name, context=context)


class UpdateView(View):
    template_name = 'gym/update.html'

    def get(self, request,pk):
        context = {'gym_members': Gym.objects.get(pk=pk)}
        return render(request, self.template_name, context=context)

    def post(self, request,pk):
        name = request.POST['name']
        age = request.POST['age']
        slot = request.POST['slot']
        weight = request.POST['weight']
        cardio = request.POST['cardio']
        image = request.FILES['image']
        update_item = Gym.objects.get(pk=pk)
        update_item.name=name
        update_item.age=age
        update_item.slot=slot
        update_item.weight=weight
        update_item.cardio = cardio
        update_item.image = image
        update_item.save()
        return redirect('read')


class DeleteView(View):
    template_name = 'gym/delete.html'

    def get(self, request, pk=None):
        if pk is None:
            context = {'gym_members': Gym.objects.all()}
            return render(request, self.template_name, context=context)
        else:
            delete_item = Gym.objects.get(pk=pk)
            delete_item.delete()
            return redirect('delete')
