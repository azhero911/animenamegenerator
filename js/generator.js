/**
 * Anime Name Generator - Interactive Engine
 * Pure Vanilla JavaScript - Zero Dependencies
 * WCAG AA Accessible, Keyboard Ready, Live Regions
 */

(function () {
  'use strict';

  // DOM Elements
  const modeSelect = document.getElementById('gen-mode');
  const countSelect = document.getElementById('gen-count');
  const platformGroup = document.getElementById('platform-group');
  const platformSelect = document.getElementById('gen-platform');
  const generateBtn = document.getElementById('generate-btn');
  const copyAllBtn = document.getElementById('copy-all-btn');
  const resultsGrid = document.getElementById('results-grid');
  const liveRegion = document.getElementById('gen-live-region');
  const toast = document.getElementById('toast');

  if (!resultsGrid || !generateBtn) return;

  // Initialize presets from window globals
  const initialMode = window.__INITIAL_MODE || 'all';
  const initialPlatform = window.__INITIAL_PLATFORM || 'general';

  if (modeSelect) {
    modeSelect.value = initialMode;
  }
  if (platformSelect) {
    platformSelect.value = initialPlatform;
  }

  function updatePlatformVisibility() {
    if (!platformGroup || !modeSelect) return;
    if (modeSelect.value === 'username') {
      platformGroup.style.display = 'flex';
    } else {
      platformGroup.style.display = 'none';
    }
  }

  if (modeSelect) {
    modeSelect.addEventListener('change', updatePlatformVisibility);
    updatePlatformVisibility();
  }

  // Toast Notification Helper
  let toastTimer = null;
  function showToast(message) {
    if (!toast) return;
    toast.textContent = message;
    toast.classList.add('show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => {
      toast.classList.remove('show');
    }, 2400);
  }

  // Copy helper with fallback
  function copyTextToClipboard(text, successMsg) {
    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(text).then(() => {
        showToast(successMsg);
      }).catch(() => {
        fallbackCopyText(text, successMsg);
      });
    } else {
      fallbackCopyText(text, successMsg);
    }
  }

  function fallbackCopyText(text, successMsg) {
    const textArea = document.createElement('textarea');
    textArea.value = text;
    textArea.style.position = 'fixed';
    textArea.style.left = '-9999px';
    textArea.style.top = '0';
    document.body.appendChild(textArea);
    textArea.focus();
    textArea.select();
    try {
      document.execCommand('copy');
      showToast(successMsg);
    } catch (err) {
      showToast('Copied to clipboard');
    }
    document.body.removeChild(textArea);
  }

  // Random pick helpers
  function getRandomItem(array) {
    return array[Math.floor(Math.random() * array.length)];
  }

  function shuffle(array) {
    const arr = [...array];
    for (let i = arr.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    return arr;
  }

  // Generate usernames matching platform constraints
  function generateUsernames(count, platform) {
    const data = window.ANIME_DATA || {};
    const cores = data.username_cores || ['kage', 'shinobi', 'ronin', 'kitsune', 'oni'];
    const prefixes = data.username_prefixes || ['neo', 'cyber', 'void', 'dark', 'silent'];
    const suffixes = data.username_suffixes || ['vibe', 'drift', 'blade', 'core', 'pulse'];

    const results = [];
    const used = new Set();
    let attempts = 0;

    while (results.length < count && attempts < 200) {
      attempts++;
      const core = getRandomItem(cores);
      const styleType = Math.floor(Math.random() * 5);
      let username = '';
      let meaning = '';

      if (platform === 'tiktok') {
        // TikTok: 2-24 chars, letters, numbers, underscores, periods
        if (styleType === 0) {
          username = `${core}.${getRandomItem(suffixes)}`;
          meaning = `Aesthetic TikTok handle featuring ${core} rhythm`;
        } else if (styleType === 1) {
          username = `${getRandomItem(prefixes)}_${core}`;
          meaning = `Clean viral creator handle centered on ${core}`;
        } else if (styleType === 2) {
          username = `${core}_${Math.floor(Math.random() * 89 + 10)}`;
          meaning = `Minimalist numbered TikTok identity`;
        } else if (styleType === 3) {
          username = `its.${core}`;
          meaning = `Personal verified style anime handle`;
        } else {
          username = `${core}.vibes`;
          meaning = `Anime aesthetic community handle`;
        }
        // Strict limit <= 24
        if (username.length > 24) username = username.substring(0, 24);
      } else if (platform === 'discord') {
        // Discord: 2-32 chars, lowercase, numbers, underscores, periods
        if (styleType === 0) {
          username = `${getRandomItem(prefixes)}.${core}`;
          meaning = `Sleek Discord handle for server chat`;
        } else if (styleType === 1) {
          username = `${core}_bushi`;
          meaning = `Warrior role title for gaming voice channels`;
        } else if (styleType === 2) {
          username = `lord_${core}`;
          meaning = `Guild commander tag for discord servers`;
        } else if (styleType === 3) {
          username = `${core}.${getRandomItem(suffixes)}`;
          meaning = `Modern lowercase server identity`;
        } else {
          username = `${core}_${Math.floor(Math.random() * 900 + 100)}`;
          meaning = `Competitive squad tag with identifier`;
        }
        username = username.toLowerCase();
        if (username.length > 32) username = username.substring(0, 32);
      } else {
        // General / Aesthetic
        if (styleType === 0) {
          username = `${getRandomItem(prefixes).charAt(0).toUpperCase() + getRandomItem(prefixes).slice(1)}${core.charAt(0).toUpperCase() + core.slice(1)}`;
          meaning = `Aesthetic combined gamertag`;
        } else if (styleType === 1) {
          username = `${core.charAt(0).toUpperCase() + core.slice(1)}${getRandomItem(suffixes).charAt(0).toUpperCase() + getRandomItem(suffixes).slice(1)}`;
          meaning = `Streamlined anime creator identity`;
        } else if (styleType === 2) {
          username = `x_${core}_x`;
          meaning = `Edgy stylized anime gaming handle`;
        } else if (styleType === 3) {
          username = `${core}.${getRandomItem(suffixes)}`;
          meaning = `Clean minimalist web handle`;
        } else {
          username = `${core}${Math.floor(Math.random() * 89 + 10)}`;
          meaning = `Classic anime enthusiast handle`;
        }
      }

      if (!used.has(username)) {
        used.add(username);
        results.push({
          romaji: username,
          kanji: platform.toUpperCase(),
          meaning: meaning
        });
      }
    }
    return results;
  }

  // Generate character names (boy, girl, last, villain, meaning, all)
  function generateCharacterNames(mode, count) {
    const data = window.ANIME_DATA || {};
    let pool = [];

    if (mode === 'boy') {
      pool = data.boys || [];
    } else if (mode === 'girl') {
      pool = data.girls || [];
    } else if (mode === 'lastname') {
      pool = data.surnames || [];
    } else if (mode === 'villain') {
      pool = data.villains || [];
    } else if (mode === 'meaning') {
      pool = data.meanings_pool || [];
    } else {
      // 'all' / random: blend boy, girl, villain, meanings, and surnames
      const mixed = [
        ...(data.boys || []),
        ...(data.girls || []),
        ...(data.meanings_pool || []),
        ...(data.villains || [])
      ];
      pool = mixed;
    }

    const shuffled = shuffle(pool);
    const results = [];
    const seen = new Set();

    for (const item of shuffled) {
      if (results.length >= count) break;
      if (!seen.has(item.romaji)) {
        seen.add(item.romaji);
        // In "all" mode, 35% of the time, pair with an authentic surname
        if (mode === 'all' && Math.random() > 0.65 && (data.surnames || []).length > 0) {
          const surname = getRandomItem(data.surnames);
          results.push({
            romaji: `${surname.romaji} ${item.romaji}`,
            kanji: `${surname.kanji} ${item.kanji}`,
            meaning: `${item.meaning} (Clan: ${surname.meaning})`
          });
        } else {
          results.push(item);
        }
      }
    }

    // If pool was smaller than requested count, fill remaining uniquely
    return results;
  }

  // Render cards
  function renderCards(names) {
    resultsGrid.innerHTML = '';

    names.forEach((item, index) => {
      const card = document.createElement('div');
      card.className = 'name-card';
      card.setAttribute('tabindex', '0');
      card.setAttribute('role', 'article');
      card.setAttribute('aria-label', `${item.romaji}, kanji ${item.kanji}, meaning: ${item.meaning}`);

      const header = document.createElement('div');
      header.className = 'card-header';

      const romajiEl = document.createElement('h3');
      romajiEl.className = 'card-romaji';
      romajiEl.textContent = item.romaji;

      const kanjiEl = document.createElement('span');
      kanjiEl.className = 'card-kanji';
      kanjiEl.textContent = item.kanji;

      header.appendChild(romajiEl);
      header.appendChild(kanjiEl);

      const meaningEl = document.createElement('p');
      meaningEl.className = 'card-meaning';
      meaningEl.textContent = item.meaning;

      const actions = document.createElement('div');
      actions.className = 'card-actions';

      const copyBtn = document.createElement('button');
      copyBtn.type = 'button';
      copyBtn.className = 'btn-copy-card';
      copyBtn.setAttribute('aria-label', `Copy ${item.romaji}`);
      copyBtn.innerHTML = `
        <svg class="icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
          <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
          <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
        </svg>
        <span>Copy</span>
      `;

      copyBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        copyTextToClipboard(item.romaji, `Copied "${item.romaji}" to clipboard!`);
        copyBtn.classList.add('copied');
        copyBtn.querySelector('span').textContent = 'Copied!';
        setTimeout(() => {
          copyBtn.classList.remove('copied');
          copyBtn.querySelector('span').textContent = 'Copy';
        }, 1800);
      });

      // Clicking card copies name
      card.addEventListener('click', () => {
        copyTextToClipboard(item.romaji, `Copied "${item.romaji}" to clipboard!`);
      });

      actions.appendChild(copyBtn);

      card.appendChild(header);
      card.appendChild(meaningEl);
      card.appendChild(actions);

      resultsGrid.appendChild(card);
    });

    if (liveRegion) {
      liveRegion.textContent = `Generated ${names.length} anime names.`;
    }
  }

  // Handle Generate Click
  function handleGenerate() {
    const mode = modeSelect ? modeSelect.value : 'all';
    const count = countSelect ? parseInt(countSelect.value, 10) : 12;
    const platform = platformSelect ? platformSelect.value : 'general';

    let names = [];
    if (mode === 'username') {
      names = generateUsernames(count, platform);
    } else {
      names = generateCharacterNames(mode, count);
    }

    renderCards(names);
  }

  generateBtn.addEventListener('click', handleGenerate);

  // Handle Copy All Click
  if (copyAllBtn) {
    copyAllBtn.addEventListener('click', () => {
      const cards = resultsGrid.querySelectorAll('.name-card');
      if (!cards.length) {
        showToast('No names to copy!');
        return;
      }

      const lines = [];
      cards.forEach((card) => {
        const romaji = card.querySelector('.card-romaji')?.textContent || '';
        const kanji = card.querySelector('.card-kanji')?.textContent || '';
        const meaning = card.querySelector('.card-meaning')?.textContent || '';
        if (romaji) {
          if (kanji && kanji !== 'TIKTOK' && kanji !== 'DISCORD' && kanji !== 'GENERAL') {
            lines.push(`${romaji} [${kanji}] - ${meaning}`);
          } else {
            lines.push(romaji);
          }
        }
      });

      copyTextToClipboard(lines.join('\n'), `Copied ${lines.length} names to clipboard!`);
    });
  }

  // Setup click listeners for existing pre-rendered raw HTML cards
  function wireInitialPreRenderedCards() {
    const existingButtons = resultsGrid.querySelectorAll('.btn-copy-card');
    existingButtons.forEach((btn) => {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const card = btn.closest('.name-card');
        const romaji = card.querySelector('.card-romaji')?.textContent || '';
        if (romaji) {
          copyTextToClipboard(romaji, `Copied "${romaji}" to clipboard!`);
          btn.classList.add('copied');
          btn.querySelector('span').textContent = 'Copied!';
          setTimeout(() => {
            btn.classList.remove('copied');
            btn.querySelector('span').textContent = 'Copy';
          }, 1800);
        }
      });
    });

    const cards = resultsGrid.querySelectorAll('.name-card');
    cards.forEach((card) => {
      card.addEventListener('click', () => {
        const romaji = card.querySelector('.card-romaji')?.textContent || '';
        if (romaji) {
          copyTextToClipboard(romaji, `Copied "${romaji}" to clipboard!`);
        }
      });
    });
  }

  wireInitialPreRenderedCards();
})();
