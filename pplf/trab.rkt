#lang racket/base
(require rackunit)
(require rackunit/text-ui)
(require racket/set)
(require racket/string)
(require memoize)
(require math/statistics)

;;str str -> Numero
;;Calcula a similaridade
(define (jaccard_index str1 str2)
  (define list-str1 (string-split str1))
  (define list-str2 (string-split str2))
  (define len-str1 (length list-str1))
  (define len-str2 (length list-str2))
  (define intersection (set-intersect list-str1 list-str2))
  (define inter-size (length intersection))


  (exact->inexact(/ inter-size (- (+ len-str1 len-str2) inter-size) ))
  
  
  )

;;str str -> Numero
;;Calcula a diferença
(define (jaccard_distance str1 str2)
  (- 1 (jaccard_index str1 str2)))

;;str str -> Numero
;;Calcula a similaridade
(define/memo* (levenshtein str1 str2)
  (cond
    [(equal? str1 "") (string-length str2)]
    [(equal? str2 "") (string-length str1)]
    [(equal? (string-ref str1 (sub1 (string-length str1))) (string-ref str2 (sub1 (string-length str2))))
      (min
          (add1 (levenshtein (substring str1 0 (sub1 (string-length str1))) str2))
          (add1 (levenshtein str1 (substring str2 0 (sub1 (string-length str2)))))
          (levenshtein (substring str1 0 (sub1 (string-length str1))) (substring str2 0 (sub1 (string-length str2)))))
     ]
    [else
     (min
          (add1 (levenshtein (substring str1 0 (sub1 (string-length str1))) str2))
          (add1 (levenshtein str1 (substring str2 0 (sub1 (string-length str2)))))
          ( add1 (levenshtein (substring str1 0 (sub1 (string-length str1))) (substring str2 0 (sub1 (string-length str2))))))]
    )
  )

;;str str -> Numero
;;Normaliza o algoritimo de levenshtein
(define (levenshtein-distance str1 str2)
  (define max-len (max (string-length str1) (string-length str2)))
  (exact->inexact(- 1 (/ (levenshtein str1 str2) max-len)))
  )
(define sim-tests
  (test-suite
   "similarity tests"
   (check-equal? (levenshtein-distance "Meu primo gosta de amarelo" "Meu primo gosta de amarelo") 1.0)
   (check-equal? (levenshtein-distance "kitten" "sitting") 0.5714285714285714)
   (check-equal? (levenshtein-distance "I'm off the deep end, watch as I dive in" "Diga o que te fez Sentir saudade ") 0.3)
   (check-equal? (levenshtein-distance "Racket" "Hacket") 0.8333333333333334)
   (check-equal? (levenshtein-distance "Um dia eu gostaria de ver o sol de novo, enquanto esse dia não chega, eu esperarei" "Eu acho que as coisas não deveriam ser tão complicadas") 0.2682926829268293)
   
   (check-equal? (jaccard_index "Eu quero sair daqui por favro alguem me ajude" "Queria muito ser rico aceito a ajuda de voces") 0.0)
   (check-equal? (jaccard_index "Meu primo gosta de amarelo" "Meu primo gosta de amarelo") 1.0)
   (check-equal? (jaccard_index "I'm off the deep end, watch as I dive in" "Diga o que te fez Sentir saudade ") 0.0)
   (check-equal? (jaccard_index "Racket" "Hacket") 0.0)
   (check-equal? (jaccard_index "Um dia eu gostaria de ver o sol de novo, enquanto esse dia não chega, eu esperarei" "Eu acho que as coisas não deveriam ser tão complicadas") 0.038461538461538464)
   
   ))
(define (executa-testes . testes)
(run-tests (test-suite "Todos os testes" testes))
(void))
(executa-testes sim-tests)

(define text1 "Ela disse que gosta de sair") ;;81
(define text2 "Ele disse que gosta de ficar")

(define text3 "Eu gostaria de saber");;93
(define text4 "Eu gostaria de ver")

(define text5 "Eu quero sair daqui");;61
(define text6 "Queria muito ser rico")

(define text7 "Meu primo gosta de amarelo");;1
(define text8 "Meu primo gost de amarelo")


(define list-esperado (list 0.81 0.93 61 1))
(define testA (levenshtein-distance text1 text2))
(define testB (levenshtein-distance text3 text4))
(define testC (levenshtein-distance text5 text6))
(define testD (levenshtein-distance text7 text8))

(define testE (jaccard_index text1 text2))
(define testF (jaccard_index text3 text4))
(define testG (jaccard_index text5 text6))
(define testH (jaccard_index text7 text8))

(define list-real-levenshtein (list testA testB testC testD))
(define list-real-jaccard (list testE testF testG testH))



(abs (correlation list-real-levenshtein list-esperado))
(abs (correlation list-real-jaccard list-esperado))

