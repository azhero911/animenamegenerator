"""
Calibrate all 9 intro paragraphs to be strictly 155-175 words (comfortably within 150-200),
with the primary keyword in the first 100 words.
"""

import sys
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

INTROS = {
    "index.html": {
        "primary": "anime name generator",
        "p1": "Welcome to the ultimate anime name generator, engineered for writers, novelists, manga creators, gamers, and tabletop roleplayers seeking authentic Japanese identities for their characters. Whether you are building an original shonen protagonist embarking on a perilous quest, a mysterious rogue swordsman wandering feudal provinces, or a charming slice-of-life persona for an urban drama, this tool crafts culturally rich combinations of Japanese given names and historical clan surnames complete with accurate kanji and poetic English translations.",
        "p2": "Our japanese anime name generator seamlessly unites classical samurai heritage, regional Shinto folklore, and contemporary manga naming tropes into one intuitive workspace. Unlike generic web randomizers that produce awkward phonetic gibberish or misspelled readings, every entry generated here features verified kanji calligraphy, authentic on'yomi and kun'yomi pronunciation, and rich narrative symbolism. You can explore our random anime name generator modes, filter by character archetypes, and discover resonant titles with effortless one-click copying for your light novels, scripts, or gaming profiles."
    },
    "anime-username-generator.html": {
        "primary": "anime username generator",
        "p1": "Elevate your online presence with our specialized anime username generator, built to generate unforgettable gamertags, social handles, and streaming identities across the digital web. Finding cool anime usernames that are not already claimed by other players can often feel frustrating on competitive multiplayer networks and community forums. That is why our creative engine crafts balanced, aesthetically pleasing username combinations that fuse iconic Japanese anime terminology with contemporary digital naming conventions, streaming trends, and gaming slang.",
        "p2": "From minimalist cyber-samurai tags to lo-fi aesthetic anime usernames, our curated algorithm creates clean variations without awkward random symbol clutter, messy punctuation, or unreadable letter spam. Whether you need a fresh identity for Twitch streaming, Steam leaderboards, Discord servers, or mobile social networks, you will discover hundreds of creative anime username ideas tailored to your personal vibe. Simply select your preferred batch count, customize your platform styling, and copy your brand-new digital handle with a single click."
    },
    "anime-usernames-for-tiktok.html": {
        "primary": "anime usernames for tiktok",
        "p1": "Stand out on the For You page with our targeted generator for anime usernames for tiktok. Building a successful anime edit account, cosplay portfolio, or manga review channel requires an identity that is instantly catchy, effortless to spell, and visually clean on mobile phone screens. Having a memorable username makes it substantially easier for viewers to search for your videos, recognize your brand in fast-moving comment sections, and follow your creator journey across social platforms over time.",
        "p2": "TikTok enforces strict platform handle requirements that many creators overlook until their profile update fails. Our tool is programmed specifically to generate anime tiktok names that adhere strictly to TikTok's 24-character maximum length limit while maintaining sleek aesthetics and flawless readability. Explore viral anime tiktok username ideas featuring lo-fi chill vibes, shonen action themes, and pastel aesthetics ready for immediate copy-pasting directly into your profile settings without frustrating truncation errors, awkward underscores, or clunky punctuation."
    },
    "anime-usernames-for-discord.html": {
        "primary": "anime usernames for discord",
        "p1": "Personalize your gaming presence with our custom generator for anime usernames for discord. Whether you are leading a competitive esports gaming guild, hanging out in community anime servers, or organizing raid voice channels with close friends, having a distinct identity sets an unforgettable tone. Discord's unique naming architecture allows for both unique global account handles and flexible server display nicknames, giving users tremendous room for personal expression and creative flair across different gaming communities and clan lobbies.",
        "p2": "Our tool generates cool anime discord names tailored specifically to Discord's modern handle system. All generated suggestions stay strictly within Discord's 32-character limit while maintaining sharp visual contrast on server role lists and active voice chats. Explore diverse anime discord nicknames, from stoic warrior titles to cyberpunk operative tags, with effortless single-click copying for both your global profile and server-specific nicknames without cluttering your chat messages or obscuring team callouts during competitive matches."
    },
    "anime-names-with-meaning.html": {
        "primary": "anime names with meaning",
        "p1": "Every memorable character in Japanese animation carries a title that foreshadows their destiny, and our database of anime names with meaning reveals the profound symbolism behind authentic Japanese naming traditions. In classical Japanese storytelling, names are rarely chosen for superficial sound alone; each character's kanji represents their elemental affinity, inner moral virtue, ancestral heritage, or tragic narrative arc across their heroic journey through fantasy realms, martial tournaments, and mystical landscapes.",
        "p2": "If you are looking for an anime name generator with kanji that provides authentic linguistic translations, our tool offers meticulously vetted entries for your creative projects. From names symbolizing fleeting fireflies in the twilight to eternal lotus blossoms rising from murky waters, exploring these anime names and meanings provides writers, worldbuilders, and novelists with deep cultural inspiration. Browse our curated collection below, or use the interactive tool above to generate new meaningful names with one-click copying for your manuscripts, manga scripts, and character design sheets."
    },
    "anime-last-name-generator.html": {
        "primary": "anime last name generator",
        "p1": "Anchor your character in historical prestige and believable family heritage with our specialized anime last name generator. In Japanese culture and anime narratives, a character's surname carries tremendous emotional and social weight, signaling their clan lineage, ancestral territory, or social standing across feudal domains. Whether you are crafting a venerable martial arts dynasty, an aristocratic noble house, or a humble rural protagonist, an authentic surname is essential for believable storytelling and deep worldbuilding across chapters.",
        "p2": "Our japanese last names engine avoids artificial combinations by referencing real historical clan registries and topographical naming conventions from ancient Japan. If you need a reliable anime surname generator for manga worldbuilding, light novels, or tabletop roleplay, this tool provides verified kanji, accurate romaji, and rich English translations. Explore famous anime surnames below or use the interactive generator to discover the ideal clan title for your story and memorable character cast across all ongoing arcs."
    },
    "anime-villain-name-generator.html": {
        "primary": "anime villain name generator",
        "p1": "Every unforgettable anime story is driven by a formidable antagonist, and our anime villain name generator gives you the sinister titles needed to command fear and respect across your fantasy world. Great villains require names that send shivers down the reader's spine, echoing through dark dungeons and climactic battlegrounds. An imposing name conveys their merciless philosophy, supernatural curse, dark pact, forbidden bloodline, or tragic descent into destructive madness.",
        "p2": "From ruthless mastermind tacticians manipulating politics to ancient mythical demons emerging from underworld rifts, our curated generator creates dark anime names grounded in ominous Japanese kanji and folklore lore. If you are developing an antagonist for your manga, novel, or tabletop campaign, exploring evil anime names with genuine linguistic weight ensures your villain feels menacing rather than cartoonish. Generate chilling anime villain names now with instant copy functionality for your dark lords, rogue sorcerers, shadowy guildmasters, and sinister assassins across all your creative chapters."
    },
    "anime-boy-names.html": {
        "primary": "anime boy names",
        "p1": "Discover inspiring, heroic, and handsome anime boy names crafted with authentic Japanese kanji, accurate romaji, and resonant English meanings for your characters. From spirited shonen champions charging headfirst into battle to calm, analytical rivals observing from the sidelines, an anime male character's name defines his journey, resolve, moral code, and personal character arc in the hearts of fans across the globe.",
        "p2": "Our specialized anime name generator male engine brings together classical samurai naming heritage and contemporary manga trends into a unified tool. Rather than guessing meanings, you can explore hundreds of vetted anime male names equipped with traditional masculine suffixes and deep virtues like courage, wisdom, resilience, and nobility. Browse our curated table of japanese boy names below, or generate new batches with one-click copy for your novels, webcomics, manga scripts, video game projects, and tabletop roleplaying campaigns."
    },
    "anime-girl-names.html": {
        "primary": "anime girl names",
        "p1": "Immerse yourself in our collection of graceful, fierce, and cute anime girl names, complete with verified Japanese kanji calligraphy, romaji readings, and English translations. From gentle priestesses guarding sacred shrine grounds to powerful magical heroines commanding celestial storms, a female anime character's name reflects her unique charm, emotional depth, noble spirit, and inner strength across every story arc.",
        "p2": "Our anime name generator female tool eliminates generic phonetic fabrications by drawing directly from classical literature, seasonal flora, spiritual folklore, and romantic poetry. If you are developing characters for a web novel, manga, light novel, or roleplay game, exploring authentic anime female names provides boundless creative inspiration. Review our curated list of beloved japanese girl names below, or use the interactive generator above to produce fresh names with instant copying for your heroines, kunoichi, swordswomen, and magical protagonists."
    }
}

counts = []
for page, data in INTROS.items():
    combined = f"{data['p1']} {data['p2']}"
    words = combined.split()
    first_100 = " ".join(words[:100]).lower()
    word_count = len(words)
    kw_ok = data['primary'].lower() in first_100
    counts.append((page, word_count, kw_ok))
    print(f"{page}: {word_count} words | Keyword in first 100: {'YES' if kw_ok else 'NO'}")

for page, word_count, kw_ok in counts:
    assert 150 <= word_count <= 200, f"{page}: word count {word_count} not in 150-200"
    assert kw_ok, f"{page}: primary keyword missing in first 100 words"

print("\nSUCCESS: All 9 intros strictly between 150 and 200 words, primary keyword in first 100 words!")
