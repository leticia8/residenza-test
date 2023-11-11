# Generated by Django 3.2.2 on 2021-08-22 15:27

from django.db import migrations

DEFAULT_NEIGH = (
    (1, 'Ciudad Vieja'),
    (2, 'Centro'),
    (3, 'Barrio Sur'),
    (4, 'Cordón'),
    (5, 'Palermo'),
    (6, 'Parque Rodó'),
    (7, 'Punta Carretas'),
    (8, 'Pocitos'),
    (9, 'Buceo'),
    (10, 'Parque Batlle, Villa Dolores'),
    (11, 'Malvín'),
    (12, 'Malvín Norte'),
    (13, 'Punta Gorda'),
    (14, 'Carrasco'),
    (15, 'Carrasco Norte'),
    (16, 'Bañados de Carrasco'),
    (17, 'Maroñas, Parque Guaraní'),
    (18, 'Flor de Maroñas'),
    (19, 'Las Canteras'),
    (20, 'Punta Rieles, Bella Italia'),
    (21, 'Jardines del Hipódromo'),
    (22, 'Ituzaingó'),
    (23, 'Unión'),
    (24, 'Villa Española'),
    (25, 'Mercado Modelo, Bolívar'),
    (26, 'Castro, P. Castellanos'),
    (27, 'Cerrito'),
    (28, 'Las Acacias'),
    (29, 'Aires Puros'),
    (30, 'Casavalle'),
    (31, 'Piedras Blancas'),
    (32, 'Manga, Toledo Chico'),
    (33, 'Paso de las Duranas'),
    (34, 'Peñarol, Lavalleja'),
    (35, 'Cerro'),
    (36, 'Casabó, Pajas Blancas'),
    (37, 'La Paloma, Tomkinson'),
    (38, 'La Teja'),
    (39, 'Prado, Nueva Savona'),
    (40, 'Capurro, Bella Vista'),
    (41, 'Aguada'),
    (42, 'Reducto'),
    (43, 'Atahualpa'),
    (44, 'Jacinto Vera'),
    (45, 'La Figurita'),
    (46, 'Larrañaga'),
    (47, 'La Blanqueada'),
    (48, 'Villa Muñoz, Retiro'),
    (49, 'La Comercial'),
    (50, 'Tres Cruces'),
    (51, 'Brazo Oriental'),
    (52, 'Sayago'),
    (53, 'Conciliación'),
    (54, 'Belvedere'),
    (55, 'Nuevo París'),
    (56, 'Tres Ombúes, Victoria'),
    (57, 'Paso de la Arena'),
    (58, 'Colón Sureste, Abayubá'),
    (59, 'Colón Centro y Noroeste'),
    (60, 'Lezica, Melilla'),
    (61, 'Villa García, Manga Rural'),
    (62, 'Manga'),
)


def add_neigh_codes(apps, schema_editor):
    ZoneCodes = apps.get_model('common', 'Zone')
    for id, description in DEFAULT_NEIGH:
        neighb = ZoneCodes(id=id,
                           description=description)
        neighb.save()


DEFAULT_DPTO = (
    (1, 'Montevideo'),
    (2, 'Artigas'),
    (3, 'Canelones'),
    (4, 'Cerro Largo'),
    (5, 'Colonia'),
    (6, 'Durazno'),
    (7, 'Flores'),
    (8, 'Florida'),
    (9, 'Lavalleja'),
    (10, 'Maldonado'),
    (11, 'Paysandú'),
    (12, 'Río Negro'),
    (13, 'Rivera'),
    (14, 'Rocha'),
    (15, 'Salto'),
    (16, 'San José'),
    (17, 'Soriano'),
    (18, 'Tacuarembó'),
    (19, 'Treinta y tres'),
)


def add_dpto_codes(apps, schema_editor):
    DptoCodes = apps.get_model('common', 'Department')
    for id, description in DEFAULT_DPTO:
        dpto_cod = DptoCodes(id=id, description=description)
        dpto_cod.save()


DEFAULT_SEX = (
    (0, 'Prefiere no decir'),
    (1, 'Hombre'),
    (2, 'Mujer'),
)


def add_sex_codes(apps, schema_editor):
    SexCodes = apps.get_model('common', 'Sex')
    for id, description in DEFAULT_SEX:
        sex_cod = SexCodes(id=id, description=description)
        sex_cod.save()


