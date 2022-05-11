from django.shortcuts import render

def buku(request):
    judul = ["Belajar Django","Belajar Phyton", "Belajar Java"] 
    penulis = "Niken Setiawati"

    konteks = {
        'title': judul,
        'penulis': penulis,
    }
    return render(request, 'buku.html', konteks)

def penerbit(request):
    return render(request, 'penerbit.html')   
