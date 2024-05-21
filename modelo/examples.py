from atexit import register
from unicodedata import category
from .models import Admin, Book, Category, Editorial, Student, StudentLoans
import secrets
import random

# List of book titles
titles = [
    "The Great Gatsby", "To Kill a Mockingbird", "1984", "Pride and Prejudice",
    "The Catcher in the Rye", "The Hobbit", "Harry Potter and the Sorcerer's Stone",
    "The Lord of the Rings", "The Da Vinci Code", "The Girl with the Dragon Tattoo",
    "The Hunger Games", "Gone Girl", "The Kite Runner", "Life of Pi",
    "The Fault in Our Stars", "Brave New World", "Fahrenheit 451",
    "The Alchemist", "Moby Dick", "War and Peace", "Crime and Punishment",
    "Wuthering Heights", "Jane Eyre", "The Picture of Dorian Gray",
    "The Book Thief", "Little Women", "The Chronicles of Narnia",
    "The Shining", "Dune", "The Martian", "The Handmaid's Tale",
    "Sapiens: A Brief History of Humankind", "Educated", "Becoming",
    "Thinking, Fast and Slow", "A Brief History of Time", "The Immortal Life of Henrietta Lacks",
    "Outliers", "Guns, Germs, and Steel", "The Power of Habit",
    "The Lean Startup", "The Subtle Art of Not Giving a F*ck",
    "Atomic Habits", "The Four Agreements", "How to Win Friends and Influence People",
    "Start with Why", "The Art of War", "The Road Less Traveled", "Man's Search for Meaning",
    "The 7 Habits of Highly Effective People"
]

# List of book authors
authors = [
    "F. Scott Fitzgerald", "Harper Lee", "George Orwell", "Jane Austen",
    "J.D. Salinger", "J.R.R. Tolkien", "J.K. Rowling", "Dan Brown",
    "Stieg Larsson", "Suzanne Collins", "Gillian Flynn", "Khaled Hosseini",
    "Yann Martel", "John Green", "Aldous Huxley", "Ray Bradbury",
    "Paulo Coelho", "Herman Melville", "Leo Tolstoy", "Fyodor Dostoevsky",
    "Emily Brontë", "Charlotte Brontë", "Oscar Wilde", "Markus Zusak",
    "Louisa May Alcott", "C.S. Lewis", "Stephen King", "Frank Herbert",
    "Andy Weir", "Margaret Atwood", "Yuval Noah Harari", "Tara Westover",
    "Michelle Obama", "Daniel Kahneman", "Stephen Hawking", "Rebecca Skloot",
    "Malcolm Gladwell", "Jared Diamond", "Charles Duhigg", "Eric Ries",
    "Mark Manson", "James Clear", "Don Miguel Ruiz", "Dale Carnegie",
    "Simon Sinek", "Sun Tzu", "M. Scott Peck", "Viktor E. Frankl",
    "Stephen R. Covey", "Robert Kiyosaki"
]

# List of book categories
categories = [
    "Classic Literature", "Modern Fiction", "Science Fiction", "Fantasy",
    "Mystery", "Thriller", "Young Adult", "Historical Fiction",
    "Romance", "Biography", "Self-Help", "Science", "History",
    "Philosophy", "Psychology", "Business", "Economics", "Health",
    "Wellness", "Religion", "Spirituality", "Adventure", "Horror",
    "Graphic Novel", "Poetry", "Memoir", "Cookbook", "Travel",
    "Technology", "Art", "Music", "Education", "Politics", "Sociology",
    "Anthropology", "Sports", "True Crime", "Environment",
    "Nature", "Parenting", "Relationships", "Law", "Engineering",
    "Mathematics", "Programming", "Fantasy Romance", "Dystopian",
    "Epics", "Short Stories", "Computer Science"
]

# List of editorials
editorials = [
    "Penguin Random House", "HarperCollins", "Simon & Schuster", "Hachette Book Group",
    "Macmillan Publishers", "Scholastic", "Bloomsbury", "Houghton Mifflin Harcourt",
    "Candlewick Press", "Farrar, Straus and Giroux", "Little, Brown and Company",
    "Crown Publishing Group", "Doubleday", "Knopf", "St. Martin's Press",
    "Algonquin Books", "Grove Atlantic", "W.W. Norton & Company", "Tor Books",
    "Harlequin", "Kensington Publishing", "Graywolf Press", "Beacon Press",
    "Workman Publishing", "Chronicle Books", "Wiley", "Pearson", "Oxford University Press",
    "Cambridge University Press", "University of Chicago Press", "MIT Press",
    "Stanford University Press", "Yale University Press", "New Directions",
    "Melville House", "Tin House", "Counterpoint Press", "City Lights Publishers",
    "Verso Books", "Seven Stories Press", "Haymarket Books", "Basic Books",
    "Nation Books", "PublicAffairs", "Regnery Publishing", "Tyndale House Publishers",
    "Zondervan", "NavPress", "WaterBrook", "Crossway"
]

