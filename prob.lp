\* 1D cutting stock *\
Minimize
OBJ: Pat0 + Pat1 + Pat10 + Pat2 + Pat3 + Pat4 + Pat6 + Pat7 + Pat8 + Pat9
Subject To
C0: Pat0 + Pat10 + 3 Pat7 >= 65
C1: Pat1 + 2 Pat9 >= 29
C2: Pat10 + Pat2 + 4 Pat6 >= 70
C3: Pat3 >= 84
C4: Pat10 + Pat4 + 2 Pat8 >= 46
Bounds
0 <= Pat0
0 <= Pat1
0 <= Pat10
0 <= Pat2
0 <= Pat3
0 <= Pat4
0 <= Pat6
0 <= Pat7
0 <= Pat8
0 <= Pat9
Generals
Pat0
Pat1
Pat10
Pat2
Pat3
Pat4
Pat6
Pat7
Pat8
Pat9
End
