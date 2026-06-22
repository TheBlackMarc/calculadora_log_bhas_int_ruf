# BlackCalculator 3.5

Aplicación de escritorio desarrollada en **Python** con **Tkinter**, orientada al cálculo matemático y al aprendizaje, con una interfaz gráfica inspirada en la estética **Windows 11**, incorporando una paleta **dark/neon**, panel lateral de navegación y una organización visual más moderna que una calculadora tradicional hecha en Tkinter.

El proyecto integra en una sola ventana distintos módulos matemáticos —**Logaritmos, Bhaskara, Ruffini e Integrales**— manteniendo una estructura simple, pero con una presentación más limpia, ordenada y agradable a nivel visual.

---

## Tabla de contenidos

- [Características](#características)
- [Módulos disponibles](#módulos-disponibles)
- [Tecnologías utilizadas](#tecnologías-utilizadas)
- [Capturas / interfaz](#capturas--interfaz)
- [Instalación](#instalación)
- [Ejecución](#ejecución)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Detalles técnicos](#detalles-técnicos)
- [Roadmap](#roadmap)
- [Licencia](#licencia)
- [Autor](#autor)

---

## Características

- Interfaz gráfica moderna con inspiración visual en **Windows 11**
- Estética **oscura + neón** con paneles tipo *glass*
- Navegación lateral para acceder a los distintos módulos
- Caja de resultados integrada en la ventana principal
- Arquitectura más limpia que una interfaz Tkinter básica basada en múltiples ventanas
- Validación de entradas y manejo básico de errores
- Integración de **cálculo simbólico** mediante SymPy

---

## Módulos disponibles

### 1) Logaritmos
Permite calcular logaritmos indicando:
- número
- base

Incluye validación para:
- números menores o iguales a 0
- bases inválidas
- errores de entrada

---

### 2) Bhaskara
Resuelve ecuaciones cuadráticas de la forma:

\[
ax^2 + bx + c = 0
\]

Calcula:
- discriminante
- raíces reales (cuando existen)

Incluye validación para evitar casos inválidos, como `a = 0`.

---

### 3) Ruffini
Permite realizar operaciones mediante el esquema de Ruffini a partir de los coeficientes ingresados por el usuario.

---

### 4) Integrales
Incluye dos modos de cálculo:

- **Integral indefinida**
- **Integral definida**

Utiliza **SymPy** para procesar expresiones matemáticas.

Ejemplo de función válida:

```python
x**2 + 2*x
