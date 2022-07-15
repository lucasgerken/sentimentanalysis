# Análise de Sentimento Utilizando Twitter e Python

**Instituto Tecnológico da Aeronáutica**

**Mestrado Profissional Em Computação Aeronáutica**

**CA-751 Inteligência Artificial**

**Alunos:**

- Gabriel Wedemann Colchiesqui  
- Lucas Gerken Glória  
- Charles Michael Ribeiro da Silva

## Introdução

A partir da explosão das redes sociais de uso global como o Twitter em 2006, a análise de sentimentos começou a ter um valor social muito importante. Opiniões nas redes sociais, se devidamente recolhidas e analisadas, permitem compreender e explicar comportamentos e tendências.

O processo de identificar as opiniões dos usuários expressas em texto e categorizá-las como positivas, negativas ou neutras é chamado de análise de sentimentos.

A verificação da análise de sentimentos pode ser um trabalho manual ou automatizado. Porém, a extração manual de sentimentos do texto inclui a leitura de cada mensagem, comentário ou revisão, o que pode consumir muito tempo e também ser tendencioso. Ao mesmo tempo, automatizar esse processo pode ajudar a acelerar as coisas e fornecer um sentimento imparcial.

Existem duas técnicas que lidam com os desafios de análise de sentimentos textuais: Técnicas supervisionadas e não supervisionadas:

Técnicas supervisionadas: Essas técnicas exigem uma etapa de treinamento de um modelo com amostras previamente classificadas.

Técnicas não supervisionadas: Diferentemente das técnicas supervisionadas, as técnicas não supervisionadas não carecem de sentenças previamente rotuladas e treinos para a criação de um modelo. Essa é uma das suas principais vantagens da técnica, uma vez que não fica restrita ao contexto para o qual foram treinados.

Para realizar a análise de sentimentos em nosso trabalho, utilizamos a biblioteca TextBlob, que utiliza a técnica do tipo não-supervisionado, ou seja, não é necessário passar uma base de frases positivas e negativas para fazer a classificação, o que torna a biblioteca poderosa e fácil de usar.

## Objetivos

Realizar uma análise de sentimento sobre cada mensagem enviada na rede social Twitter para saber a satisfação do público sobre determinado assunto.


