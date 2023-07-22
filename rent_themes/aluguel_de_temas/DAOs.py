from .models import *


class ClienteDAO:

    def listaClientes():
        lista_clientes = Client.objects.all()
        return lista_clientes

    def salvaCliente(dados):
        c = Client(name=dados['name'], cpf=dados['cpf'])
        c.save()

        if dados['ddd1'] != '':
            t1 = Phone(ddd=dados['ddd1'], number=dados['phone1'], client=c)
            t1.save()

        if dados['ddd2'] != '':
            t2 = Phone(ddd=dados['ddd2'], number=dados['phone2'], client=c)
            t2.save()

    def deletaCliente(id):
        c = Client.objects.get(pk=id)
        c.delete()

    def detalheCliente(id):
        return Client.objects.get(pk=id)

    def atualizaCliente(dados, id):
        c = Client.objects.get(pk=id)
        c.name = dados['name']
        c.cpf = dados['cpf']
        c.save()

        if dados['ddd1'] != '' and dados['phone1'] != '':
            if c.phones.first():
                t1 = c.phones.first()
                t1.ddd = dados['ddd1']
                t1.number = dados['phone1']
                t1.save()
            else:
                t1 = Phone(ddd=dados['ddd1'], number=dados['phone1'], client=c)
                t1.save()

        if dados['ddd2'] != '' and dados['phone2'] != '':
            if c.phones.last() and c.phones.count() > 1:
                t2 = c.phones.last()
                t2.ddd = dados['ddd2']
                t2.number = dados['phone2']
                t2.save()
            else:
                t2 = Phone(ddd=dados['ddd2'], number=dados['phone2'], client=c)
                t2.save()


class TemaDAO:
    def listaTemas():
        lista_temas = Theme.objects.all()
        return lista_temas

    def salvaTema(dados):
        t = Theme(name=dados['name'], color=dados['color'], price=dados['price'])
        t.save()

        minha_lista = dados.getlist('item')
        for i in minha_lista:
            item = Item.objects.get(id=i)
            t.itens.add(item)
        t.save()

    def detalheTema(id):
        return Theme.objects.get(pk=id)

    def deletaTema(id):
        t = Theme.objects.get(pk=id)
        t.delete()

    def atualizaTema(dados, id):
        t = Theme.objects.get(pk=id)
        t.name = dados['name']
        t.color = dados['color']
        t.price = dados['price']
        t.save()


class ItemDAO:  # ENTIDADE IMPORTANTE P/ ATIVIDADE

    def listaItens():
        lista_itens = Item.objects.all()
        return lista_itens

    def salvaItem(dados):
        i = Item(name=dados['name'], description=dados['description'])
        i.save()

    def deletaItem(id):
        i = Item.objects.get(pk=id)
        i.delete()

    def detalheItem(id):
        return Item.objects.get(pk=id)

    def atualizaItem(dados, id):
        i = Item.objects.get(pk=id)
        i.name = dados['name']
        i.description = dados['description']
        i.save()


class RentDAO:
    def listaAlugueis():
        lista_alugueis = Rent.objects.all()
        return lista_alugueis

    def saveRent(street, number, complement, district, city, state, cep, date, start_hours, end_hours, select_client, select_theme):
        e = Address(street=street, number=number, complement=complement,
                     district=district, city=city, state=state, cep=cep)
        e.save()

        a = Rent(date=date, start_hours=start_hours, end_hours=end_hours,
                    client_id=select_client, theme_id=select_theme, address=e)
        a.save()

    def deletaAluguel(id):
        a = Rent.objects.get(pk=id)
        a.delete()

    def detalheAluguel(id):
        return Rent.objects.get(pk=id)

    def atualizaAluguel(dados, id):
        a = Rent.objects.get(pk=id)
        a.date = dados['date']
        a.start_hours = dados['start_hours']
        a.end_hours = dados['end_hours']

        end = a.address
        if not end:
            end = Address(street=dados['street'], number=dados['number'], complement=dados['complement'],
                           district=dados['district'], city=dados['city'], state=dados['state'])
            print('novo endereço.')
        else:
            end.street = dados['street']
            end.number = dados['number']
            end.complement = dados['complement']
            end.district = dados['district']
            end.city = dados['city']
            end.state = dados['state']
            print('endereço atualizado.')
        end.save()
        a.address = end
        a.save()