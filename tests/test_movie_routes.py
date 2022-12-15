from flask.testing import FlaskClient
from src.models import Movie, db
from app import app


def test_get_all_movies(test_app: FlaskClient):
    with app.app_context():
        test_movie = Movie(title = "the dark knight", director ="Chris", rating = 5)
        db.session.add(test_movie)
        db.session.commit()


        res = test_app.get('/movies')
        page_data = res.data

        assert res.status_code == 200
        assert b'<td>Chris</td>' in page_data