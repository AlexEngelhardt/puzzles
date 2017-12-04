leap <- function(year) {
    y <- year

    if (y %% 4 == 0) {
        if (y %% 100 == 0) {
            leapyear <- y %% 400 == 0
        } else {
            leapyear <- TRUE
        }
    } else {
        leapyear <- FALSE
    }

    leapyear
}
