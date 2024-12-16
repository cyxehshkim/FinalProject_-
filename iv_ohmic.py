import pandas as pd
import matplotlib.pyplot as plt

# 데이터 불러오기
file_path = r'C:\Users\user\Desktop\CPS\Gr_4P_RT_without annaling.csv'  # r을 추가하여 raw string으로 처리
# 또는 슬래시 사용
# file_path = 'C:/Users/user/Desktop/CPS/Gr_4P_RT_without annaling.csv'

data = pd.read_csv(file_path)

# 필요 없는 열 제거
data_cleaned = data.loc[:, ~data.columns.str.contains('^Unnamed')]

# V1 vs Current
plt.figure(figsize=(8, 6))
plt.scatter(data_cleaned['V1'], data_cleaned['current'], color='blue', alpha=0.7)
plt.title('V1 vs Current')
plt.xlabel('V1 (Voltage)')
plt.ylabel('Current (A)')
plt.grid(True)
plt.show()

# V2 vs Current
plt.figure(figsize=(8, 6))
plt.scatter(data_cleaned['V2'], data_cleaned['current'], color='green', alpha=0.7)
plt.title('V2 vs Current')
plt.xlabel('V2 (Voltage)')
plt.ylabel('Current (A)')
plt.grid(True)
plt.show()

# V1 vs V2
plt.figure(figsize=(8, 6))
plt.scatter(data_cleaned['V1'], data_cleaned['V2'], color='purple', alpha=0.7)
plt.title('V1 vs V2')
plt.xlabel('V1 (Voltage)')
plt.ylabel('V2 (Voltage)')
plt.grid(True)
plt.show()

