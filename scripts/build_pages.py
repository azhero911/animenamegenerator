"""
Builds all 9 content pages, plus /about.html, /privacy.html, and 404.html
with complete raw HTML content, prefilled generator cards, unique sections,
JSON-LD schemas, and strict SEO rules.
"""

import json
import os
import re

with open("scripts/static_names.json", "r", encoding="utf-8") as f:
    STATIC_DATA = json.load(f)

PAGES_CONFIG = [
    {
        "filename": "index.html",
        "url_path": "/",
        "mode": "all",
        "platform": "general",
        "primary_keyword": "anime name generator",
        "secondary_keywords": ["random anime name generator", "anime character name generator", "japanese anime name generator", "anime oc name generator"],
        "title": "Anime Name Generator: Random Japanese Names + Kanji",
        "h1": "Anime Name Generator",
        "meta_desc": "Generate authentic Japanese character names with our anime name generator. Explore kanji, romaji, and English meanings with one-click copy and instant export.",
        "og_image": "og-anime-name-generator.png",
        "is_home": True,
        "static_key": "home",
        "intro_p1": "Welcome to the ultimate anime name generator, engineered for writers, novelists, manga creators, gamers, and tabletop roleplayers seeking authentic Japanese identities for their characters. Whether you are building an original shonen protagonist embarking on a perilous quest, a mysterious rogue swordsman wandering feudal provinces, or a charming slice-of-life persona for an urban drama, this tool crafts culturally rich combinations of Japanese given names and historical clan surnames complete with accurate kanji and poetic English translations.",
        "intro_p2": "Our japanese anime name generator seamlessly unites classical samurai heritage, regional Shinto folklore, and contemporary manga naming tropes into one intuitive workspace. Unlike generic web randomizers that produce awkward phonetic gibberish or misspelled readings, every entry generated here features verified kanji calligraphy, authentic on'yomi and kun'yomi pronunciation, and rich narrative symbolism. You can explore our random anime name generator modes, filter by character archetypes, and discover resonant titles with effortless one-click copying for your light novels, scripts, or gaming profiles.",
        "h2_primary": "How Our Anime Name Generator Creates Authentic Japanese Names",
        "h2_secondaries": [
            "Explore the Random Anime Name Generator and Custom Modes",
            "Crafting Believable Characters with an Anime OC Name Generator",
            "Frequently Asked Questions About Anime Character Names"
        ],
        "unique_section_title": "How the Generator Works and What the Modes Do",
        "unique_section_content": """
          <p>Our generator operates on a dual-layer linguistic engine that pairs Japanese onomastic traditions with anime narrative archetypes. When you select a mode, the algorithm draws from vetted dictionaries containing verified kanji pairings, historical clan surnames, and symbolic epithets.</p>
          <div class="feature-callout">
            <h4>Algorithm Breakdown & Generation Modes</h4>
            <ul>
              <li><strong>All / Random Mode:</strong> Seamlessly balances hero names, elegant classical names, and iconic multi-part names (family name + given name). In 35% of generations, it pairs renowned historical clan surnames with complementary given names.</li>
              <li><strong>Boy & Girl Modes:</strong> Filters specifically for masculine kanji roots (such as <em>-ro</em>, <em>-to</em>, <em>-ki</em>) and feminine floral or virtue roots (such as <em>-ko</em>, <em>-mi</em>, <em>-ka</em>).</li>
              <li><strong>Surnames (Last Names):</strong> Curates noble samurai lineages, geographical markers (mountains, rivers, rice paddies), and historical Sengoku era clan identities.</li>
              <li><strong>Names with Meaning:</strong> Prioritizes deep elemental, astrological, and philosophical kanji with rich backstory descriptions.</li>
              <li><strong>Villain Mode:</strong> Selects ominous kanji associated with shadows, curses, blades, and mythical yokai.</li>
              <li><strong>Username Mode:</strong> Formats names for digital handles across platforms, honoring specific length and character requirements.</li>
            </ul>
          </div>
          <p>Every dynamic generation guarantees zero duplicates within a batch, giving you fresh inspiration each time you click generate.</p>
        """,
        "faqs": [
            {
                "q": "How does this anime name generator select kanji for each name?",
                "a": "Every name in our database is paired with authentic Japanese kanji characters chosen for their historical validity and poetic meaning. We verify on'yomi and kun'yomi readings to ensure linguistic correctness."
            },
            {
                "q": "Can I use these generated names for commercial manga, light novels, or games?",
                "a": "Yes. All names generated by this tool are free to use in your creative projects, including published light novels, webcomics, indie video games, and tabletop roleplaying campaigns."
            },
            {
                "q": "What is the difference between romaji and kanji in the results?",
                "a": "Romaji represents the Japanese pronunciation spelled out using the Latin alphabet (such as Kazuki), while kanji represents the traditional logographic characters adopted from Chinese (such as 一輝), conveying symbolic meaning."
            },
            {
                "q": "Does the generator include authentic Japanese surnames?",
                "a": "Yes. When using the default generator or the dedicated surname filter, names can include authentic clan surnames such as Takahashi, Fujimoto, and Minamoto."
            }
        ],
        "related": [
            {"title": "Anime Boy Names", "path": "/anime-boy-names", "desc": "Cool masculine Japanese names with traditional kanji endings."},
            {"title": "Anime Girl Names", "path": "/anime-girl-names", "desc": "Cute, graceful female character names with poetic meanings."},
            {"title": "Anime Names With Meaning", "path": "/anime-names-with-meaning", "desc": "Deep philosophical, elemental, and nature-inspired names."}
        ]
    },
    {
        "filename": "anime-username-generator.html",
        "url_path": "/anime-username-generator",
        "mode": "username",
        "platform": "general",
        "primary_keyword": "anime username generator",
        "secondary_keywords": ["cool anime usernames", "aesthetic anime usernames", "anime username ideas"],
        "title": "Anime Username Generator: Cool & Aesthetic Usernames",
        "h1": "Anime Username Generator",
        "meta_desc": "Create aesthetic handles and gamertags with our anime username generator. Discover cool anime usernames with clean style, zero repeats, and instant copying.",
        "og_image": "og-anime-username-generator.png",
        "is_home": False,
        "breadcrumb_name": "Anime Username Generator",
        "static_key": "username",
        "intro_p1": "Elevate your online presence with our specialized anime username generator, built to generate unforgettable gamertags, social handles, and streaming identities across the digital web. Finding cool anime usernames that are not already claimed by other players can often feel frustrating on competitive multiplayer networks and community forums. That is why our creative engine crafts balanced, aesthetically pleasing username combinations that fuse iconic Japanese anime terminology with contemporary digital naming conventions, streaming trends, and gaming slang.",
        "intro_p2": "From minimalist cyber-samurai tags to lo-fi aesthetic anime usernames, our curated algorithm creates clean variations without awkward random symbol clutter, messy punctuation, or unreadable letter spam. Whether you need a fresh identity for Twitch streaming, Steam leaderboards, Discord servers, or mobile social networks, you will discover hundreds of creative anime username ideas tailored to your personal vibe. Simply select your preferred batch count, customize your platform styling, and copy your brand-new digital handle with a single click.",
        "h2_primary": "Generate Cool Anime Usernames with Clean Aesthetic Balance",
        "h2_secondaries": [
            "Finding Aesthetic Anime Usernames That Stand Out",
            "Creative Anime Username Ideas for Gamers and Creators",
            "Frequently Asked Questions About Anime Usernames"
        ],
        "unique_section_title": "How to Build a Memorable Anime Username (Cores, Prefixes & Numbers)",
        "unique_section_content": """
          <p>A memorable anime handle relies on structure rather than random punctuation. When building an aesthetic username, top creators use a proven tripartite architecture: a thematic core, a tonal modifier, and an optional subtle delimiter.</p>
          <div class="feature-callout">
            <h4>Anatomy of a High-Tier Anime Username</h4>
            <ul>
              <li><strong>Thematic Core:</strong> The anchor of your identity. Choose an iconic anime archetype or element, such as <em>Ronin</em> (wandering samurai), <em>Kage</em> (shadow), <em>Kitsune</em> (fox spirit), or <em>Senshi</em> (warrior).</li>
              <li><strong>Tonal Prefixes:</strong> Establish your aesthetic vibe. Clean modifiers like <em>Neo</em>, <em>Cyber</em>, <em>Silent</em>, <em>Astro</em>, or <em>Void</em> instantly frame the genre of your profile.</li>
              <li><strong>Dynamic Suffixes:</strong> Add motion or atmosphere with endings like <em>Pulse</em>, <em>Drift</em>, <em>Blade</em>, <em>Core</em>, or <em>Haze</em>.</li>
              <li><strong>Intelligent Delimiters:</strong> Avoid cluttering your handle with excessive underscores (e.g., <code>xX_ronin_Xx</code>). Instead, use clean single periods or low-profile separators like <code>kage.pulse</code> or <code>void.ronin</code>.</li>
              <li><strong>Styling Numbers:</strong> If your chosen handle is taken, avoid random strings like <code>7834</code>. Instead, opt for thematic numbers such as <code>00</code> (cyborg prototype), <code>07</code>, or area codes like <code>03</code> (Tokyo).</li>
            </ul>
          </div>
          <p>By blending these components, you maintain readability while ensuring your handle looks sleek on leaderboards and profile cards.</p>
        """,
        "faqs": [
            {
                "q": "What makes an anime username aesthetic?",
                "a": "Aesthetic anime usernames rely on balanced syllable rhythm, evocative Japanese words like kage or yume, and minimalist formatting without excessive numbers or chaotic symbols."
            },
            {
                "q": "Can I use these handles for gaming platforms like Steam and Riot Games?",
                "a": "Yes. The generated usernames fit character length guidelines across Steam, Epic Games, Riot, PlayStation Network, and Xbox Live."
            },
            {
                "q": "How can I tell if a generated username is available?",
                "a": "Because our generator combines diverse prefixes, cores, and suffixes, many generated combinations remain unclaimed. You can test your favorites directly on your desired platform's sign-up page."
            },
            {
                "q": "Are these usernames safe from profanity filters?",
                "a": "Yes. Our naming dictionary is rigorously vetted to exclude offensive terms, slurs, and accidental inappropriate slang in both English and Japanese."
            }
        ],
        "related": [
            {"title": "Anime Usernames for TikTok", "path": "/anime-usernames-for-tiktok", "desc": "Snappy, viral anime handles formatted specifically under 24 characters."},
            {"title": "Anime Usernames for Discord", "path": "/anime-usernames-for-discord", "desc": "Clean handles and guild nicknames optimized for Discord servers."},
            {"title": "Anime Villain Names", "path": "/anime-villain-name-generator", "desc": "Dark, sinister antagonist names with menacing Japanese kanji."}
        ]
    },
    {
        "filename": "anime-usernames-for-tiktok.html",
        "url_path": "/anime-usernames-for-tiktok",
        "mode": "username",
        "platform": "tiktok",
        "primary_keyword": "anime usernames for tiktok",
        "secondary_keywords": ["anime tiktok names", "anime tiktok username ideas"],
        "title": "Anime Usernames for TikTok: Free Generator & Ideas",
        "h1": "Anime Usernames for TikTok",
        "meta_desc": "Find aesthetic, viral anime usernames for tiktok under 24 characters. Generate clean anime tiktok names with zero duplicates, instant copy, and bio ready style.",
        "og_image": "og-anime-usernames-for-tiktok.png",
        "is_home": False,
        "breadcrumb_name": "Anime Usernames for TikTok",
        "static_key": "tiktok",
        "intro_p1": "Stand out on the For You page with our targeted generator for anime usernames for tiktok. Building a successful anime edit account, cosplay portfolio, or manga review channel requires an identity that is instantly catchy, effortless to spell, and visually clean on mobile phone screens. Having a memorable username makes it substantially easier for viewers to search for your videos, recognize your brand in fast-moving comment sections, and follow your creator journey across social platforms over time.",
        "intro_p2": "TikTok enforces strict platform handle requirements that many creators overlook until their profile update fails. Our tool is programmed specifically to generate anime tiktok names that adhere strictly to TikTok's 24-character maximum length limit while maintaining sleek aesthetics and flawless readability. Explore viral anime tiktok username ideas featuring lo-fi chill vibes, shonen action themes, and pastel aesthetics ready for immediate copy-pasting directly into your profile settings without frustrating truncation errors, awkward underscores, or clunky punctuation.",
        "h2_primary": "Generate Viral Anime Usernames for TikTok That Fit Platform Limits",
        "h2_secondaries": [
            "Choosing Aesthetic Anime TikTok Names for Content Creators",
            "Fresh Anime TikTok Username Ideas for Edits and Cosplay",
            "Frequently Asked Questions About TikTok Anime Usernames"
        ],
        "unique_section_title": "TikTok Username Guidelines: Length Limits, Style Tips & Mistakes to Avoid",
        "unique_section_content": """
          <p>TikTok is a mobile-first visual platform where your handle appears on every video overlay, comment thread, and search snippet. To maximize discoverability, your handle must follow official TikTok standards while remaining appealing.</p>
          <div class="feature-callout">
            <h4>Verified TikTok Username Rules & Optimization Strategies</h4>
            <ul>
              <li><strong>Strict 24-Character Limit:</strong> TikTok usernames can only be up to 24 characters long. Our generator strictly caps every suggestion well below this threshold.</li>
              <li><strong>Allowed Characters:</strong> Only letters, numbers, underscores (<code>_</code>), and periods (<code>.</code>) are permitted. Periods cannot be placed at the very end of your handle.</li>
              <li><strong>30-Day Change Restriction:</strong> TikTok only allows you to change your username once every 30 days. Selecting a timeless anime handle prevents you from getting locked into a name you dislike.</li>
              <li><strong>Lowercase Aesthetic:</strong> Lowercase usernames (such as <code>senpai.vibe</code> or <code>chibi_kage</code>) look substantially cleaner on mobile video feeds than capitalized or fragmented words.</li>
              <li><strong>What to Avoid:</strong> Avoid stacking multiple underscores (e.g., <code>__otaku__</code>), which looks bot-like, harms search rankings, and makes your handle difficult for fans to tag in video duets.</li>
            </ul>
          </div>
          <p>Combine a tight niche keyword (like <em>edits</em>, <em>cuts</em>, or <em>lore</em>) with your favorite anime concept to signal your content focus immediately to the TikTok recommendation algorithm.</p>
        """,
        "faqs": [
            {
                "q": "What are the exact character limits for TikTok usernames?",
                "a": "TikTok usernames must be between 2 and 24 characters in length and may only contain letters, numbers, underscores, and periods. They cannot end with a period."
            },
            {
                "q": "How often can I change my TikTok username?",
                "a": "TikTok permits username changes once every 30 days. Be sure to test your favorite handle before confirming the change in your profile settings."
            },
            {
                "q": "Why does a clean anime username help on TikTok?",
                "a": "Clean handles without symbol clutter are easier for viewers to remember, pronounce in video voiceovers, and tag in comments and stitches, which boosts overall algorithmic reach."
            },
            {
                "q": "Can I use Japanese kanji directly in my TikTok username?",
                "a": "No, TikTok usernames only permit alphanumeric Latin characters, periods, and underscores. However, you can place Japanese kanji in your TikTok Display Name (nickname)."
            }
        ],
        "related": [
            {"title": "Anime Username Generator", "path": "/anime-username-generator", "desc": "Universal aesthetic handles and gamertags for creators and gamers."},
            {"title": "Anime Usernames for Discord", "path": "/anime-usernames-for-discord", "desc": "Discord server nicknames and handles tailored to 32 characters."},
            {"title": "Anime Girl Names", "path": "/anime-girl-names", "desc": "Cute and elegant Japanese female names with authentic kanji."}
        ]
    },
    {
        "filename": "anime-usernames-for-discord.html",
        "url_path": "/anime-usernames-for-discord",
        "mode": "username",
        "platform": "discord",
        "primary_keyword": "anime usernames for discord",
        "secondary_keywords": ["anime discord names", "anime discord nicknames"],
        "title": "Anime Usernames for Discord: Free Generator & Ideas",
        "h1": "Anime Usernames for Discord",
        "meta_desc": "Generate unique anime usernames for discord and server display nicknames. Meets the 32-character limit with aesthetic formats and instant one-click copying.",
        "og_image": "og-anime-usernames-for-discord.png",
        "is_home": False,
        "breadcrumb_name": "Anime Usernames for Discord",
        "static_key": "discord",
        "intro_p1": "Personalize your gaming presence with our custom generator for anime usernames for discord. Whether you are leading a competitive esports gaming guild, hanging out in community anime servers, or organizing raid voice channels with close friends, having a distinct identity sets an unforgettable tone. Discord's unique naming architecture allows for both unique global account handles and flexible server display nicknames, giving users tremendous room for personal expression and creative flair across different gaming communities and clan lobbies.",
        "intro_p2": "Our tool generates cool anime discord names tailored specifically to Discord's modern handle system. All generated suggestions stay strictly within Discord's 32-character limit while maintaining sharp visual contrast on server role lists and active voice chats. Explore diverse anime discord nicknames, from stoic warrior titles to cyberpunk operative tags, with effortless single-click copying for both your global profile and server-specific nicknames without cluttering your chat messages or obscuring team callouts during competitive matches.",
        "h2_primary": "Find Unique Anime Usernames for Discord and Server Nicknames",
        "h2_secondaries": [
            "Formatting Cool Anime Discord Names for Member Lists",
            "Creative Anime Discord Nicknames for Gaming Guilds",
            "Frequently Asked Questions About Discord Anime Usernames"
        ],
        "unique_section_title": "Discord Identity Breakdown: Usernames vs Display Names & Role Styling",
        "unique_section_content": """
          <p>Discord uses a dual-identity architecture: your unique <strong>Username</strong> (account handle) and your flexible <strong>Display Name / Server Nickname</strong>. Understanding the technical rules between them lets you customize your profile effectively.</p>
          <div class="feature-callout">
            <h4>Discord Naming Rules and Formatting Best Practices</h4>
            <ul>
              <li><strong>Global Usernames (Handles):</strong> Must be between 2 and 32 characters long. They must be strictly lowercase alphanumeric characters, with periods (<code>.</code>) and underscores (<code>_</code>) allowed. No consecutive periods or special unicode symbols.</li>
              <li><strong>Display Names & Server Nicknames:</strong> Also capped at 32 characters, but they support unicode characters, full Japanese kanji (e.g. <code>影武士 | Kage</code>), and custom emojis.</li>
              <li><strong>Member List Visibility:</strong> In busy Discord servers, colored role tags often crowd the sidebar. A concise name between 6 and 14 characters ensures your name is never truncated with an ellipsis.</li>
              <li><strong>Voice Channel Clarity:</strong> When teammates call out callouts during fast-paced games, having a clean two-syllable root (like <em>Ryu</em>, <em>Kage</em>, or <em>Tengu</em>) ensures clear communication over voice comms.</li>
            </ul>
          </div>
          <p>Use our generator to grab a clean lowercase handle for your global account, then pair it with an authentic kanji tag in your server nickname for maximum prestige.</p>
        """,
        "faqs": [
            {
                "q": "What are the rules for Discord's new username system?",
                "a": "Discord usernames are unique, all-lowercase, 2 to 32 characters in length, and can only contain letters (a-z), numbers (0-9), periods, and underscores without discriminatory discriminators (#0000)."
            },
            {
                "q": "Can I use Japanese kanji in my Discord server nickname?",
                "a": "Yes! While global usernames are restricted to lowercase Latin characters, your Display Name and server nicknames support full Japanese kanji and unicode characters."
            },
            {
                "q": "How long can a Discord display name be?",
                "a": "Discord display names and server nicknames can be up to 32 characters long, matching the limit enforced by our generator."
            },
            {
                "q": "How do I change my nickname in a specific Discord server?",
                "a": "Click the server name in the top left, select 'Edit Server Profile', and enter your desired anime nickname into the 'Server Nickname' text field."
            }
        ],
        "related": [
            {"title": "Anime Username Generator", "path": "/anime-username-generator", "desc": "Universal aesthetic usernames and gamer handles."},
            {"title": "Anime Usernames for TikTok", "path": "/anime-usernames-for-tiktok", "desc": "Punchy viral handles optimized for the 24-character TikTok limit."},
            {"title": "Anime Villain Names", "path": "/anime-villain-name-generator", "desc": "Dark, imposing names perfect for gaming guild masters."}
        ]
    },
    {
        "filename": "anime-names-with-meaning.html",
        "url_path": "/anime-names-with-meaning",
        "mode": "meaning",
        "platform": "general",
        "primary_keyword": "anime names with meaning",
        "secondary_keywords": ["anime names and meanings", "anime name generator with kanji", "japanese names with meanings"],
        "title": "Anime Names With Meaning: Kanji, Romaji and Origins",
        "h1": "Anime Names With Meaning",
        "meta_desc": "Discover deep anime names with meaning, complete with kanji calligraphy and romaji origins. Find spiritual, nature, and symbolic Japanese character names now.",
        "og_image": "og-anime-names-with-meaning.png",
        "is_home": False,
        "breadcrumb_name": "Anime Names With Meaning",
        "static_key": "meaning",
        "intro_p1": "Every memorable character in Japanese animation carries a title that foreshadows their destiny, and our database of anime names with meaning reveals the profound symbolism behind authentic Japanese naming traditions. In classical Japanese storytelling, names are rarely chosen for superficial sound alone; each character's kanji represents their elemental affinity, inner moral virtue, ancestral heritage, or tragic narrative arc across their heroic journey through fantasy realms, martial tournaments, and mystical landscapes.",
        "intro_p2": "If you are looking for an anime name generator with kanji that provides authentic linguistic translations, our tool offers meticulously vetted entries for your creative projects. From names symbolizing fleeting fireflies in the twilight to eternal lotus blossoms rising from murky waters, exploring these anime names and meanings provides writers, worldbuilders, and novelists with deep cultural inspiration. Browse our curated collection below, or use the interactive tool above to generate new meaningful names with one-click copying for your manuscripts, manga scripts, and character design sheets.",
        "h2_primary": "Explore Authentic Anime Names With Meaning, Kanji, and Cultural Origins",
        "h2_secondaries": [
            "Understanding Symbolism in Japanese Names and Meanings",
            "Using an Anime Name Generator with Kanji for Rich Backstories",
            "Frequently Asked Questions About Japanese Name Meanings"
        ],
        "unique_section_title": "How Japanese Name Meanings Work: Kanji Readings, On'yomi, Kun'yomi & Ateji",
        "unique_section_content": """
          <p>Understanding Japanese name meanings requires looking beyond phonetic spelling into the logographic nature of kanji. Unlike English names where spelling dictates sound, Japanese kanji characters encode both concept and pronunciation.</p>
          <div class="feature-callout">
            <h4>Linguistic Nuances of Japanese Name Construction</h4>
            <ul>
              <li><strong>Kun'yomi (Native Japanese Readings):</strong> The native Japanese pronunciation of a character, often used for solitary kanji names rooted in nature, such as <em>Ren</em> (蓮 - Lotus) or <em>Kaede</em> (楓 - Maple).</li>
              <li><strong>On'yomi (Sino-Japanese Readings):</strong> Readings borrowed historically from the Chinese language, frequently combined in compound names like <em>Kazuhiko</em> (和彦 - Harmonious boy).</li>
              <li><strong>Nanori (Special Name Readings):</strong> Certain kanji possess rare pronunciations reserved exclusively for personal names, imbuing the individual with auspicious blessings.</li>
              <li><strong>Ateji (Phonetic Kanji Assignment):</strong> Manga authors frequently select kanji for their visual or poetic weight rather than strictly standard readings, creating iconic signature names that hint at secret supernatural abilities.</li>
              <li><strong>Nature and Virtue Roots:</strong> The most celebrated anime names feature elements like light (<em>hikari</em>), moon (<em>tsuki</em>), truthful heart (<em>makoto</em>), and ocean harbors (<em>minato</em>).</li>
            </ul>
          </div>
          <p>When selecting a name for your original character, matching the kanji's thematic weight with your character's emotional journey creates immediate resonance with your audience.</p>
        """,
        "faqs": [
            {
                "q": "Can the same Japanese name have different kanji meanings?",
                "a": "Yes. A single spoken name like 'Ren' can be written as 蓮 (lotus), 恋 (romantic love), or 廉 (honest integrity), completely transforming the character's thematic symbolism."
            },
            {
                "q": "Why do anime characters have deeply symbolic names?",
                "a": "Japanese writers utilize the visual and historical layers of kanji to foreshadow a character's destiny, elemental powers, or personality traits from the moment they are introduced."
            },
            {
                "q": "What are some of the most popular Japanese name meanings?",
                "a": "Auspicious themes such as celestial bodies (stars, sun, moon), blooming flora (sakura, lotus, wisteria), and moral virtues (courage, harmony, integrity) are among the most revered."
            },
            {
                "q": "How accurate are the translations provided on this page?",
                "a": "All kanji pairings and English translations on this site are researched and verified against authoritative Japanese onomastic dictionaries to ensure linguistic integrity."
            }
        ],
        "related": [
            {"title": "Anime Name Generator", "path": "/", "desc": "Our flagship tool with random Japanese names, kanji, and clan surnames."},
            {"title": "Anime Last Name Generator", "path": "/anime-last-name-generator", "desc": "Authentic Japanese family names and noble clan surnames with kanji."},
            {"title": "Anime Boy Names", "path": "/anime-boy-names", "desc": "Masculine Japanese names with traditional kanji and meanings."}
        ]
    },
    {
        "filename": "anime-last-name-generator.html",
        "url_path": "/anime-last-name-generator",
        "mode": "lastname",
        "platform": "general",
        "primary_keyword": "anime last name generator",
        "secondary_keywords": ["anime surname generator", "anime surnames", "japanese last names"],
        "title": "Anime Last Name Generator: Japanese Surnames + Kanji",
        "h1": "Anime Last Name Generator",
        "meta_desc": "Generate noble clan titles and authentic family names with our anime last name generator. Features accurate kanji, romaji readings, and English translations.",
        "og_image": "og-anime-last-name-generator.png",
        "is_home": False,
        "breadcrumb_name": "Anime Last Name Generator",
        "static_key": "lastname",
        "intro_p1": "Anchor your character in historical prestige and believable family heritage with our specialized anime last name generator. In Japanese culture and anime narratives, a character's surname carries tremendous emotional and social weight, signaling their clan lineage, ancestral territory, or social standing across feudal domains. Whether you are crafting a venerable martial arts dynasty, an aristocratic noble house, or a humble rural protagonist, an authentic surname is essential for believable storytelling and deep worldbuilding across chapters.",
        "intro_p2": "Our japanese last names engine avoids artificial combinations by referencing real historical clan registries and topographical naming conventions from ancient Japan. If you need a reliable anime surname generator for manga worldbuilding, light novels, or tabletop roleplay, this tool provides verified kanji, accurate romaji, and rich English translations. Explore famous anime surnames below or use the interactive generator to discover the ideal clan title for your story and memorable character cast across all ongoing arcs.",
        "h2_primary": "Generate Authentic Japanese Surnames with the Anime Last Name Generator",
        "h2_secondaries": [
            "The Historical Origins and Geography of Japanese Last Names",
            "Selecting Fitting Anime Surnames for Clans and Dynasties",
            "Frequently Asked Questions About Japanese Surnames"
        ],
        "unique_section_title": "Common Japanese Surname Patterns and Clan Tradition Table",
        "unique_section_content": """
          <p>The vast majority of Japanese surnames derive from topographic landmarks or historical samurai clans. Prior to the 1875 Meiji decree requiring all citizens to adopt a surname, family names were a privilege largely reserved for the aristocracy and warrior class.</p>
          <div class="feature-callout">
            <h4>Topographic Suffix Patterns in Japanese Surnames</h4>
            <ul>
              <li><strong>-ta / -da (田 - Rice Paddy):</strong> Demonstrates agrarian prosperity, found in widespread names like <em>Matsuda</em> (pine field), <em>Nishida</em> (west field), and <em>Yoshida</em>.</li>
              <li><strong>-kawa / -gawa (川 - River):</strong> Denotes settlements along vital waterways, exemplified by <em>Kurokawa</em> (black river) and <em>Hasegawa</em>.</li>
              <li><strong>-yama (山 - Mountain):</strong> Highlights high-altitude ancestral heritage, seen in <em>Shiroyama</em> (white mountain) and <em>Yamamoto</em>.</li>
              <li><strong>-to / -fuji (藤 - Wisteria):</strong> Traces historical ancestral ties to the imperial Fujiwara clan, forming celebrated surnames such as <em>Sato</em>, <em>Kato</em>, <em>Ito</em>, and <em>Fujimoto</em>.</li>
              <li><strong>-mura (村 - Village):</strong> Marks regional settlements and community leaders, as in <em>Yukimura</em> and <em>Nakamura</em>.</li>
            </ul>
          </div>
          <p>When naming a character, pairing a topographic surname with an elemental first name immediately evokes the natural landscapes of classical Japan.</p>
        """,
        "faqs": [
            {
                "q": "Do Japanese names write the last name or first name first?",
                "a": "In traditional Japanese order, the surname comes first followed by the given name (e.g., Takahashi Kazuki). In Western translations, the order is frequently reversed for international readers."
            },
            {
                "q": "What are the most common last names in Japan?",
                "a": "The five most common surnames across Japan are Sato (佐藤), Suzuki (鈴木), Takahashi (高橋), Tanaka (田中), and Watanabe (渡辺)."
            },
            {
                "q": "Why do so many Japanese surnames end in 'to' or 'fuji'?",
                "a": "Names ending with the kanji 藤 (such as Sato, Kato, and Saito) denote ancestral lineage or historical bureaucratic ties to the influential noble Fujiwara clan of the Heian era."
            },
            {
                "q": "Can I combine these last names with first names from other generators?",
                "a": "Absolutely. All surnames on this site are linguistically compatible with the given names found across our Boy, Girl, and Meaning generators."
            }
        ],
        "related": [
            {"title": "Anime Name Generator", "path": "/", "desc": "The primary generator featuring full Japanese names with both given names and surnames."},
            {"title": "Anime Names With Meaning", "path": "/anime-names-with-meaning", "desc": "Deep character names with rich kanji etymology and spiritual origins."},
            {"title": "Anime Boy Names", "path": "/anime-boy-names", "desc": "Strong male Japanese names with traditional kanji characters."}
        ]
    },
    {
        "filename": "anime-villain-name-generator.html",
        "url_path": "/anime-villain-name-generator",
        "mode": "villain",
        "platform": "general",
        "primary_keyword": "anime villain name generator",
        "secondary_keywords": ["anime villain names", "dark anime names", "evil anime names"],
        "title": "Anime Villain Name Generator: Dark, Evil Names + Kanji",
        "h1": "Anime Villain Name Generator",
        "meta_desc": "Forge menacing antagonist titles with our anime villain name generator. Browse dark anime names and sinister kanji meanings for manga villains and dark lords.",
        "og_image": "og-anime-villain-name-generator.png",
        "is_home": False,
        "breadcrumb_name": "Anime Villain Name Generator",
        "static_key": "villain",
        "intro_p1": "Every unforgettable anime story is driven by a formidable antagonist, and our anime villain name generator gives you the sinister titles needed to command fear and respect across your fantasy world. Great villains require names that send shivers down the reader's spine, echoing through dark dungeons and climactic battlegrounds. An imposing name conveys their merciless philosophy, supernatural curse, dark pact, forbidden bloodline, or tragic descent into destructive madness.",
        "intro_p2": "From ruthless mastermind tacticians manipulating politics to ancient mythical demons emerging from underworld rifts, our curated generator creates dark anime names grounded in ominous Japanese kanji and folklore lore. If you are developing an antagonist for your manga, novel, or tabletop campaign, exploring evil anime names with genuine linguistic weight ensures your villain feels menacing rather than cartoonish. Generate chilling anime villain names now with instant copy functionality for your dark lords, rogue sorcerers, shadowy guildmasters, and sinister assassins across all your creative chapters.",
        "h2_primary": "Forge Feared Antagonists with the Anime Villain Name Generator",
        "h2_secondaries": [
            "The Psychology Behind Iconic Anime Villain Names",
            "Crafting Dark Anime Names with Ominous Kanji and Mythology",
            "Frequently Asked Questions About Anime Villains"
        ],
        "unique_section_title": "Anime Villain Archetypes and How to Match a Name to Their Motive",
        "unique_section_content": """
          <p>A memorable villain name should mirror their psychological archetype. Giving a cold calculating strategist a berserker's name creates dissonance. Use these five core antagonist archetypes to match your villain's name to their narrative role:</p>
          <div class="feature-callout">
            <h4>The 5 Primary Villain Archetypes & Naming Conventions</h4>
            <ul>
              <li><strong>The Nihilistic Philosopher:</strong> Characters who believe existence is meaningless or rotten (e.g., <em>Mukuro</em> - Skeletal corpse, <em>Mugen</em> - Endless void). Their names feature kanji representing emptiness, illusions, or the pitch-black night.</li>
              <li><strong>The Fallen Hero:</strong> Former protectors corrupted by grief or betrayal (e.g., <em>Kageyoshi</em> - Shadow saint, <em>Zetsuei</em> - Severed shadow). Their names often pair a virtuous root with an ominous shadow modifier.</li>
              <li><strong>The Ruthless Mastermind:</strong> Calculating puppet masters who manipulate kingdoms from the shadows (e.g., <em>Yagami</em> - Night deity, <em>Genkaku</em> - Hallucination). Crisp, sophisticated syllables evoke intellect and calm menace.</li>
              <li><strong>The Bloodthirsty Berserker:</strong> Unstoppable physical forces driven by slaughter and chaos (e.g., <em>Rasetsu</em> - Flesh-devouring demon, <em>Ryuuketsu</em> - Flowing blood). Sharp consonants and guttural sounds communicate raw violence.</li>
              <li><strong>The Eldritch Calamity:</strong> Ancient gods or curses that threaten the cosmos (e.g., <em>Orochi</em> - Mythic serpent, <em>Jigoku</em> - Subterranean hell). Traditional mythological yokai titles give these entities primordial terror.</li>
            </ul>
          </div>
          <p>Pairing these archetypes with vetted kanji guarantees that your antagonist leaves a permanent impression on your readers.</p>
        """,
        "faqs": [
            {
                "q": "What makes an anime villain name sound intimidating?",
                "a": "Intimidating villain names frequently employ sharp consonants (k, r, z), ominous kanji concepts (shadow, void, blood, demon), and concise, striking syllable cadences."
            },
            {
                "q": "Are these names based on actual Japanese mythology?",
                "a": "Yes. Many entries draw inspiration from classical Shinto and Buddhist folklore, including yokai, oni, raksasa demons, and underworld judges like Enma."
            },
            {
                "q": "Can villain names also be used for anti-heroes?",
                "a": "Certainly. Morally ambiguous anti-heroes, renegade ninjas, and dark fantasy protagonists frequently share the aesthetic naming conventions of villains."
            },
            {
                "q": "Do these names contain offensive slurs?",
                "a": "No. While the meanings represent dark concepts such as shadows, curses, and blades, every entry has been curated to ensure zero real-world slurs or inappropriate vulgarities."
            }
        ],
        "related": [
            {"title": "Anime Name Generator", "path": "/", "desc": "Balanced Japanese character names for heroes and protagonists."},
            {"title": "Anime Usernames for Discord", "path": "/anime-usernames-for-discord", "desc": "Intimidating handles and clan nicknames for gaming servers."},
            {"title": "Anime Last Name Generator", "path": "/anime-last-name-generator", "desc": "Historical samurai clan surnames to establish ancient villainous dynasties."}
        ]
    },
    {
        "filename": "anime-boy-names.html",
        "url_path": "/anime-boy-names",
        "mode": "boy",
        "platform": "general",
        "primary_keyword": "anime boy names",
        "secondary_keywords": ["anime name generator male", "anime male names", "japanese boy names"],
        "title": "Anime Boy Names: Cool Japanese Male Names with Kanji",
        "h1": "Anime Boy Names",
        "meta_desc": "Explore heroic and handsome anime boy names with authentic kanji, romaji, and meanings. Pick traditional endings like -ro and -to with instant one-click copy.",
        "og_image": "og-anime-boy-names.png",
        "is_home": False,
        "breadcrumb_name": "Anime Boy Names",
        "static_key": "boy",
        "intro_p1": "Discover inspiring, heroic, and handsome anime boy names crafted with authentic Japanese kanji, accurate romaji pronunciation, and resonant English meanings for your original characters. From spirited shonen champions charging headfirst into fierce battle to calm, analytical rivals observing strategically from the sidelines, an anime male character's name defines his personal journey, moral code, and character arc in the hearts of readers across the globe.",
        "intro_p2": "Our specialized anime name generator male engine brings together classical samurai naming heritage, historical clan lineages, and contemporary manga trends into one unified creative workspace. Rather than guessing meanings, you can explore hundreds of vetted anime male names equipped with traditional masculine suffixes and deep virtues like courage, wisdom, resilience, honor, and nobility. Browse our curated table of japanese boy names below, or generate new batches with one-click copy for your light novels, webcomics, manga scripts, video game projects, and tabletop roleplaying campaigns.",
        "h2_primary": "Discover Cool Anime Boy Names with Traditional Japanese Heritage",
        "h2_secondaries": [
            "Masculine Suffixes and Structure in Japanese Boy Names",
            "Finding Heroic Anime Male Names for Manga and Gaming",
            "Frequently Asked Questions About Anime Boy Names"
        ],
        "unique_section_title": "Masculine Japanese Naming Conventions and Common Suffixes (-ro, -to, -ki)",
        "unique_section_content": """
          <p>Masculine Japanese names follow time-honored phonetic and linguistic patterns that immediately communicate strength, birth order, or aspirational character traits. Understanding these common suffixes helps you choose the perfect name for your male lead:</p>
          <div class="feature-callout">
            <h4>Key Masculine Endings in Japanese Onomastics</h4>
            <ul>
              <li><strong>-ro / -rou (郎 / 朗):</strong> Traditionally means 'son' or 'cheerful young man'. Classical names like <em>Renjiro</em> (second son) or <em>Rintaro</em> carry an air of reliability, maturity, and honorable duty.</li>
              <li><strong>-to (人 / 斗 / 翔):</strong> Highly popular in modern anime. When written with 翔 (soaring flight), names like <em>Haruto</em> evoke unbounded potential and heroic dreams.</li>
              <li><strong>-ki (輝 / 樹 / 貴):</strong> Conveys brilliance (輝) or steadfast tree timber (樹), seen in dynamic names like <em>Kazuki</em>, <em>Daiki</em>, and <em>Haruki</em>.</li>
              <li><strong>-suke (助 / 介):</strong> Denotes a loyal helper, defender, or trusted companion, epitomized by iconic anime characters like <em>Daisuke</em> and <em>Sasuke</em>.</li>
              <li><strong>-ya (也 / 哉):</strong> A classical particle indicating affirmation and presence, creating refined names like <em>Kazuya</em> and <em>Tomoya</em>.</li>
              <li><strong>-hei (平):</strong> Represents peace, fairness, and calm composure, found in stalwart warrior names like <em>Kouhei</em>.</li>
            </ul>
          </div>
          <p>Balancing these endings with powerful prefixes gives your male character immediate presence on the page.</p>
        """,
        "faqs": [
            {
                "q": "What are the most popular endings for Japanese boy names in anime?",
                "a": "The most common endings in anime and modern Japan are -to (Haruto, Kaito), -ki (Kazuki, Daiki), -ro (Rintaro, Kenjiro), and -suke (Daisuke, Shunsuke)."
            },
            {
                "q": "Can these names be used for real Japanese baby naming?",
                "a": "Yes. All masculine names featured in this generator use official jinmeiyo and joyo kanji approved for legal birth registration in Japan."
            },
            {
                "q": "What does the ending '-taro' mean in a Japanese name?",
                "a": "The suffix '-taro' (太郎) traditionally designates the eldest or firstborn son, conveying great familial hope and leadership qualities."
            },
            {
                "q": "How can I pair a first name with a fitting last name?",
                "a": "Visit our Anime Last Name Generator to browse noble clan surnames like Takahashi or Kurosawa that pair naturally with these masculine given names."
            }
        ],
        "related": [
            {"title": "Anime Name Generator", "path": "/", "desc": "The primary generator featuring male, female, and full clan names."},
            {"title": "Anime Girl Names", "path": "/anime-girl-names", "desc": "Graceful female Japanese names with floral and virtue kanji."},
            {"title": "Anime Last Name Generator", "path": "/anime-last-name-generator", "desc": "Authentic Japanese family names and noble clan titles."}
        ]
    },
    {
        "filename": "anime-girl-names.html",
        "url_path": "/anime-girl-names",
        "mode": "girl",
        "platform": "general",
        "primary_keyword": "anime girl names",
        "secondary_keywords": ["anime name generator female", "anime female names", "japanese girl names"],
        "title": "Anime Girl Names: Cute Japanese Female Names with Kanji",
        "h1": "Anime Girl Names",
        "meta_desc": "Discover elegant and cute anime girl names complete with Japanese kanji and graceful meanings. Perfect for female anime characters, novelists, and OC creators.",
        "og_image": "og-anime-girl-names.png",
        "is_home": False,
        "breadcrumb_name": "Anime Girl Names",
        "static_key": "girl",
        "intro_p1": "Immerse yourself in our collection of graceful, fierce, and cute anime girl names, complete with verified Japanese kanji calligraphy, romaji readings, and English translations for your creative writing. From gentle priestesses guarding sacred shrine grounds to powerful magical heroines commanding celestial storms, a female anime character's name reflects her unique charm, emotional depth, noble spirit, and inner strength across every story arc and dramatic turning point.",
        "intro_p2": "Our anime name generator female tool eliminates generic phonetic fabrications by drawing directly from classical literature, seasonal flora, spiritual folklore, and romantic Japanese poetry. If you are developing memorable characters for a web novel, manga series, light novel, or roleplay game, exploring authentic anime female names provides boundless creative inspiration. Review our curated list of beloved japanese girl names below, or use the interactive generator above to produce fresh names with instant copying for your heroines, kunoichi, swordswomen, and magical protagonists.",
        "h2_primary": "Find Graceful and Cute Anime Girl Names with Authentic Kanji",
        "h2_secondaries": [
            "Feminine Suffixes and Flora Symbolism in Japanese Girl Names",
            "Crafting Unforgettable Anime Female Names for Manga Heroines",
            "Frequently Asked Questions About Anime Girl Names"
        ],
        "unique_section_title": "Feminine Japanese Naming Conventions and Suffixes (-ko, -mi, -ka, -na)",
        "unique_section_content": """
          <p>Feminine Japanese onomastics celebrate natural beauty, seasonal transitions, melody, and compassionate virtues. Familiarity with key feminine endings helps you craft names with authentic emotional resonance:</p>
          <div class="feature-callout">
            <h4>Common Feminine Endings and Flora Motifs in Japanese Names</h4>
            <ul>
              <li><strong>-ko (子 - Child):</strong> The timeless classical ending symbolizing precious innocence and lineage, present in dignified names like <em>Chiyo</em>, <em>Tsukiko</em>, and <em>Riko</em>.</li>
              <li><strong>-mi (美 - Beauty):</strong> Represents elegance, charm, and inner grace, showcased in melodious names like <em>Kasumi</em> (mist beauty), <em>Ayame</em>, and <em>Nanami</em>.</li>
              <li><strong>-ka (花 / 香 - Flower or Fragrance):</strong> Imbues a character with floral delicate sweetness, seen in names like <em>Renka</em> (lotus flower) and <em>Chika</em>.</li>
              <li><strong>-na (奈 / 菜):</strong> Evokes lush greens and gentle harmony, popular in modern anime heroines like <em>Yuna</em>, <em>Hina</em>, and <em>Kanna</em>.</li>
              <li><strong>-ri (莉 / 里):</strong> Often references fragrant white jasmine (莉) or peaceful countryside villages (里), as in <em>Hikari</em> (radiant light) and <em>Sayuri</em>.</li>
              <li><strong>Floral Monikers:</strong> Single-kanji flora names remain among the most iconic across anime history: <em>Sakura</em> (cherry blossom), <em>Tsubaki</em> (winter camellia), and <em>Aoi</em> (hollyhock).</li>
            </ul>
          </div>
          <p>Whether your heroine is soft-spoken or a battle-hardened kunoichi, these naming roots add natural elegance to her character design.</p>
        """,
        "faqs": [
            {
                "q": "What is the meaning of the '-ko' suffix in anime girl names?",
                "a": "The suffix '-ko' (子) translates to 'child' and was historically a noble title. In modern names, it represents cherished youth, elegance, and traditional cultural grace."
            },
            {
                "q": "What are some popular nature-inspired anime girl names?",
                "a": "Iconic nature names include Sakura (cherry blossom), Kasumi (morning mist), Hinata (facing the sun), Yuki (pure snow), and Ame (gentle rain)."
            },
            {
                "q": "Can these female names be used in published fiction?",
                "a": "Yes. All names generated on this site are culturally authentic and free for use in commercial manga, light novels, indie games, and creative writing."
            },
            {
                "q": "Why do some female anime characters have single-syllable or single-kanji names?",
                "a": "Single-kanji names like Rin (凛 - dignified), Mei (芽 - sprout), or Mio (美桜 - beautiful cherry) are celebrated for their punchy modern aesthetic and direct poetic meaning."
            }
        ],
        "related": [
            {"title": "Anime Boy Names", "path": "/anime-boy-names", "desc": "Cool masculine Japanese names with traditional kanji endings."},
            {"title": "Anime Names With Meaning", "path": "/anime-names-with-meaning", "desc": "Deep character names with rich spiritual and elemental symbolism."},
            {"title": "Anime Username Generator", "path": "/anime-username-generator", "desc": "Aesthetic handles and gamertags for creators and streamers."}
        ]
    }
]

