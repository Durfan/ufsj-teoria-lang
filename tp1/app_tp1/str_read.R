isAccepted <- function(str) {

  if(nchar(str) == 0)
    return(img(src='q0.svg', width='90%'))

  str_split <- strsplit(str, "")[[1]]

  initial <- 0
  state <- initial
  img_state <- NULL
  
  for(c in str_split) {
    if(state == -1)
      break
    if(state == 0) {
      state <- state0(c)
      if(state == 1)
        img_state <- img(src='q1.svg', width='90%')
      else
        img_state <- img(src='q0_err.svg', width='90%')
    }
    else if(state == 1) {
      state <- state1(c)
      if(state == 3)
        img_state <- img(src='q3.svg', width='90%')
      else if(state == 2)
        img_state <- img(src='q2.svg', width='90%')
      else
        img_state <- img(src='q1_err.svg', width='90%')
    }
    else if(state == 2) {
      state <- state2(c)
      if(state == 4)
        img_state <- img(src='q4.svg', width='90%')
      else
        img_state <- img(src='q2_err.svg', width='90%')
    }
    else if(state == 3) {
      state <- state3(c)
      if(state == 4)
        img_state <- img(src='q4.svg', width='90%')
      else
        img_state <- img(src='q3_err.svg', width='90%')
    }
    else if(state == 4) {
      state <- state4(c)
      if(state == 3)
        img_state <- img(src='q3.svg', width='90%')
      else if(state == 5)
        img_state <- img(src='q5.svg', width='90%')
      else
        img_state <- img(src='q4_err.svg', width='90%')
    }
    else if(state == 5) {
      state <- state5(c)
      if(state == 4)
        img_state <- img(src='q4.svg', width='90%')
      else
        img_state <- img(src='q5_err.svg', width='90%')
    }
    else {
      state <- -1
      break
    }
  }
  
  if(state == 5) {
    tags$div(
      img_state,
      h3(icon('check-circle'),'Aceita', align = 'center')
    )
  }
  else if(state == -1) {
    tags$div(
      img_state,
      h3(icon('times-circle'),'Rejeitada (Indefinição)', align = 'center')
    )
  }
  else {
    tags$div(
      img_state,
      h3(icon('times-circle'),'Rejeitada (estado não final)', align = 'center')
    )
  }
}

isAccepted_file <- function(str) {

  str_split <- strsplit(str, "")[[1]]

  initial <- 0
  state <- initial
  
  for(c in str_split) {
    if(state == -1)
      break
    if(state == 0)
      state <- state0(c)
    else if(state == 1)
      state <- state1(c)
    else if(state == 2)
      state <- state2(c)
    else if(state == 3)
      state <- state3(c)
    else if(state == 4)
      state <- state4(c)
    else if(state == 5)
      state <- state5(c)
    else {
      state <- -1
      break
    }
  }
  
  if(state == 5) {
    return(list('Aceita',''))
  }
  else if(state == -1) {
    return(list('Rejeitada','Indefinição'))
  }
  else {
    return(list('Rejeitada','Estado não final'))
  }
}