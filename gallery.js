const search = document.querySelector('#search');
const chips = [...document.querySelectorAll('.chip')];
const sections = [...document.querySelectorAll('section.category')];
const status = document.querySelector('#status');
let category = '';
const normalize = value => value.normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase().trim();

function filter() {
  const query = normalize(search.value);
  let visible = 0;
  for (const section of sections) {
    let inSection = 0;
    for (const card of section.querySelectorAll('article')) {
      card.hidden = !(normalize(card.dataset.search).includes(query) && (!category || card.dataset.category === category));
      if (!card.hidden) inSection++;
    }
    section.hidden = inSection === 0;
    visible += inSection;
  }
  document.querySelector('#count').textContent = `${visible} ${visible === 1 ? 'icono' : 'iconos'} · ${visible * 2} variantes`;
  document.querySelector('#empty').hidden = visible !== 0;
}

search.addEventListener('input', filter);
for (const chip of chips) {
  chip.addEventListener('click', () => {
    category = chip.dataset.category;
    for (const other of chips) other.setAttribute('aria-pressed', String(other === chip));
    filter();
  });
}
document.querySelector('#color').addEventListener('input', event => document.documentElement.style.setProperty('--icon-color', event.target.value));

let toastTimer;
function announce(message) {
  status.textContent = message;
  status.classList.add('show');
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => status.classList.remove('show'), 2200);
}

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
    announce(`HTML copiado: ${button.dataset.name} (${button.dataset.style})`);
  } catch {
    const dialog = document.querySelector('#copy-fallback');
    dialog.querySelector('textarea').value = html;
    dialog.showModal(); dialog.querySelector('textarea').select();
  }
});
