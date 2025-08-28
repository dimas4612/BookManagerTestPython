class Book:
    def __init__(self, title: str, author: str, year: int):
        if not title or not title.strip():
            raise ValueError("Judul buku tidak boleh kosong")
        if not author or not author.strip():
            raise ValueError("Penulis tidak boleh kosong")
        if year < 2000 or year > 2100:
            raise ValueError("Tahun hanya bisa diisi dari 2000 sampai 2100")

        self.title = title.strip()
        self.author = author.strip()
        self.year = year
