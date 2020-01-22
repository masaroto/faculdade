cls :- write('\e[H\e[2J').
%verificar resposta
resposta(0):- cls.
resposta(1):- cls.
resposta(2):- cls.
resposta(3):- cls.
resposta(4):- cls.

% Escolhas
escolha(1):- depressao().
escolha(2):- ansiedade().
escolha(3):- stress().

% Niveis de depressao 
nivelDepre(X,Y) :- X < 5, Y = 'Voce nao tem depressao.'.
nivelDepre(X,Y) :- X >= 5, X < 10 , Y = 'Voce tem depressao moderada.'.
nivelDepre(X,Y) :- X >= 10, X =< 15 , Y = 'Alto nivel de depressao.'.
nivelDepre(X,Y) :- X > 15, X =< 27,Y = 'Nivel de depressao severo.'.

% Niveis de stress
nivelStress(X,Y) :- X < 14, Y = 'Voce tem um nivel de stress baixo.'.
nivelStress(X,Y) :- X >= 14, X < 27 , Y = 'Voce tem um nivel de stress moderado.'.
nivelStress(X,Y) :- X >= 27, Y = 'Voce tem um nivel de stress alto.'.

% Niveis de Ansiedade
nivelAnsiedade(X,Y) :- X < 5, Y = 'Voce tem ansiedade leve.'.
nivelAnsiedade(X,Y) :- X >= 5, X < 10 , Y = 'Ansiedade moderada.'.
nivelAnsiedade(X,Y) :- X >= 10, X =< 15 , Y = 'Alto nivel de ansiedade.'.
nivelAnsiedade(X,Y) :- X > 15, Y = 'Nivel de ansiedade severo.'.


:- begin_tests(depressao).

	test(t0) :- nivelDepre(4, 'Voce nao tem depressao.').
	test(t1) :- nivelDepre(8, 'Voce tem depressao moderada.').
	test(t2) :- nivelDepre(14, 'Alto nivel de depressao.').
	test(t3) :- nivelDepre(18, 'Nivel de depressao severo.').

:- end_tests(depressao).

:- begin_tests(ansiedade).

	test(t0) :- nivelAnsiedade(4, 'Voce tem ansiedade leve.').
	test(t1) :- nivelAnsiedade(8, 'Ansiedade moderada.').
	test(t2) :- nivelAnsiedade(14, 'Alto nivel de ansiedade.').
	test(t3) :- nivelAnsiedade(18, 'Nivel de ansiedade severo.').

:- end_tests(ansiedade).

:- begin_tests(stress).

	test(t0) :- nivelStress(4, 'Voce tem um nivel de stress baixo.').
	test(t1) :- nivelStress(18, 'Voce tem um nivel de stress moderado.').
	test(t2) :- nivelStress(30, 'Voce tem um nivel de stress alto.').

:- end_tests(stress).

menu:-
	writeln('O presente programa se trata de um questionario que calcula o seu nivel de depressao, ansiedade ou stress baseado nas medidas PHQ-9, GAD-7, PSS respectivamente. Esse teste NAO é um diagnostico, para isso consulte um profissional.'),
	writeln('Por favor, pressione enter.'),
	get_single_char(A),
	cls,
	writeln('Escolha uma opção de teste:'),
	writeln('1 - Teste de Depressao.'),
	writeln('2 - Teste de Ansiedade.'),
	writeln('3 - Teste de Stress.'),
	read(X), escolha(X). 


op:-
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

op2:-
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


ansiedade():-
	cls,
	writeln('TESTE DE ANSIEDADE: Responda as perguntas com base nas suas últimas duas semanas.'),
	nl,
	write('Com que frequencia voce se sente nervoso ou ansioso?'),
	op(),
    read(A), resposta(A),
	write('Com que frequencia voce se sente incapaz de controlar preocupaçao?'),
	op(),
    read(B), resposta(B),
	write('Com que frequencia voce se preocupa demais com coisas diferentes?'),
	op(),
    read(C), resposta(C),
	write('Com que frequencia voce tem dificuldade de relaxar?'),
	op(),
    read(D), resposta(D),
	write('Com que frequencia voce se sente tão desgastado que é dificil ficar parado?'),
	op(),
    read(E), resposta(E),
	write('Com que frequencia voce se irrita facilmente?'),
	op(),
    read(E), resposta(E),
	write('Com que frequencia voce sente medo como se algo ruim fosse acontecer?'),
	op(),
    read(F), resposta(F),
	Z is A+B+C+D+E+F-6,
	nivelAnsiedade(Z,Y), write(Y).
	

stress():-
	cls,
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
	nivelStress(Z,Y) , write(Y).



depressao():-
	cls,
	writeln('TESTE DE DEPRESSAO: Responda as perguntas com base nas suas últimas duas semanas.'),
	nl,
    write('Com que frequencia voce não sente interesse ou prazer em fazer coisas?'),
	op(),
    read(A), resposta(A),
	write('Com que frequencia voce se sente desanimado(a) ou sem esperanças?'),
	op(),
    read(B),resposta(B),
	write('Com que frequencia voce tem problemas para dormir ou acaba dormindo muito?'),
	op(),
    read(C),resposta(C),
	write('Com que frequencia voce se sente cansado ou com pouca energia?'),
	op(),
    read(D),resposta(D),
	write('Com que frequencia voce nao tem apetite ou come muito?'),
	op(),
    read(E),resposta(E),
	write('Com que frequencia voce se sente mal sobre si mesmo, ou que é uma falha ou é uma decepção pra voce mesmo ou pra usa familia?'),
	op(),
    read(F),resposta(F),
	write('Com que frequencia voce tem problemas pra se concentrar em coisas como ler, ver TV?'),
	op(),
    read(G),resposta(G),
	write('Com que frequencia voce se move ou fala tão devagar que outras pessoas poderiam notar? Ou o oposto, sendo tão inquieto que voce tem se movido muito mais do que o habitual?'),
	op(),
    read(H),resposta(H),
	write('Com que frequencia voce pensa que seria melhor se estivesse morto ou se machucando de alguma forma?'),
	op(),
    read(I),
	Z is A+B+C+D+E+F+G+H+I-9,
	nivelDepre(Z,Y), write(Y).
  
% ['/Users/pedro/Documents/faculdade/pplf/trab.pl'].