from database.connection import get_db_connection

class Magazine:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category

    def __repr__(self):
        return f'<Magazine {self.name}>'

    @staticmethod
    def delete_magazine(magazine_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM articles WHERE magazine_id = ?', (magazine_id,))
        cursor.execute('DELETE FROM magazines WHERE id = ?', (magazine_id,))
        conn.commit()
        conn.close()
