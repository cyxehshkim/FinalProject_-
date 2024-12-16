#머신러닝을 통해 어닐링 조건 예측

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

file_before = 'C:/Users/user/Desktop/CPS/Gr_transistor_bc pair_1e-4 mbar_before annealing.csv'
file_60C = "C:/Users/user/Desktop/CPS/Gr_transistor_bc pair_1e-4 mbar_60'C.csv"
file_80C = "C:/Users/user/Desktop/CPS/Gr_transistor_bc pair_1e-4 mbar_80'C.csv"
file_100C = "C:/Users/user/Desktop/CPS/Gr_transistor_bc pair_1e-4 mbar_100'C_after annealing.csv"


data_before = pd.read_csv(file_before)[['Gate_voltage', 'Drain_current']]
data_60C = pd.read_csv(file_60C)[['Gate_voltage', 'Drain_current']]
data_80C = pd.read_csv(file_80C)[['Gate_voltage', 'Drain_current']]
data_100C = pd.read_csv(file_100C)[['Gate_voltage', 'Drain_current']]

data_before['Temperature'] = 0
data_60C['Temperature'] = 60
data_80C['Temperature'] = 80
data_100C['Temperature'] = 100

data_combined = pd.concat([data_before, data_60C, data_80C, data_100C], ignore_index=True)

X = data_combined[['Gate_voltage', 'Temperature']]  # Gate Voltage와 온도
y = data_combined['Drain_current']  # Drain Current

# 머신러닝 모델 학습 (Random Forest 사용) 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 예측할 온도 범위 설정
temperatures = [120, 140, 160, 180, 200]
gate_voltage_range = np.linspace(data_combined['Gate_voltage'].min(), data_combined['Gate_voltage'].max(), 100)

# 새로운 온도에 대한 IV 커브 예측
predicted_IV_curves = {}
for temp in temperatures:
    X_pred = pd.DataFrame({'Gate_voltage': gate_voltage_range, 'Temperature': [temp] * len(gate_voltage_range)})
    predicted_IV_curves[temp] = model.predict(X_pred)


plt.figure(figsize=(10, 7))


plt.plot(data_before['Gate_voltage'], data_before['Drain_current'], label='0°C (Before Annealing)', linewidth=2, color='blue')
plt.plot(data_60C['Gate_voltage'], data_60C['Drain_current'], label='60°C', linewidth=2, color='green')
plt.plot(data_80C['Gate_voltage'], data_80C['Drain_current'], label='80°C', linewidth=2, color='orange')
plt.plot(data_100C['Gate_voltage'], data_100C['Drain_current'], label='100°C', linewidth=2, color='red')

# 예측된 IV 커브 플롯
for temp, drain_current in predicted_IV_curves.items():
    plt.plot(gate_voltage_range, drain_current, label=f'{temp}°C (Predicted)', linestyle='--')


plt.title('IV Curve Prediction for Different Annealing Temperatures')
plt.xlabel('Gate Voltage ($V_G$)')
plt.ylabel('Drain Current ($I_D$)')
plt.legend()
plt.grid(True)
plt.show()

#스스로 부여하는 학점 : A+

#수업 전 목표는 CV에 Python을 자신 있게 추가할 실력을 갖추는 것이었습니다. 
# 초기에는 Python은 물론 어떠한 코딩 경험도 전무하고 단축키조차 잘 몰랐지만, 
# 이번 학기 동안 Python의 기초부터 시작해 데이터를 분석하고 몇 가지의 머신러닝 모델을 익혔습니다.
# 한 학기 동안 쌓은 성과를 통해 더 나은 연구를 할 수 있는 기반을 마련했다고 생각합니다.
# 한학기 동안 노력한 성과와 발전에 만족하며 A+를 부여하고자 합니다.


