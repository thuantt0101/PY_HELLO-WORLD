import datetime
from pathlib import Path
from unittest.mock import MagicMock
import matplotlib.pyplot

from app import App

BASE_DIR = Path(__file__).resolve(strict=True).parent

def test_read():


    # app = App()
    # for key, value in app.read(file_name=Path(BASE_DIR).joinpath('london.csv')).items():
    #     assert datetime.datetime.fromisoformat(key) # moi key la mot chuoi ngay gio duoc dinh dang ISO 8601
    #     assert value - 0 == value # mọi gia tri deu la so

    hour = datetime.datetime.now().isoformat()
    temperature = 14.52
    temperature_by_hour = {hour:temperature}

    data_source = MagicMock()
    data_source.read.return_value = temperature_by_hour
    
    # Lợi ích đầu tiên của Dependency Injection : dễ dàng test  hơn vì chún ta Tiêm vào các phụ thuộc cơ bản 
    app = App(
        data_source = data_source,
        plot=MagicMock()
    )
    assert app.read(file_name='something.csv') == temperature_by_hour


def test_draw(monkeypatch):
    plot_mock = MagicMock()

    app = App(
        data_source=MagicMock,
        plot=plot_mock
    )
    
    hour = datetime.datetime.now()
    iso_hour = hour.isoformat()
    temperature = 14.52
    temperature_by_hour = {iso_hour:temperature}

    app.draw(temperature_by_hour)
    plot_mock.draw.assert_called_with([hour], [temperature])

def test_configure():
    app = App.configure(
         'config.json'
    )

    assert isinstance(app, App)