# List of first names
first_names = [
    "Emma", "Liam", "Olivia", "Noah", "Ava", "Elijah", "Sophia", "James",
    "Isabella", "Benjamin", "Mia", "Lucas", "Charlotte", "Henry", "Amelia",
    "Alexander", "Harper", "Sebastian", "Evelyn", "Jackson", "Aria", "Daniel",
    "Ella", "Matthew", "Avery", "Samuel", "Scarlett", "David", "Grace", "Joseph",
    "Zoe", "John", "Hannah", "Gabriel", "Lily", "Carter", "Victoria", "Wyatt",
    "Chloe", "Julian", "Penelope", "Owen", "Layla", "Levi", "Mila", "Isaac",
    "Nora", "Anthony", "Riley", "Dylan"
]

# List of last names
last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis",
    "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
    "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson",
    "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker",
    "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill",
    "Flores", "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell",
    "Mitchell", "Carter", "Garcia"
]

# List of emails with the same domain
emails = [
    "emma.smith@example.com", "liam.johnson@example.com", "olivia.williams@example.com",
    "noah.brown@example.com", "ava.jones@example.com", "elijah.garcia@example.com",
    "sophia.miller@example.com", "james.davis@example.com", "isabella.rodriguez@example.com",
    "benjamin.martinez@example.com", "mia.hernandez@example.com", "lucas.lopez@example.com",
    "charlotte.gonzalez@example.com", "henry.wilson@example.com", "amelia.anderson@example.com",
    "alexander.thomas@example.com", "harper.taylor@example.com", "sebastian.moore@example.com",
    "evelyn.jackson@example.com", "jackson.martin@example.com", "aria.lee@example.com",
    "daniel.perez@example.com", "ella.thompson@example.com", "matthew.white@example.com",
    "avery.harris@example.com", "samuel.sanchez@example.com", "scarlett.clark@example.com",
    "david.ramirez@example.com", "grace.lewis@example.com", "joseph.robinson@example.com",
    "zoe.walker@example.com", "john.young@example.com", "hannah.allen@example.com",
    "gabriel.king@example.com", "lily.wright@example.com", "carter.scott@example.com",
    "victoria.torres@example.com", "wyatt.nguyen@example.com", "chloe.hill@example.com",
    "julian.flores@example.com", "penelope.green@example.com", "owen.adams@example.com",
    "layla.nelson@example.com", "levi.baker@example.com", "mila.hall@example.com",
    "isaac.rivera@example.com", "nora.campbell@example.com", "anthony.mitchell@example.com",
    "riley.carter@example.com", "dylan.smith@example.com"
]


def fill_admin():
    t1 = secrets.token_hex(25)
    t2 = secrets.token_hex(25)
    t3 = secrets.token_hex(25)
    t4 = secrets.token_hex(25)
    t5 = secrets.token_hex(25)
    Admin.objects.create(register=120012345,
                         first_name='Juan', last_name='Sanchez', e_mail='example@adm.buas.mx', token=t1)
    Admin.objects.create(register=120012346,
                         first_name='Olivia', last_name='Lopez', e_mail='example@adm.buas.mx', token=t2)
    Admin.objects.create(register=120012347,
                         first_name='Pablo', last_name='Castillo', e_mail='example@adm.buas.mx', token=t3)
    Admin.objects.create(register=120012348,
                         first_name='Pedro', last_name='Martinez', e_mail='example@adm.buas.mx', token=t4)
    Admin.objects.create(register=120012349,
                         first_name='Maria', last_name='Juarez', e_mail='example@adm.buas.mx', token=t5)


def fill_editorial():
    for e in editorials:
        Editorial.objects.create(name=e)


def fill_category():
    for c in categories:
        Category.objects.create(name=c)


def fill_book():
    for _ in range(100):
        Book.objects.create(title=titles[random.randrange(50)], author=authors[random.randrange(
            50)], editorial=Editorial.objects.get(id=random.randrange(1, 51)), category=Category.objects.get(id=random.randrange(1, 51)))


def fill_students():
    for i in range(100):
        register_aux = random.randrange(201700000, 202499999)
        token_aux = secrets.token_hex(20)
        Student.objects.create(register=register_aux, first_name=first_names[random.randrange(
            50)], last_name=last_names[random.randrange(50)], e_mail=emails[random.randrange(50)], loans_id=StudentLoans.objects.create().id, token=token_aux)
