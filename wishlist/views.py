from django.shortcuts import render
from wishlist.models import BarangWishlist # from lab01 docs

# Create your views here.
def show_wishlist(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    context = {
        'list_barang': data_barang_wishlist,
        'nama': 'James Smith'
    }
    return render(request, "wishlist.html", context)
