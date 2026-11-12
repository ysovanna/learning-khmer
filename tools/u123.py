# -*- coding: utf-8 -*-
"""Units 1-3 for Learning Khmer Part 1, built from ភាសាខ្មែរ កម្រិត ១ (MoEYSP literacy level 1)."""
import io, json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUB = "2026-11-11"

def unit_dir(slug):
    d = os.path.join(ROOT, slug)
    os.makedirs(d, exist_ok=True)
    return d

def save(u):
    d = unit_dir(u["slug"])
    with io.open(os.path.join(d, "unit.json"), "w", encoding="utf-8", newline="\n") as f:
        json.dump(u, f, ensure_ascii=False, indent=1)
    tiles = []
    for i, c in enumerate(u["cards"]):
        if c.get("tile"):
            tiles.append({"out": f'{u["slug"]}/img/{os.path.basename(c["img"])}', "text": c["tile"],
                          "bg": c.get("tile_bg", "#F4E9D8"), "fg": c.get("tile_fg", "#2B2118")})
    for x in u.get("explain", {}).get("tiles", []):
        if x.get("tile"):
            tiles.append({"out": f'{u["slug"]}/img/{os.path.basename(x["img"])}', "text": x["tile"],
                          "bg": x.get("tile_bg", "#EDE4F5"), "fg": x.get("tile_fg", "#3A2B4D")})
    return tiles

