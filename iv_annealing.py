import pandas as pd
import matplotlib.pyplot as plt

# 파일 불러오기
file_before = 'C:/Users/user/Desktop/CPS/Gr_transistor_bc pair_1e-4 mbar_before annealing.csv'
file_60C = "C:/Users/user/Desktop/CPS/Gr_transistor_bc pair_1e-4 mbar_60'C.csv"
file_80C = "C:/Users/user/Desktop/CPS/Gr_transistor_bc pair_1e-4 mbar_80'C.csv"
file_100C = "C:/Users/user/Desktop/CPS/Gr_transistor_bc pair_1e-4 mbar_100'C_after annealing.csv"

# 데이터 읽기
data_before = pd.read_csv(file_before)
data_60C = pd.read_csv(file_60C)
data_80C = pd.read_csv(file_80C)
data_100C = pd.read_csv(file_100C)

# 데이터 확인 및 정리 (Gate_voltage, Drain_current 열 사용)
data_before_clean = data_before[['Gate_voltage', 'Drain_current']]
data_60C_clean = data_60C[['Gate_voltage', 'Drain_current']]
data_80C_clean = data_80C[['Gate_voltage', 'Drain_current']]
data_100C_clean = data_100C[['Gate_voltage', 'Drain_current']]

# 플롯
plt.figure(figsize=(10, 7))

plt.plot(data_before_clean['Gate_voltage'], data_before_clean['Drain_current'], label='Before Annealing (1e-4 mbar)', linewidth=2)
plt.plot(data_60C_clean['Gate_voltage'], data_60C_clean['Drain_current'], label="60°C Annealing (1e-4 mbar)", linewidth=2)
plt.plot(data_80C_clean['Gate_voltage'], data_80C_clean['Drain_current'], label="80°C Annealing (1e-4 mbar)", linewidth=2)
plt.plot(data_100C_clean['Gate_voltage'], data_100C_clean['Drain_current'], label="100°C Annealing (1e-4 mbar)", linewidth=2)

# 그래프 스타일 설정
plt.title('Dependence: Annealing Effect on $V_G$-$I_D$ Curve', fontsize=14)
plt.xlabel('Gate Voltage ($V_G$)', fontsize=12)
plt.ylabel('Drain Current ($I_D$)', fontsize=12)
plt.axhline(y=0, color='gray', linestyle='--', linewidth=0.8)  # 기준선
plt.legend(title='Conditions')
plt.grid(True)
plt.show()
