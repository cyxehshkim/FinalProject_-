import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 불러오기
file_path = r'C:\Users\user\Desktop\Gr_transistor_bc pair_1e-4 mbar_before annealing.csv'  # 파일 경로 설정
data = pd.read_csv(file_path)

# 필요 없는 열 제거
data_cleaned = data.loc[:, ~data.columns.str.contains('^Unnamed')]

# Gate Voltage vs Drain Current 그래프
plt.figure(figsize=(8, 6))
plt.plot(data_cleaned['Gate_voltage'], data_cleaned['Drain_current'], color='green', linewidth=2)
plt.title('$V_G$-$I_D$ curve of Graphene FET', fontsize=14)
plt.xlabel('Gate Voltage ($V_G$)', fontsize=12)
plt.ylabel('Drain Current ($I_D$)', fontsize=12)
plt.axhline(y=0, color='gray', linestyle='--', linewidth=0.8)  # 기준선 추가
plt.axvline(x=67, color='yellow', linestyle='--', linewidth=2, label='67V Contact')  # 특정 점 강조
plt.grid(True)
plt.legend()
plt.show()
