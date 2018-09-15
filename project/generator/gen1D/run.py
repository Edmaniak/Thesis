from project.generator.gen1D.Data1D import Data1D
from project.generator.gen1D.Object1D import Object1D

podlaha = Object1D("podlaha")
stul = Object1D("stul")
chleba_na_spodu = Object1D("chleba ve spodu")
chleba_na_vrchu = Object1D("chleba na vrchu")
maslo = Object1D("maslo")
sunka = Object1D("sunka")
syr = Object1D("syr")
vajicka = Object1D("vajicka")
papricka = Object1D("papricka")

# Constraints
podlaha.set_obligatory()
stul.set_object_const("ABOVE", podlaha)
stul.set_obligatory()

chleba_na_spodu.set_object_const("ABOVE", stul)
chleba_na_vrchu.set_object_const("ABOVE", chleba_na_spodu)
chleba_na_vrchu.set_object_const("ABOVE", sunka)
chleba_na_vrchu.set_object_const("ABOVE", syr)
chleba_na_vrchu.set_object_const("ABOVE", papricka)
chleba_na_vrchu.set_object_const("ABOVE", maslo)
chleba_na_spodu.set_obligatory()

vajicka.set_object_const("ABOVE", maslo)
vajicka.set_object_const("ABOVE", maslo)

syr.set_object_const("ABOVE", chleba_na_spodu)
syr.set_object_const("UNDER", chleba_na_vrchu)
syr.set_object_const("ABOVE", maslo)

sunka.set_object_const("ABOVE", maslo)
sunka.set_object_const("UNDER", syr)
sunka.set_object_const("ABOVE", chleba_na_spodu)
sunka.set_object_const("UNDER", chleba_na_vrchu)

papricka.set_object_const("ABOVE", vajicka)
papricka.set_object_const("ABOVE", maslo)
papricka.set_object_const("ABOVE", sunka)
papricka.set_object_const("ABOVE", syr)
papricka.set_object_const("ABOVE", chleba_na_spodu)
papricka.set_object_const("UNDER", chleba_na_vrchu)

maslo.set_object_const("ABOVE", chleba_na_spodu)
maslo.set_object_const("UNDER", syr)
maslo.set_object_const("UNDER", sunka)
maslo.set_object_const("UNDER", papricka)
maslo.set_object_const("UNDER", vajicka)

gen = Data1D([podlaha, stul, chleba_na_spodu, chleba_na_vrchu, maslo, sunka, syr, vajicka, papricka])
gen.generate_random(100)

# Kompletni hierarchie

# Castecne hierarchie