U1 = {
 "slug": "l1-a-series",
 "title_ko": "ព្យញ្ជនៈពួក «អ» ផ្សំស្រៈ",
 "title_en": "The “a” consonants meet the vowels",
 "subtitle": "មេរៀនទី ១ · Lesson 1 of ភាសាខ្មែរ កម្រិត ១",
 "description": "Start reading Khmer: the fifteen a-family consonants, their built-in -aa sound, and the first vowel signs (េ ែ ោ ៅ ា) with real words from the level-1 literacy book.",
 "sections": [
  {"id": "letters", "ko": "ពួកអ", "en": "The a-family", "color": "#0052A4"},
  {"id": "vowels", "ko": "ស្រៈ", "en": "First vowels", "color": "#00A84D"},
  {"id": "words", "ko": "ពាក្យ", "en": "Real words", "color": "#EF7C1C"}],
 "spine": {"title": "ខ្សែទី១ · From letters to words",
           "note": "Learn the fifteen a-family letters, see how vowels attach, then read real one-syllable words."},
 "explain": {
  "why": "អក្សរខ្មែរមានព្យញ្ជនៈ ៣៣ តួ បែងជាពីរពួក។ ពួកទីមួយហៅថា «ពួកអ» ព្រោះវាមានសំឡេង «អ» ជាប់ខាងក្នុង។",
  "tiles": [
   {"img": "img/x-15.svg", "tile": "១៥ តួ", "ko": "ពួកអ ១៥ តួ", "en": "Fifteen letters in the a-family"},
   {"img": "img/x-inherent.svg", "tile": "កា", "ko": "គ្មានស្រៈ = មាន អា", "en": "A bare letter already says -aa"},
   {"img": "img/x-front.svg", "tile": "េត", "ko": "ស្រៈខ្លះនៅពីមុខ", "en": "Some vowels are written in front"},
   {"img": "img/x-top.svg", "tile": "កោ", "ko": "ស្រៈខ្លះនៅពីលើ", "en": "Others sit on top or below"}]},
 "cards": [
  {"sec": "letters", "img": "img/c1.svg", "tile": "ក ខ ច ឆ", "flat": True, "alt": "Khmer letters ក ខ ច ឆ",
   "hook": "ពួកអ", "ko": "ព្យញ្ជនៈពួក «អ» មាន ១៥ តួ គឺ ក ខ ច ឆ ដ ឋ ណ ត ថ ប ផ ស ហ ឡ អ។",
   "en": "The “a” family has fifteen letters: ក ខ ច ឆ ដ ឋ ណ ត ថ ប ផ ស ហ ឡ អ.", "audio": "audio/c1.mp3"},
  {"sec": "letters", "img": "img/c2.svg", "tile": "ក=កា", "flat": True, "alt": "ក equals កា",
   "hook": "សំឡេង «អា»", "ko": "ព្យញ្ជនៈនៅម្នាក់ឯង មាន «អា» ជាប់ខាងក្នុង ដូចជា ក = កា ត = តា។",
   "en": "A bare consonant already carries -aa: ក reads “kaa”, ត reads “taa”.", "audio": "audio/c2.mp3"},
  {"sec": "vowels", "img": "img/c3.svg", "tile": "េ", "flat": True, "alt": "Vowel sign េ",
   "hook": "ស្រៈ េ", "ko": "ស្រៈ «េ» សរសេរនៅពីមុខព្យញ្ជនៈ ប៉ុន្តែអាននៅក្រោយ ដូចជា តេ។",
   "en": "The vowel េ is written before the letter but read after it: តេ = tae.", "audio": "audio/c3.mp3"},
  {"sec": "vowels", "img": "img/c4.svg", "tile": "ែ", "flat": True, "alt": "Vowel sign ែ",
   "hook": "ស្រៈ ែ", "ko": "ស្រៈ «ែ» នៅពីលើ ដូចជា តែ ផែ ខែ។",
   "en": "The vowel ែ sits on top: តែ tea, ផែ sandbar, ខែ moon/month.", "audio": "audio/c4.mp3"},
  {"sec": "vowels", "img": "img/c5.svg", "tile": "ោ", "flat": True, "alt": "Vowel sign ោ",
   "hook": "ស្រៈ ោ", "ko": "ស្រៈ «ោ» នៅពីលើដែរ ដូចជា ខោ សោ តោ។",
   "en": "The vowel ោ also sits on top: ខោ trousers, សោ padlock, តោ lion.", "audio": "audio/c5.mp3"},
  {"sec": "words", "img": "img/c6.svg", "tile": "ដៃ", "flat": True, "alt": "Two hands",
   "hook": "ដៃ", "ko": "ពាក្យថ្មី «ដៃ» ផ្សំពី ដ + ៃ។ សូមអានក្នុងចិត្ត។",
   "en": "New word ដៃ “hand”: ដ + ៃ. Read it in your head.", "audio": "audio/c6.mp3"},
  {"sec": "words", "img": "img/c7.svg", "tile": "ថ្ងៃ", "flat": True, "alt": "Sun over a day calendar",
   "hook": "ថ្ងៃ", "ko": "ពាក្យ «ថ្ងៃ» មានជើងអក្សរតូចនៅខាងក្រោម ប៉ុន្តែអានថា ថាំង។",
   "en": "In ថ្ងៃ “day” a small subscript letter hides below; the word still reads “thngai”.", "audio": "audio/c7.mp3"},
  {"sec": "words", "img": "img/c8.svg", "tile": "ខោ សោ តែ", "flat": True, "alt": "Trousers, padlock and tea",
   "hook": "អានឃ្លា", "ko": "សូមអានឃ្លា៖ «ប៉ាទិញខោ ម៉ែផឹកតែ»។",
   "en": "Read the phrase: “Pa tikh khao, me phuek tae” — Dad buys trousers, Mum drinks tea.", "audio": "audio/c8.mp3"}],
 "qa": [
  {"title": "គ្រោះ · Traps", "small": "Read these first", "kind": "trap",
   "items": [
    {"q": "ហេតុអ្វី «ក» និង «គ» សរសេរស្ទើរដូចគ្នា?", "qen": "Why do ក and គ look almost the same?",
     "qaudio": "audio/q1.mp3",
     "a": "ពួកវានៅខុសគ្នាពួក។ «ក» ជាពួកអ «គ» ជាពួកអ៊ សំឡេងស្រៈក៏ប្លែងទៅ។",
     "aen": "They belong to different families. ក is a-family, គ is â-family — the vowel sound changes with it.",
     "why": "សំឡេងពួកព្យញ្ជនៈកំណត់សំឡេងស្រៈទាំងអស់នៅក្នុងពាក្យ។",
     "audio": "audio/a1.mp3"},
    {"q": "«េ» សរសេរពីមុខ តើអានពីមុខដែរទេ?", "qen": "េ is written first — do I read it first?",
     "qaudio": "audio/q2.mp3",
     "a": "ទេ។ អានព្យញ្ជនៈមុន រួចស្រៈ «េ» ក្រោយ ដូចជា «តែ» អាន ត-ែ។",
     "aen": "No. Read the consonant first, then េ: តែ is “t” + “ae”.",
     "audio": "audio/a2.mp3"}]},
  {"title": "សំណួរ · Questions", "small": "Questions learners really ask", "kind": "qa",
   "items": [
    {"q": "តើខ្ញុំត្រូវចាំពួកអទាំង ១៥ តួមុនគេទេ?", "qen": "Must I memorise all fifteen letters first?",
     "qaudio": "audio/q3.mp3",
     "a": "មិនចាំបាច់ចាំភ្លាមទេ។ អានរាល់ថ្ងៃតិចៗ ពាក្យនឹងជួយឱ្យចាំខ្លួនឯង។",
     "aen": "Not all at once. Read a little every day; the words will make you remember.",
     "audio": "audio/a3.mp3"},
    {"q": "ពាក្យណាប្រើស្រៈ «ោ» ខ្លះ?", "qen": "Which words use ោ?",
     "qaudio": "audio/q4.mp3",
     "a": "ខោ សោ តោ គោ នៅ។",
     "aen": "ខោ trousers, សោ lock, តោ lion, គោ cow.",
     "audio": "audio/a4.mp3"},
    {"q": "«ថ្ងៃ» អានដូចម្តេច?", "qen": "How do I read ថ្ងៃ?",
     "qaudio": "audio/q5.mp3",
     "a": "អាន «ថាំង»។ និយាយពីជើងអក្សរនៅមេរៀនទី ៥។",
     "aen": "Read it “thngai”. Subscript letters get their own lesson (Lesson 5).",
     "audio": "audio/a5.mp3"}]},
  {"title": "ពាក្យសង្គ្រោះ · Survival lines", "kind": "surv",
   "items": [
    {"ko": "ជួយអានឱ្យខ្ញុំស្តាប់ផង។", "en": "Please read this aloud for me.", "audio": "audio/s1.mp3"},
    {"ko": "ពាក្យនេះអានដូចម្តេច?", "en": "How is this word read?", "audio": "audio/s2.mp3"}]}],
 "vocab": [
  {"title": "ពួកអ · a-family letters", "color": "#0052A4",
   "items": [{"ko": "ក", "en": "kaa"}, {"ko": "ខ", "en": "khaa"}, {"ko": "ច", "en": "chaa"},
             {"ko": "ត", "en": "taa"}, {"ko": "ប", "en": "paa"}, {"ko": "ស", "en": "saa"}]},
  {"title": "ពាក្យមួយព្យាង្គ · One-syllable words", "color": "#00A84D",
   "items": [{"ko": "ខោ", "en": "trousers"}, {"ko": "សោ", "en": "padlock"}, {"ko": "ដៃ", "en": "hand"},
             {"ko": "តែ", "en": "tea"}, {"ko": "ផែ", "en": "sandbar / road"}, {"ko": "គោ", "en": "cow"}]},
  {"title": "ពាក្យបន្តិចបន្តួច · Everyday bits", "color": "#EF7C1C",
   "items": [{"ko": "ថ្ងៃ", "en": "day"}, {"ko": "ខែ", "en": "moon / month"}, {"ko": "ប៉ា", "en": "dad"},
             {"ko": "ម៉ែ", "en": "mum"}, {"ko": "ទិញ", "en": "to buy"}, {"ko": "ផឹក", "en": "to drink"}]}],
 "published": PUB}

