(define (factorial n)
    (if (= n 0)
        1
        (* n (factorial (sub1 n)))
    )
)

(print (factorial 10))