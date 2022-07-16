(defun triple (X)
  "Compute three times X."
  (* 3 X))


(princ "Programa para calcular o triplo de um numero")
(terpri)
(princ "Enter a number: ")
(setq num1 (read))
(princ (triple num1))
