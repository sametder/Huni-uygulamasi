#10 tane huni oluşturup bu hunilerde kaç tane top var bunlari ve sonunda bütün hunilerin toplamini yazdiran program.

import random

# Huni oluşturma 
def create_funnel():
    funnel = []
    top_sayisi = random.randint(1, 10)
    for _ in range(top_sayisi):
        funnel.append(1)  
    return funnel


funnels = [create_funnel() for _ in range(10)]                      # 10 tane huni oluştur(range(10))


top_sayimi = [sum(funnel) for funnel in funnels]                   #hunilerde kaç top var ?


for i, count in enumerate(top_sayimi):
    print(f"Huni {i + 1}: {count} top")


toplarin_toplami = sum(top_sayimi)
print(f"Toplam top sayisi: {toplarin_toplami}")                              #total top