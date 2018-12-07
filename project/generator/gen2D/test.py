from project.generator.gen2D.Object2D import Object2D
from project.generator.gen2D.Relation import Relation, RelationType
from project.generator.gen2D.Space2D import Space2D

stul1 = Object2D("stul1")
stul2 = Object2D("stul2")
zidle1 = Object2D("zidle1")
zidle2 = Object2D("zidle2")
zidle3 = Object2D("zidle3")
zidle4 = Object2D("zidle4")
stred = Object2D("stred")
stolicka = Object2D("stolicka")
klavir = Object2D("klavir")
skrin = Object2D("skrin")
zedW = Object2D("zedW")
zedE = Object2D("zedE")
zedS = Object2D("zedS")
zedN = Object2D("zedN")
koberec = Object2D("koberec")

space1 = Space2D()
space1.add_relation(Relation(stul1, RelationType.IN, stred))
space1.add_relation(Relation(klavir, RelationType.IN_FRONT, zedN))
space1.add_relation(Relation(stolicka, RelationType.IN_FRONT, klavir))
space1.add_relation(Relation(stolicka, RelationType.IN, stred))
space1.add_relation(Relation(skrin, RelationType.RIGHT, klavir))

space2 = Space2D()
space2.add_relation(Relation(stul1, RelationType.LEFT, klavir))
space2.add_relation(Relation(zidle1, RelationType.IS_BY_LEFT, stul1))
space2.add_relation(Relation(zidle1, RelationType.IN_FRONT, klavir))
