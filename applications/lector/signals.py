def update_libro_stock(sender, instance, **kwargs):
    # actualizamos el stok si se elimina un prestamo
    instance.libro.stock = instance.libro.stock + 1
    instance.libro.save()