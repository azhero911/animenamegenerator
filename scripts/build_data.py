"""
Data generator script for Anime Name Generator
Generates:
1. static_names.json: 25 unique names per page (total 225 unique names)
2. js/data.js: client-side generator dataset for dynamic generations
Verifies:
- Zero cross-page duplicates
- Kanji, romaji, and meaning on every entry
"""

import json
import os

STATIC_PAGE_DATA = {
    "home": [
        {"romaji": "Renjiro", "kanji": "蓮二郎", "meaning": "Second son who blooms like an honest lotus"},
        {"romaji": "Kazuki", "kanji": "一輝", "meaning": "Singular brilliance and radiant light"},
        {"romaji": "Sora", "kanji": "蒼空", "meaning": "Vast azure summer sky"},
        {"romaji": "Hayato", "kanji": "隼人", "meaning": "Falcon person; swift and resolute spirit"},
        {"romaji": "Daiki", "kanji": "大輝", "meaning": "Vast shining radiance and great glory"},
        {"romaji": "Kaito", "kanji": "海斗", "meaning": "Big dipper constellations over the calm ocean"},
        {"romaji": "Aoi", "kanji": "葵", "meaning": "Hollyhock blossom; turning always toward the sun"},
        {"romaji": "Hinata", "kanji": "日向", "meaning": "Facing the sunlight with warmth and hope"},
        {"romaji": "Riku", "kanji": "陸", "meaning": "Enduring continental earth and solid ground"},
        {"romaji": "Taiga", "kanji": "大河", "meaning": "Mighty flowing river carving its own path"},
        {"romaji": "Yuto", "kanji": "悠人", "meaning": "Distant, gentle wanderer of calm seas"},
        {"romaji": "Ryusei", "kanji": "流星", "meaning": "Shooting star piercing the midnight sky"},
        {"romaji": "Kouki", "kanji": "光輝", "meaning": "Brilliant luminous aura of pure hope"},
        {"romaji": "Asahi", "kanji": "朝日", "meaning": "Morning sunrise over the mountain ridge"},
        {"romaji": "Souta", "kanji": "蒼大", "meaning": "Vast azure expanse of tranquil heights"},
        {"romaji": "Haruma", "kanji": "春真", "meaning": "True clarity and vitality of springtime"},
        {"romaji": "Itsuki", "kanji": "樹", "meaning": "Stalwart timber tree standing firm against wind"},
        {"romaji": "Ibuki", "kanji": "息吹", "meaning": "Fresh living breath of the awakening wilderness"},
        {"romaji": "Ginga", "kanji": "銀河", "meaning": "Silver river; the sprawling Milky Way galaxy"},
        {"romaji": "Kensei", "kanji": "剣聖", "meaning": "Master sword saint dedicated to the blade"},
        {"romaji": "Shinra", "kanji": "森羅", "meaning": "Endless myriad forest; all things in nature"},
        {"romaji": "Tatsuki", "kanji": "竜樹", "meaning": "Sacred dragon tree rooted between heaven and earth"},
        {"romaji": "Subaru", "kanji": "昴", "meaning": "The Pleiades star cluster guiding travelers"},
        {"romaji": "Kaname", "kanji": "要", "meaning": "Crucial pivot and foundational cornerstone"},
        {"romaji": "Suzaku", "kanji": "朱雀", "meaning": "Vermilion bird guardian of the southern realm"}
    ],
    "username": [
        {"romaji": "KitsuneDrift", "kanji": "狐漂流", "meaning": "Ghostly fox wanderer drifting through midnight mists"},
        {"romaji": "KagePulse", "kanji": "影脈動", "meaning": "Rhythmic shadow heartbeat lurking beneath neon light"},
        {"romaji": "RamenRonin", "kanji": "麺浪人", "meaning": "Masterless wandering samurai who travels for noodles"},
        {"romaji": "NeonKatana", "kanji": "刀光", "meaning": "Cyberpunk blade forged with electric edge"},
        {"romaji": "ZenithGhost", "kanji": "頂霊", "meaning": "Ascendant phantom reigning over silent rooftops"},
        {"romaji": "VoidKenshi", "kanji": "虚剣士", "meaning": "Wandering swordsman trained in the empty void"},
        {"romaji": "MochiPhantom", "kanji": "餅幻影", "meaning": "Deceptively sweet apparition with lightning reflex"},
        {"romaji": "ChronoShinobi", "kanji": "時忍", "meaning": "Ninja capable of slipping through fractured timelines"},
        {"romaji": "AeroTengu", "kanji": "風天狗", "meaning": "Winged crow-spirit commanding high-altitude storms"},
        {"romaji": "SolarShinigami", "kanji": "日死神", "meaning": "Reaper draped in solar flare and blazing light"},
        {"romaji": "BonsaiBlade", "kanji": "盆栽刃", "meaning": "Disciplined miniature precision backed by lethal focus"},
        {"romaji": "SakeSpecter", "kanji": "酒亡霊", "meaning": "Tipsy tavern spirit who never misses a strike"},
        {"romaji": "FrostKitsune", "kanji": "霜狐", "meaning": "Nine-tailed fox walking across frozen tundra"},
        {"romaji": "NovaSenshi", "kanji": "新星戦士", "meaning": "Stellar warrior born from cosmic supernova energy"},
        {"romaji": "EchoRonin", "kanji": "響浪人", "meaning": "Solemn swordsman whose strikes resonate after defeat"},
        {"romaji": "PixelYakuza", "kanji": "画素極道", "meaning": "Retro arcade outlaw with an iron code of honor"},
        {"romaji": "VaporSamurai", "kanji": "蒸気侍", "meaning": "Lo-fi synthwave duelist drifting through pink fog"},
        {"romaji": "SilentKuromi", "kanji": "無黒魅", "meaning": "Quiet rebel with a charming yet lethal edge"},
        {"romaji": "TokyoCipher", "kanji": "暗号東京", "meaning": "Digital codebreaker roaming the Shinjuku alleys"},
        {"romaji": "AstroOni", "kanji": "星鬼", "meaning": "Horned demon wanderer from an orbital space station"},
        {"romaji": "MirageKunoichi", "kanji": "幻影くのいち", "meaning": "Illusionist female ninja who leaves cherry petals"},
        {"romaji": "HollowBonsai", "kanji": "虚盆", "meaning": "Ancient miniature cedar concealing a hidden seal"},
        {"romaji": "StaticShogun", "kanji": "静将軍", "meaning": "Glitch-armored warlord commanding analog signals"},
        {"romaji": "RogueNeko", "kanji": "野良猫", "meaning": "Independent stray cat assassin jumping rooftops"},
        {"romaji": "GlitchDaimyo", "kanji": "歪大名", "meaning": "Digital feudal lord governing corrupted server realms"}
    ],
    "tiktok": [
        {"romaji": "ani.miku", "kanji": "未来音", "meaning": "Aesthetic anime soundwave tuned to future pop"},
        {"romaji": "senpai.vibe", "kanji": "先輩気", "meaning": "Effortless charismatic energy of an admired upperclassman"},
        {"romaji": "chibi_kage", "kanji": "影小", "meaning": "Cute miniature shadow assassin with quick edits"},
        {"romaji": "otaku_tempo", "kanji": "拍子", "meaning": "Rhythmic high-energy anime beat edits and loops"},
        {"romaji": "waifu.lore", "kanji": "伝記", "meaning": "Deep character storytelling and manga breakdown aesthetic"},
        {"romaji": "tokyo_lofi", "kanji": "東京音", "meaning": "Rainy Shibuya window view set to mellow chords"},
        {"romaji": "boba_kenshi", "kanji": "珠剣士", "meaning": "Sweet boba milk tea lover with swordsman precision"},
        {"romaji": "manga_scroll", "kanji": "絵巻", "meaning": "Infinite vertical webtoon panel pacing and review"},
        {"romaji": "sakura_cuts", "kanji": "桜斬", "meaning": "Crisp transition cuts showered in falling petals"},
        {"romaji": "dusk_ronin", "kanji": "夕浪人", "meaning": "Twilight swordsman walking solitary cinematic paths"},
        {"romaji": "kawaii_rebel", "kanji": "反逆", "meaning": "Pastel aesthetic hiding punk rock battle energy"},
        {"romaji": "shonen_spark", "kanji": "火花", "meaning": "Determined spark of an underdog shonen protagonist"},
        {"romaji": "neon_noodle", "kanji": "夜麺", "meaning": "Midnight anime cooking clips and glowing broth"},
        {"romaji": "blade_beats", "kanji": "刃拍", "meaning": "Sword clashing sync tracks for hype AMV edits"},
        {"romaji": "cozy_ghibli", "kanji": "温森", "meaning": "Peaceful cottagecore anime nature scenery and tea"},
        {"romaji": "zen_senpai", "kanji": "禅先", "meaning": "Calm, stoic mentor offering slice-of-life advice"},
        {"romaji": "kami_snaps", "kanji": "神瞬", "meaning": "Divine frame freezes on decisive combat moments"},
        {"romaji": "yume_drift", "kanji": "夢漂", "meaning": "Dreamy pastel daydream aesthetic and cloud timelapses"},
        {"romaji": "kuro_edits", "kanji": "黒編", "meaning": "High-contrast dark-mode anime highlight montages"},
        {"romaji": "poke_pastel", "kanji": "淡獣", "meaning": "Soft watercolor pocket monster art showcase"},
        {"romaji": "glitch_oni", "kanji": "崩鬼", "meaning": "Distorted bass and demon mask transition creator"},
        {"romaji": "pixel_mecha", "kanji": "画機", "meaning": "8-bit robotic pilot sharing retro sci-fi animations"},
        {"romaji": "matcha_mist", "kanji": "茶霧", "meaning": "Tranquil green tea vapor and study room ambience"},
        {"romaji": "kaiju_drop", "kanji": "怪落", "meaning": "Heavy bass drops paired with towering monster battles"},
        {"romaji": "shojo_haze", "kanji": "少女霞", "meaning": "Sparkling romantic manga frames with nostalgic filter"}
    ],
    "discord": [
        {"romaji": "kage.bushi", "kanji": "影武士", "meaning": "Shadow warrior guarding the guild hall lobby"},
        {"romaji": "ryu_overlord", "kanji": "竜主", "meaning": "Dragon lord presiding over midnight raid comms"},
        {"romaji": "tengu_mod", "kanji": "天狗守", "meaning": "Swift-winged server sentinel watching chat channels"},
        {"romaji": "shogun_ping", "kanji": "将軍響", "meaning": "Warlord who commands silence with a single mention"},
        {"romaji": "phantom_guild", "kanji": "幻団", "meaning": "Co-op gaming clan operating unseen in the shadows"},
        {"romaji": "katana_whisper", "kanji": "刀囁", "meaning": "Quiet assassin who only speaks in tactical callouts"},
        {"romaji": "oni_sentinel", "kanji": "鬼番兵", "meaning": "Fierce demon guardian protecting voice channels"},
        {"romaji": "void_samurai", "kanji": "虚侍", "meaning": "Wandering fighter who thrives in the server AFK room"},
        {"romaji": "nexus_shinobi", "kanji": "連結忍", "meaning": "Cross-server operative bridging gaming communities"},
        {"romaji": "astral_kitsune", "kanji": "星狐", "meaning": "Star-weaving fox celestial reigning in voice chat"},
        {"romaji": "ronin_bot", "kanji": "浪人機", "meaning": "Rogue automaton automating discord welcome roles"},
        {"romaji": "cyber_senshi", "kanji": "電脳戦士", "meaning": "High-tech mech commander strategizing squad loadouts"},
        {"romaji": "echo_valkyrie", "kanji": "響乙女", "meaning": "Anime battle maiden cheering the lobby to victory"},
        {"romaji": "frost_daimyo", "kanji": "霜大名", "meaning": "Cool-headed administrator resolving chat disputes"},
        {"romaji": "solar_kunoichi", "kanji": "日女忍", "meaning": "Blazing fast scout leading competitive tournaments"},
        {"romaji": "vortex_shinra", "kanji": "渦森羅", "meaning": "Mystic elemental sage who organizes bot commands"},
        {"romaji": "blaze_ronin", "kanji": "焔浪人", "meaning": "Fiery berserker fighting until the server shuts down"},
        {"romaji": "mystic_tanuki", "kanji": "狸仙", "meaning": "Mischievous shape-shifter spamming reaction roles"},
        {"romaji": "tsunami_blade", "kanji": "波刀", "meaning": "Fluid swordsman wiping enemy squads in ranked matches"},
        {"romaji": "zero_shinigami", "kanji": "零死神", "meaning": "Number zero death god holding the leaderboard crown"},
        {"romaji": "lunar_genshin", "kanji": "月原神", "meaning": "Moonlit traveler traversing co-op fantasy realms"},
        {"romaji": "storm_bushi", "kanji": "嵐武士", "meaning": "Tempest warrior whose microphone crackles with hype"},
        {"romaji": "dark_kami", "kanji": "暗神", "meaning": "Ancient deity observing silent chat lurkers from afar"},
        {"romaji": "pixel_kenshin", "kanji": "画剣心", "meaning": "Humble pixel wanderer helping newcomers in general chat"},
        {"romaji": "iron_yakuza", "kanji": "鉄極道", "meaning": "Loyal gaming syndicate enforcer backing his teammates"}
    ],
    "meaning": [
        {"romaji": "Kazuhiko", "kanji": "和彦", "meaning": "Harmonious boy; brings peace to broken families"},
        {"romaji": "Hotaru", "kanji": "蛍", "meaning": "Firefly; gentle flicker of life illuminating dark swamps"},
        {"romaji": "Chihiro", "kanji": "千尋", "meaning": "A thousand fathoms; boundless emotional depth and resilience"},
        {"romaji": "Ren", "kanji": "蓮", "meaning": "Sacred lotus rising pristine from muddy waters"},
        {"romaji": "Akane", "kanji": "茜", "meaning": "Deep madder red; vibrant crimson hue of sunset clouds"},
        {"romaji": "Makoto", "kanji": "誠", "meaning": "Pure truth, unyielding integrity and absolute loyalty"},
        {"romaji": "Kohaku", "kanji": "琥珀", "meaning": "Precious amber gemstone preserving ancient memories"},
        {"romaji": "Tsukiko", "kanji": "月子", "meaning": "Child of the moon; blessed with calm nocturnal grace"},
        {"romaji": "Shinobu", "kanji": "忍", "meaning": "Endurance, stealth and patient resilience under pressure"},
        {"romaji": "Takumi", "kanji": "匠", "meaning": "Master artisan craftsman with peerless hand precision"},
        {"romaji": "Midori", "kanji": "翠", "meaning": "Verdant jade green; lush vitality of springtime foliage"},
        {"romaji": "Haruto", "kanji": "陽翔", "meaning": "Soaring toward radiant sunlight with boundless courage"},
        {"romaji": "Kagami", "kanji": "鏡", "meaning": "Sacred mirror reflecting truth without distortion"},
        {"romaji": "Minato", "kanji": "湊", "meaning": "Sheltered harbor where wandering ships find safe refuge"},
        {"romaji": "Shiori", "kanji": "詩織", "meaning": "Weaving delicate poetry; gentle chronicler of life"},
        {"romaji": "Kousei", "kanji": "公正", "meaning": "Righteous justice, balance and unwavering fairness"},
        {"romaji": "Nanami", "kanji": "七海", "meaning": "The seven expansive seas uniting distant lands"},
        {"romaji": "Renka", "kanji": "蓮花", "meaning": "Lotus blossom symbolizing spiritual awakening"},
        {"romaji": "Soutaro", "kanji": "創太郎", "meaning": "Original pioneer son who creates new paths for others"},
        {"romaji": "Yozora", "kanji": "夜空", "meaning": "Vast midnight sky glittering with silent distant stars"},
        {"romaji": "Chitose", "kanji": "千歳", "meaning": "A thousand years of longevity, peace and enduring honor"},
        {"romaji": "Genki", "kanji": "元気", "meaning": "Original primal spirit brimming with joy and health"},
        {"romaji": "Ayumu", "kanji": "歩", "meaning": "Walking forward step by step with steady determination"},
        {"romaji": "Kaede", "kanji": "楓", "meaning": "Maple tree whose autumn leaves glow like amber fires"},
        {"romaji": "Ryota", "kanji": "涼太", "meaning": "Refreshing cool breeze bringing comfort on sweltering days"}
    ],
    "lastname": [
        {"romaji": "Takahashi", "kanji": "高橋", "meaning": "High wooden bridge spanning a deep mountain gorge"},
        {"romaji": "Fujimoto", "kanji": "藤本", "meaning": "Rooted beneath ancient cascading purple wisteria"},
        {"romaji": "Kurosawa", "kanji": "黒沢", "meaning": "Dark marshland valley veiled in perpetual mist"},
        {"romaji": "Minamoto", "kanji": "源", "meaning": "Pure mountain springhead and legendary imperial samurai clan"},
        {"romaji": "Hattori", "kanji": "服部", "meaning": "Historical weaving guild and legendary Iga ninja clan"},
        {"romaji": "Katsuragi", "kanji": "葛城", "meaning": "Fortress overgrown with creeping kudzu vines"},
        {"romaji": "Amamiya", "kanji": "雨宮", "meaning": "Sacred celestial shrine blessed by falling rain"},
        {"romaji": "Shiroyama", "kanji": "白山", "meaning": "Snow-capped white mountain standing eternal"},
        {"romaji": "Matsuda", "kanji": "松田", "meaning": "Fertile rice field sheltered by evergreen pine trees"},
        {"romaji": "Kamisato", "kanji": "神里", "meaning": "Sacred village inhabited and protected by local deities"},
        {"romaji": "Tachibana", "kanji": "立花", "meaning": "Standing orange blossoms and classical flower arrangement noble clan"},
        {"romaji": "Saotome", "kanji": "早乙女", "meaning": "Young maiden rice planter singing seasonal hymns"},
        {"romaji": "Miyamoto", "kanji": "宮本", "meaning": "Residing at the base of the imperial shrine"},
        {"romaji": "Kirishima", "kanji": "霧島", "meaning": "Mystical misty volcanic island rising from coastal waters"},
        {"romaji": "Kanzaki", "kanji": "神崎", "meaning": "Divine coastal cape where spiritual winds blow"},
        {"romaji": "Hoshino", "kanji": "星野", "meaning": "Open expansive wilderness under a canopy of stars"},
        {"romaji": "Yukimura", "kanji": "幸村", "meaning": "Village of good fortune and legendary samurai courage"},
        {"romaji": "Kusanagi", "kanji": "草薙", "meaning": "Grass-mower; the sacred mythic imperial storm sword"},
        {"romaji": "Akimoto", "kanji": "秋元", "meaning": "Origin of autumn; golden harvests and changing leaves"},
        {"romaji": "Shimizu", "kanji": "清水", "meaning": "Crystal clear spring water bubbling from mountain stones"},
        {"romaji": "Nakamura", "kanji": "中村", "meaning": "Central village nestled safely between protective hills"},
        {"romaji": "Endo", "kanji": "遠藤", "meaning": "Distant wisteria clan carrying ancestral nobility"},
        {"romaji": "Kikuchi", "kanji": "菊地", "meaning": "Sacred land blooming with golden imperial chrysanthemums"},
        {"romaji": "Sugimoto", "kanji": "杉本", "meaning": "Living at the roots of towering aromatic cedar trees"},
        {"romaji": "Ogasawara", "kanji": "小笠原", "meaning": "Small straw hat plains; masters of archery and etiquette"}
    ],
    "villain": [
        {"romaji": "Kurokiba", "kanji": "黒牙", "meaning": "Black wolf fang tearing through the veil of peace"},
        {"romaji": "Yagami", "kanji": "夜神", "meaning": "Nocturnal god passing quiet judgment from the shadows"},
        {"romaji": "Rasetsu", "kanji": "羅刹", "meaning": "Flesh-devouring demon fiend born from Buddhist hells"},
        {"romaji": "Mukuro", "kanji": "骸", "meaning": "Hollow skeletal corpse devoid of human remorse"},
        {"romaji": "Zetsuei", "kanji": "絶影", "meaning": "Severed shadow moving faster than mortal perception"},
        {"romaji": "Byakuya", "kanji": "白夜", "meaning": "White night where merciless light reveals every weakness"},
        {"romaji": "Gouma", "kanji": "業魔", "meaning": "Karmic demon inflicting retributive torment"},
        {"romaji": "Shinraku", "kanji": "深落", "meaning": "Abyssal plunge into madness and psychological ruin"},
        {"romaji": "Kageyoshi", "kanji": "影善", "meaning": "False shadow saint masking slaughter with calm charity"},
        {"romaji": "Enma", "kanji": "閻魔", "meaning": "Dreaded sovereign judge of the underworld underworlds"},
        {"romaji": "Kyouraku", "kanji": "狂楽", "meaning": "Unhinged sadist who derives ecstatic joy from chaos"},
        {"romaji": "Kokushibo", "kanji": "黒死暴", "meaning": "Black death tempest leaving withered fields and ruins"},
        {"romaji": "Akuma", "kanji": "悪魔", "meaning": "Malevolent fiend completely consumed by violent intent"},
        {"romaji": "Ryuuketsu", "kanji": "流血", "meaning": "Flowing torrent of spilled enemy blood"},
        {"romaji": "Kuragari", "kanji": "暗がり", "meaning": "Suffocating pitch blackness swallowing every candle flame"},
        {"romaji": "Hanzaki", "kanji": "半裂", "meaning": "Brutal cleaver who splits shields and bodies in two"},
        {"romaji": "Mugen", "kanji": "無限", "meaning": "Infinite void that consumes prayers without answers"},
        {"romaji": "Dokuro", "kanji": "髑髏", "meaning": "Crowned grinning skull of a fallen conqueror"},
        {"romaji": "Orochi", "kanji": "大蛇", "meaning": "Eight-headed mythical venomous serpent of disaster"},
        {"romaji": "Kurogane", "kanji": "黒鉄", "meaning": "Cold black forged iron showing no mercy or warmth"},
        {"romaji": "Banshee", "kanji": "挽詩", "meaning": "Chilling funeral dirge foretelling immediate doom"},
        {"romaji": "Genkaku", "kanji": "幻覚", "meaning": "Sinister hallucination trapping heroes in mental prisons"},
        {"romaji": "Shiroma", "kanji": "白魔", "meaning": "Pale white demon smiling as kingdoms turn to ash"},
        {"romaji": "Kagehisa", "kanji": "影久", "meaning": "Eternal shadow that outlasts dynasties and light"},
        {"romaji": "Jigoku", "kanji": "地獄", "meaning": "The subterranean inferno that swallows all trespassers"}
    ],
    "boy": [
        {"romaji": "Hiroshi", "kanji": "寛", "meaning": "Tolerant, generous-hearted and broad-minded leader"},
        {"romaji": "Kenji", "kanji": "賢二", "meaning": "Wise and intelligent second son with sharp insight"},
        {"romaji": "Rintaro", "kanji": "倫太郎", "meaning": "Principled firstborn son guided by strong moral ethics"},
        {"romaji": "Shota", "kanji": "翔太", "meaning": "Big soaring bird flying high across unbounded horizons"},
        {"romaji": "Daisuke", "kanji": "大輔", "meaning": "Great noble helper standing loyal at his friend's side"},
        {"romaji": "Kenshin", "kanji": "剣心", "meaning": "Heart of the sword; unwavering integrity and discipline"},
        {"romaji": "Ryuto", "kanji": "竜斗", "meaning": "Dragon champion commanding celestial dippers"},
        {"romaji": "Takashi", "kanji": "貴", "meaning": "Noble, esteemed and held in high cultural honor"},
        {"romaji": "Kazuma", "kanji": "一真", "meaning": "One singular truth; sincere warrior without deception"},
        {"romaji": "Shinji", "kanji": "真司", "meaning": "Truthful guardian in charge of defending sacred oaths"},
        {"romaji": "Yuuki", "kanji": "勇気", "meaning": "Heroic courage that stands tall against impossible odds"},
        {"romaji": "Tsubasa", "kanji": "翼", "meaning": "Feathered wings carrying the dream of absolute freedom"},
        {"romaji": "Osamu", "kanji": "修", "meaning": "Diligent scholar cultivating martial and literary arts"},
        {"romaji": "Kazuya", "kanji": "和也", "meaning": "Bearer of tranquility and peaceful family balance"},
        {"romaji": "Naoki", "kanji": "直樹", "meaning": "Honest, upright tree growing straight toward heaven"},
        {"romaji": "Masato", "kanji": "正人", "meaning": "Upright, righteous person committed to chivalry"},
        {"romaji": "Seiji", "kanji": "誠二", "meaning": "Sincere second son known for loyal and honest counsel"},
        {"romaji": "Kouhei", "kanji": "公平", "meaning": "Justice and peace; mediator who brings fair treaties"},
        {"romaji": "Tetsuo", "kanji": "鉄雄", "meaning": "Iron-willed hero whose resolve never bends or shatters"},
        {"romaji": "Haruki", "kanji": "春樹", "meaning": "Spring timber tree flourishing with youthful vitality"},
        {"romaji": "Ryoma", "kanji": "竜馬", "meaning": "Dragon-spirited noble steed charging boldly into the fray"},
        {"romaji": "Shingo", "kanji": "真吾", "meaning": "Self-aware champion who speaks and defends truth"},
        {"romaji": "Tomoya", "kanji": "智也", "meaning": "Wise thinker who navigates complex conflicts smoothly"},
        {"romaji": "Eiji", "kanji": "栄二", "meaning": "Prosperous second son bringing glory to his household"},
        {"romaji": "Kouta", "kanji": "幸太", "meaning": "Blessed with boundless fortune and joyful strength"}
    ],
    "girl": [
        {"romaji": "Sakura", "kanji": "桜", "meaning": "Cherry blossom; ephemeral beauty and springtime renewal"},
        {"romaji": "Ame", "kanji": "雨", "meaning": "Gentle rain that cleanses the earth and nurtures flowers"},
        {"romaji": "Yuna", "kanji": "優奈", "meaning": "Gentle grace intertwined with calm fragrant greens"},
        {"romaji": "Kagura", "kanji": "神楽", "meaning": "Sacred ceremonial dance dedicated to ancient deities"},
        {"romaji": "Hina", "kanji": "陽菜", "meaning": "Sun-drenched greens blooming in peaceful valley gardens"},
        {"romaji": "Nozomi", "kanji": "望", "meaning": "Cherished hope and longing for an inspiring future"},
        {"romaji": "Mio", "kanji": "美桜", "meaning": "Exquisite cherry blossom glowing in morning dew"},
        {"romaji": "Asuka", "kanji": "飛鳥", "meaning": "Soaring bird flying freely across dawn horizons"},
        {"romaji": "Rin", "kanji": "凛", "meaning": "Dignified, cold elegance and courageous inner strength"},
        {"romaji": "Kasumi", "kanji": "霞", "meaning": "Delicate morning mist rolling over peaceful hillsides"},
        {"romaji": "Sayuri", "kanji": "小百合", "meaning": "Little white lily symbolizing purity and innocence"},
        {"romaji": "Ayame", "kanji": "菖蒲", "meaning": "Purple iris blossom guarding water gardens with beauty"},
        {"romaji": "Hikari", "kanji": "光", "meaning": "Radiant beam of light piercing through dark clouds"},
        {"romaji": "Kokoro", "kanji": "心", "meaning": "Pure soulful heart capable of boundless empathy"},
        {"romaji": "Mirai", "kanji": "未来", "meaning": "The hopeful future waiting to be written by dreamers"},
        {"romaji": "Suzu", "kanji": "鈴", "meaning": "Clear silver bell whose chimes ward off negative spirits"},
        {"romaji": "Yuki", "kanji": "雪", "meaning": "Pristine white snow blanketing the winter forest"},
        {"romaji": "Nanaho", "kanji": "七穂", "meaning": "Seven golden ears of ripening harvest grain"},
        {"romaji": "Mei", "kanji": "芽衣", "meaning": "Fresh sprout dressed in gentle woven silks"},
        {"romaji": "Tsubaki", "kanji": "椿", "meaning": "Winter camellia blooming proudly amid falling snow"},
        {"romaji": "Chiyo", "kanji": "千代", "meaning": "A thousand generations of happiness and harmony"},
        {"romaji": "Koharu", "kanji": "小春", "meaning": "Warm gentle Indian summer day in late autumn"},
        {"romaji": "Riko", "kanji": "莉子", "meaning": "Child of fragrant jasmine who brings joy to all"},
        {"romaji": "Hanabi", "kanji": "花火", "meaning": "Fireworks illuminating festival summer nights"},
        {"romaji": "Natsuki", "kanji": "夏希", "meaning": "Summer hope shining bright under golden sunbeams"}
    ]
}

def verify_uniqueness():
    seen = {}
    for page, names in STATIC_PAGE_DATA.items():
        assert len(names) == 25, f"Page {page} has {len(names)} names, expected 25"
        for item in names:
            name = item["romaji"].lower()
            if name in seen:
                raise ValueError(f"Duplicate name '{item['romaji']}' found on '{page}' and '{seen[name]}'")
            seen[name] = page
            assert item["kanji"].strip(), f"Empty kanji in {item}"
            assert item["meaning"].strip(), f"Empty meaning in {item}"
    print(f"SUCCESS: Verified {len(seen)} totally unique names across all 9 pages with zero duplicates!")

if __name__ == "__main__":
    verify_uniqueness()
    
    # Save static lists json
    with open("scripts/static_names.json", "w", encoding="utf-8") as f:
        json.dump(STATIC_PAGE_DATA, f, ensure_ascii=False, indent=2)
    print("Saved scripts/static_names.json")
