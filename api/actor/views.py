from pprint import pprint
from django.shortcuts import render
from .models import Employes, Entreprise
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Count

class EntreprisesManage(APIView):

    def get(self, request):

        return Response(Entreprise.objects.all().values(), status=200)

    def post(self, request):

        data = request.data

        entreprise = Entreprise.objects.create(**data)

        return Response({'message': 'created ' + entreprise.id}, status=201)

class EntrepriseManage(APIView):

    def get(self, request, **kwargs):

        id = kwargs.get('id')
        entreprises = Entreprise.objects.filter(id=id)
        if not entreprises.exists():
            return Response({'message': 'not found'}, status=404)
        return Response(entreprises.values()[0], status=200)

    def put(self, request, **kwargs) :

        id= kwargs.get('id')

        data = request.data

        entreprise = Entreprise.objects.filter(id=id)

        if entreprise.exists():
            entreprise.update(**data)

            return Response({'message': 'created'})
        return Response({'message': 'not found'}, status=404)

    def delete(self, request, **kwargs) :

        id= kwargs.get('id')

        
        entreprise = Entreprise.objects.filter(id=id) 
        if entreprise.exists() : 
            entreprise.delete()
            return Response({'message': 'delete'})
        return Response({'message': 'not found'}, status=404)
class EntreprisesManage(APIView):

    def get(self, request):

        return Response(Entreprise.objects.all().values(), status=200)

    def post(self, request):

        data = request.data

        Entreprise.objects.create(**data)

        return Response({'message': 'created'}, status=201)

class EmployeManage(APIView):

    def get(self, request):

        return Response(Employes.objects.all().values(), status=200)

    def post(self, request):

        data = request.data

        Employes.objects.create(**data)

        return Response({'message': 'created'}, status=201)


class EmployesManage(APIView):

    def get(self, request, **kwargs):

        id = kwargs.get('id')
        employes = Employes.objects.filter(id=id)
        if not employes.exists():
            return Response({'message': 'not found'}, status=404)
        return Response(employes.values()[0], status=200)

    def put(self, request, **kwargs) :

        id= kwargs.get('id')

        data = request.data

        Employes.objects.filter(id=id).update(**data)

        return Response({'message': 'created'})

    def delete(self, request, **kwargs) :

        id= kwargs.get('id')

        Employes.objects.filter(id=id).delete()

        return Response({'message': 'delete'})

class AfficherEmploi(APIView) :

    def get(self, request, **kwargs) :
        entreprise_id = kwargs.get('entreprise_id')
        Employes.objects.filter(entreprise_id=entreprise_id)       
















def add_entreprise(request) :
    b = Entreprise(identreprise='2', nomentreprise='CIC', adressent='Chevilly-larue')
    b.save()
    return HttpResponse(b)

def add_employes(request) :
    b = Employes(idemployes='2', nomemp='Kiyindou', preemp='Pacha', email='ncpy42@vde-technologie', tel='0745462100', identreprise='2')
    b.save()
    return HttpResponse(b)

def sup_entreprise(request) :    
    det = Entreprise.objects.get(nomentreprise='CIC')
    det.delete()
    return HttpResponse(det.delete())

def sup_employes(request) :
    det = Employes.objects.get(nomemp='Kiyindou')
    det.delete()
    return HttpResponse(det.delete())
def opd_employes(request) :
    Employes.objects.filter(idemployes=1).update(identreprise = 1)
    return HttpResponse()
def opd_Entreprise(request) :    
    e = Entreprise.objects.get(nomentreprise='CIC')
    e.adressent='Chevilly'
    e.save()
    return HttpResponse(e)

def affich_entreprise(request) :
#    one_entry = Entry.objects.get(pk=1)
    o = Entreprise.objects.filter(nomentreprise='CIC')
    o.coco()
    
    return HttpResponse(o)

def affich_employes(request) :
    employes = Employes.idemployes.get(idemployes=1)
    context = {'employes': employes}
    return HttpResponse(context)