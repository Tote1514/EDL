(princ "Enter Your name: ")
(setq your_name (read-line))
(print your_name)

(terpri)

(princ "Enter a character: ")
(setq a (read-char))
(print a)

(terpri)

(princ "Enter num1: ")
(setq num1 (read))
(princ "Enter num2: ")
(setq num2 (read))
(setq answer (+ num1 num2))
(princ answer)
