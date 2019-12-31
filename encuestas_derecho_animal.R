library(dplyr)
library(tidyr)
library(ggplot2)
library(waffle)

setwd('/home/carlos/Documentos/Encuestas_UNAM/')

list.files()

encuestas <- read.csv('encuestas.csv')

encuestas$Pregunta <- as.character(encuestas$Pregunta)
encuestas$Opción <- as.character(encuestas$Opción)
encuestas$Edad <- as.factor(encuestas$Edad)

#table(encuestas$Pregunta)

conteo <- encuestas %>% 
  group_by(Opción) %>%
  summarise(conteo = n())

# ¿Numero de encuenstados?

conteo <- encuestas %>% 
  group_by(Facultad) %>%
  summarise(conteo = n()) %>%
  mutate(conteo, encuestados = conteo/12 , nueva = encuestados / sum(encuestados))

conteo

ggplot(conteo, aes(x = 1, y = nueva, fill = Facultad)) + 
  geom_col() + 
  coord_polar(theta = "y") +
  geom_text(aes(label = encuestados), position = position_fill(vjust = 0.5)) +
  theme_void() + 
  ggtitle('¿Qué piensan los Universitarios sobre el Derecho Animal?'
          ,subtitle = paste0('Encuestados: ' , sum(conteo$encuestados)))
  
# ¿Como está segmentado las encuestas?
#¿Sexo por facultad?
#Falta color y etiquetas 
conteo <- encuestas %>% 
  group_by(Sexo) %>%
  summarise(conteo = n()) %>%
  mutate(conteo, encuestados = conteo/12 , nueva = encuestados / sum(encuestados))

conteo 

ggplot(encuestas, aes(Sexo), fill = Sexo) +
  geom_bar() + 
  facet_wrap(~Facultad) +
  ggtitle('Sexo por Facultad')

# Rango de Edad General y Facultad
conteo <- encuestas %>% 
  group_by(Edad) %>%
  summarise(conteo = n()) %>%
  mutate(conteo, encuestados = conteo/12 , nueva = encuestados / sum(encuestados))

ggplot(conteo, aes(x = Edad,y = encuestados)) + 
  geom_col() + 
  ggtitle('Rango de Edad')

conteo <- encuestas %>% 
  group_by(Edad,Facultad) %>%
  summarise(conteo = n()) %>%
  mutate(conteo, encuestados = conteo/12 , nueva = encuestados / sum(encuestados))

conteo

ggplot(conteo, aes(x = Edad,y = encuestados)) + 
  geom_col() + 
  facet_wrap(~Facultad) + 
  ggtitle('Rango de Edad por Facultad')

head(encuestas)

#Preguntas

for(i in seq(12)){
  eval(parse(text = paste0("encuestas$Pregunta[encuestas$Pregunta == ",i,"] <- 'Pregunta_",i,"'")))
}

head(encuestas)

tmp <- encuestas %>% 
  group_by(Pregunta) %>% 
  mutate(grouped_id = row_number()) %>%
  select(-Edad,-Sexo,-Facultad,-Comentarios) %>% 
  spread(Pregunta, Opción) %>%
  select(-grouped_id)

head(tmp)

Pregunta_1 <- tmp %>% group_by(Pregunta_1) %>% summarise(Conteo = n()) %>%
  mutate(Porcentaje = paste0(round(Conteo/sum(Conteo),2)*100,'%'))

Pregunta_1

ggplot(Pregunta_1, aes(x = "", y = Conteo, fill = Pregunta_1, label = Conteo)) + 
  geom_bar(stat = "identity", position = position_fill()) +
  geom_text(aes(label = Porcentaje), position = position_fill(vjust = 0.5)) +
  coord_polar(theta = "y") + 
  theme_void() +
  theme(axis.title.x = element_blank(),
        axis.title.y = element_blank()) +
  ggtitle(paste0('¿Conoces de la existencia del derecho animal?'))

#¿Distribución de Respuestas en las Opciones?

ggplot(encuestas, aes(x = Pregunta, fill = Opción)) +
  geom_bar(position = "fill") +
  scale_y_continuous(breaks = seq(0,1, by = .2), labels = scales::percent) +
  coord_flip() +
  facet_wrap(~Facultad)


table(encuestas$Opción)







