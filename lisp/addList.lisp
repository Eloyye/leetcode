(define (addList list1 list2)
    (if (empty? list1)
        ()
        (pair
            (+ (left list1) (left list2))
            (addList (right list1) (right list2))
        )
    )
)

(let
    (
        (list1 (pair 1 (pair 2 (pair 3 ()))))
    )
    (let
        (
            (list2 (pair 10 (pair 9 (pair 12 ()))))
        )
        (print (addList list1 list2))
    )
)