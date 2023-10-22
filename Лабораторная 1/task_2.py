# TODO Найдите количество книг, которое можно разместить на дискете
disk_mb = 1.44
pages = 100
lines = 50
symbols = 25
volume_for_symbol_b = 4
volume_for_book_mb = pages * lines * symbols *volume_for_symbol_b/1024**2
number_of_books = int(disk_mb // volume_for_book_mb)
print("Количество книг, помещающихся на дискету:", number_of_books)
