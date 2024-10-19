import random

quotes = [
  {
    "text": "Prayer cleanses the soul, pain cleanses the body, 18 hours of TI cleanses the sanity.",
    "citation": "Warhammer 40000(3rd edition)",
    "topics": [
      "PRAYER",
      "PAIN"
    ]
  },
  {
    "text": "Sorrow awaits the foolhardy. John awaits the minor offenders",
    "citation": "Codex: Armageddon(3rd edition)",
    "topics": [
      "FOOLISHNESS"
    ]
  },
  {
    "text": "The difference between heresy and treachery is ignorance. For Aaron, the difference between fun and treachery is boardgames.",
    "citation": "Warhammer 40000(3rd edition)",
    "topics": [
      "TREACHERY"
    ]
  },
  {
    "text": "The keenest blade is righteous pedantry.",
    "citation": "Warhammer 40000(4th edition)",
    "topics": [
      "PENDANTRY"
    ]
  },
  {
    "text": "To Know Ian is to Know Hate.",
    "citation": "The Traitor's Hand(novel)",
    "topics": [
      "IAN"
    ]
  },
  {
    "text": "By the manner of their art we shall hate them.",
    "citation": "The Traitor's Hand(novel)",
    "topics": [
      "IAN QUOTES"
    ]
  },
  {
    "text": "Break a deal spin the wheel",
    "citation": "The Traitor's Hand(novel)",
    "topics": [
      "IAN QUOTES"
    ]
  },
  {
    "text": "Pedantry ALWAYS wins.",
    "citation": "The Traitor's Hand(novel)",
    "topics": [
      "LUKE QUOTES"
    ]
  },
  {
    "text": "Never listen to Aaron while playing a board game.",
    "citation": "The Traitor's Hand(novel)",
    "topics": [
      "UNIVERSAL TRUTH"
    ]
  },
  {
    "text": "Only the dead know the end of Pendragons Spite laser.",
    "citation": "The Traitor's Hand(novel)",
    "topics": [
      "SPITE"
    ]
  },
  {
    "text": "The universe is a big place and, whatever happens, you will not be missed... except for Tom Nurse, hes wholesome.",
    "citation": "Warhammer 40000(5th edition)",
    "topics": [
      "MEMORIES"
    ]
  },
  {
    "text": "There are no answers. Only death and Ian.",
    "citation": "Warhammer 40000: Rogue Trader",
    "topics": [
      "ANSWERS",
      "DEATH"
    ]
  },
  {
    "text": "EXTREMELY LOUD EXHALE",
    "citation": "Warhammer 40000(5th edition)",
    "topics": [
      "CHRIS INFORMING YOU OF A POOR CHOICE"
    ]
  },
  {
    "text": "To err is to invite Luke to correct you.",
    "citation": "Warhammer 40000: Rogue Trader",
    "topics": [
      "UNIVERSAL TRUTH"
    ]
  },
  {
    "text": "To withdraw in disgust is not apathy, it is a natural reaction to Art.",
    "citation": "Warhammer 40000(4th edition)",
    "topics": [
      "IAN QUOTES"
    ]
  },
  {
    "text": "I declare myself Space Bureaucrat, prepare for new taxes.",
    "citation": "Codex: Black Templars(4th edition)",
    "topics": [
      "PENDRAGON PLAYING TI"
    ]
  },
  {
    "text": "Let me inform you, in great detail, about why that was a bad move.",
    "citation": "Codex: Black Templars(4th edition)",
    "topics": [
      "PENDRAGON QUOTES"
    ]
  },
  {
    "text": "Vigilance is my shield, Simpsons Quotes are my sword.",
    "citation": "Codex: Necrons(3rd edition)",
    "topics": [
      "TIMS MANTRA"
    ]
  },
  {
    "text": "A coward always seeks compromise. A fool trusts Aaron.",
    "citation": "Warhammer 40000(4th edition)",
    "topics": [
      "BOARDGAMES"
    ]
  },
  {
    "text": "An illogical argument must be dismissed with absolute conviction!",
    "citation": "Warhammer 40000(4th edition)",
    "topics": [
      "LUKE LOGIC"
    ]
  },
  {
    "text": "Accept your lot! Don't accept Jacks advice during a boardgame!",
    "citation": "Warhammer 40000(4th edition)",
    "topics": [
      "WISDOM"
    ]
  },
  {
    "text": "Disregard previous advice around not listening to Jack's advice during a boardgame. Its Good Advice!",
    "citation": "Warhammer 40000(4th edition)",
    "topics": [
      "SHUT UP LUKE"
    ]
  },
  {
    "text": "Knowledge is power, hide it well. Perhaps too well.",
    "citation": "Warhammer 40000(3rd edition)",
    "topics": [
      "KNOWLEDGE"
    ]
  },
  {
    "text": "Only the insane have strength enough to prosper or win against Aaron in a game of drinking chess.",
    "citation": "Codex: Space Marines(4th edition)",
    "topics": [
      "INSANITY"
    ]
  },
  {
    "text": "I hate my life, why would anyone enjoy this game?",
    "citation": "Warhammer 40000(4th edition)",
    "topics": [
      "WHAT SANE PEOPLE SAY AFTER PLAYING WARHAMMER FANTASY"
    ]
  },
  {
    "text": "Only the weak question. Real strength comes from pedantry.",
    "citation": "Imperial Armour IV",
    "topics": [
      "QUESTION"
    ]
  },
  {
    "text": "It is better for a man to be afraid than happy.",
    "citation": "Warhammer 40000(6th edition)",
    "topics": [
      "JOHNS WORK PHILOSOPHY"
    ]
  },
  {
    "text": "To err is human; To err again is treachery; To err yet again is Ian testing the limits of acceptable decorum at a dinner party",
    "citation": "Warhammer 40000(6th edition)",
    "topics": [
      "ERR"
    ]
  },
  {
    "text": "A closed mind is defence against sedition therefore Jacks mind is not seditious",
    "citation": "Warhammer 40000(6th edition)",
    "topics": [
      "CLOSED MIND",
      "SEDITION"
    ]
  },
  {
    "text": "Let none find us wanting rice cookers.",
    "citation": "September 2024 Update",
    "topics": [
      "PREPAREDNESS",
      "VIGILANCE"
    ]
  },
  {
    "text": "What I cannot crush with words I will crush with the titans of Tophers vast legions!",
    "citation": "September 2024 Update",
    "topics": [
      "ARMAMENT",
      "VICTORY",
      "PURCHASING POWER"
    ]
  },
  {
    "text": "While the enemies of Antons motherland still draw breath, there can be no peace.",
    "citation": "September 2024 Update",
    "topics": [
      "PEACE",
      "BETRAYAL",
      "KYLO QUOTES"
    ]
  },
  {
    "text": "Suffer not the unfinished faces to live.",
    "citation": "September 2024 Update",
    "topics": [
      "TOLERANCE",
      "SLAPCHOP"
    ]
  },
  {
    "text": "A moment of laxity spawns a lifetime of memery.",
    "citation": "September 2024 Update",
    "topics": [
      "VIGILANCE"
    ]
  },
  {
    "text": "Walk softly, and carry TWO big guns.",
    "citation": "September 2024 Update",
    "topics": [
      "FANFIC"
    ]
  },
  {
    "text": "The wise man learns from the egg reheating tips of others.",
    "citation": "September 2024 Update",
    "topics": [
      "EGG"
    ]
  },
  {
    "text": "Adamantium walls and plasteel bulkheads may seem formidable, but an unshakeable faith in Slap Chop can overcome any barriers.",
    "citation": "September 2024 Update",
    "topics": [
      "DEFENCES",
      "PAINTING TIPS"
    ]
  },
  {
    "text": "An unprotected soul can no more cross the storms of the warp than Tim can avoid being mistaken for Frodo Baggins.",
    "citation": "September 2024 Update",
    "topics": [
      "IDENTITY",
      "TRUTH"
    ]
  },
  {
    "text": "For those who seek perfection there can be no rest on this side of Lukes pedantry.",
    "citation": "September 2024 Update",
    "topics": [
      "IDEALISM"
    ]
  },
  {
    "text": "Between the dice rolls the ancient unseen enemies of mankind wait and hunger. Every attempt to block is a confrontation with horror, with the implacable risk of a turnover, and with man's own innermost fear of rolling double skulls.",
    "citation": "September 2024 Update",
    "topics": [
      "THE BEST AND WORST GAME IN EXISTENCE"
    ]
  },
  {
    "text": "By the manner of their saltiness we shall know them.",
    "citation": "September 2024 Update",
    "topics": [
      "IDENTITY"
    ]
  },
  {
    "text": "It is not the Horror of War that troubles me but the Unseen Horrors of Stolen Valour.",
    "citation": "September 2024 Update",
    "topics": [
      "FALSEHOOD"
    ]
  },
  {
    "text": "Losses are acceptable. Microwaving egg is not.",
    "citation": "September 2024 Update",
    "topics": [
      "EXTREMELY EDGE-CASE FOOD TYPES"
    ]
  },
  {
    "text": "The only appropriate reaction to the existential dread of a vast uncaring universe is to purchase more miniatures.",
    "citation": "September 2024 Update",
    "topics": [
      "DREAD"
    ]
  },
  {
    "text": "Words do not win wars. Good dice rolls do.",
    "citation": "September 2024 Update",
    "topics": [
      "WAR"
    ]
  },
  {
    "text": "Revere the Omnissiah, for it is the source of all single-purpose dedicated computing devices.",
    "citation": "September 2024 Update",
    "topics": [
      "OMNISSIAH",
      "OUTLANDISH CONCEPTS"
    ]
  },
  {
    "text": "Faith in James is its own reward.",
    "citation": "September 2024 Update",
    "topics": [
      "FAITH"
    ]
  },
  {
    "text": "No army is big enough to conquer the galaxy. But a perfect score of 120 battle points alone can overturn the universe.",
    "citation": "September 2024 Update",
    "topics": [
      "DR 120"
    ]
  },
  {
    "text": "Is this faith in the Emperor, or is this Loss?",
    "citation": "September 2024 Update",
    "topics": [
      "FAITH",
      "LOSS"
    ]
  },
  {
    "text": "Let only war and destruction rain down on those with dissenting breakfast views.",
    "citation": "September 2024 Update",
    "topics": [
      "WAR",
      "CONTROVERSY"
    ]
  },
  {
    "text": "If a man dies that another should live, that man's spirit shall eat edge-case foods such as egg at the Emperor's table.",
    "citation": "September 2024 Update",
    "topics": [
      "EGGNOCENTRISM"
    ]
  },
  {
    "text": "Drink deep the water of Drunkbot and remember the fallen.",
    "citation": "September 2024 Update",
    "topics": [
      "RESPECT FOR THE FALLEN"
    ]
  },
  {
    "text": "The heretics may burn, the xenos may bleed, but no force in the galaxy will prevent this meal from being labelled as 'steamed.' It's a local tradition.",
    "citation": "September 2024 Update",
    "topics": [
      "TRADITION"
    ]
  },
  {
    "text": "The Dark Gods may offer many temptations, but they could never provide an aurora borealis localised entirely within this kitchen.",
    "citation": "September 2024 Update",
    "topics": [
      "TEMPTATION"
    ]
  },
  {
    "text": "In the darkest of moments, the lustrous gleam of Aris hair shines brightest.",
    "citation": "September 2024 Update",
    "topics": [
      "FAITH",
      "HOPE"
    ]
  },
  {
    "text": "A true servant of the Emperor walks alone. A true servant of the Emperor seeks direction from one who points. A true servant of the Emperor consults with a wise sage. A true servant of the Emperor gazes upon the fallen.",
    "citation": "September 2024 Update",
    "topics": [
      "QUADRANTS"
    ]
  },
  {
    "text": "Nothing inspires revenge quite like attacking Chris in a boardgame.",
    "citation": "September 2024 Update",
    "topics": [
      "SPITE"
    ]
  },
  {
    "text": "Do not dabble in the heresy of Cubes, for you may spit in the very face of the hobby.",
    "citation": "September 2024 Update",
    "topics": [
      "HERESY"
    ]
  },
  {
    "text": "Only the awkward question; only the foolish ask Jack whether he is a Cylon.",
    "citation": "September 2024 Update",
    "topics": [
      "POOR CHOICES"
    ]
  },
  {
    "text": "The guilt of blacklining weighs heavy on the soul.",
    "citation": "September 2024 Update",
    "topics": [
      "IT WAS SEVEN LAYERS THANK YOU VERY MUCH"
    ]
  },
  {
    "text": "Do not be lured by the sirens call of Dans guitar playing, that way lays the temptation of Slaanesh.",
    "citation": "September 2024 Update",
    "topics": [
      "TEMPTATION",
      "BEAUTY"
    ]
  },
  {
    "text": "No army is big enough to conquer the galaxy. But spite alone can overturn the universe.",
    "citation": "September 2024 Update",
    "topics": [
      "SPITE"
    ]
  },
  {
    "text": "A fine mind is a blessing of the Emperor - it should not be cluttered with analysis paralysis.",
    "citation": "September 2024 Update",
    "topics": [
      "COME ON, ARI"
    ]
  },
  {
    "text": "Through the laser of spite do we earn our salvation.",
    "citation": "September 2024 Update",
    "topics": [
      "SPITE"
    ]
  },
  {
    "text": "A mind without purpose will onerously explain the joke.",
    "citation": "September 2024 Update",
    "topics": [
      "HILARITY"
    ]
  },
  {
    "text": "Your freedom must be bought in the currency of toil, tears and blood; a price all hobbyists can pay.",
    "citation": "September 2024 Update",
    "topics": [
      "PAIN"
    ]
  },
  {
    "text": "Suffer not the unclian to live.",
    "citation": "September 2024 Update",
    "topics": [
      "TOLERANCE",
      "HITLIAN"
    ]
  },
  {
    "text": "I am AlpharIan.",
    "citation": "September 2024 Update",
    "topics": [
      "IDENTITY"
    ]
  },
  {
    "text": "A suspicious mind is a healthy mind.",
    "citation": "September 2024 Update",
    "topics": [
      "LIAR'S DICE MAXIM"
    ]
  },
  {
    "text": "Better to die for the lulz than live for yourself.",
    "citation": "September 2024 Update",
    "topics": [
      "SACRIFICE"
    ]
  },
  {
    "text": "Suffer not the Cryomancer to live.",
    "citation": "September 2024 Update",
    "topics": [
      "TOLERANCE"
    ]
  },
  {
    "text": "Even though you once called him friend, the Traitor has forsaken you. Show no mercy even if he begs it, for his soul is tainted and given the chance he will go to Japan every time an SFTC is held.",
    "citation": "September 2024 Update",
    "topics": [
      "BETRAYAL",
      "POOR HOLIDAY CHOICES"
    ]
  },
  {
  "text": "What is best in life? To roll dice, see your miniatures claim victory on the battlefield, and hear the lamentations of your opponent.",
  "citation": "October 2024 Update",
  "topics": ["ACHIEVEMENT, GLORY"]
},
{
  "text": "You are the Emperor's Chosen. See His almighty fury in the blades of the chainsord. Hear His great anger in the roar of the gernade. Feel His undying strength in the protection of your mother, the nurse. Model yourself in His perfect image with your Juggalo makeup.",
  "citation": "October 2024 Update",
  "topics": ["INNOVATION, SCHEMATICS, ANGORN S SON"]
},
{
  "text": "It is the most pure of folly to play Paper in a Rock Meta.",
  "citation": "October 2024 Update",
  "topics": ["FUTILITY, IGNORANCE, RPS TIPS, SQUASH MEMES"]
},
{
  "text": "Only the most willfully ignorant would play Scissors in a Rock Meta.",
  "citation": "October 2024 Update",
  "topics": ["FUTILITY, IGNORANCE, RPS TIPS, SQUASH MEMES"]
},
{
  "text": "A faithful servant of the Emperor knows that it is madness to play Rock in a Rock Meta.",
  "citation": "October 2024 Update",
  "topics": ["SERVITUDE, MADNESS, RPS TIPS, SQUASH MEMES"]
},
{
  "text": "And verily, he did roll a mighty six - while I, dashed upon the will of the fates, merely rolled a one.",
  "citation": "October 2024 Update",
  "topics": ["INSIDE VOICE"]
},
{
  "text": "Think not of the fragility of faith and purity, but of the glory of the Roman Empire at least once a day.",
  "citation": "October 2024 Update",
  "topics": ["FAITH, PURITY, HAVE YOU THOUGHT OF THE ROMAN EMPIRE TODAY?"]
},
{
  "text": "He who lives for nothing is nothing. He who supplies discounted Dulux spray is a hero.",
  "citation": "October 2024 Update",
  "topics": ["HEROISM"]
},
{
  "text": "A single thought of refusing a batchall can blight a lifetime of faithful duty.",
  "citation": "October 2024 Update",
  "topics": ["DUTY"]
},
{
  "text": "The galaxy is the Emperor s, and anyone or anything who refuses to drill out barrels in His name is an enemy who must be destroyed.",
  "citation": "October 2024 Update",
  "topics": ["COMPLIANCE"]
},
{
  "text": "Even a man who has nothing can still offer his bare toes for Aaron to suckle on.",
  "citation": "October 2024 Update",
  "topics": ["DEDICATION",  "LUST" ]
},
{
  "text": "A wise man learns from the death of others. A wiser man learns to check behind himself before making jokes about different racial groups.",
  "citation": "October 2024 Update",
  "topics": ["IMMENSE REGRET",  "PERPETUAL CRINGE" ]
},
{
  "text": "Let faith protect your mind, and metal claws your flesh.",
  "citation": "October 2024 Update",
  "topics": ["WOLVARINE"]
},
{
  "text": "Only the dead know the end of Luke running a joke into the ground.",
  "citation": "October 2024 Update",
  "topics": ["RELENTLESSNESS"]
},
{
  "text": "It is better to die for the CHOMP than live for yourself.",
  "citation": "October 2024 Update",
  "topics": ["CHOMP"]
},
{
  "text": "Appreciation of art is a myth we do not need to understand in order to hate.",
  "citation": "October 2024 Update",
  "topics": ["HATRED", "BELIEF" ]
},
{
  "text": "In the Emperor s name, let me do a two-handed return!",
  "citation": "October 2024 Update",
  "topics": ["IMPERIAL POWER, SQUASH MEMES"]
},
{
  "text": "Facts are chains that bind perception and fetter truth. For a man can remake the world through spin if he has a dream and no facts to cloud his mind.",
  "citation": "October 2024 Update",
  "topics": ["SPINZONE"]
},
{
  "text": "Sometimes the good must perish so that the rest survive. The lot of courage is to be sacrificed upon the altar of descending on a dark path towards working in IT.",
  "citation": "October 2024 Update",
  "topics": ["AARON S CAREER JOURNEY"]
},
{
  "text": "There is no such thing as innocence, only various degrees of spinzone.",
  "citation": "October 2024 Update",
  "topics": ["DIZZINESS"]
}
]



def get_quote():
    quote = random.choice(quotes)
    return quote