DEFAULT_PAYMETH = (
    (1, 'Efectivo'),
    (2, 'Redes de cobranza'),
    (3, 'Débito'),
    (4, 'Crédito'),
    (5, 'Depósito bancario'),
    (6, 'Otro'),
)


def add_payment_codes(apps, schema_editor):
    StateCodes = apps.get_model('common', 'PaymentMethod')
    for id, description in DEFAULT_PAYMETH:
        paymentsmet = StateCodes(id=id, description=description)
        paymentsmet.save()

DEFAULT_SERVICE_CODES = (
    (1, 'Lavandería'),
    (2, 'Desayuno'),
    (3, 'Almuerzo'),
    (4, 'Alquiler bicicletas'),
    (5, 'Impresiones'),
    (6, 'Servicio de correo'),
)


def add_servicetype_codes(apps, schema_editor):
    ServiceCodes = apps.get_model('common', 'ServiceType')
    for id, description in DEFAULT_SERVICE_CODES:
        serv_cod = ServiceCodes(id=id, description=description)
        serv_cod.save()


DEFAULT_ADDRESS = (
    (25, "ALBERTO LASPLACES", 1620, None,
     "POINT (-56.1412888363647 -34.8968265319322)", 10),
    (9, "AVENIDA GONZALO RAMIREZ", 1926, None,
     "POINT (-56.1732471467819 -34.9119640844967)", 6),
    (12, "AVENIDA DIECIOCHO DE JULIO", 1824, None,
     "POINT (-56.1767115015472 -34.9022949556816)", 4),
    (36, "AVENIDA DIECIOCHO DE JULIO", 1772, None,
     "POINT(-56.17780163655648 -34.902896287649945)", 4),
    (3, "AVENIDA GENERAL EUGENIO GARZON", 780, None,
     "POINT (-56.2215081398352 -34.8376994454414)", 52),
    (24, "AVENIDA GENERAL FLORES", 2124, None,
     "POINT (-56.1858669452376 -34.8883620805339)", 41),
    (21, "AVENIDA GENERAL FLORES", 2125, None,
     "POINT (-56.1860572874363 -34.8882919382333)", 41),
    (17, "AVENIDA INGENIERO LUIS PONCE", 1307, None,
     "POINT (-56.1626210830138 -34.9042654457688)", 8),
    (18, "AVENIDA JULIO HERRERA Y REISSIG", 565, None,
     "POINT (-56.1659475341075 -34.9182276360813)", 7),
    (27, "AVENIDA OCHO DE OCTUBRE", 2738, None,
     "POINT (-56.1593137908751 -34.8885702592019)", 47),
    (26, "AVENIDA OCHO DE OCTUBRE", 2882, None,
     "POINT (-56.1570194476652 -34.8858207851111)", 47),
    (43, "AVENIDA URUGUAY", 1225, None,
     "POINT (-56.1900248828786 -34.9030491630763)", 2),
    (14, "AVENIDA URUGUAY", 1695, None,
     "POINT (-56.18130297312405 -34.900513299378545)", 2),
    (42, "COLONIA", 1870, None, "POINT (-56.1763324735917 -34.9009567505298)", 4),
    (10, "CONSTITUYENTE", 1502, None, "POINT (-56.1830368625465 -34.9058805218)", 4),
    (31, "DOCTOR PRUDENCIO DE PENA", 2544, None,
     "POINT (-56.1603452697535 -34.8978360435264)", 10),
    (44, "ESTERO BELLACO", 2717, None,
     "POINT (-56.1597595377221 -34.8876332005302)", 47),
    (22, "GENERAL LAS HERAS", 1925, None,
     "POINT (-56.1505690571374 -34.8902743385909)", 10),
    (6, "IGUA", 4225, None,
     "POINT (-56.1158899723573 -34.8818540901781)", 12),
    (39, "JUAN RAMON GOMEZ", 2706, None,
     "POINT (-56.1616390793711 -34.8879015715687)", 47),
    (34, "LORD PONSOMBY", 2530, None,
     "POINT (-56.1609003314515 -34.8967974817524)", 10),
    (11, "LORD PONSOMBY", 2506, None,
     "POINT (-56.1612834722173 -34.8969079725758)", 10),
    (16, "SAN SALVADOR", 1944, None, "POINT (-56.1730528198107 -34.9111937961276)", 5),
    (29, "SORIANO", 959, None, "POINT (-56.195460685179 -34.9080343979248)", 2),
    (30, "VEINTIUNO DE SETIEMBRE", 2741, None,
     "POINT (-56.1577264560965 -34.9171682000714)", 7),
    (28, "ZELMAR MICHELINI", 1220, None,
     "POINT (-56.189882922555 -34.9083090715178)", 2),
    (32, "AVENIDA ITALIA", 6201, None,
     "POINT (-56.07654598607914 -34.877807913937055)", 15),
    (13, "AVENIDA ITALIA", 0, None,
     "POINT(-56.15435515499875 -34.885153212063905)", 10),
    (20, "COMANDANTE BRAGA", 2715, None,
     "POINT (-56.15841991766162 -34.88667345738665)", 47),
    (8, "CORNELIO CANTERA", 2728, None,
     "POINT (-56.158505275212335 -34.88899156846525)", 47),
    (1, "JOSÉ BRITO FORESTI", 2952, None,
     "POINT (-56.15315730219931 -34.88852506855643)", 47),
    (2, "BOULEVARD GENERAL ESPAÑA", 2627, None,
     "POINT(-56.15694284637613 -34.91264792847505)", 8),
    (4, "BOULEVARD GENERAL ESPAÑA", 2633, None,
     "POINT(-56.15673947336321 -34.912786230933314)", 8),
    (5, "BOULEVARD GENERAL JOSE GERVASIO ARTIGAS", 1031,
     None, "POINT (-56.1635413442206 -34.9099897985013)", 6),
    (7, "LUIS ALBERTO DE HERRERA", 2890, None,
     "POINT(-56.15757948882709 -34.87591075359517)", 25),
    (15, "PRUDENCIO DE PENA", 2514, None,
     "POINT(-56.161060073363544 -34.89734939077657)", 10),
    (17, "AVENIDA INGENIERO LUIS P PONCE", 1307, None,
     "POINT(-56.15757948882709 -34.87591075359517)", 8),
    (19, "CUAREIM", 1451, None, "POINT(-56.19077627336335 -34.90343790132502)", 2),
    (23, "TRISTÁN NARVAJA", 1674, None,
     "POINT(-56.17848991569245 -34.899353594361266)", 4),
    (33, "AVENIDA URUGUAY", 1185, None,
     "POINT(-56.190949746376496 -34.90277239064764)", 2),
    (35, "AVENIDA RICALDONI", 2890, None,
     "POINT(-56.152576830688986 -34.89221879499177)", 10),
    (37, "JOSE MARTÍ", 3328, None, "POINT(-56.14998384255499 -34.91178158633729)", 8),
    (38, "AVENIDA DIECIOCHO DE JULIO", 1772, None,
     "POINT(-56.17772666894804 -34.902644259759896)", 4),
    (40, "RAMBLA EUSKAL ERRÍA", 4101, None,
     "POINT(-56.12030467318107 -34.88302569343949)", 12),
    (41, "PARQUE JOSÉ BATLLE Y ORDÓÑEZ", 0, None,
     "POINT(-56.15626773346382 -34.89502825205433)", 10)

)


