WHILE_START_1:                          < B1
t0 := i < n
t1 := j < m
ifnot t0 && t1 goto WHILE_END_1
t2 := a[i]                              < B2
t3 := b[j]
ifnot t2 < t3 goto IF_ELSE_1
t4 := a[i]                              < B3
c[k] := t4
i := i + 1
goto IF_END_1
IF_ELSE_1:                              < B4
t5 := b[j]
c[k] := t5
j := j + 1
IF_END_1:                               < B5
k := k + 1
goto WHILE_START_1
WHILE_END_1:                            < B6
WHILE_START_2:                          
ifnot i < n goto WHILE_END_2            
t6 := a[i]                              < B7
c[k] := t6
i := i+1
k := k+1
goto WHILE_START_2
WHILE_END_2:                            < B8
WHILE_START_3:
ifnot j < m goto WHILE_END_3
t7 := b[j]                              < B9
c[k] := t7
j := j+1
k := k+1
goto WHILE_START_3
WHILE_END_3:                            < B10
exit

======================================
== Bloques
======================================
B1:
    WHILE_START_1:
    t0 := i < n
    t1 := j < m
    ifnot t0 && t1 goto WHILE_END_1

B2:
    t2 := a[i]
    t3 := b[j]
    ifnot t2 < t3 goto IF_ELSE_1

B3:
    t4 := a[i]                              
    c[k] := t4
    i := i + 1
    goto IF_END_1

B4:
    IF_ELSE_1
    t5 := b[j]
    c[k] := t5
    j := j + 1

B5:
    IF_END_1:
    k := k + 1
    goto WHILE_START_1
B6:
    WHILE_END_1:
    WHILE_START_2:
    ifnot i < n goto WHILE_END_2
B7:
    t6 := a[i]
    c[k] := t6
    i := i+1
    k := k+1
    goto WHILE_START_2      
B8:
    WHILE_END_2:
    WHILE_START_3:
    ifnot j < m goto WHILE_END_3
B9:
    t7 := b[j]                              
    c[k] := t7
    j := j+1
    k := k+1
    goto WHILE_START_3
B10:
    WHILE_END_3:                            < B10
    exit

======================================
== Aristas:
======================================

B1 -> B6
B1 -> B2
B2 -> B4
B2 -> B3
B3 -> B5
B4 -> B5
B5 -> B1
B6 -> B8
B6 -> B7
B7 -> B6
B8 -> B10
B8 -> B9
B9 -> B8