def render_prefilled_cards(static_names):
    cards_html = []
    for item in static_names[:6]:
        card = f"""          <div class="name-card" tabindex="0" role="article" aria-label="{item['romaji']}, kanji {item['kanji']}, meaning: {item['meaning']}">
            <div class="card-header">
              <h3 class="card-romaji">{item['romaji']}</h3>
              <span class="card-kanji">{item['kanji']}</span>
            </div>
            <p class="card-meaning">{item['meaning']}</p>
            <div class="card-actions">
              <button type="button" class="btn-copy-card" aria-label="Copy {item['romaji']}">
                <svg class="icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                  <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                  <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                </svg>
                <span>Copy</span>
              </button>
            </div>
          </div>"""
        cards_html.append(card)
    return "\n".join(cards_html)

def render_static_table(static_names):
    rows = []
    for item in static_names:
        row = f"""            <tr>
              <td class="table-romaji">{item['romaji']}</td>
              <td class="table-kanji">{item['kanji']}</td>
              <td>{item['meaning']}</td>
            </tr>"""
        rows.append(row)
    return "\n".join(rows)

def render_faqs(faqs):
    faq_html = []
    for faq in faqs:
        item = f"""        <details class="faq-item">
          <summary class="faq-question">
            <span>{faq['q']}</span>
            <svg class="faq-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
              <polyline points="6 9 12 15 18 9"></polyline>
            </svg>
          </summary>
          <div class="faq-answer">
            <p>{faq['a']}</p>
          </div>
        </details>"""
        faq_html.append(item)
    return "\n".join(faq_html)

