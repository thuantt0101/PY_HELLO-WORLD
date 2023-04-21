import csv
import datetime
from pathlib import Path 
import matplotlib.pyplot
import matplotlib.dates
import json
    
BASE_DIR = Path(__file__).resolve(strict=True).parent

class App:

    # Constructor injection
    def __init__(self, data_source, plot):
        self.data_source  = data_source
        self.plot = plot

    def read(self, **kwargs):
        return self.data_source.read(**kwargs)
    
    def draw(self, temperatures_by_hour):
        dates = []
        temperatures = []
        
        for date, temperature in temperatures_by_hour.items():
            dates.append(datetime.datetime.fromisoformat(date))
            temperatures.append(temperature)

        self.plot.draw(dates, temperatures)


    @classmethod
    def configure(cls, filename):
        with open(filename) as file:
            config = json.load(file)

        # __import__ được sử dụng để nhập động các module    
        # Ví dụ :   config['data_source']['name']) = urban_climate_csv
                    # -->  urban_climate_csv.DataSource()  đây là tạo datasource 1 cách động.
        data_source = __import__(config['data_source']['name']).DataSource()
        plot = __import__(config['plot']['name']).Plot()

        return cls(data_source, plot)


# đưa nguồn dữ liệu của mình vào App để tạo instance
if __name__ == '__main__':
    import sys
    # from urban_climate_csv import DataSource
    # Lợi ích thứ 2 của Dependency Inject : Mở rộng mà đơn giản hơn nhiều. 
        # 1. Các thử nghiệm hiện tại không thay đổi
        # 2. Viết một testcase cho một nguồn dữ liệu mới thật đơn giản.
        # 3. Việc triển khai giao diện cho một nguồn dữ liệu mới khá đơn giản ( bạn chỉ cần biết hình dạng của dữ liệu )
        # 4. Chúng tôi không thể thực hiện bất cứ thay đổi nào đối với class App.
        # ==> giờ chúng ta có thể mở rộng cơ sở code bằng các bước đơn giản và có thể dự đoán được mà không cần phải
        #       chạm vào các testcase có sẵn hoặc thay đổi ứng dụng chính.
        #       Giờ đây  bạn có thể yêu cầu nhà phát triển chỉ tập trung vào việc thêm các nguồn dữ liệu mới mà họ không cần
        #       phải hiểu  hoặc có ngữ cảnh trên ứng dụng chính.
    # from open_weather_json import DataSource # python app.py moscow.json
    # from matplotlib_plot import Plot
    # from plotly_plot import Plot
    
    config_file = sys.argv[1]
    file_name = sys.argv[2]
    
    app = App.configure(config_file)
    temperatures_by_hour = app.read(file_name=file_name)
    app.draw(temperatures_by_hour)

    # Run : python app.py moscow.json
    # Run nếu dùng config : python app.py config.json london.csv
    


