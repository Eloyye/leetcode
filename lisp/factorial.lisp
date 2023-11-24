(define (mult n1 n2)
    (if (= n1 0)
        0
        (if (= n1 1)
            n2
            (+ n2 (mult (sub1 n1) n2))
        )
    )
)
(define (factorial n)
    (if (= n 0)
        1
        (let ((r (factorial (sub1 n))))
            (mult n r)
        )
    )
)

(print (factorial 10))