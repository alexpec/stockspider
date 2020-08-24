docker build -t stockspider:latest .
docker run -v $PWD:/app/StockSpider StockSpider:latest /bin/bash
