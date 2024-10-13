sozluk = {
    "anakart": "bilgisayar parçalarının iletişimini sağlayan ana devre",
    "python": "yorumlanan bir programlama dili",
    "java": "derlenen, obje tabanlı bir programlama dili",
    "ram": "programların üzerinde çalıştığı geçici depolama alanı",
    "optik disk": "verilerin üzerine depolandığı optik depolama aracı",
    "linux": "açık kaynak kodlu işletim sistemi çekirdeği",
    "html": "hyper text markup language"
}

# for elm in sozluk.items():
#     print(elm)

sorgu = input("Hangi terimi soruyorsun?\n")
print(sozluk[sorgu])

