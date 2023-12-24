import psycopg2

# from django.conf import settings --> bug...bug...bug
# need:??
#   settingd.congigure()??
#   django.setup()??
# 
# or fucking DJANGO_SETTINGS_MODULE???
import settings


conn = psycopg2.connect(
    database = settings.env('POSTGRES_DB'),
    user = settings.env('POSTGRES_USER'),
    password = settings.env('POSTGRES_PASSWORD'),
    host = settings.env('POSTGRES_HOST'),
    port = settings.env('POSTGRES_PORT')
)

def insertions_to_authors():
    print('Start insertions to `author_author`:')
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO author_author
            (name)
        VALUES
            ('Pavel'),
            ('Vika'),
            ('Yana');
        """
    )
    conn.commit()
    cursor.close()

    print('Complete')

def insertions_to_categoryes():
    print('\nStart insertions to `category_category`:')
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO category_category
            (title)
        VALUES
            ('python'),
            ('java'),
            ('ruby'),
            ('c#');
        """
    )
    conn.commit()
    cursor.close()

    print('Complete')


if __name__ == "__main__":
    insertions_to_authors()
    insertions_to_categoryes()

    conn.close()
