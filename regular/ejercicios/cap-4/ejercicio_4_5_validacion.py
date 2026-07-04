"""
Validación del Ejercicio 4.5 inciso a)
Variable aleatoria X ~ Binomial(n=10, p=0.5)

Calcular:
a) P(μ - σ ≤ X ≤ μ + σ) y P(μ - 2σ ≤ X ≤ μ + 2σ)
"""

import numpy as np
from scipy.stats import binom
import pandas as pd

# Parámetros
n = 10
p = 0.5

# Calcular media y desviación estándar
mu = n * p
sigma = np.sqrt(n * p * (1 - p))

print("=" * 70)
print("EJERCICIO 4.5 INCISO a)")
print("=" * 70)
print(f"\nDistribución Binomial: X ~ B(n={n}, p={p})")
print(f"\nMedia (μ) = n·p = {n}·{p} = {mu}")
print(f"Desviación estándar (σ) = √(n·p·(1-p)) = √({n}·{p}·{1-p}) = {sigma:.6f}")

# Calcular límites para μ ± 2σ
limite_inferior_2sigma = mu - 2 * sigma
limite_superior_2sigma = mu + 2 * sigma

print(f"\n--- CASO: μ ± 2σ ---")
print(f"μ - 2σ = {mu} - 2·{sigma:.6f} = {limite_inferior_2sigma:.6f}")
print(f"μ + 2σ = {mu} + 2·{sigma:.6f} = {limite_superior_2sigma:.6f}")

# Como X es discreta, convertir a números enteros
# Hay dos formas de redondear: hacia adentro o hacia afuera

print(f"\nComo X es discreta (solo puede tomar valores 0,1,2,...,10):")
print(f"Necesitamos redondear los límites a números enteros.")

# Forma 1: Redondeo estándar (lo más común en textos)
limite_inf_redondeado = int(np.round(limite_inferior_2sigma))
limite_sup_redondeado = int(np.round(limite_superior_2sigma))

print(f"\n→ Redondeo estándar: P({limite_inf_redondeado} ≤ X ≤ {limite_sup_redondeado})")

# Forma 2: Hacia adentro (ceil del inferior, floor del superior)
limite_inf_ceil = int(np.ceil(limite_inferior_2sigma))
limite_sup_floor = int(np.floor(limite_superior_2sigma))

print(f"→ Hacia adentro (más restrictivo): P({limite_inf_ceil} ≤ X ≤ {limite_sup_floor})")

# Forma 3: Hacia afuera (floor del inferior, ceil del superior)
limite_inf_floor = int(np.floor(limite_inferior_2sigma))
limite_sup_ceil = int(np.ceil(limite_superior_2sigma))

print(f"→ Hacia afuera (menos restrictivo): P({limite_inf_floor} ≤ X ≤ {limite_sup_ceil})")

# Calcular probabilidades para cada caso
print("\n" + "=" * 70)
print("CÁLCULO DE PROBABILIDADES")
print("=" * 70)

casos = [
    (f"Redondeo estándar", limite_inf_redondeado, limite_sup_redondeado),
    (f"Hacia adentro (ceil/floor)", limite_inf_ceil, limite_sup_floor),
    (f"Hacia afuera (floor/ceil)", limite_inf_floor, limite_sup_ceil),
]

resultados = []

for descripcion, a, b in casos:
    # P(a ≤ X ≤ b) = P(X ≤ b) - P(X ≤ a-1) = F(b) - F(a-1)
    prob = binom.cdf(b, n, p) - binom.cdf(a - 1, n, p)
    resultados.append((descripcion, a, b, prob))
    print(f"\n{descripcion}:")
    print(f"  P({a} ≤ X ≤ {b})")
    print(f"  = P(X ≤ {b}) - P(X ≤ {a-1})")
    print(f"  = {binom.cdf(b, n, p):.6f} - {binom.cdf(a-1, n, p):.6f}")
    print(f"  = {prob:.6f} ≈ {prob:.4f}")

# Comparar con los resultados del usuario y del libro
print("\n" + "=" * 70)
print("COMPARACIÓN CON RESULTADOS DADOS")
print("=" * 70)
print(f"Resultado del usuario: 0.9785")
print(f"Resultado del libro:   0.9346")

print(f"\nProbabilidades calculadas:")
for desc, a, b, prob in resultados:
    print(f"  {desc:30} → {prob:.4f}")
    if abs(prob - 0.9785) < 0.001:
        print(f"    ✓ Coincide con resultado del usuario")
    if abs(prob - 0.9346) < 0.001:
        print(f"    ✓ Coincide con resultado del libro")

# Mostrar tabla de distribución binomial para referencia
print("\n" + "=" * 70)
print("TABLA DE DISTRIBUCIÓN BINOMIAL B(10, 0.5)")
print("=" * 70)

x_values = np.arange(0, n + 1)
probs = binom.pmf(x_values, n, p)
cumprobs = binom.cdf(x_values, n, p)

df = pd.DataFrame({
    'X': x_values,
    'P(X=x)': probs,
    'P(X≤x)': cumprobs
})

print(df.to_string(index=False))

# Suma manual para verificar el intervalo más probable
print("\n" + "=" * 70)
print("VERIFICACIÓN MANUAL - Suma de probabilidades")
print("=" * 70)

print("\nP(2 ≤ X ≤ 8):")
suma_2_8 = sum(probs[2:9])
print(f"  = P(X=2) + P(X=3) + ... + P(X=8)")
print(f"  = {' + '.join([f'{p:.6f}' for p in probs[2:9]])}")
print(f"  = {suma_2_8:.6f}")

print("\nP(1 ≤ X ≤ 9):")
suma_1_9 = sum(probs[1:10])
print(f"  = P(X=1) + P(X=2) + ... + P(X=9)")
print(f"  = {suma_1_9:.6f}")

print("\nP(2 ≤ X ≤ 9):")
suma_2_9 = sum(probs[2:10])
print(f"  = {suma_2_9:.6f}")

print("\nP(1 ≤ X ≤ 8):")
suma_1_8 = sum(probs[1:9])
print(f"  = {suma_1_8:.6f}")
