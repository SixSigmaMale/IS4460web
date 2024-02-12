from django.views import View
from django.shortcuts import render, redirect
from . import my_functions, my_objects


def title_name(the_name: str):
    return the_name.title()

class HomePageView(View):
    def get(self, request):

        my_name = "ALEX"
        new_name = title_name(my_name)

        the_names = ['MAT', 'JAMES', 'MATT']
        other_names = the_names
        the_names.append('TIM')

        #new_names = [x.title() for x in the_names]
        new_names =my_functions.title_names(the_names)

        car1 = my_objects.car('honda','civic','2000','green','honk honk')
        car2 = my_objects.car('toyota','camry','2001','blue', 'beep beep')
        Motorcycle1 = my_objects.Motorcycle('Honda','bike','1998','blue','beepy')

        the_context = {'hi':'hello world!!!!!!',
                       'name':new_name,
                       'og_name':my_name,
                       'og_names':the_names,
                       'names_list':new_names,
                       'car1':car1,
                       'car2':car2,
                       'motorcycle1':Motorcycle1}
        

     
        return render(request, 'my_app/index.html',the_context)