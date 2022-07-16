(defun factorial (N)
  "Compute the factorial of N."
  (if (= N 1)
      1
    (* N (factorial (- N 1)))))


(princ "Programa para calcular o fatorial de um numero")
(terpri)
(princ "Digite um numero: ")
(setq num1 (read))
(princ (factorial num1))
