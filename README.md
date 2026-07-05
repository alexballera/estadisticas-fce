# Analisis Estadistico - Economia (FCE-UBA)

Repositorio de apoyo para la materia Analisis Estadistico de la carrera de Economia, Facultad de Ciencias Economicas (UBA).

Concentra el material completo del curso intensivo de invierno, tablas estadisticas, bibliografia, documentacion de HP Prime y configuracion de entorno para practicar con Jupyter/Python. Todo el material de cursada esta organizado bajo `sesiones/`.

## Objetivo del proyecto

- Centralizar el material del intensivo (clases, teoria y ejercicios por unidad).
- Facilitar el estudio teorico y la preparacion de parciales.
- Dar una base reproducible para trabajo con Python.
- Integrar verificacion de resultados con HP Prime.

## Estructura real del repositorio

```text
estadisticas-fce/
├── README.md
├── JUPYTER_GUIA.md
├── requirements.txt
├── start_jupyter.sh
├── sesiones/
│   ├── intensivo/
│   │   ├── Cronograma_Analisis_Estadistico_I_Intensivo_invierno.pdf
│   │   ├── u1-probabilidad/
│   │   │   ├── Clase_Probabilidad.pdf
│   │   │   ├── Practica-1-Probabilidad_teoria.pdf
│   │   │   └── Practica-1-Probabilidad_ejercicios.pdf
│   │   ├── u2-va-discretas/
│   │   │   ├── Clase_VA_Discretas.pdf
│   │   │   ├── Practica_2_Variables_Aleatorias_Discretas_teoria.pdf
│   │   │   └── Practica_2_Variables_Aleatorias_Discretas_Ejercicios.pdf
│   │   ├── u3-va-continuas/
│   │   │   ├── Clase_VA_Continuas.pdf
│   │   │   ├── Practica_3_Variables_Aleatorias_Continuas_teoria.pdf
│   │   │   └── Practica_3-VA-Continuas.pdf
│   │   ├── u4-va-bidimensionales/
│   │   │   ├── Clase_VA_Bidimensionales.pdf
│   │   │   ├── Practica_4_VA_Bidimiensionales_teoria.pdf
│   │   │   └── Practica_4_VA_Bidimiensionales.pdf
│   │   ├── u5-estadisticas-descriptiva/
│   │   │   ├── Clase_Descriptiva.pdf
│   │   │   ├── Practica_5_Estadistica_Descriptiva_teoria.pdf
│   │   │   └── Practica_5_Estadistica_Descriptiva.pdf
│   │   ├── u6-muestreo-e-ic/
│   │   │   ├── Clase_Muestreo_e_IC.pdf
│   │   │   ├── Practica_6_Muestreo_e_IC_teoria.pdf
│   │   │   └── Practica_6_Muestreo_e_IC.pdf
│   │   ├── u7-test-hipotesis/
│   │   │   ├── Clase_TH.pdf
│   │   │   ├── Practica_7_Test_de_Hipotesis_teoria.pdf
│   │   │   └── Practica_7_Test_de_Hipotesis.pdf
│   │   └── u8-test-no-parametricos/
│   │       ├── Clase_Estadistica_no_parametrica.pdf
│   │       └── Practica_8_Estadistica_no_parametrica.pdf
│   └── regular/
│       ├── Analisis-Estadistico-Programa.pdf
│       ├── Analisis-Estadistico-Cronograma-1T2026-LuMiJu.pdf
│       ├── ejercicios/
│       │   ├── cap-2/  Ejercicios-Cap2-2025-08-23.pdf
│       │   ├── cap-3/  Ejercicios-Cap3-2025-08-30.pdf
│       │   └── cap-4/  ejercicio_4_5_validacion.py
│       └── parcial2/
│           └── [imagenes del parcial 2 - junio 2026]
├── fuentes/
│   ├── RESUMEN_DE_FORMULAS.pdf
│   ├── libros/
│   │   ├── Bacchini_Introduccion-a-la-probabilidad-y-a-la-estadistica-2018.pdf
│   │   ├── CAVIEZEL-(540)-Guia-de-trabajos-practicos.pdf
│   │   └── [1988] Probabilidad y Estadistica.pdf
│   └── tablas/
│       ├── Tabla_Normal.pdf / TablaNormal.pdf
│       ├── Tabla_T_de_Student.pdf / TablaTdeStudent.pdf
│       ├── Tabla_Chi2.pdf / TablaChi2.pdf
│       ├── Tabla_F_de_Snedecor.pdf / TablaFdeFisher-Snedecor.pdf
│       ├── Tabla_Binomial.pdf / TablaBinomial.pdf
│       ├── Tabla_Poisson.pdf / TablaPoisson.pdf
│       └── Tabla_Normal_Fractiles.pdf / TablaNormalFractiles.pdf
├── hp-prime/
│   ├── docs/
│   │   ├── Guia_HP_Prime_Probabilidad.md
│   │   ├── Guia_HP_Prime_Variables_Aleatorias.md
│   │   ├── Guia_HP_Prime_Variables_Continuas.md
│   │   └── Guia_Rapida_HP_Prime_Complejos.md
│   └── manuales/
│       └── [manuales oficiales HP Prime en PDF]
└── .github/
    ├── copilot-instructions.md
    ├── prompts/
    ├── agents/
    └── skills/
```

