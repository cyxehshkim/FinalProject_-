import pandas as pd
import matplotlib.pyplot as plt

# 파일 불러오기
file_8e_2 = r'C:\Users\user\Desktop\CPS\Gr_transistor_bc pair_8e-2 mbar.csv'
file_6e_2 = r'C:\Users\user\Desktop\CPS\Gr_transistor_bc pair_6e-2 mbar.csv'
file_4e_3 = r'C:\Users\user\Desktop\CPS\Gr_transistor_bc pair_4e-3 mbar.csv'
file_1e_3 = r'C:\Users\user\Desktop\CPS\Gr_transistor_bc pair_1e-3 mbar.csv'
file_4e_4 = r'C:\Users\user\Desktop\CPS\Gr_transistor_bc pair_4e-4 mbar.csv'
file_1e_2 = r'C:\Users\user\Desktop\CPS\Gr_transistor_bc pair_1e-2 mbar.csv'

# 데이터 읽기
data_8e_2 = pd.read_csv(file_8e_2)
data_6e_2 = pd.read_csv(file_6e_2)
data_4e_3 = pd.read_csv(file_4e_3)
data_1e_3 = pd.read_csv(file_1e_3)
data_4e_4 = pd.read_csv(file_4e_4)
data_1e_2 = pd.read_csv(file_1e_2)

# 데이터 정리 (Gate_voltage, Drain_current 열 사용)
data_8e_2_clean = data_8e_2[['Gate_voltage', 'Drain_current']]
data_6e_2_clean = data_6e_2[['Gate_voltage', 'Drain_current']]
data_4e_3_clean = data_4e_3[['Gate_voltage', 'Drain_current']]
data_1e_3_clean = data_1e_3[['Gate_voltage', 'Drain_current']]
data_4e_4_clean = data_4e_4[['Gate_voltage', 'Drain_current']]
data_1e_2_clean = data_1e_2[['Gate_voltage', 'Drain_current']]

# 그래프 플롯
plt.figure(figsize=(10, 7))

plt.plot(data_8e_2_clean['Gate_voltage'], data_8e_2_clean['Drain_current'], label='8e-2 Torr', linewidth=2)
plt.plot(data_6e_2_clean['Gate_voltage'], data_6e_2_clean['Drain_current'], label='6e-2 Torr', linewidth=2)
plt.plot(data_4e_3_clean['Gate_voltage'], data_4e_3_clean['Drain_current'], label='4e-3 Torr', linewidth=2)
plt.plot(data_1e_3_clean['Gate_voltage'], data_1e_3_clean['Drain_current'], label='1e-3 Torr', linewidth=2)
plt.plot(data_4e_4_clean['Gate_voltage'], data_4e_4_clean['Drain_current'], label='4e-4 Torr', linewidth=2)
plt.plot(data_1e_2_clean['Gate_voltage'], data_1e_2_clean['Drain_current'], label='1e-2 Torr', linewidth=2)

# 그래프 스타일 설정
plt.title('Dependence: Vacuum Level', fontsize=14)
plt.xlabel('Gate Voltage ($V_G$)', fontsize=12)
plt.ylabel('Drain Current ($I_D$)', fontsize=12)
plt.axhline(y=0, color='gray', linestyle='--', linewidth=0.8)  # 기준선 추가
plt.legend(title='Vacuum Levels')
plt.grid(True)
plt.show()