def render_schema_json(page):
    schemas = []
    url = f"https://animenamevault.com{page['url_path'] if page['url_path'] != '/' else ''}"

    if page.get("is_home"):
        website_schema = {
            "@context": "https://schema.org",
            "@type": "WebSite",
            "name": "Anime Name Generator",
            "url": "https://animenamevault.com/",
            "description": page["meta_desc"],
            "publisher": {
                "@type": "Organization",
                "name": "Anime Name Generator",
                "url": "https://animenamevault.com/",
                "logo": {
                    "@type": "ImageObject",
                    "url": "https://animenamevault.com/img/icon-512.png"
                }
            }
        }
        schemas.append(website_schema)

    webapp_schema = {
        "@context": "https://schema.org",
        "@type": "WebApplication",
        "name": page["h1"],
        "url": url if url.endswith('/') else f"{url}",
        "description": page["meta_desc"],
        "applicationCategory": "UtilitiesApplication",
        "operatingSystem": "Any",
        "offers": {
            "@type": "Offer",
            "price": "0",
            "priceCurrency": "USD"
        }
    }
    schemas.append(webapp_schema)

    if not page.get("is_home"):
        breadcrumb_schema = {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": 1,
                    "name": "Home",
                    "item": "https://animenamevault.com/"
                },
                {
                    "@type": "ListItem",
                    "position": 2,
                    "name": page["breadcrumb_name"],
                    "item": url
                }
            ]
        }
        schemas.append(breadcrumb_schema)

    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": f["q"],
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": f["a"]
                }
            } for f in page["faqs"]
        ]
    }
    schemas.append(faq_schema)

    schema_scripts = []
    for s in schemas:
        schema_scripts.append(f'<script type="application/ld+json">\n{json.dumps(s, ensure_ascii=False, indent=2)}\n</script>')
    return "\n".join(schema_scripts)