U2 = {
 "slug": "l2-aa-series",
 "title_ko": "ព្យញ្ជនៈពួក «អ៊» ផ្សំស្រៈ",
 "title_en": "The “â” consonants meet the vowels",
 "subtitle": "មេរៀនទី ២ · Lesson 2 of ភាសាខ្មែរ កម្រិត ១",
 "description": "The eighteen soft (voiced) consonants of the â-family, how they bend every vowel sound, and family/job words from the level-1 book.",
 "sections": [
  {"id": "letters", "ko": "ពួកអ៊", "en": "The â-family", "color": "#996CAC"},
  {"id": "sound", "ko": "សំឡេង", "en": "How they bend vowels", "color": "#CD7C2F"},
  {"id": "family", "ko": "គ្រួសារ", "en": "Family & work", "color": "#AE432E"}],
 "spine": {"title": "ខ្សែទី២ · The soft family",
           "note": "Meet the eighteen voiced letters, hear how they bend vowels, then use them in family and job words."},
 "explain": {
  "why": "ពួកអ៊ (ឃោសៈ) មានសំឡេងធំគ្រលរ។ នៅពេលវាជួបស្រៈតែមួយ សំឡេងស្រៈប្លែងខុសពីពួកអ។",
  "tiles": [
   {"img": "img/x-18.svg", "tile": "១៨ តួ", "ko": "ពួកអ៊ ១៨ តួ", "en": "Eighteen letters in the â-family"},
   {"img": "img/x-pair.svg", "tile": "កា គា", "ko": "ស្រៈដូច សំឡេងខុស", "en": "Same vowel sign, different sound"},
   {"img": "img/x-soft.svg", "tile": "ង ញ ន", "ko": "សំឡេងក្រាស់", "en": "Nasals and voiced sounds"}]},
 "cards": [
  {"sec": "letters", "img": "img/c1.svg", "tile": "គ ឃ ង ជ", "flat": True, "alt": "Khmer letters គ ឃ ង ជ",
   "hook": "ពួកអ៊", "ko": "ពួក «អ៊» មាន ១៨ តួ ដូចជា គ ឃ ង ជ ឈ ញ ទ ធ ន ព ភ ម យ រ ល វ។",
   "en": "The â-family has eighteen letters: គ ឃ ង ជ ឈ ញ ទ ធ ន ព ភ ម យ រ ល វ and friends.", "audio": "audio/c1.mp3"},
  {"sec": "letters", "img": "img/c2.svg", "tile": "គ=កោ", "flat": True, "alt": "គ reads kô",
   "hook": "សំឡេង «អូ»", "ko": "ពួកអ៊ នៅម្នាក់ឯង មានសំឡេង «អូ» ជាប់ខាងក្នុង ដូចជា គ = កោ។",
   "en": "A bare â-family letter carries -ô: គ reads “kô”.", "audio": "audio/c2.mp3"},
  {"sec": "sound", "img": "img/c3.svg", "tile": "ទឹក", "flat": True, "alt": "A glass of water",
   "hook": "ទឹក", "ko": "«ទ» ជាពួកអ៊។ «ទឹក» អាន តឹក មានន័យថាទឹកសម្រាប់ផឹក។",
   "en": "ទ is â-family. ទឹក “water” — the drink.", "audio": "audio/c3.mp3"},
  {"sec": "sound", "img": "img/c4.svg", "tile": "នាង", "flat": True, "alt": "A woman",
   "hook": "នាង", "ko": "«នាង» អាន នៀង សម្រាប់ហៅស្ត្រី។",
   "en": "នាង reads “nieng” — she / a young woman.", "audio": "audio/c4.mp3"},
  {"sec": "family", "img": "img/c5.svg", "tile": "យាយ", "flat": True, "alt": "A grandmother",
   "hook": "យាយ", "ko": "ពាក្យគ្រួសារពួកអ៊ ដូចជា យាយ មាតា ភរិយា។",
   "en": "Family words from the â-family: យាយ grandmother, មាតا mother, ភរិយា wife.", "audio": "audio/c5.mp3"},
  {"sec": "family", "img": "img/c6.svg", "tile": "គ្រូ", "flat": True, "alt": "A teacher at a blackboard",
   "hook": "គ្រូ", "ko": "«គ្រូ» មានជើង «រ» នៅក្រោម «គ»។ គ្រូបង្រៀនអក្ខរកម្មនៅមណ្ឌលសិក្សា។",
   "en": "គ្រូ “teacher” hides a subscript រ under គ. Literacy teachers work at learning centres.", "audio": "audio/c6.mp3"},
  {"sec": "family", "img": "img/c7.svg", "tile": "មុខរបរ", "flat": True, "alt": "Farming tools",
   "hook": "មុខរបរ", "ko": "«មុខរបរ» មានពីរព្យាង្គ។ មុខរបរសំខាន់របស់គ្រួសារនាងចន្តាគឺធ្វើស្រែ។",
   "en": "មុខរបរ “occupation” has two syllables. Chantha's family main job is rice farming.", "audio": "audio/c7.mp3"},
  {"sec": "family", "img": "img/c8.svg", "tile": "ដាំបន្លែ", "flat": True, "alt": "Growing vegetables",
   "hook": "ដាំបន្លែ", "ko": "មុខរបរបន្ថែមគឺ «ដាំបន្លែ» ដើម្បីបង្កើនប្រាក់ចំណូល។",
   "en": "The side job is growing vegetables (ដាំបន្លែ) to raise the family income.", "audio": "audio/c8.mp3"}],
 "qa": [
  {"title": "គ្រោះ · Traps", "small": "Read these first", "kind": "trap",
   "items": [
    {"q": "«កា» និង «គា» អានដូចគ្នាទេ?", "qen": "Are កា and គា read the same?",
     "qaudio": "audio/q1.mp3",
     "a": "ខុស។ «កា» (ពួកអ) អាន kaa «គា» (ពួកអ៊) អាន kaô ស្ទើរ «កៅ»។",
     "aen": "No. កា (a-family) = “kaa”; គា (â-family) bends toward “kaô”.",
     "why": "នេះជាគន្លឹះធំបំផុតនៃការអានខ្មែរ៖ ពួកព្យញ្ជនៈកំណត់សំឡេងស្រៈ។",
     "audio": "audio/a1.mp3"},
    {"q": "«ទ» នៅពួកអ៊ ហេតុអ្វី «ទារក» ស្តាប់ទូច «ត»? ", "qen": "If ទ is voiced, why does ទារក sound like t?",
     "qaudio": "audio/q2.mp3",
     "a": "សំឡេង «ទ» ខ្សោយជាងមុនទៅតាមពេលវេលា ប៉ុន្តែវានៅរាប់ជាក្រុមអ៊ ដូច្នេះស្រៈនៅតែប្លែង។",
     "aen": "ទ softened over time but still counts as â-family, so it still bends the vowel.",
     "audio": "audio/a2.mp3"}]},
  {"title": "សំណួរ · Questions", "small": "Questions learners really ask", "kind": "qa",
   "items": [
    {"q": "តើ «យ» និង «វ» នៅពួកណា?", "qen": "Which family do យ and វ belong to?",
     "qaudio": "audio/q3.mp3",
     "a": "ទាំងពីរនៅពួកអ៊។ ដូច្នេះ «យាយ» និង «វាល» មានសំឡេងស្រៈបែបអ៊។",
     "aen": "Both are â-family, so យាយ and វាល carry the bent vowels.",
     "audio": "audio/a3.mp3"},
    {"q": "«មុខរបរ» និង «មុខងារ» ខុសគ្នាទេ?", "qen": "Is មុខរបរ different from មុខងារ?",
     "qaudio": "audio/q4.mp3",
     "a": "«មុខរបរ» ជាការរកស៊ី «មុខងារ» ជាតួនាទីនៅកន្លែងធ្វើការ។",
     "aen": "មុខរបរ is your livelihood; មុខងារ is a role or function at work.",
     "audio": "audio/a4.mp3"},
    {"q": "ពាក្យគ្រួសារមានអ្វីខ្លះ?", "qen": "What family words should I know?",
     "qaudio": "audio/q5.mp3",
     "a": "ឪពុក ម្តាយ បង ប្អូន កូន ចៅ ស្វាមី ភរិយា។",
     "aen": "ឪពុក father, ម្តាយ mother, បង older sibling, ប្អូន younger sibling, កូន child, ចៅ grandchild.",
     "audio": "audio/a5.mp3"}]},
  {"title": "ពាក្យសង្គ្រោះ · Survival lines", "kind": "surv",
   "items": [
    {"ko": "មុខរបរអ្នកធ្វើអ្វី?", "en": "What is your occupation?", "audio": "audio/s1.mp3"},
    {"ko": "គ្រួសារខ្ញុំមានប្រាំនាក់។", "en": "My family has five members.", "audio": "audio/s2.mp3"}]}],
 "vocab": [
  {"title": "ពួកអ៊ · â-family letters", "color": "#996CAC",
   "items": [{"ko": "គ", "en": "kô"}, {"ko": "ង", "en": "ngô"}, {"ko": "ជ", "en": "cô"},
             {"ko": "ទ", "en": "tô"}, {"ko": "ន", "en": "nô"}, {"ko": "ម", "en": "mô"}]},
  {"title": "គ្រួសារ · Family", "color": "#AE432E",
   "items": [{"ko": "ឪពុក", "en": "father"}, {"ko": "ម្តាយ", "en": "mother"}, {"ko": "បង", "en": "older sibling"},
             {"ko": "ប្អូន", "en": "younger sibling"}, {"ko": "កូន", "en": "child"}, {"ko": "ចៅ", "en": "grandchild"}]},
  {"title": "មុខរបរ · Work", "color": "#CD7C2F",
   "items": [{"ko": "គ្រួសារ", "en": "family"}, {"ko": "សមាជិក", "en": "member"}, {"ko": "មុខរបរ", "en": "occupation"},
             {"ko": "ដាំបន្លែ", "en": "to grow vegetables"}, {"ko": "ប្រាក់ចំណូល", "en": "income"}, {"ko": "គ្រូ", "en": "teacher"}]}],
 "published": PUB}

