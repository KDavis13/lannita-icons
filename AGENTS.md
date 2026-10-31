# Convenciones de Lannita Icons

- Mantener exactamente los 10 iconos piloto hasta una solicitud de ampliar catálogo.
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
  recursos de marca separados del catálogo de 10 pares. Se permiten los colores
  de marca fijos y texto con fuentes del sistema en el logo. Mantener la cabecera
  accesible y el favicon enlazado con rutas relativas para GitHub Pages.
