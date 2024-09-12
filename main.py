#Контейнер расчета
from import
k, T, C, L = symbols('k C T L')
#1 способ
C_ost=30000 #изменил
Am_lst=[]
C_ost_lst=[]
for i in range(8):
  Am = (C-L)/T
  C_ost -= Am.subs({C: 30000, T:8, L:0}) #изменил
  Am_lst.append(round(Am.subs({C: 30000, T:8, L:0}), 2)) #изменил
  C_ost_lst.append(round(C_ost, 2))
print('Am_lst:', Am_lst)
print('C_ost_lst:', C_ost_lst)
