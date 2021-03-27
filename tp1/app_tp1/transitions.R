state0 <- function(c) {
  if(c == '5')
    state <- 1
  else
    state <- -1
  return(state)
}

state1 <- function(c) {
  if(c == '7')
    state <- 2
  else if (c == '8')
    state <- 3
  else
    state <- -1
  return(state)
}

state2 <- function(c) {
  if(c == 'p')
    state <- 4
  else
    state <- -1
  return(state)
}

state3 <- function(c) {
  if(c == 'a')
    state <- 4
  else
    state <- -1
  return(state)
}

state4 <- function(c) {
  if(c == '8')
    state <- 3
  else if(c == '7')
    state <- 5
  else
    state <- -1
  return(state)
}

state5 <- function(c) {
  if(c == 'p')
    state <- 4
  else
    state <- -1
  return(state)
}