## Ruta de estudio: Intensivo de invierno

El material del intensivo esta organizado en 8 unidades, cada una con tres componentes:

| Unidad | Tema | Clase | Teoria | Ejercicios |
|--------|------|-------|--------|------------|
| U1 | Probabilidad | Clase_Probabilidad.pdf | Practica-1-..._teoria.pdf | Practica-1-..._ejercicios.pdf |
| U2 | VA Discretas | Clase_VA_Discretas.pdf | Practica_2-..._teoria.pdf | Practica_2-..._Ejercicios.pdf |
| U3 | VA Continuas | Clase_VA_Continuas.pdf | Practica_3-..._teoria.pdf | Practica_3-VA-Continuas.pdf |
| U4 | VA Bidimensionales | Clase_VA_Bidimensionales.pdf | Practica_4-..._teoria.pdf | Practica_4-..._ejercicios.pdf |
| U5 | Estadistica Descriptiva | Clase_Descriptiva.pdf | Practica_5-..._teoria.pdf | Practica_5-..._ejercicios.pdf |
| U6 | Muestreo e IC | Clase_Muestreo_e_IC.pdf | Practica_6-..._teoria.pdf | Practica_6-..._ejercicios.pdf |
| U7 | Test de Hipotesis | Clase_TH.pdf | Practica_7-..._teoria.pdf | Practica_7-..._ejercicios.pdf |
| U8 | Tests No Parametricos | Clase_Estadistica_no_parametrica.pdf | — | Practica_8-..._ejercicios.pdf |

Ruta base: `sesiones/intensivo/u{N}-{tema}/`

Flujo recomendado por unidad:
1. Leer las diapositivas de clase (Clase_*.pdf) para la vision general.
2. Estudiar el marco teorico (Practica_*_teoria.pdf) con definiciones y formulas.
3. Resolver los ejercicios de practica (Practica_*_ejercicios.pdf).
4. Verificar calculos con las guias de HP Prime en hp-prime/docs/.
5. Repasar con tablas estadisticas en fuentes/tablas/.

## Guia rapida para entorno Python

Requisitos minimos: Python 3.10+, entorno virtual activo, dependencias de requirements.txt.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
./start_jupyter.sh
```

Mas detalle tecnico en JUPYTER_GUIA.md.

## Recursos clave para alumnos

Cronograma del intensivo:
- `sesiones/intensivo/Cronograma_Analisis_Estadistico_I_Intensivo_invierno.pdf`

Cronograma y programa del cuatrimestre regular:
- `sesiones/regular/Analisis-Estadistico-Programa.pdf`
- `sesiones/regular/Analisis-Estadistico-Cronograma-1T2026-LuMiJu.pdf`

Bibliografia de referencia (`fuentes/libros/`):
- Bacchini (2018) - Introduccion a la probabilidad y a la estadistica.
- Caviezel (540) - Guia de trabajos practicos.
- Probabilidad y Estadistica [1988].

Tablas estadisticas (`fuentes/tablas/`):
- Normal, t de Student, Chi-cuadrado, F de Snedecor, Binomial, Poisson y Fractiles.

Resumen de formulas: `fuentes/RESUMEN_DE_FORMULAS.pdf`

HP Prime (`hp-prime/docs/`):
- Probabilidad, Variables Aleatorias, Variables Continuas, Numeros Complejos.

Material de examen:
- Ejercicios cap. 2, 3 y 4 con fechas en `sesiones/regular/ejercicios/`.
- Imagenes del Parcial 2 (junio 2026) en `sesiones/regular/parcial2/`.

## Tutor IA del proyecto

El repositorio incluye personalizaciones de Copilot para asistencia academica:
- Skill: `.github/skills/tutor-profesor-analisis-estadistico/SKILL.md`
- Agente: `.github/agents/tutor-profesor-analisis-estadistico.agent.md`

Uso sugerido del tutor:
- pedir explicaciones paso a paso de cualquier unidad del intensivo;
- preparar parciales con formato de resolucion;
- validar interpretacion economica de resultados estadisticos;
- comparar metodos (distribuciones, tests, estimadores).

## Buenas practicas de cursada

- Escribir siempre datos, supuestos y formula antes de calcular.
- Verificar si el metodo elegido corresponde al tipo de variable/muestra.
- Reportar resultado numerico y conclusion en lenguaje economico.
- Controlar errores comunes: unidades, redondeo y lectura de tablas.

## Estado actual

El material del intensivo de invierno (8 unidades) esta completo con clases, teoria y ejercicios en `sesiones/intensivo/`. El material del cuatrimestre regular cubre hasta el capitulo 4 con ejercicios digitalizados y el Parcial 2 de junio 2026 en `sesiones/regular/parcial2/`.

## Licencia

Proyecto bajo licencia MIT. Ver LICENSE.
