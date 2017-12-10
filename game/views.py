from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Propositions
from .parameters import group



@csrf_exempt
def index(request):
    """aiguille joueur"""
    # répartition role
    # créer table si j1
    # sinon return id table
    #
    # redirect "/<id game>/<1>" ou "/<id_game>/<2>"

    parties_libres = Propositions.objects.filter(accessible=True)
    if(len(parties_libres) > 0):
        return HttpResponse(str(parties_libres[0].id)+"/2")
    else:
        entry = Propositions(accessible=False,complete=False,proposition=0,answer=None,group=group)
        entry.save()
        _id_ = Propositions.objects.last().id
        return HttpResponse(str(_id_)+"/1")

# si joueur 1 -> écrit avec slider dans index -> redirect "/propose"


@csrf_exempt
def propose(request):
    v = request.POST["proposition"] #récupère le slider
    _id_ = request.POST["id"] #récupère l'ID de la partie

    #
    # Changer attributs table
    #

    """called by first player"""
    #entry = Propositions(accessible=True,complete=False,proposition=v,answer=False,group=group) #modifier proposition J1 dans table

    entry = Propositions.objects.get(id=_id_)
    entry.proposition = v
    entry.save(force_update=True)

    return HttpResponse("ok")


@csrf_exempt
def what_has_been_proposed(request):
    """Called by second player"""

    if 'id' in request.POST:
        _id_ = request.POST['id'] #récupère id
        result = ""
        if((Propositions.objects.get(id=_id_)).accessible):
            result = result+"0"
        else:
            result = result+"1"
        result = result+"/"+str((Propositions.objects.get(id=_id_)).proposition)

        return HttpResponse(result)

    #
    # retourner soit 00/01/10/11 <J1 a proposé><Proposition J1> en str
    #
    else:
        return HttpResponse("Impossible de récupérer la proposition !")


@csrf_exempt
def acceptation(request):
    """choice of the second player"""
    choice = request.POST["choice"]
    _id_ = request.POST['id']
    entry = Propositions.objects.get(id=_id_)
    entry.answer = choice #rentre le choix du J2 dans la table
    entry.save()
    return HttpResponse(choice)


@csrf_exempt
def accepted(request):
    """Called by first player"""
    if 'id' in request.POST:
        _id_ = request.POST['id']
        if Propositions.objects.get(id=_id_).answer is not None:
            request = "1/"+str(Propositions.objects.get(id=_id_).answer) #récupération de l'acceptation ou non du J2 par le J1
        else:
            request = "0/"+str(Propositions.objects.get(id=_id_).answer)  # récupération de l'acceptation ou non du J2 par le J1
        return HttpResponse(request)
    #
    # retourner soit 00/01/10/11 <J2 a répondu><Réponse de J2> en str
    #
    else:
        return HttpResponse("Impossible de récupérer la réponse !")
    
