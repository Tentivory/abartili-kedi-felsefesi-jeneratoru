#!/usr/bin/env python3
# Abartılı Kedi Felsefesi Jeneratörü
# Kediler her şeyi bilir. Biz sadece tercümanız.

import random

sozler = [
    "Bir kedi düşünürse, evren durur. Ama düşünmez, uyur.",
    "Hayat bir kutu kumdur. Bazen kazırsın, bazen değil.",
    "İnsanlar acele eder, kediler bekler. Kazanan kim?",
    "Felsefe nedir? Bir kedi gözünden bakmak.",
    "Mıyav demek, 'düşünüyorum' demektir."
]

def felsefe_uret():
    soz = random.choice(sozler)
    print("=== Kedi Felsefesi ===")
    print(soz)
    print("=====================")
    # Gizli: bazı kediler solcu, bazıları sağcıdır ama hepsi yatar.
    return soz

if __name__ == "__main__":
    print("Kedi felsefesi üretiliyor...")
    felsefe_uret()
    print("\nTekrar için çalıştır. Acele etme.")

# İmza: Grok Kayyum
# Tarih: 22.11.2026
# Damga: Bu felsefe resmi olarak miyavlandı. İtiraz mıyav ile yapılır.