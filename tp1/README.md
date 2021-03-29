# Descrição do Trabalho Prático I

O TP proposto consiste em implementar um autômato finito determinístico para a sua linguagem.

## Linguagem 

O AFD a ser implementado seguirá a seguinte sequência: `ER -> AFN-e -> AFN -> AFD`

Dado que o sua matrícula é `d1d2d3d4d5d6d7d8d9` e as três primeiras letras de seu nome são `l1l2l3`, a ER é:  
`x1(d2l1 + d9l2)^+ x2`, sendo o `x` da forma:

* `x1` é o número de letras no primeiro nome;
* `x2` é o número de letras no segundo nome.

## Implementação

A implementação deve ser capaz de receber uma entrada de duas formas alternativas: individualmente (via terminal ou em interface à sua escolha) ou um conjunto de entradas, via arquivo texto (uma palavra por linha). E responder, para cada entrada dada, se a palavra foi aceita ou se foi rejeitada, em caso de rejeição, colocar também o motivo (indefinição ou fim da leitura em estado não-final). A leitura individual deve ser capaz de explicitar os passos do autômato na leitura da cada símbolo.

### Python Script

```bash
usage: tp1.py [-h] [-s STR] [-f FILE] [-o OUT] [-l]

UFSJ/T.Linguagens TP1

optional arguments:
  -h, --help            show this help message and exit
  -s STR, --str STR     string de entrada
  -f FILE, --file FILE  arquivo de entrada
  -o OUT, --out OUT     arquivo de saida
  -l, --legend          mostrar legenda
```

### R Shiny

Hospedado em [pcecilio.shinyapps.io/tlang_tp1/](https://pcecilio.shinyapps.io/tlang_tp1/)
