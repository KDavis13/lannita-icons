# Convenciones de Lannita Icons

- Conservar los 40 conceptos base (listados en `scripts/core-icons.json`) y los 10 pares
  piloto. El catálogo puede ampliarse con nuevos pares a petición del usuario; el
  proyecto es gratuito y sin monetización.
- Cada nombre debe existir en `icons/outline/` y `icons/heraldic/`; nombres ingleses
  en minúsculas, separados por guiones cuando sea necesario.
- Mantener `viewBox="0 0 64 64"`, proporciones y significado coherentes entre estilos.
- Outline: minimalista, trazos sin relleno. Heraldic: sólido y ornamental.
- Color visible mediante `currentColor`; recortes transparentes mediante máscaras,
  nunca parches blancos. Blanco/negro solo se permiten dentro de máscaras.
- SVG autocontenidos y editables: sin scripts, fuentes, imágenes ni recursos externos.
- Prefijar IDs con nombre de icono; al copiar SVG inline, generar IDs por instancia.
- Editar SVG fuente y `scripts/build.py`; regenerar con `python3 scripts/build.py`.
  No editar manualmente `index.html` ni `css/lannita-icons.css`, que son generados.
- Mantener rutas relativas para servir desde cualquier subdirectorio y desde CDN.
- Galería sin dependencias externas. Mantener búsqueda, categorías, ambas variantes,
  copia accesible con alternativa manual y descargas individuales.
- Usar máscaras CSS para integración en Foroactivo con `currentColor`.
- Ejecutar `python3 scripts/check.py` y revisar en navegador cuando cambie la galería.
- Documentar cambios, pruebas y límites reales; no publicar sin petición del usuario.

- Identidad visual en `assets/brand/`: logo horizontal, símbolo y favicon. Son
  recursos de marca separados del catálogo de iconos. Se permiten los colores
  de marca fijos y texto con fuentes del sistema en el logo. Mantener la cabecera
  accesible y el favicon enlazado con rutas relativas para GitHub Pages.

- `catalog.json` define nombres, etiquetas y categorías. `comparison.html`, `guia.html` y `404.html`
  son generados. La galería agrupa por categoría en el orden del catálogo y marca como
  «Nuevo» los iconos fuera de `scripts/core-icons.json`.
- Al añadir iconos, regenerar también `assets/brand/og-image.png` con `scripts/og_image.py`.
- La usuaria trabaja directamente en `main`: sin ramas ni pull requests.
- Validar XML, parejas, nombres, referencias y hashes piloto con `scripts/check.py`.

Revisión de cuervos: `raven` y `flying-raven` redibujados en ambos estilos a petición del usuario, con pico, cabeza y cola más reconocibles. Se actualizó la referencia de hashes de `raven` para reflejar el cambio autorizado.

- Licencias: iconos y marca CC BY 4.0 con mención obligatoria a Lannita Codes
  (https://lannitacodes.tumblr.com/); código MIT. Mantener la mención en la web y la guía.
  Cada SVG lleva como primer hijo el comentario de crédito
  `<!-- Lannita Icons · Iconos de Lannita Codes (https://lannitacodes.tumblr.com/) · CC BY 4.0, mención obligatoria -->`;
  los iconos nuevos deben incluirlo (check.py lo exige). Hashes piloto actualizados por este cambio autorizado.
