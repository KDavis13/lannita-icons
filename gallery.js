const search = document.querySelector('#search');
const category = document.querySelector('#category');
const cards = [...document.querySelectorAll('article')];
const normalize = value => value.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase().trim();
function filter() {
  let visible = 0;
  for (const card of cards) {
    card.hidden = !(normalize(card.dataset.search).includes(normalize(search.value)) && (!category.value || card.dataset.category === category.value));
    if (!card.hidden) visible++;
  }
  document.querySelector('#count').textContent = `${visible} ${visible === 1 ? "icono" : "iconos"} · ${visible * 2} variantes`;
  document.querySelector('#empty').hidden = visible !== 0;
}
search.addEventListener('input', filter);
category.addEventListener('change', filter);
document.querySelector('#color').addEventListener('input', event => document.documentElement.style.setProperty('--icon-color', event.target.value));
let copies = 0;
document.querySelector('main').addEventListener('click', async event => {
  const button = event.target.closest('button[data-name]');
  if (!button) return;
  const svg = button.closest('.variant').querySelector('svg').cloneNode(true);
  // Every pasted instance needs distinct mask IDs, including repeated copies.
  const prefix = `li-${Date.now().toString(36)}-${++copies}-`;
  for (const node of svg.querySelectorAll('[id]')) {
    const old = node.id;
    node.id = prefix + old;
    for (const reference of svg.querySelectorAll('[mask]')) {
      if (reference.getAttribute('mask') === `url(#${old})`) reference.setAttribute('mask', `url(#${node.id})`);
    }
  }
  svg.setAttribute('width', '1em'); svg.setAttribute('height', '1em');
  const html = svg.outerHTML;
  try {
    await navigator.clipboard.writeText(html);
    document.querySelector('#status').textContent = `HTML copiado: ${button.dataset.name} (${button.dataset.style}).`;
  } catch {
    const dialog = document.querySelector('#copy-fallback');
    dialog.querySelector('textarea').value = html;
    dialog.showModal(); dialog.querySelector('textarea').select();
  }
});
