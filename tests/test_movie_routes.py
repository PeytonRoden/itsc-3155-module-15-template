from flask.testing import FlaskClient
from src.models import Movie, db
from app import app
from tests.utils import refresh_db, create_movie


def test_get_all_movies(test_app: FlaskClient):
    #set up
    refresh_db()
    test_movie = create_movie()

    #run action
    res = test_app.get('/movies')
    page_data: str = res.data.decode()

    #assserts
    assert res.status_code == 200
    assert f'<td>Christopher Nolan</td>' in page_data