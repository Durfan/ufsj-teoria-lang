source('transitions.R', local = TRUE)
source('str_read.R', local = TRUE)

ui <- fluidPage(

  fluidRow(
    img(
      src='logo_ufsj.png',
      align='left',
      style='margin:25px 10px 30px 15px;'),
    titlePanel(
      'Teoria de Linguagens',
      windowTitle = 'Teoria de Linguagens'
      ),
    p('Trabalho Prático I', style='margin-top:-10px;')
  ),
  
  fluidRow(
    column(
      width = 3,
      textInput('string', 'Palavra'),
      helpText(
        HTML('5(7p+8a)<sup>+</sup>7'),
        style='margin-top: -10px;'),
      fileInput("tests_upload", "Carregar arquivo", accept = ".txt"),
      tags$div(
        tags$small('Pablo Cecilio Oliveira 172050108'),
        tags$br(),
        tags$small(
          icon('code-branch'),
          a('github.com/Durfan/ufsj-teoria-lang',
            href='https://github.com/Durfan/ufsj-teoria-lang')
        ), style='margin-top: 50px;'
      )
    ),
    column(
      width = 9,
      htmlOutput('results')
    )
  )
)

server <- function(input, output, session) {
  
  file_upload <- reactive({
    inFile <- input$tests_upload
    if (is.null(inFile))
      return(NULL)
    tests <- read.table(inFile$datapath)
    return(tests)
  })

  observeEvent(input$string, {
    output$results <- renderUI({
      isAccepted(input$string)
    })
  })

  observeEvent(input$tests_upload, {
    output$results <- renderTable({
      tests <- file_upload()
      results <- t(sapply(tests[,1],isAccepted_file))
      results
    },
    striped = TRUE, hover = TRUE,
    rownames = TRUE, colnames = FALSE, spacing = 'xs')
  })

}

shinyApp(ui = ui, server = server)