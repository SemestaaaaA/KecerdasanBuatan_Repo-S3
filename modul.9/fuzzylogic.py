import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


# Variabel input dan output
suhu = ctrl.Antecedent(np.arange(0, 101, 1), 'suhu')
ac = ctrl.Consequent(np.arange(0, 101, 1), 'ac')


# Fuzzy set dan fungsi keanggotaan
suhu['dingin'] = fuzz.trimf(suhu.universe, [0, 0, 50])
suhu['sejuk'] = fuzz.trimf(suhu.universe, [0, 50, 100])
suhu['normal'] = fuzz.trimf(suhu.universe, [50, 100, 100])
suhu['hangat'] = fuzz.trimf(suhu.universe, [50, 100, 150])
suhu['panas'] = fuzz.trimf(suhu.universe, [100, 150, 150])

# Fuzzy set dan fungsi keanggotaan
ac['rendah'] = fuzz.trimf(ac.universe, [0, 0, 50])
ac['sedang'] = fuzz.trimf(ac.universe, [0, 50, 100])
ac['tinggi'] = fuzz.trimf(ac.universe, [50, 100, 100])


# Aturan fuzzy
rule1 = ctrl.Rule(suhu['dingin'], ac['tinggi'])
rule2 = ctrl.Rule(suhu['sejuk'], ac['sedang'])
rule3 = ctrl.Rule(suhu['normal'], ac['sedang'])
rule4 = ctrl.Rule(suhu['hangat'], ac['rendah'])
rule5 = ctrl.Rule(suhu['panas'], ac['rendah'])


# Sistem kontrol
sisfuzzy = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
pengendali = ctrl.ControlSystemSimulation(sisfuzzy)


# Input dan komputasi
pengendali.input['suhu'] = 120
pengendali.compute()


# Output
hasil_pengaturan_ac = pengendali.output['ac']
print(f"Hasil pengaturan AC: {hasil_pengaturan_ac:.2f}")