def render_page_html(page):
    static_names = STATIC_DATA[page["static_key"]]
    prefilled_cards = render_prefilled_cards(static_names)
    static_table_rows = render_static_table(static_names)
    faqs_html = render_faqs(page["faqs"])
    schema_html = render_schema_json(page)
    canonical_url = f"https://animenamevault.com{page['url_path'] if page['url_path'] != '/' else '/'}"

    related_cards = []
    for r in page["related"]:
        card = f"""        <a href="{r['path']}" class="related-card">
          <h3>
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#C8392B" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"></circle><polyline points="12 16 16 12 12 8"></polyline><line x1="8" y1="12" x2="16" y2="12"></line></svg>
            <span>{r['title']}</span>
          </h3>
          <p>{r['desc']}</p>
        </a>"""
        related_cards.append(card)
    related_html = "\n".join(related_cards)

    breadcrumb_html = ""
    if not page.get("is_home"):
        breadcrumb_html = f"""  <nav class="breadcrumb-nav" aria-label="Breadcrumb">
    <ol class="breadcrumbs">
      <li><a href="/">Home</a></li>
      <li><span aria-hidden="true">/</span></li>
      <li aria-current="page">{page['breadcrumb_name']}</li>
    </ol>
  </nav>"""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{page['title']}</title>
  <meta name="description" content="{page['meta_desc']}">
  <!-- Pre-launch protection -->
  <meta name="robots" content="noindex, nofollow">
  <link rel="canonical" href="{canonical_url}">

  <!-- Favicons & Manifest -->
  <link rel="icon" type="image/svg+xml" href="/img/favicon.svg">
  <link rel="alternate icon" type="image/x-icon" href="/img/favicon.ico">
  <link rel="icon" type="image/png" sizes="32x32" href="/img/favicon-32.png">
  <link rel="apple-touch-icon" sizes="180x180" href="/img/apple-touch-icon.png">
  <link rel="manifest" href="/site.webmanifest">
  <meta name="theme-color" content="#C8392B">

  <!-- Open Graph / Social Media -->
  <meta property="og:title" content="{page['title']}">
  <meta property="og:description" content="{page['meta_desc']}">
  <meta property="og:image" content="https://animenamevault.com/img/{page['og_image']}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="{page['h1']} in Sumi and Shu Japanese calligraphy design">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:type" content="website">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{page['title']}">
  <meta name="twitter:description" content="{page['meta_desc']}">
  <meta name="twitter:image" content="https://animenamevault.com/img/{page['og_image']}">

  <!-- Stylesheet -->
  <link rel="stylesheet" href="/css/style.css">

  <!-- JSON-LD Schemas -->
{schema_html}
</head>
<body>
  <a href="#main" class="skip-link">Skip to main content</a>

  <header class="site-header">
    <div class="header-container">
      <a href="/" class="brand-link" aria-label="Anime Name Generator Home">
        <span class="brand-hanko" aria-hidden="true">名</span>
        <span class="brand-text">Anime Name Vault</span>
      </a>
      <nav aria-label="Main Navigation">
        <ul class="nav-links">
          <li><a href="/" {"aria-current='page'" if page.get("is_home") else ""}>Home</a></li>
          <li><a href="/anime-boy-names" {"aria-current='page'" if page['url_path'] == '/anime-boy-names' else ""}>Boy Names</a></li>
          <li><a href="/anime-girl-names" {"aria-current='page'" if page['url_path'] == '/anime-girl-names' else ""}>Girl Names</a></li>
          <li><a href="/anime-names-with-meaning" {"aria-current='page'" if page['url_path'] == '/anime-names-with-meaning' else ""}>Meanings</a></li>
          <li><a href="/anime-username-generator" {"aria-current='page'" if page['url_path'] == '/anime-username-generator' else ""}>Usernames</a></li>
        </ul>
      </nav>
    </div>
  </header>

