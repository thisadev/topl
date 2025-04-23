x <- 1

func_a <- function() {
        print(x)
}

func_b <- function() {
        x <- 2
        func_a()
}

func_b()
