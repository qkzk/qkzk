factorielle(0,1) :- !.
factorielle(1,1) :- !.
factorielle(N, Result) :- N > 0, 
    					  N_moins_1 is N-1,
    					  factorielle(N_moins_1,   Fact_N_moins_1),
    					  Result is N * Fact_N_moins_1.