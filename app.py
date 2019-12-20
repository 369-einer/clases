import piloto
import avion
import jinete
import caballo
import machete
import agricultor
import escritor
import libro
import soldado
import fusil
import chofer
import omnibus
import boxceador
import boxeo
import jovenes
import playa
import grifo
import automovil
import cliente
import celular
import pais
import armanuclear
import niño
import bicicleta
import laptop
import adolesente
import perro
import gato
import gallina
import zorro






print("#################################################......A")

p1=piloto.Piloto("einer",28,"experto")
p1.nombre="einer"
p1.edad=28
p1.destreza="experto"
print("level del piloto ..."+ str(p1.destreza))
print("#################################################....A")

a1=avion.Avion("apodo_nave","nro_asientos","ofrecimiento")
a1.apodo_nave="hercules"
a1.nro_asientos=386
a1.ofrecimiento="bebidas..comida..peliculas"
print("la nave apodada",str(a1.apodo_nave),"fue capturada por fuerzas inexplicables" ,
      "con ",str(a1.nro_asientos),"pasajeros desaparecidos")
print("#########################################################...........B")
j1=jinete.jinete("nombre","peso","nro_corredor")
j1.nombre="einer"
j1.peso=800
j1.nro_corredor=52
print("el jinete",str(j1.nombre),"con numero",str(52),"es el ganador!!!!!")
print("################################################################...........B")
c1=caballo.Caballo("tamaño","raza","nombre")
c1.tamaño=3
c1.raza="mulato"
c1.nombre="rocinante"
print("el caballo llamado ",str(c1.nombre),"de raza",str(c1.raza),"son los mejores")
print("#########################################################.##############..........C")
m1=machete.Machete("material","espesor","tamaño","marca")
m1.material="acero"
m1.espesor=14
m1.tamaño=125
m1.marca="leex"
print("el machete llamado de ",str(m1.material),"de tamaño",str(m1.tamaño),"son los mejores")
print("#########################################################...........C")
a1=agricultor.Agricultor("nombre","edad","horas_trabajo","sembrio")
a1.nombre="salas"
a1.edad=14
a1.horas_trabajo=8
a1.sembrio="algodon"
print("el agricultor llamado : ",str(a1.nombre),"cultiva",str(a1.sembrio))

print("#########################################################...........D")
e1=escritor.Escritor("nombre","nacionalidad","idioma")
e1.nombre="yunhsetil"
e1.nacionalidad="peruano"
e1.idioma="español"
print("el escritor",str(e1.nombre),"es :",str(e1.nacionalidad))
print("#########################################################...........D")
l1=libro.Libro("catdd_paginas","grosor_pagina","figuras_literarias")
l1.catdd_paginas=847
l1.grosor_pagina=0.8
l1.figuras_literarias="polisindeton..metafora...elipsis"
print("este libro  tiene ",str(l1.catdd_paginas),
      "y se encuentran las suiguientes figuras literarias, como:",str(l1.figuras_literarias))
print("#########################################################...........E")
s1=soldado.Soldado("tiempode_entrenamiento","misiones","apodo")
s1.tiempode_entrenamiento=4850
s1.misiones=8
s1.apodo="serpiente852"
print("soldado",str(s1.apodo),"reportese de inmediato a las oficinas de su superior")
print("#########################################################...........E")
f1=fusil.Fusil("calibre","tiempo_dedisparo","lisencia")
f1.calibre="22"
f1.tiempo_dedisparo=0.05
f1.lisencia="activa"
print("usted soldado tiense licensia y esta ",str(f1.lisencia),)
print("#########################################################...........F")

ch1=chofer.Chofer("experiencia","edad","identidad")
ch1.experiencia="experto"
ch1.edad=56
ch1.identidad="peruano"
print("usted chofer tiene una gran ",str(ch1.experiencia))
print("#########################################################...........F")
o1=omnibus.Omnibus("nro_asientos","nombre","velocidad_maxima")
ch1.nro_asientos=48
ch1.nombre="firulais"
ch1.velocidad_maxima=200

print("el mejor omnibus del peru es: ",str(ch1.nombre))
print("#########################################################...........G")
bo1=boxceador.Boxceador("nombre","nacionalidad","peso","talla")
bo1.nombre="yanclan"
bo1.nacionalidad="marteriano"
bo1.peso=5000
bo1.talla=1000
print("el boxceador de nombre ",str(bo1.nombre),"y es de nacionalidad ",str(bo1.nacionalidad))
print("#########################################################...........G")
box=boxeo.Boxeo("clasificatorias","ubicacion","premios","hora")
box.clasificatorias=8
box.ubicacion="neptuno"
box.premio="una galaxia"
box.hora=1969
print("el mejor boxeo se realizara en ",str(box.ubicacion),"a las ",str(box.hora),
      "horas universales.....con un premio de una de las mejores",str(box.premio),"del universo")
