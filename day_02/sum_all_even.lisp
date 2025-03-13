(defun sum-even-numbers (n)
  (let ((sum 0))
    (loop for i from 2 to n by 2 do
         (setf sum (+ sum i)))
    sum))

;; Call the function to sum all even numbers until 10
(format t "The sum of even numbers up to 10 is: ~A~%" (sum-even-numbers 10))

