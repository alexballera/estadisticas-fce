# Analisis Estadistico - Economia (FCE-UBA)

Repositorio de apoyo para la materia Analisis Estadistico de la carrera de Economia, Facultad de Ciencias Economicas (UBA).

Este espacio concentra material de estudio, tablas de referencia, documentacion de HP Prime y configuracion de entorno para practicar con Jupyter/Python.

## Objetivo del proyecto

- Centralizar fuentes academicas de la cursada.
- Facilitar estudio teorico y preparacion de parciales.
- Dar una base reproducible para trabajo con Python.
- Integrar verificacion de resultados con HP Prime.

## Estructura real del repositorio

```text
estadisticas-fce/
├── README.md
├── JUPYTER_GUIA.md
├── requirements.txt
├── start_jupyter.sh
├── AGENTS.md
├── fuentes/
│   ├── fce/
│   │   ├── Analisis-Estadistico-Programa.pdf
│   │   ├── Analisis-Estadistico-Cronograma-1T2026-LuMiJu.pdf
│   │   ├── CAVIEZEL-(540)-Guia-de-trabajos-practicos.pdf
│   │   └── [1988] Probabilidad y Estadistica.pdf
│   ├── TablaNormal.pdf
│   ├── TablaTdeStudent.pdf
│   ├── TablaChi2.pdf
│   ├── TablaFdeFisher-Snedecor.pdf
│   ├── TablaBinomial.pdf
│   ├── TablaPoisson.pdf
│   ├── TablaNormalFractiles.pdf
│   └── RESUMEN_DE_FORMULAS.pdf
├── hp-prime/
│   ├── docs/
│   │   ├── Guia_HP_Prime_Probabilidad.md
│   │   ├── Guia_HP_Prime_Variables_Aleatorias.md
│   │   ├── Guia_HP_Prime_Variables_Continuas.md
│   │   └── Guia_Rapida_HP_Prime_Complejos.md
│   └── manuales/
│       └── manuales oficiales PDF
└── .github/
    ├── copilot-instructions.md
    ├── prompts/
    ├── agents/
    └── skills/
```

## Como estudiar con este repositorio

1. Leer el programa y cronograma en fuentes/fce para ubicar contenidos y fechas.
2. Estudiar teoria con bibliografia y guia de trabajos practicos.
3. Resolver ejercicios usando tablas estadisticas de fuentes.
4. Verificar calculos con guias de hp-prime/docs.
5. Repetir ejercicios en Python/Jupyter para automatizar procedimientos.

## Guia rapida para entorno Python

Requisitos minimos:
- Python 3.10 o superior.
- Entorno virtual activo.
- Dependencias de requirements.txt.

Pasos recomendados:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
./start_jupyter.sh
```

Mas detalle tecnico en JUPYTER_GUIA.md.

## Recursos clave para alumnos

Documentos de catedra:
- Programa oficial y cronograma en fuentes/fce.
- Guia de trabajos practicos en fuentes/fce/CAVIEZEL-(540)-Guia-de-trabajos-practicos.pdf.

Tablas y formularios:
- Normal, t de Student, Chi-cuadrado, F, Binomial y Poisson en fuentes/.
- Resumen de formulas en fuentes/RESUMEN_DE_FORMULAS.pdf.

HP Prime:
- Procedimientos por tema en hp-prime/docs.
- Manuales completos en hp-prime/manuales.

## Tutor IA del proyecto

El repositorio incluye personalizaciones de Copilot para asistencia academica:
- Skill: .github/skills/tutor-profesor-analisis-estadistico/SKILL.md
- Agente: .github/agents/tutor-profesor-analisis-estadistico.agent.md

Uso sugerido del tutor:
- pedir explicaciones paso a paso;
- preparar parciales con formato de resolucion;
- validar interpretacion economica de resultados estadisticos;
- comparar metodos (distribuciones, tests, estimadores).

## Buenas practicas de cursada

- Escribir siempre datos, supuestos y formula antes de calcular.
- Verificar si el metodo elegido corresponde al tipo de variable/muestra.
- Reportar resultado numerico y conclusion en lenguaje economico.
- Controlar errores comunes: unidades, redondeo, y lectura de tablas.

## Estado actual

Este repositorio se encuentra en evolucion continua. Si faltan notebooks o practicas digitalizadas, se iran incorporando progresivamente respetando el programa de la materia.

## Licencia

Proyecto bajo licencia MIT. Ver LICENSE.