U3 = {
 "slug": "l3-two-syllable",
 "title_ko": "ពាក្យពីរព្យាង្គ",
 "title_en": "Two-syllable words",
 "subtitle": "មេរៀនទី ៣ · Lesson 3 of ភាសាខ្មែរ កម្រិត ១",
 "description": "Break and rebuild two-syllable Khmer words (អាហារ ចំណូល កៅអី…), with the hobbies reading passage from the level-1 book.",
 "sections": [
  {"id": "split", "ko": "បំបែក", "en": "Break it apart", "color": "#008778"},
  {"id": "build", "ko": "ផ្ទុំ", "en": "Build it back", "color": "#576BB6"},
  {"id": "hobby", "ko": "ចំណង់", "en": "Hobbies & farm life", "color": "#BA6266"}],
 "spine": {"title": "ខ្សែទី៣ · Two beats per word",
           "note": "Split two-syllable words, rebuild them from letters, then read the hobby passage."},
 "explain": {
  "why": "ពាក្យខ្មែរភាគច្រើនមានពីរព្យាង្គ។ ព្យាង្គទីមួយអានស្រាលៗ ព្យាង្គទីពីរអានខ្លាំងជាង។",
  "tiles": [
   {"img": "img/x-beat.svg", "tile": "អា-ហារ", "ko": "ពីរចង្វាក់", "en": "Two beats: light then strong"},
   {"img": "img/x-split.svg", "tile": "ស+រ=សរ", "ko": "បំបែក រួចផ្ទុំវិញ", "en": "Split the word, build it back"},
   {"img": "img/x-same.svg", "tile": "សរ-សេរ", "ko": "អក្សរដូច សំឡេងអាចខុស", "en": "Same letters can hide different words"}]},
 "cards": [
  {"sec": "split", "img": "img/c1.svg", "tile": "បំបែក", "flat": True, "alt": "A word split into two halves",
   "hook": "ពីរព្យាង្គ", "ko": "ពាក្យពីរព្យាង្គ អានចង្វាក់ទីមួយស្រាល ចង្វាក់ទីពីរធ្ងន់ ដូចជា «អា-ហារ»។",
   "en": "Two-syllable words: light first beat, heavier second — អា-ហារ “food”.", "audio": "audio/c1.mp3"},
  {"sec": "split", "img": "img/c2.svg", "tile": "កកេរ=ក+កេរ", "flat": True, "alt": "Splitting កកេរ",
   "hook": "បំបែកពាក្យ", "ko": "ឧទាហរណ៍ «កកេរ» = ក + កេរ។ សូមបំបែក «សរសេរ» តាមវិធីដូចគ្នា។",
   "en": "Example: កកេរ = ក + កេរ. Now split សរសេរ the same way.", "audio": "audio/c2.mp3"},
  {"sec": "split", "img": "img/c3.svg", "tile": "ចរចា", "flat": True, "alt": "Two people talking",
   "hook": "ចរចា", "ko": "«ចរចា» មានន័យថានិយាយគ្នាដើម្បីឈានដល់កិច្ចព្រមព្រៀង។",
   "en": "ចរចា means to negotiate, to talk toward an agreement.", "audio": "audio/c3.mp3"},
  {"sec": "build", "img": "img/c4.svg", "tile": "ក+ៅ+អ+ី=កៅអី", "flat": True, "alt": "A chair built from letters",
   "hook": "កៅអី", "ko": "ផ្ទុំពាក្យ៖ ក + ៅ + អ + ី = «កៅអី» (chair)។",
   "en": "Build: ក + ៅ + អ + ី = កៅអី “chair”.", "audio": "audio/c4.mp3"},
  {"sec": "build", "img": "img/c5.svg", "tile": "សរសើរ≠សរសេរ", "flat": True, "alt": "A medal and a pencil side by side",
   "hook": "សរសើរ / សរសេរ", "ko": "ប្រយ័ត្ន «សរសើរ» (to praise) និង «សរសេរ» (to write) សរសេរជិតដូចគ្នា។",
   "en": "Careful: សរសើរ “praise” and សរសេរ “write” look almost alike.", "audio": "audio/c5.mp3"},
  {"sec": "build", "img": "img/c6.svg", "tile": "ដំណាំ≠ចំណាំ", "flat": True, "alt": "A plant and a note pin",
   "hook": "ដំណាំ / ចំណាំ", "ko": "«ដំណាំ» ជាដើមឈើ «ចំណាំ» ជាការទុកក្នុងចិត្ត។",
   "en": "ដំណាំ is a plant; ចំណាំ means to remember / mark.", "audio": "audio/c6.mp3"},
  {"sec": "hobby", "img": "img/c7.svg", "tile": "ចម្ការ", "flat": True, "alt": "A farm plot by a river",
   "hook": "ចម្ការ", "ko": "សុខាមានដីចម្ការមួយកន្លែងតាមដងទន្លេ មានដំណាំជាច្រើនមុខ។",
   "en": "Sokha has a plot of farm land along the river with many crops.", "audio": "audio/c7.mp3"},
  {"sec": "hobby", "img": "img/c8.svg", "tile": "ចិតពោត", "flat": True, "alt": "Hands shelling corn",
   "hook": "ចិត / ដេញ", "ko": "ធីតាចិតពោត រួចដើរទៅទិញទឹកអំពៅ។ នាងដេញចាបហើរចេញទៅ។",
   "en": "Tida shells corn, then goes to buy sugarcane juice. She chases the birds away.", "audio": "audio/c8.mp3"}],
 "qa": [
  {"title": "គ្រោះ · Traps", "small": "Read these first", "kind": "trap",
   "items": [
    {"q": "«បបរ» និង «ប៉ប៉រ»? ពាក្យណាត្រូវ?", "qen": "Which spelling is right for porridge?",
     "qaudio": "audio/q1.mp3",
     "a": "«បបរ» ត្រូវ។ សរសេរពីរព្យាង្គដោយអក្សរពិត មិនចាំបាច់មានសញ្ញាផ្សេងទេ។",
     "aen": "«បបរ» is correct — plain two-syllable spelling, no extra marks.",
     "audio": "audio/a1.mp3"},
    {"q": "ហេតុអ្វី «ឆាឆៅ» មិនមែន «ឆាឆៅ» សំឡេងដូចគ្នា?", "qen": "Why do the two halves of ឆាឆៅ sound different?",
     "qaudio": "audio/q2.mp3",
     "a": "ព្រោះ «ឆ» ជាពួកអ «ឋ/ថ» សំឡេងខុសគ្នា។ «ឆៅ» raw មានសំឡេងពួកអ។",
     "aen": "Each syllable keeps its own consonant family, so the vowel colours differ.",
     "audio": "audio/a2.mp3"}]},
  {"title": "សំណួរ · Questions", "small": "Questions learners really ask", "kind": "qa",
   "items": [
    {"q": "«អាហារ» «អាកាស» ចាប់ផ្តើមដូចគ្នាទេ?", "qen": "Do អាហារ and អាកាស start the same?",
     "qaudio": "audio/q3.mp3",
     "a": "បាទ/ចាស ទាំងពីរចាប់ផ្តើម «អា»។ ន័យខុសគ្នា៖ អាហារ food, អាកាស sky/air។",
     "aen": "Yes — both start អា; meanings differ: food vs sky/air.",
     "audio": "audio/a3.mp3"},
    {"q": "«បង្កើន» និង «បន្ថែម» ប្រើដូចគ្នាទេ?", "qen": "Are បង្កើន and បន្ថែម interchangeable?",
     "qaudio": "audio/q4.mp3",
     "a": "ប្រហាក់ប្រហែល។ «បង្កើនចំណូល» ឬ «បន្ថែមចំណូល» សុទ្ធតែត្រូវ។",
     "aen": "Close enough: both បង្កើន and បន្ថែម work with income.",
     "audio": "audio/a4.mp3"},
    {"q": "«ចំណាយ» ន័យអ្វី?", "qen": "What does ចំណាយ mean?",
     "qaudio": "audio/q5.mp3",
     "a": "«ចំណាយ» គឺការប្រើប្រាស់លុយ។ ចំណូលចូល ចំណាយចេញ។",
     "aen": "ចំណាយ is spending. Income comes in, expenses go out.",
     "audio": "audio/a5.mp3"}]},
  {"title": "ពាក្យសង្គ្រោះ · Survival lines", "kind": "surv",
   "items": [
    {"ko": "ខ្ញុំចូលចិត្តដាំដំណាំ។", "en": "I like growing crops.", "audio": "audio/s1.mp3"},
    {"ko": "តើពាក្យនេះមានពីរប៉ុន្មានព្យាង្គ?", "en": "How many syllables does this word have?", "audio": "audio/s2.mp3"}]}],
 "vocab": [
  {"title": "បំបែក-ផ្ទុំ · Split & build", "color": "#008778",
   "items": [{"ko": "អាហារ", "en": "food"}, {"ko": "កៅអី", "en": "chair"}, {"ko": "សំឡី", "en": "wasp"},
             {"ko": "ដំបៅ", "en": "brooding / warm nest"}, {"ko": "បបរ", "en": "rice porridge"}, {"ko": "កីឡា", "en": "sport"}]},
  {"title": "ចម្ការ · Farm life", "color": "#BA6266",
   "items": [{"ko": "ដំណាំ", "en": "crop"}, {"ko": "ចម្ការ", "en": "farm plot"}, {"ko": "ទឹកអំពៅ", "en": "sugarcane juice"},
             {"ko": "ពោត", "en": "corn"}, {"ko": "ចាប", "en": "sparrow"}, {"ko": "ហាល", "en": "to sun-dry"}]},
  {"title": "សកម្មភាព · Actions", "color": "#576BB6",
   "items": [{"ko": "ចិត", "en": "to shell / peel"}, {"ko": "ដេញ", "en": "to chase"}, {"ko": "កោស", "en": "to scratch / sweep"},
             {"ko": "ផឹក", "en": "to drink"}, {"ko": "ដោត", "en": "to stick in"}, {"ko": "បឺក", "en": "to pluck"}]}],
 "published": PUB}

if __name__ == "__main__":
    all_tiles = []
    for u in (U1, U2, U3):
        # fix a stray Arabic char that slipped into U1/U2 copy
        s = json.dumps(u, ensure_ascii=False).replace("មាតا", "មាតា")
        u = json.loads(s)
        all_tiles += save(u)
    with io.open(os.path.join(ROOT, "_tiles_u123.json"), "w", encoding="utf-8") as f:
        json.dump(all_tiles, f, ensure_ascii=False, indent=1)
    print("units 1-3 written;", len(all_tiles), "tiles queued")