def add_address_codes(apps, schema_editor):
    Address = apps.get_model('common', 'Address')
    for id, street, number, apartment, location, zone_id in DEFAULT_ADDRESS:
        address = Address(
            id=id, street=street, number=number, apartment=apartment, location=location, zone_id=zone_id)
        address.save()


DEFAULT_INSTITUTES = (
    (1, 'BUSINESS SCHOOL – UNIVERSIDAD CATÓLICA', 1),
    (2, 'FACULTAD DE ADMINISTRACIÓN Y CIENCIAS SOCIALES – ORT', 2),
    (3, 'FACULTAD DE AGRONOMIA – UDELAR', 3),
    (4, 'FACULTAD DE ARQUITECTURA – ORT', 4),
    (5, 'FACULTAD DE ARQUITECTURA, DISEÑO Y URBANISMO – UDELAR', 5),
    (6, 'FACULTAD DE CIENCIAS – UDELAR', 6),
    (7, 'FACULTAD DE CIENCIAS AGRARIAS – UNIVERSIDAD DE LA EMPRESA', 7),
    (8, 'FACULTAD DE CIENCIAS DE LA SALUD – UNIVERSIDAD CATOLICA', 8),
    (9, 'FACULTAD DE CIENCIAS ECONOMICAS Y DE ADMINISTRACION – UDELAR', 9),
    (10, 'FACULTAD DE CIENCIAS SOCIALES – UDELAR', 10),
    (11, 'FACULTAD DE DERECHO - UNIVERSIDAD DE MONTEVIDEO', 11),
    (12, 'FACULTAD DE DERECHO – UDELAR', 12),
    (13, 'FACULTAD DE ENFERMERIA – UDELAR', 13),
    (14, 'FACULTAD DE HUMANIDADES Y CIENCIAS DE LA EDUCACION – UDELAR', 14),
    (15, 'FACULTAD DE HUMANIDADES Y EDUCACIÓN – UNIVERSIDAD DE MONTEVIDEO', 15),
    (16, 'FACULTAD DE INFORMACION Y COMUNICACION – UDELAR', 16),
    (17, 'FACULTAD DE INGENIERÍA - UNIVERSIDAD DE MONTEVIDEO', 17),
    (18, 'FACULTAD DE INGENIERIA – UDELAR', 18),
    (19, 'FACULTAD DE INGENIERÍA, ESCUELA DE DISEÑO E INSTITUTO DE EDUCACIÓN – ORT', 19),
    (20, 'FACULTAD DE INGENIERÍAS Y TECNOLOGÍAS Y CIENCIAS DE LA SALUD – UNIVERSIDAD CATÓLICA', 20),
    (21, 'FACULTAD DE MEDICINA – UDELAR', 21),
    (22, 'FACULTAD DE ODONTOLOGIA – UDELAR', 22),
    (23, 'FACULTAD DE PSICOLOGÍA – UDELAR', 23),
    (24, 'FACULTAD DE QUIMICA – UDELAR', 24),
    (25, 'FACULTAD DE VETERINARIA – UDELAR', 25),
    (26, 'FACULTAD LATINOAMERICANA DE CIENCIAS SOCIALES (FLACSO)', 26),
    (27, 'UNIVERSIDAD CATOLICA DEL URUGUAY – SEDE CENTRAL', 27),
    (28, 'UNIVERSIDAD CENTRO LATINOAMERICANO DE ECONOMIA HUMANA', 28),
    (29, 'UNIVERSIDAD DE LA EMPRESA – SEDE CENTRO', 29),
    (30, 'UNIVERSIDAD DE LA EMPRESA – SEDE POCITOS', 30),
    (31, 'UNIVERSIDAD DE MONTEVIDEO – SEDE CENTRAL', 31),
    (32, 'UNIVERSIDAD TECNOLOGICA – UTEC', 32),
    (33, 'FACULTAD DE COMUNICACIÓN Y DISEÑO – ORT', 33),
    (34, 'ESCUELA DE NEGOCIOS – UNIVERSIDAD DE MONTEVIDEO', 34),
    (35, 'ESCUELA DE NUTRICIÓN – UDELAR', 35),
    (36, 'ESCUELA UNIVERSITARIA DE MÚSICA – UDELAR', 36),
    (37, 'INSTITUTO ESCUELA NACIONAL DE BELLAS ARTES – UDELAR', 37),
    (38, 'INSTITUTO ESCUELA NACIONAL DE BELLAS ARTES – UDELAR – ANEXO CENTRO', 38),
    (39, 'INSTITUTO METODISTA UNIVERSITARIO CRANDON (IMUC)', 39),
    (40, 'INSTITUTO SUPERIOR DE EDUCACIÓN FÍSICA – SEDE MALVÍN NORTE – UDELAR', 40),
    (41, 'INSTITUTO SUPERIOR DE EDUCACIÓN FÍSICA – UDELAR', 41),
    (42, 'INSTITUTO UNIVERSITARIO ASOC. CRISTIANA DE JOVENES', 42),
    (43, 'INSTITUTO UNIVERSITARIO AUTONOMO DEL SUR', 43),
    (44, 'INSTITUTO UNIVERSITARIO MONSEÑOR MARIANO SOLER', 44)
)


def add_institute_codes(apps, schema_editor):
    InstituteCodes = apps.get_model('common', 'Institute')
    for id, description, contact_id in DEFAULT_INSTITUTES:
        institutedesc = InstituteCodes(
            id=id, description=description, contact_id=contact_id)
        institutedesc.save()



class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_neigh_codes),
        migrations.RunPython(add_dpto_codes),
        migrations.RunPython(add_sex_codes),
        migrations.RunPython(add_servicetype_codes),
        migrations.RunPython(add_payment_codes),
        migrations.RunPython(add_address_codes),
        migrations.RunPython(add_institute_codes),

    ]