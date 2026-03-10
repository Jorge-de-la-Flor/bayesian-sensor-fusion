[English](README.md) | Español

# Fusión de Sensores Bayesianos

Experimentos mínimos que ilustran la fusión de sensores bayesianos y la estimación probabilística del estado en sistemas robóticos.

Este repositorio explora enfoques probabilísticos simples para combinar múltiples mediciones con ruido para estimar estados ocultos del sistema.

Los ejemplos demuestran cómo las técnicas de filtrado bayesiano, como los filtros de Kalman y los filtros de partículas, pueden mejorar la estimación del estado cuando los sensores presentan incertidumbre o ruido.

## Contenido

El directorio `src/` contiene tres experimentos mínimos:

* `kalman_filter_2d.py`

Implementa un filtro de Kalman bidimensional simple para el seguimiento de un objeto en movimiento.

* `multi_sensor_fusion.py`

Demuestra cómo se pueden fusionar múltiples sensores con ruido para estimar una señal latente.

* `particle_filter_demo.py`

Implementa un filtro de partículas básico para el seguimiento de un objetivo en movimiento en condiciones de incertidumbre.

## Propósito

Estos experimentos ilustran conceptos de ingeniería relevantes para:

* Robótica probabilística
* Estimación de estado bayesiana
* Fusión multisensorial
* Modelado de incertidumbre

## Motivación

La robótica y los sistemas ciberfísicos deben operar con datos de sensores incompletos y ruidosos.

Las técnicas de estimación bayesiana proporcionan un marco de principios para combinar mediciones inciertas y estimar el estado subyacente de un sistema.

Estos métodos se utilizan ampliamente en robótica, vehículos autónomos y sistemas de percepción integrados.

## Método

El repositorio implementa técnicas simplificadas de filtrado bayesiano para la estimación de estado.

Los experimentos incluyen:

* Filtrado de Kalman para sistemas gaussianos lineales
* Fusión de múltiples mediciones de sensores ruidosos
* Filtrado de partículas para la estimación de estado no lineal

Estos ejemplos son intencionadamente minimalistas y se centran en ilustrar el comportamiento conceptual de los métodos de filtrado bayesiano en lugar de implementarlos en producción.

## Ejecución de los ejemplos

Clonar el repositorio y ejecutar cualquiera de los scripts:

```bash
git clone https://github.com/Jorge-de-la-Flor/bayesian-sensor-fusion
cd bayesian-sensor-fusion
python src/kalman_filter_2d.py
```

Cada script genera mediciones simuladas del sensor y visualiza el proceso de estimación del estado resultante.

## Ejemplo de salida

![Ejemplo de seguimiento de Kalman](assets/kalman_2d_tracking.png)
![Ejemplo de fusión multisensor](assets/multi_sensor_fusion.png)
![Ejemplo de seguimiento de filtro de partículas](assets/particle_filter_tracking.png)

## Árbol del proyecto

```bash
bayesian-sensor-fusion
├─ .python-version
├─ LICENCIA
├─ README.es.md
├─ README.md
├─ assets
│ ├─ kalman_2d_tracking.png
│ ├─ multi_sensor_fusion.png
│ └─ particle_filter_tracking.png
├─ pyproject.toml
├─ src
│ ├─ kalman_filter_2d.py
│ ├─ multi_sensor_fusion.py
│ └─ particle_filter_demo.py
└─ uv.lock
```

## Requisitos

Los ejemplos usan:

* Python 3.12+
* NumPy
* Matplotlib

## Instalación

Instalar las dependencias necesarias:

* using `pip`

```bash
pip install numpy matplotlib
```

* using `uv`

```bash
uv add numpy matplotlib
```

## Referencias

* Thrun, S., Burgard, W. y Fox, D. (2005).
  *Robótica Probabilística.*

* Doucet, A., De Freitas, N. y Gordon, N. (2001).
  *Métodos Secuenciales de Monte Carlo en la Práctica.*
