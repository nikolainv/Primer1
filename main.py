#Контейнер расчета
k, T, C, L = symbols('k C T L')
#1 способ
C_ost=30000
Am_lst=[]
C_ost_lst=[]
for i in range(8):
  Am = (C-L)/T
    C_ost_lst.append(round(C_ost, 2))
print('Am_lst:', Am_lst)
print('C_ost_lst:', C_ost_lst)