print("#########################################################...........H")
j1=jovenes.Jovenes("edades","nacionalidades","preferencias")
j1.edades="mixto"
j1.nacionalidades="extranjeras"
j1.preferencias="distintas"
print("en la playa encontrmos jovenes de distintos lugares, algunos son ",(j1.nacionalidades))

print("#########################################################...........H")
p1=playa.Playa( "arerna","ubicacion", "temperatura")
p1.arena="caliente"
p1.ubicacion="chiclayo-santa rosa"
p1.temperatura=25
print("la playa que visitaremos se encuentra en ",str(p1.ubicacion),"con una emperatura de ",
      str(p1.temperatura),"grados celcius")
print("#########################################################...........I")
au1=automovil.Automovil( "color","nro_asientos","marca")
au1.color="negro"
au1.nro_asientos=6
au1.marca="suzuki"
print("la tia se compro un carro color ",str(au1.color),"marca ",str(au1.marca))

print("#########################################################...........I")
g1=grifo.Grifo( "ubicacion","disposicion_de_combustible","precios")
g1.ubicacion="piedra grande"
g1.disposicion_de_combustible="90-60-80"
g1.precios=2789
print("el grifo se encuentra en ",str(g1.ubicacion),"les ofrece gasolina de ",
      str(g1.disposicion_de_combustible))
print("#########################################################...........J")
ce1=celular.Celular("año_fabricaion","modelo","marca")
ce1.año_fabricaion=2022
ce1.modelo="tactil....v3100"
ce1.marca="phone"
print("tu celular esta fabricado en el año ",str(ce1.año_fabricaion),"de modelo",str(ce1.modelo),"marca",ce1.marca)
print("#########################################################...........J")
cl=cliente.Cliente("dis_dinero","nombre","identidad","trabajo")
cl.dis_dinero=5000
cl.nombre="francisca"
cl.identidad="peruano"
cl.trabajo="estable"
print("uted señor ",cl.nombre,"cuenta con ",cl.dis_dinero,"es muy claro que tiene un trabajo",cl.trabajo)
print("#########################################################...........K")
ar=armanuclear.Armanuclear("xy","xu","x123","x666")
ar.xy = "1000 km cuadrados"
ar.xu = "40000 km cuadrados"
ar.x123 = "destruccion medio planeta"
ar.x666 = "&&&&planeta entero ....$%&FR$$&#"
print("fin de la humanidad sera con la bomba ",ar.x666)

print("#########################################################...........K")
p=pais.Pais("peru","chile")
p.peru="mejor armamento nuclear"
p.chile="mejor armamento belico"
print("el mejor pais es que tiene es ",p.peru)
print("#########################################################...........L")
n1=niño.Niño("nombre","edad","color_ojos","apellido")
n1.nombre="juan"
n1.edad=9
n1.color_ojos="verdes claros"
n1.apellido="shells"
print("el niño",n1.nombre,"tiene",str(n1.edad),"años")
print("########################################################...........L")
bi1=bicicleta.Bicicleta("color","precio","longitud","marca")
bi1.color="rojo..blanco"
bi1.precio=300
bi1.longitud=128
bi1.marca="pioner"
print("mi bicicleta es de color ",bi1.color,"con una longitud",str(bi1.longitud))
print("########################################################...........M")
a=adolesente.Adolesente("edad","nombre","sexo","talla")
a.edad=14
a.nombre="iris"
a.sexo="femenino"
a.talla=196
print("tu hija adolesente se llama",a.nombre,"con una edad de ","a.edad")

print("########################################################...........M")
l=laptop.Laptop("made_in","marca","disco_duro","tajeta_de_video")
l.made_in="en china"
l.marac="lenovo"
l.disco_duro="8terabyt"
l.tajeta_de_video="4 de video"
print("la laptop que desea es la de ",l.disco_duro,"y",l.tajeta_de_video)
print("########################################################...........N")
pe1=perro.Perro("color","velocidad_perro","tamaño","edad")
pe1.color="amarillo"
pe1.velocidad_perro=1800
pe1.tamaño=56
pe1.edad=6
print("velocidad del perro es de ",str(pe1.velocidad_perro),"metros po minuto")
print("########################################################...........N")
g=gato.Gato("color","edad","velocidad_gato","longitud")
g.color="negro"
g.edad=2
g.velocidad_gato=200
g.longitud=20
print("color del gato",g.color,"con una edad de",str(g.edad))
print("########################################################...........Ñ")
ga=gallina.Gallina("raza","peso","precio")
ga.raza="alonrg"
ga.peso=7
ga.precio=150
print("el precio de la gallina es ",ga.precio,"y un peso de ",str(ga.peso))
print("########################################################...........Ñ")
z=zorro.Zorro("raza","peso","velocidad_zorro")
z.raza="perica"
z.peso=21
z.velocidad_zorro=150
print("la velocidad del zorro es ",z.velocidad_zorro,"con un peso de  ",str(z.peso))




