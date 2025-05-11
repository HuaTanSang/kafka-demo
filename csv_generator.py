import pandas as pd 
import numpy as np 
import random 

from datetime import datetime 

num_rows = 100

# Tạo dữ liệu
data = {
    "datetime": [datetime.now().strftime("%Y-%m-%d %H:%M:%S") for _ in range(num_rows)],
    "random_number": [random.randint(1, 100) for _ in range(num_rows)]
}

# Tạo DataFrame từ dữ liệu
df = pd.DataFrame(data)

# Ghi DataFrame vào file CSV
df.to_csv('data.csv', index=False)

print("File CSV đã được tạo thành công!")
