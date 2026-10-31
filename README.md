# Lannita Icons

Colección piloto de 10 símbolos para foros de rol medieval y fantasía, con variantes
`outline` y `heraldic`: crown, shield, swords, raven, scroll, castle, coins, key,
quill y dice. Se conserva el catálogo y la geometría del prototipo proporcionado.
SVG editables, `viewBox="0 0 64 64"`, color mediante `currentColor`.
Los recortes heráldicos son transparentes y funcionan sobre cualquier fondo.

## Probar localmente

Desde la carpeta del proyecto:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Abre http://127.0.0.1:8000. Para detenerlo, pulsa Ctrl+C.
También puedes abrir `index.html` directamente: la galería no depende de fetch.
Si el navegador impide copiar al portapapeles, aparece un cuadro de copia manual.
Requiere JavaScript para buscar, filtrar y copiar; los SVG y las descargas son estáticos.

Comprueba búsqueda por «corona» y «key», categorías, resultados vacíos, cambio de
color, copia de ambas variantes y descarga de SVG. El HTML copiado es un SVG
inline decorativo: acompáñalo de texto visible o añade un nombre accesible si
transmite información por sí solo.

## Foroactivo

Carga `css/lannita-icons.css` mediante un enlace de hoja de estilos en una plantilla
HTML o importa su URL al principio de la hoja CSS del foro. Usa una URL absoluta
alojada en tu repositorio/CDN: pegar el contenido con rutas relativas en el foro
requiere convertir las rutas de `../icons/` en URL absolutas.

```html
<span class="li li-crown" aria-hidden="true"></span> Administración
<span class="li li-heraldic li-crown" aria-hidden="true"></span> Nobleza
```

```css
.li { color: #b69353; font-size: 24px; }
```

La hoja usa máscaras CSS externas para heredar el color sin insertar SVG en
mensajes. Se puede usar donde el foro permita HTML/clases; depende de los permisos
y plantillas de cada foro. No se ha probado en una instalación real de Foroactivo.
Un `<img>` externo no hereda `currentColor` del documento: usa SVG inline o estas clases.

## Estructura y mantenimiento

- `icons/outline/` y `icons/heraldic/`: los 20 SVG fuente.
- `index.html`, `gallery.js`, `css/gallery.css`: galería estática.
- `css/lannita-icons.css`: integración en foros.
- `scripts/build.py`: regenera HTML y CSS de iconos con Python 3, sin dependencias.
- `scripts/check.py`: comprueba catálogo, SVG, referencias y rutas locales.

```sh
python3 scripts/build.py
python3 scripts/check.py
```

## Publicar en GitHub y jsDelivr

Sube esta estructura a un repositorio público, incluida la licencia, y crea una
etiqueta de versión, por ejemplo `v0.1.0`. No se ha publicado ningún repositorio.
La URL prevista para la hoja CSS es (sustituye USUARIO y REPO):

```text
https://cdn.jsdelivr.net/gh/USUARIO/REPO@v0.1.0/css/lannita-icons.css
```

Para un SVG: `...@v0.1.0/icons/heraldic/crown.svg`. Mantén la estructura de
carpetas para que funcionen las rutas relativas del CSS. Fija una versión para
que una actualización no cambie el aspecto del foro de forma inesperada.

## Licencia

MIT; véase `LICENSE`. Los SVG proceden del piloto entregado como diseños originales;
no se ha realizado una auditoría independiente de su autoría.

## Identidad visual y GitHub Pages

`assets/brand/lannita-logo.svg` es el logo horizontal de la cabecera;
`lannita-mark.svg` es el símbolo independiente y `favicon.svg` el icono de pestaña.
La identidad combina llaves, un monograma L, una pluma y un pequeño rombo,
inspirada en la referencia de Lannita Codes. Son vectores editables, con fondo
transparente (salvo el favicon); el logo está preparado para el fondo oscuro de
la galería. El texto usa tipografía sans serif del sistema sin descargar fuentes.
Los colores de marca son independientes del selector de color del catálogo.
Estos archivos de marca no añaden iconos al catálogo piloto.

Para GitHub Pages, publica la raíz del repositorio desde la rama elegida en
Settings → Pages. `index.html` es el punto de entrada; `.nojekyll` permite servir
los archivos estáticos directamente. No hace falta Node ni ejecutar un build en
Pages: los archivos generados ya están incluidos. Todas las rutas son relativas,
también las del logo y favicon, para funcionar bajo `/nombre-del-repositorio/`.

### Referencia visual oficial

La galería toma como referencia https://lannitacodes.tumblr.com/: fondo carbón
`#141416`, marfil `#ede7da`, dorado `#b48a3c`, tipografía sans serif, bordes finos
y llaves ornamentales. Se mantiene un símbolo propio para Icons (L y pluma).
No se cargan imágenes ni fuentes del Tumblr: los recursos de marca son locales.
