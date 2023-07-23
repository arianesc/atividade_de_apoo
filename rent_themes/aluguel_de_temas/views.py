from django.shortcuts import redirect, render
from .models import *
from .DAOs import *
from.BusinessObject import BusinessObject
def index(request):
    return render(request, 'index.html')

class ClientViews:
    def listClient(request):
        context = {'clients_list': ClienteDAO.listaClientes()}
        return render(request, 'client/listClient.html', context)

    def formClient(request):
        return render(request, 'client/formClient.html')

    def saveClient(request):
        print(request.POST)
        ClienteDAO.salvaCliente(request.POST)
        return redirect('/listClient')

    def deleteClient(request, id):
        ClienteDAO.deletaCliente(id)

        return redirect('/listClient')

    def detailClient(request, id):
        client = ClienteDAO.detalheCliente(id)
        return render(request, 'client/formEditClient.html', {'client': client} )

    def updateClient(request, id):
        ClienteDAO.atualizaCliente(request.POST, id)
        return redirect('/listClient')

class ThemeViews:
    def listTheme(request):
        context = {'theme_list': TemaDAO.listaTemas()}
        return render(request, 'theme/listTheme.html', context)

    def formTheme(request):
        list_item = ItemDAO.listaItens()
        return render(request, 'theme/formTheme.html', {'list_item':list_item})

    def saveTheme(request):
        TemaDAO.salvaTema(request.POST)
        return redirect('/listTheme')
    
    def deleteTheme(request, id):
        TemaDAO.deletaTema(id)
        return redirect('/listTheme')

    def detailTheme(request, id):
        theme = TemaDAO.detalheTema(id)
        return render(request, 'theme/formEditTheme.html', {'theme': theme})

    def updateTheme(request, id):
        TemaDAO.atualizaTema(request.POST, id)
        return redirect('/listTheme')

class ItemViews:
    def listItem(request):
        context = {'item_list': ItemDAO.listaItens()}
        return render(request, 'item/listItem.html', context)

    def formItem(request):
        return render(request, 'item/formItem.html')

    def saveItem(request):
        ItemDAO.salvaItem(request.POST)
        return redirect('/listItem')

    def deleteItem(request, id):
        ItemDAO.deletaItem(id)
        return redirect('/listItem')
    
    def detailItem(request, id):
        item = ItemDAO.detalheItem(id)
        return render(request, 'item/formEditItem.html', {'item': item} )

    def updateItem(request, id):
        ItemDAO.atualizaItem(request.POST, id)
        return redirect('/listItem')

class RentViews:
    
    def listRent(request):
        context = {'rent_list': RentDAO.listaAlugueis()}
        return render(request, 'rent/listRent.html', context) 
    
    def formRent(request):
        client_list = ClienteDAO.listaClientes()
        theme_list = TemaDAO.listaTemas()
        context = {'client_list':client_list, 'theme_list': theme_list}
        return render(request, 'rent/formRent.html', context)
    
    def saveRent(request):
        data = request.POST
        discount = BusinessObject.discountCalc(data['date'])

        RentDAO.saveRent(data['street'], data['number'], data['complement'],
                                data['district'], data['city'], data['state'], data['cep'],
                                data['date'], data['start_hours'], data['end_hours'],
                                data['select_client'], data['select_theme'], discount)
        return redirect('/listRent')

    def deleteRent(request, id):
        RentDAO.deletaAluguel(id)
        return redirect('/listRent')
    
    def detailRent(request, id):
        rent = RentDAO.detalheAluguel(id)
        return render(request, 'rent/formEditRent.html', {'rent': rent})
    
    def updateRent(request, id):
        discount = BusinessObject.discountCalc(request.POST['date'])
        RentDAO.atualizaAluguel(request.POST, id, discount)
        return redirect('/listRent')