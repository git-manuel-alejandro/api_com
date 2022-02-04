from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .import models
import json

# Create your views here.

class CompanyView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request , id=0):
        if id > 0:
            companies = list(models.Company.objects.filter(id = id).values())
            compani = companies[0]
            context = {
                    'message':'success',
                    'data' : compani
                }
            return JsonResponse(context)      

        else:
            companies = list(models.Company.objects.values())
            if len(companies)>0:
                context = {
                    'message':'success',
                    'data' : companies
                }
            else:
                context = {
                    'message':'not found'
                }
            return JsonResponse(context)        
    
    def post(self, request):
        jd= json.loads(request.body)
        # print(jd)
        models.Company.objects.create(name=jd['name'], website=jd['website'], foundation=jd['foundation'])
        context = {
            'message': 'success'
        }
        return JsonResponse(context)

    def put(self, request ,id ):
        jd= json.loads(request.body)
        c = list(models.Company.objects.filter(id = id).values())
        if len(c) > 0:
            c = models.Company.objects.get(id= id)
            c.name=jd['name']
            c.website=jd['website']
            c.foundation=jd['foundation']
            c.save()
            context = {
                    'message':'Success'
                }
            return JsonResponse(context)
        else:
            context = {
                    'message':'not fail'
                }
        return JsonResponse(context)

    def delete(self, request ,id):
        compani = models.Company.objects.get(id= id)
        compani.delete()
        context = {
                    'message':'deleted'
                }

        return JsonResponse(context)
