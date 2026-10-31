# Validación de la colección gratuita

- 40 nombres únicos en inglés y kebab-case; cinco categorías.
- 80 archivos SVG con XML válido y viewBox 0 0 64 64; pareja completa por nombre.
- 18 archivos piloto conservados byte por byte; las dos variantes de raven se rediseñaron por petición del usuario. La referencia SHA-256 refleja esta revisión autorizada.
- 80 rutas SVG servidas por HTTP local con respuesta 200 y contenido idéntico al disco.
- Galería: 40 tarjetas, 80 SVG inline, 80 descargas y 80 clases CSS.
- Comparativa: 320 muestras renderizadas en navegador. Anchos efectivos verificados:
  16, 24, 32 y 64 px. IDs de máscaras únicos en todas las muestras.
- Buscador probado: “pocion” sin tilde y “flying-raven” devuelven una pareja;
  búsqueda inexistente muestra estado vacío; Nobleza y política devuelve siete iconos.
- Sin errores en la consola durante estas comprobaciones.

## Incidencias resueltas

Se corrigió un segmento relativo de la aldea y un hueco no deseado en la
superficie del mapa heráldico. Se reforzaron la silueta de las espigas y la
separación del asiento del trono. No quedan archivos ausentes o XML inválidos.
Los adornos finos pierden definición a 16 px; las vistas de 32 y 64 px permiten
apreciar mejor los detalles. No se ha realizado una matriz de navegadores ni
una prueba en una instalación real de Foroactivo.

## Reproducir

```sh
python3 scripts/build.py
python3 scripts/check.py
python3 -m http.server 8001 --bind 127.0.0.1
```

Abrir index.html y comparison.html en http://127.0.0.1:8001/.

Revisión de cuervos: `raven` y `flying-raven` redibujados en ambos estilos a petición del usuario, con pico, cabeza y cola más reconocibles. Se actualizó la referencia de hashes de `raven` para reflejar el cambio autorizado.
