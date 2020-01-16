
%verificar resposta
resposta(0):- nl,nl,nl,nl,nl.
resposta(1):- nl,nl,nl,nl,nl.
resposta(2):- nl,nl,nl,nl,nl.
resposta(3):- nl,nl,nl,nl,nl.
resposta(4):- nl,nl,nl,nl,nl.
	
escolha(1):- depressao().
escolha(2):- ansiedade().
escolha(3):- stress().
% Niveis de depressao 
nivelDepre(X) :- X < 5, write('voce nao tem depressao.').
nivelDepre(X) :- X >= 5, X < 10 , write('Depressao moderada.').
nivelDepre(X) :- X >= 10, X =< 15 , write('Alto nivel de depressao.').
nivelDepre(X) :- X > 15, write('nivel de depressao severo.').

% Niveis de stress
nivelStress(X) :- X < 14, write('voce tem um nivel de stress baixo.').
nivelStress(X) :- X >= 14, X < 27 , write('voce tem um nivel de stress moderado.').
nivelStress(X) :- X >= 27, write('voce tem um nivel de stress alto.').

% Niveis de Ansiedade
nivelAnsiedade(X) :- X < 5, write('voce nao tem ansiedade.').
nivelAnsiedade(X) :- X >= 5, X < 10 , write('ansiedade moderada.').
nivelAnsiedade(X) :- X >= 10, X =< 15 , write('Alto nivel de ansiedade.').
nivelAnsiedade(X) :- X > 15, write('nivel de ansiedade severo.').

menu():-
	writeln('Escolha uma opção de teste:'),
	writeln('1 - Teste de Depressao.'),
	writeln('2 - Teste de Ansiedade.'),
	writeln('3 - Teste de Stress.'),
	read(X), escolha(X). 


op():-
    nl,nl,
	write('1 - Quase todo dia.'),
    nl,
    write('2 - Mais de metade dos dias.'),
	nl,
	write('3 - Alguns dias.'),
	nl,
	write('4 - Nenhuma.'),
	nl,nl,
	write('digite um numero:'),
	nl.

op2():-
	nl,nl,
	write('0 - Nunca.'),
    nl,
    write('1 - Quase nunca.'),
	nl,
	write('2 - As vezes.'),
	nl,
	write('3 - Quase sempre.'),
	nl,
	write('4 - Muito frequentemente.'),
	nl,nl,
	write('digite um numero:'),
	nl.

op3():-
    nl,nl,
	write('1 - Nenhuma.'),
    nl,
    write('2 - Alguns dias.'),
	nl,
	write('3 - Mais que metade dos dias.'),
	nl,
	write('4 - Quase todo dia.'),
	nl,nl,
	write('digite um numero:'),
	nl.

ansiedade():-
	nl,nl,nl,
	writeln('TESTE DE ANSIEDADE: '),
	nl,
	write('Nas ultimas duas semana, com que frequencia voce se sente nervoso ou ansioso?'),
	op3(),
    read(A), resposta(A),
	write('Nas ultimas duas semana, com que frequencia voce se sente incapaz de controlar preocupaçao?'),
	op3(),
    read(B), resposta(B),
	write('Nas ultimas duas semana, com que frequencia voce se preocupa demais com coisas diferentes?'),
	op3(),
    read(C), resposta(C),
	write('Nas ultimas duas semana, com que frequencia voce tem dificuldade de relaxar?'),
	op3(),
    read(D), resposta(D),
	write('Nas ultimas duas semana, com que frequencia voce se sente tão desgastado que é dificil ficar parado?'),
	op3(),
    read(E), resposta(E),
	write('Nas ultimas duas semana, com que frequencia voce se irrita facilmente?'),
	op3(),
    read(E), resposta(E),
	write('Nas ultimas duas semana, com que frequencia voce sente medo como se algo ruim fosse acontecer?'),
	op3(),
    read(F), resposta(F),
	Z is A+B+C+D+E+F-6,
	nivelAnsiedade(Z).
	

stress():-
	nl,nl,nl,
	writeln('TESTE DE STRESS: '),
	nl,
	write('No ultimo mes, com que frequencia voce ficou chateado por causa de algo que aconteceu inesperadamente?'),
	op2(),
    read(A), resposta(A),
	write('No ultimo mes, com que frequencia voce se sentiu incapaz de controlar as coisas importantes na sua vida?'),
	op2(), 
    read(B),resposta(B),
	write('No ultimo mes, com que frequencia voce se sentiu nervoso e estressado?'),
	op2(),
    read(C),resposta(C),
	write('No ultimo mes, com que frequencia voce se sentiu falta de confiança em sua capacidade de lidar com seus problemas pessoais? Problemas?'),
	op2(),
    read(D),resposta(D),
	write('No ultimo mes, com que frequencia voce sentiu que as coisas nao estavam indo do seu jeito?'),
	op2(),
    read(E),resposta(E),
	write('No ultimo mes, com que frequencia voce descobriu que nao podia lidar com todas as coisas que voce teve que fazer?'),
	op2(),
    read(F),resposta(F),
	write('No ultimo mes, com que frequencia voce nao conseguiu controlar as irritações em sua vida?'),
	op2(),
    read(G),resposta(G),
	write('No ultimo mes, com que frequencia voce sentiu que nao estava no topo das coisas?'),
	op2(),
    read(H),resposta(H),
	write('No ultimo mes, com que frequencia voce se irritou por coisas que aconteceram que estavam fora do seu controle?'),
	op2(),
    read(I),resposta(I),
	write('No ultimo mes, quantas vezes voce sentiu dificuldades se acumulando tanto que nao conseguiu supera-las?'),
	op2(),
    read(J),resposta(J),
	Z is A+B+C+D+E+F+G+H+I+J,
	nivelStress(Z).



depressao():-
	nl,nl,nl,
	writeln('TESTE DE DEPRESSAO: '),
	nl,
    write('Nas ultimas duas semana, com que frequencia voce sente interesse ou prazer em fazer coisas?'),
	op(),
    read(A), resposta(A),
	write('Nas ultimas duas semana, com que frequencia voce se sente desanimado(a) ou sem esperanças?'),
	op(),
    read(B),resposta(B),
	write('Nas ultimas duas semana, com que frequencia voce tem problemas para dormir ou acaba dormindo muito?'),
	op(),
    read(C),resposta(C),
	write('Nas ultimas duas semana, com que frequencia voce se sente cansado ou com pouca energia?'),
	op(),
    read(D),resposta(D),
	write('Nas ultimas duas semana, com que frequencia voce nao tem apetite ou come muito?'),
	op(),
    read(E),resposta(E),
	write('Nas ultimas duas semana, com que frequencia voce se mal sobre si mesmo, ou que é uma falha ou é uma decepção pra voce mesmo ou pra usa familia?'),
	op(),
    read(F),resposta(F),
	write('Nas ultimas duas semana, com que frequencia voce tem problemas pra se concentrar em coisas como ler, ver TV?'),
	op(),
    read(G),resposta(G),
	write('Nas ultimas duas semana, com que frequencia voce se move ou fala tão devagar que outras pessoas poderiam notar? Ou o oposto, sendo tão inquieto que voce tem se movido muito mais do que o habitual?'),
	op(),
    read(H),resposta(H),
	write('Nas ultimas duas semana, com que frequencia voce pensa que seria melhor se estivesse morto ou se machucando de alguma forma?'),
	op(),
    read(I),
	Z is A+B+C+D+E+F+G+H+I-9,
	nivelDepre(Z).
  
% ['/Users/pedro/Documents/faculdade/pplf/trab.pl'].