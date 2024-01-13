# Descrição do Projeto

## 1. Desafio de Negócio

A Fome Zero é uma plataforma de restaurantes, atuando como um marketplace que facilita as interações entre clientes e estabelecimentos. Os restaurantes cadastram-se na plataforma, fornecendo informações como endereço, tipo de culinária, disponibilidade de reservas, opção de entrega e avaliações. O recém-contratado CEO, Guerra, busca compreender melhor o negócio para tomar decisões estratégicas informadas. Para isso, é necessário realizar uma análise dos dados e criar dashboards para responder diversas perguntas.

## Visão Geral

1. Quantos restaurantes únicos estão registrados?
2. Quantos países únicos estão registrados?
3. Quantas cidades únicas estão registradas?
4. Qual o total de avaliações feitas?
5. Qual o total de tipos de culinária registrados?

## Por País

1. Qual o país com mais cidades registradas?
2. Qual o país com mais restaurantes registrados?
3. Qual o país com mais restaurantes de nível de preço 4?
4. Qual o país com mais tipos de culinária distintos?
5. Qual o país com mais avaliações?
6. Qual o país com mais restaurantes que fazem entrega?
7. Qual o país com mais restaurantes que aceitam reservas?
8. Qual o país com a maior média de avaliações?
9. Qual o país com a maior média de nota?
10. Qual o país com a menor média de nota?

## Por Cidade

1. Qual a cidade com mais restaurantes registrados?
2. Qual a cidade com mais restaurantes com média acima de 4?
3. Qual a cidade com mais restaurantes com média abaixo de 2.5?
4. Qual a cidade com mais tipos de culinária distintos?
5. Qual a cidade com mais restaurantes que fazem reservas?
6. Qual a cidade com mais restaurantes que fazem entregas?
7. Qual a cidade com mais restaurantes que aceitam pedidos online?

## Restaurantes e Tipos de Culinária

1. Qual o restaurante com mais avaliações?
2. Qual o restaurante com a maior média de notas?
3. Qual o restaurante italiano com a maior média de avaliações?
4. Qual o restaurante italiano com a menor média de avaliações?
5. Qual o restaurante americano com a maior média de avaliações?
6. Qual o restaurante americano com a menor média de avaliações?
7. Qual o restaurante árabe com a maior média de avaliações?
8. Qual o restaurante árabe com a menor média de avaliações?
9. Qual o restaurante japonês com a maior média de avaliações?
10. Qual o restaurante japonês com a menor média de avaliações?

## 2. Premissas do Negócio

- O banco de dados contém as seguintes observações:

| Column | Description |
| --- | --- |
| Restaurant ID | ID do restaurante |
| Restaurant Name | Nome do Restaurante |
| Country Code | Código do País |
| City | Nome da Cidade onde o restaurante está |
| Address | Endereço do restaurante |
| Locality | Localização e pontos de referência do restaurante |
| Locality Verbose | Localização e pontos de referência do restaurante (Mais informações) |
| Longitude | Ponto geográfico de Longitude do Restaurante |
| Latitude | Ponto geográfico de Latitude do Restaurante |
| Cuisines | Tipos de Culinária servidos no restaurante |
| Average Cost for two | Preço Médio de um prato para duas pessoas no restaurante |
| Currency | Moeda do país |
| Has Table booking | Se o restaurante possui serviços de reserva; 1 - Sim; 0 - Não |
| Has Online delivery | Se o restaurante possui serviços de pedido on-line; 1 - Sim; 0 - Não |
| Is delivering now | Se o restaurante faz entregas; 1 - Sim; 0 - Não |
| Switch to order menu | - |
| Price range | Variação de preços do restaurante; 1 a 4 - Quanto maior o valor, mais caro serão os pratos |
| Aggregate rating | Nota média do restaurante |
| Rating color | Código Hexadecimal da cor do restaurante com base em sua nota média |
| Rating text | Categoria em que o restaurante está com base em sua nota média |
| Votes | Quantidade de avaliações que o restaurante já recebeu |


## 3. Estratégia da Solução

Desenvolvimento de dashboards para análise de dados, fornecendo informações detalhadas sobre o negócio da Fome Zero em quatro visões macro: geral, por país, por cidade e por tipos culinários.

## 4. Top 3 Insights dos Dados

1. A Índia lidera em número de cidades (39%) e restaurantes registrados (52%).
2. Menos da metade dos restaurantes aceitam pedidos online (41%), realizam entregas (20%) e reservam mesas (7%).
3. O tipo culinário "outros" recebe a melhor avaliação.

## 5. Produto Final

