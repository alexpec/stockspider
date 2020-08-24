FROM python:3.8
WORKDIR /app/StockSpider
COPY requirements.txt /app/StockSpider
COPY TimeSeries /app/StockSpider/TimeSeries
RUN pip3 install --upgrade pip -r requirements.txt
COPY . /app/StockSpider
EXPOSE 8000
CMD ["/bin/bash"]
