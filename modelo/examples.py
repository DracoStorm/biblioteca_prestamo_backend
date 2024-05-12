from .models import Admin, Category, Editorial
import secrets


def fill_category(categories: list[str]):
    for c in categories:
        Category.objects.create(name=c)


def fill_editorial(editorials: list[str]):
    for e in editorials:
        Editorial.objects.create(name=e)


def fill_admin():
    t1 = secrets.token_hex(25)
    t2 = secrets.token_hex(25)
    t3 = secrets.token_hex(25)
    t4 = secrets.token_hex(25)
    t5 = secrets.token_hex(25)
    Admin.objects.create(register=120012345,
                         first_name='Juan', last_name='Sánchez', e_mail='example@mail.edu.mx', token=t1)
    Admin.objects.create(register=120012346,
                         first_name='Olivia', last_name='López', e_mail='example@mail.edu.mx', token=t2)
    Admin.objects.create(register=120012347,
                         first_name='Pablo', last_name='Castillo', e_mail='example@mail.edu.mx', token=t3)
    Admin.objects.create(register=120012348,
                         first_name='Pedro', last_name='Martínez', e_mail='example@mail.edu.mx', token=t4)
    Admin.objects.create(register=120012349,
                         first_name='Maria', last_name='Juárez', e_mail='example@mail.edu.mx', token=t5)


cats = ['Action',
        'Adventure',
        'Alternate History',
        'Anthology',
        'Bildungsroman',
        "Children's",
        'Comedy',
        'Commercial Fiction',
        'Crime',
        'Drama',
        'Dystopian',
        'Espionage',
        'Fairy Tale',
        'Fantasy',
        'Gothic',
        'Graphic Novel',
        'Historical Fiction',
        'Horror',
        'Inspirational',
        'LGBTQ+',
        'Literary Fiction',
        'Magical Realism',
        'Mystery',
        'Mythology',
        'Picaresque',
        'Poetry',
        'Political Fiction',
        'Romance',
        'Satire',
        'Science Fiction',
        'Short Story',
        'Southern Gothic',
        'Speculative Fiction',
        'Suspense',
        'Thriller',
        'Swashbuckler',
        'Urban Fantasy',
        'War',
        'Western',
        'Young Adult',
        'Biography',
        'Business and Economics',
        'Cookbooks',
        'Education',
        'Health and Wellness',
        'History',
        'Memoir',
        'Philosophy',
        'Political Science',
        'Psychology',
        'Religion and Spirituality',
        'Science',
        'Self-Help',
        'Social Sciences',
        'True Crime',
        'Technology',
        'Travel',
        'Historical Fiction and Romance',
        'Science Fiction and Thriller',
        'Fantasy and Mystery',
        'Horror and Psychological Thriller',
        'Young Adult and Dystopian']

edis = ['Alpha Book Publisher ',
        'CIDCLI ',
        'Editorial Almadía ',
        'Ink it',
        'Editorial Sexto Piso',
        'Trice Ediciones ',
        'Ediciones Tecolote, S.A. de C.V. ',
        'Cámara Nacional de la Industria Editorial Mexicana. CANIEM',
        'La Cifra Editorial ',
        'Editorial Paraíso Perdido',
        'Petra Ediciones Sa De Cv ',
        'Librería Porrúa ',
        'Editorial Macmillan de Mexico',
        'Ediciones Era',
        'Artes de Mexico ',
        'Ediciones AKAL s.a.',
        'Ediciones Larousse S.A. de C.V.',
        'Editorial Turner México',
        'Editorial Hiperlibro ',
        'Revista Contenido',
        'Tirant lo Blanch México S. de R.L. de C.V.',
        'Aqua Ediciones ',
        'Editorial Fontamara ',
        'Lexus Editores de México',
        'Almacen Ek Editores ',
        'Editorial Terracota, SA de CV',
        'Stanford Publishing ',
        'Editorial Ovaciones Sa De Cv',
        'Editorial Ebica ',
        'Editorial Alba, S.A. de C.V.',
        'Narra',
        'Editorial El Dragón Rojo',
        'Hazme Cuento',
        'Grupo Editorial Disal, S.A. de C.V.',
        'Fredo Velazquez (Cantera Rosa Ediciones)',
        'Montenegro Editores, S.A. de C.V.',
        'Ediciones Eón',
        'CAPE Books Publishing Services',
        'Editorial Everest Mexicana',
        'La Emboscadura México',
        'Publicaciones de las Montañas De México',
        'Editorial Shem Tob',
        'ONE Editorial ',
        'Alboroto Ediciones ',
        'Grupo Editorial Endira México, SA de CV',
        'Editorial 3 abejas',
        'UMBRAL EDITORIAL SA DE CV',
        'TOTAL BOOK',
        'Fernández editores',
        'Editorial Valegra, S.A. de C.V.']
