from django.http.response import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from .models import *
import random as rd
# Create your views here.
def home(request):
    context = {"categories": Category.objects.all()}
    if request.GET.get('category'):

        return redirect(f"/quiz/?category={request.GET.get('category')}")

    return render(request,"home.html",context)

def quiz(request):
    #return HttpResponse("Something went wrong")
    context={'category':request.GET.get('category')}
    return render(request,"quiz.html",context)



def get_quiz(request):
    try:
        ques_objs = Question.objects.all()
        data = []
        if request.GET.get('category'):
            ques_objs = ques_objs.filter(category__category_name__icontains=request.GET.get('category'))
        ques_objs = list(ques_objs)
        for ques_obj in ques_objs:
            data.append({
                         "uid":ques_obj.uid,
                         "category":ques_obj.category.category_name,
                         "question":ques_obj.question,
                         "marks":ques_obj.marks,
                         "answers": ques_obj.get_answers(),
                         })
        payload = {'status': True,"data":data}
        return JsonResponse(payload)
    except Exception as e:
        print(e)
        return HttpResponse("Something went wrong")
