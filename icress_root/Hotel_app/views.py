from django.shortcuts import render, redirect
from.models import Rooms
from.forms import Room_form


def load_dashboard(request):
    if request.method == 'GET':
        room_form = Room_form()
        room_list = Rooms.objects.all()
        room_dict = {
            'room_form':room_form,
            'room_list':room_list
        }
        return render(request,'Hotel_app/room_load.html',content_type=room_dict)
    elif request.method == 'POST':
        room_form  =Room_form(request.POST)
        if room_form.is_valid():
            room_form.save()
            return redirect('/Hotel/load_room/')
###############################################################################
        # room_form = Room_form(request.POST)
        # if room_form.is_valid():
        #     username = room_form.cleaned_data['username']
        #     room_no = room_form.cleaned_data['room_no']
        #     room_name =room_form.cleaned_data['room_name']
        #     room_image =room_form.cleaned_data['room_image']
        #     start_date =room_form.cleaned_data['start_date']
        #     is_available =room_form.cleaned_data['is_available']
        #     no_of_dats = room_form.cleaned_data['no_of_dats']
        #     room_data = Rooms(username=username,room_name=room_name,room_no=room_no,room_image=room_image,
        #                       start_date=start_date,is_available=is_available,no_of_dats=no_of_dats)
        #     room_data.save()
        #     return redirect('/Hotel/load_room')
##################################################################################################3
            # username = request.POST['username']
            # room_no = request.POST['room_no']
            # room_name =request.POST['room_name']
            # room_image =request.POST['room_image']
            # start_date =request.POST['start_date']
            # is_available =request.POST['is_available']
            # no_of_dats = request.POST['no_of_dats']
            # room_data = Rooms(username=username,room_name=room_name,room_no=room_no,room_image=room_image,
            #                   start_date=start_date,is_available=is_available,no_of_dats=no_of_dats)
            # room_data.save()
            # return redirect('/Hotel/load_room')
def room_update(request,pk):
    if request.method == 'GET':
        room = Rooms.objects.get(id=pk)
        room_form =Room_form(instance=room)
        room_list = Rooms.objects.all()
        room_dict = {
            'room_form':room_form,
            'room_list':room_list
        }
        return render(request,'Hotel_app/room_load.html',content_type=room_dict)
    elif request.method== 'POST':
        room_db = Rooms.objects.get(id=pk)
        room_form = Room_form(request.POST,instance=room_db)
        if room_form.is_valid():
            room_form.save()
            return redirect('/Hotel/load_room/')
def room_delete(request,pk):
    room_db  =Rooms.objects.get(id=pk)
    room_db.delete()
    return redirect('/Hotel/load_room/')