Painel online hospedado na nuvem, acessível em qualquer dispositivo conectado à internet. Link do painel: [Fome Zero Dashboard](https://projects-fomezero-marcelobrandao.streamlit.app/)

## 6. Conclusão

O projeto tem como objetivo apresentar métricas de negócios de forma visual e compreensível para o CEO.

## 7. Próximos Passos

1. Padronizar o custo da refeição para uma moeda única e realizar comparações.
2. Analisar a relação entre a proporção de restaurantes que aceitam pedidos online, entregam e/ou reservam mesas com tipos culinários, custo da refeição e avaliação.

# In English

# Project Description

## 1. Business Challenge

Fome Zero is a restaurant platform that operates as a marketplace, facilitating interactions between customers and establishments. Restaurants register on the platform, providing information such as address, cuisine type, reservation availability, delivery option, and reviews. The newly hired CEO, Guerra, aims to better understand the business to make informed strategic decisions. To achieve this, data analysis is necessary, and dashboards need to be created to answer various questions.

## Overview

1. How many unique restaurants are registered?
2. How many unique countries are registered?
3. How many unique cities are registered?
4. What is the total number of reviews?
5. What is the total number of registered cuisine types?

## By Country

1. Which country has the most registered cities?
2. Which country has the most registered restaurants?
3. Which country has the most restaurants with a price level of 4?
4. Which country has the most distinct cuisine types?
5. Which country has the most reviews?
6. Which country has the most restaurants offering delivery?
7. Which country has the most restaurants accepting reservations?
8. Which country has the highest average number of reviews?
9. Which country has the highest average rating?
10. Which country has the lowest average rating?

## By City

1. Which city has the most registered restaurants?
2. Which city has the most restaurants with an average rating above 4?
3. Which city has the most restaurants with an average rating below 2.5?
4. Which city has the most distinct cuisine types?
5. Which city has the most restaurants offering reservations?
6. Which city has the most restaurants offering delivery?
7. Which city has the most restaurants accepting online orders?

## Restaurants and Cuisine Types

1. Which restaurant has the most reviews?
2. Which restaurant has the highest average rating?
3. Which Italian restaurant has the highest average rating?
4. Which Italian restaurant has the lowest average rating?
5. Which American restaurant has the highest average rating?
6. Which American restaurant has the lowest average rating?
7. Which Arabic restaurant has the highest average rating?
8. Which Arabic restaurant has the lowest average rating?
9. Which Japanese restaurant has the highest average rating?
10. Which Japanese restaurant has the lowest average rating?

## 2. Business Assumptions

- The database contains the following observations:

| Column | Description |
| --- | --- |
| Restaurant ID | Restaurant ID |
| Restaurant Name | Restaurant Name |
| Country Code | Country Code |
| City | City where the restaurant is located |
| Address | Restaurant address |
| Locality | Location and landmarks of the restaurant |
| Locality Verbose | Location and landmarks of the restaurant (More information) |
| Longitude | Geographic Longitude point of the restaurant |
| Latitude | Geographic Latitude point of the restaurant |
| Cuisines | Types of cuisines served in the restaurant |
| Average Cost for two | Average cost of a meal for two people in the restaurant |
| Currency | Country's currency |
| Has Table booking | Whether the restaurant offers reservation services; 1 - Yes; 0 - No |
| Has Online delivery | Whether the restaurant offers online ordering services; 1 - Yes; 0 - No |
| Is delivering now | Whether the restaurant delivers; 1 - Yes; 0 - No |
| Switch to order menu | - |
| Price range | Restaurant price range; 1 to 4 - Higher value indicates more expensive dishes |
| Aggregate rating | Restaurant's average rating |
| Rating color | Hexadecimal code of the restaurant's color based on its average rating |
| Rating text | Category in which the restaurant falls based on its average rating |
| Votes | Number of reviews the restaurant has received |

## 3. Solution Strategy

Development of dashboards for data analysis, providing detailed information about Fome Zero's business in four macro views: general, by country, by city, and by cuisine types.

## 4. Top 3 Data Insights

1. India leads in the number of cities (39%) and registered restaurants (52%).
2. Less than half of the restaurants accept online orders (41%), provide delivery services (20%), and accept reservations (7%).
3. The cuisine type "others" receives the highest rating.

## 5. Final Product

Online dashboard hosted in the cloud, accessible on any internet-connected device. Dashboard link: [Fome Zero Dashboard](https://projects-fomezero-marcelobrandao.streamlit.app/)

## 6. Conclusion

The project aims to present business metrics visually and comprehensibly for the CEO.

## 7. Next Steps

1. Standardize the cost of a meal to a single currency and make comparisons.
2. Analyze the relationship between the proportion of restaurants accepting online orders, delivering, and/or reserving tables with cuisine types, meal cost, and ratings.
