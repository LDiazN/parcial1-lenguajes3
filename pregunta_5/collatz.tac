=======================================
== TAC
=======================================

steps := 0                          < B1
WHILE_START:                        < B2
ifnot n != 1 goto WHILE_END
t0 := n % 2                         < B3
if t0 == 0 goto IF_ELSE
n := n / 2                          < B4
goto IF_END
IF_ELSE:                            < B5
t1 := n * 3
n := t1 + 1
IF_END:                             < B6
steps := steps + 1
goto WHILE_START
WHILE_END:                          < B7
return steps

=======================================
== Bloques
=======================================

B1:
    steps := 0

B2:
    WHILE_START:
    ifnot n != 1 goto WHILE_END
B3:
    t0 := n % 2
    ifnot t0 == 0 goto IF_ELSE
B4:
    n := n / 2
    goto IF_END

B5:
    IF_ELSE:
    t1 := n * 3
    n := t1 + 1

B6:
    IF_END:
    steps := steps + 1
    goto WHILE_START

B7:
    WHILE_END:
    return steps

=======================================
== Aristas
=======================================
B1 -> B2
B2 -> B7 
B2 -> B3
B3 -> B5
B3 -> B4
B4 -> B6
B5 -> B6
B6 -> B2