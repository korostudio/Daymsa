# Daymsa — maqueta de rediseño web

Demo navegable del rediseño de la web de **Daymsa** (Desarrollo Agrícola y Minero, S.A.).
Es una maqueta de presentación: los datos de catálogo son reales pero parciales, y algunos
contenidos están marcados como pendientes dentro de la propia interfaz.

## Cómo levantarla

Necesitas Python 3 (ya viene en la mayoría de equipos):

```bash
python serve.py          # http://127.0.0.1:5173/
python serve.py 8080     # otro puerto
```

Ábrela en `http://127.0.0.1:5173/`.

> Hay que servirla por HTTP. Si abres el `index.html` directamente con doble clic
> (`file://`), las rutas relativas del framework no resuelven y verás una página en blanco.

## Qué incluye

| Pantalla | Contenido |
|---|---|
| Inicio | Hero, gamas de producto, soluciones por cultivo, noticias, newsletter |
| Catálogo | 74 productos con filtros por gama, necesidad y cultivo, y comparador |
| Cultivos | Rejilla de cultivos con programa nutricional por cultivo |
| Ficha de producto | Descripción, composición, dosis y solicitud de ficha técnica |

Responsive con menú hamburguesa y panel de filtros a pantalla completa por debajo de 900 px.

## Funciona sin conexión

Todas las dependencias están en el repositorio, así que la demo se puede presentar
sin internet:

- `vendor/` — React, ReactDOM y Babel (verificados contra los hashes SRI oficiales)
- `vendor/fonts/` — tipografía Nunito Sans
- `img/web/` — imágenes de cultivo y producto

## Estructura

```
index.html                   la maqueta entera (marcado + datos + lógica)
support.js                   runtime del design-canvas
_ds/                         design system (tokens y estilos)
serve.py                     servidor estático local
vendor/  img/                dependencias y assets locales
```

## Pendiente

- El número de WhatsApp es un marcador (`34XXXXXXXXX`)
- Solo los cultivos cargados en la maqueta tienen programa completo
- Textos de ficha técnica pendientes de migrar desde la web actual
