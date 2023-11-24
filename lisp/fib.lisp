(define (fib n)
    (if (= n 0)
        0
        (if (< n 3)
            1
            (+ (fib (sub1 n)) (fib (- n 2)))
        )
    )
)

(print (fib 30))