{breadcrumb_html}

  <main id="main">
    <section class="hero-section">
      <span class="hero-tag">Authentic Japanese Onomastics</span>
      <h1>{page['h1']}</h1>
      <p class="hero-subtitle">Authentic Japanese kanji, accurate romaji pronunciation, and verified meanings with zero dependencies.</p>
    </section>

    <!-- Generator Tool Box -->
    <section class="generator-card" aria-label="{page['h1']} Tool">
      <div class="generator-controls">
        <div class="control-group">
          <label for="gen-mode">Select Category</label>
          <select id="gen-mode" class="control-select">
            <option value="all">All / Random Japanese Names</option>
            <option value="boy">Anime Boy Names</option>
            <option value="girl">Anime Girl Names</option>
            <option value="lastname">Anime Surnames (Last Names)</option>
            <option value="meaning">Names with Meaning</option>
            <option value="villain">Anime Villain Names</option>
            <option value="username">Aesthetic Anime Usernames</option>
          </select>
        </div>

        <div class="control-group" id="platform-group" style="display: {'flex' if page['mode'] == 'username' else 'none'};">
          <label for="gen-platform">Platform Style</label>
          <select id="gen-platform" class="control-select">
            <option value="general">General / Aesthetic Gamertag</option>
            <option value="tiktok">TikTok (Max 24 chars)</option>
            <option value="discord">Discord (Max 32 chars)</option>
          </select>
        </div>

        <div class="control-group">
          <label for="gen-count">Batch Size</label>
          <select id="gen-count" class="control-select">
            <option value="6">6 Names</option>
            <option value="12" selected>12 Names</option>
            <option value="20">20 Names</option>
          </select>
        </div>

        <div class="action-buttons">
          <button type="button" id="generate-btn" class="btn-primary">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21.5 2v6h-6M21.34 15.57a10 10 0 1 1-.57-8.38l5.67-5.67"></path></svg>
            <span>Generate Names</span>
          </button>
          <button type="button" id="copy-all-btn" class="btn-secondary">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
            <span>Copy All</span>
          </button>
        </div>
      </div>

      <!-- Pre-filled Results Grid (Works 100% with JS turned off) -->
      <div id="results-grid" class="results-grid" aria-label="Generated Names">
{prefilled_cards}
      </div>

      <!-- Accessible screen reader announcement -->
      <div id="gen-live-region" class="sr-only" aria-live="polite"></div>
    </section>

    <!-- Introductory SEO Content -->
    <article class="content-section">
      <h2>{page['h2_primary']}</h2>
      <p>{page['intro_p1']}</p>
      <p>{page['intro_p2']}</p>
    </article>

    <!-- Static Curated List of 25 Unique Names -->
    <section class="content-section">
      <h2>Curated Collection: 25 Authentic Names with Kanji and Meaning</h2>
      <p>Browse our hand-curated registry of authentic names, complete with kanji calligraphy, romaji pronunciation, and English meaning. Every name in this collection is verified for onomastic accuracy and guaranteed unique across our website.</p>
      
      <div class="table-responsive">
        <table class="name-table">
          <thead>
            <tr>
              <th scope="col">Romaji Name</th>
              <th scope="col">Japanese Kanji</th>
              <th scope="col">English Meaning & Symbolism</th>
            </tr>
          </thead>
          <tbody>
{static_table_rows}
          </tbody>
        </table>
      </div>
    </section>

    <!-- Page-Specific Deep Dive Section -->
    <section class="content-section">
      <h2>{page['unique_section_title']}</h2>
{page['unique_section_content']}
    </section>

    <!-- Unique FAQs Section -->
    <section class="content-section">
      <h2>Frequently Asked Questions</h2>
      <div class="faq-list">
{faqs_html}
      </div>
    </section>

    <!-- Related Generators Navigation -->
    <section class="content-section">
      <h2>Explore Related Name Generators</h2>
      <p>Continue your creative discovery across our suite of specialized Japanese naming tools:</p>
      <div class="related-grid">
{related_html}
      </div>
    </section>

    <!-- Decorative Stamp -->
    <div style="text-align: center; margin: 2rem 0;">
      <img src="/img/hanko-stamp.svg" alt="Authentic {page['primary_keyword']} seal badge" width="48" height="48" class="section-stamp" loading="lazy">
    </div>
  </main>

  <footer class="site-footer">
    <div class="footer-container">
      <div class="footer-col">
        <h4>Anime Name Vault</h4>
        <p>A fast, ad-free, and culturally accurate Japanese anime name generator. Dedicated to authentic kanji, romaji, and onomastic storytelling with zero dependencies.</p>
      </div>
      <div class="footer-col">
        <h4>Popular Generators</h4>
        <ul class="footer-links">
          <li><a href="/">Anime Name Generator</a></li>
          <li><a href="/anime-boy-names">Anime Boy Names</a></li>
          <li><a href="/anime-girl-names">Anime Girl Names</a></li>
          <li><a href="/anime-names-with-meaning">Anime Names With Meaning</a></li>
          <li><a href="/anime-last-name-generator">Anime Last Name Generator</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Digital & Creative</h4>
        <ul class="footer-links">
          <li><a href="/anime-username-generator">Anime Username Generator</a></li>
          <li><a href="/anime-usernames-for-tiktok">Anime Usernames for TikTok</a></li>
          <li><a href="/anime-usernames-for-discord">Anime Usernames for Discord</a></li>
          <li><a href="/anime-villain-name-generator">Anime Villain Name Generator</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Trust & Legal</h4>
        <ul class="footer-links">
          <li><a href="/about">About Us</a></li>
          <li><a href="/privacy">Privacy Policy</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 Anime Name Vault. All rights reserved. Pure static HTML, CSS &amp; JS.</p>
      <p><a href="#main">Back to top &uarr;</a></p>
    </div>
  </footer>

  <!-- Toast Notice Container -->
  <div id="toast" class="toast-notice" role="status" aria-live="polite"></div>

  <!-- Scripts -->
  <script>
    window.__INITIAL_MODE = "{page['mode']}";
    window.__INITIAL_PLATFORM = "{page['platform']}";
  </script>
  <script src="/js/data.js"></script>
  <script src="/js/generator.js"></script>
</body>
</html>"""
    return html

def build_all_pages():
    for page in PAGES_CONFIG:
        html = render_page_html(page)
        with open(page["filename"], "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Generated {page['filename']}")

if __name__ == "__main__":
    build_all_pages()
