
nguoi = input ("Người (Kéo, Búa, Bao): ")

while ['Kéo', 'Búa', 'Bao']:
    nguoi = input ("Người (Kéo - Búa - Bao) nhập lại:")


import random as r
may = r.choice(['Kéo', 'Búa', 'Bao'] )
print ("Máy:", may)

print ("Kết quả:")

if nguoi == "Kéo":
    if may == "Kéo":
       print("Người hoà máy")
    elif may == "Búa":
        print("Người thua")
    elif may ==  "Bao":
        print("Người thắng")
elif nguoi == "Búa":
    if may == "Kéo":
        print("Người thắng")
    elif may == "Búa":
        print("Người hoà máy")
    elif may == "Bao":
        print("Người thua")
elif nguoi == "Bao":
    if may == "Kéo":
        print("Người thua")
    elif may == "Búa":
        print("Người thắng")
    elif may == "Bao":
        print("Người hoà máy")
