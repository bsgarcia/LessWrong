from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Propositions
import random

@csrf_exempt
def index(request):
    """aiguille joueur"""
    return HttpResponse(str(random.choice(["first", "second"])))


@csrf_exempt
def propose(request):
    v = request.POST["proposition"]
    """called by first player"""
    entry = Propositions(accessible=True,complete=False,proposition=v,answer=False)
    entry.save()
    return HttpResponse(str(random.choice(["first", "second"])))

##@csrf_exempt
##def create(request):
##    if 'P' in request.POST:
##        p = request.POST['P']
##        return HttpResponse(p)
##    else:
##        return HttpResponse("Impossible de récupérer la proposition !")

@csrf_exempt
def what_has_been_proposed(request):
    """Called by second player"""
    if 'id' in request.POST:
        _id_ = request.POST['id']
        request = Propositions.objects.get(id=_id_).proposition
        return HttpResponse(request)
    else:
        return HttpResponse("Impossible de récupérer la proposition !")

@csrf_exempt
def acceptation(request):
    """choice of the second player"""
    choice = request.POST["choix"]
    _id_ = request.POST['ID']
    entry = Propositions.objects.get(id=_id_)
    entry.answer = choice
    entry.save()
    return HttpResponse(choix)
    
@csrf_exempt
def accepted(request):
    """Called by first player"""
    if 'ID' in request.POST:
        _id_ = request.POST['ID']
        request = Propositions.objects.get(id=_id_).answer
        return HttpResponse(request)
    else:
        return HttpResponse("Impossible de récupérer la réponse !")
    
