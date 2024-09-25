import random

quotes = [
  {
    "text": "There is no such thing as innocence - only varying degrees of guilt.",
    "citation": "Codex: Black Templars(4th edition)",
    "topics": [
      "INNOCENCE",
      "GUILT"
    ]
  },
  {
    "text": "Prayer cleanses the soul, pain cleanses the body, 18 hours of TI cleanses the sanity.",
    "citation": "Warhammer 40000(3rd edition)",
    "topics": [
      "PRAYER",
      "PAIN"
    ]
  },
  {
    "text": "Innocence proves nothing.",
    "citation": "Codex: Black Templars(4th edition)",
    "topics": [
      "INNOCENCE"
    ]
  },
  {
    "text": "There is nothing to fear but failure.",
    "citation": "Codex: Black Templars(4th edition)",
    "topics": [
      "FAILURE"
    ]
  },
  {
    "text": "To question is to doubt.",
    "citation": "Warhammer 40000(4th edition)",
    "topics": [
      "QUESTION"
    ]
  },
  {
    "text": "Reason is the cloak of traitors.",
    "citation": "Warhammer 40000(4th edition)",
    "topics": [
      "REASON"
    ]
  },
  {
    "text": "Ruthlessness is the kindness of the wise.",
    "citation": "Warhammer 40000(4th edition)",
    "topics": [
      "RUTHLESSNESS"
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
    "text": "The common man is like a worm in the gut of a corpse, trapped inside a prison of cold flesh, helpless and uncaring, unaware even of the inevitability of its own doom.",
    "citation": "Codex: Imperialis",
    "topics": [
      "DOOM"
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
    "text": "The dissident invites only retribution.",
    "citation": "Warhammer 40000(4th edition)",
    "topics": [
      "DISSIDENCE"
    ]
  },
  {
    "text": "The justice of your action is measured by the strength of your conviction.",
    "citation": "Warhammer 40000(4th edition)",
    "topics": [
      "JUSTICE",
      "CONVICTION"
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
    "text": "The most deviant mind is often concealed in an unblemished body.",
    "citation": "Warhammer 40000(5th edition)",
    "topics": [
      "DEVIANCE"
    ]
  },
  {
    "text": "The mutant bears his heresy on the outside, the traitor hides it in his soul.",
    "citation": "Warhammer 40000(3rd edition)",
    "topics": [
      "TREACHERY"
    ]
  },
  {
    "text": "The only reaction to treachery is vengeance.",
    "citation": "Warhammer 40000(3rd edition)",
    "topics": [
      "TREACHERY"
    ]
  },
  {
    "text": "The road to purity is drenched in the blood of the martyred.",
    "citation": "Codex: Imperial Guard(3rd edition)",
    "topics": [
      "PURITY"
    ]
  },
  {
    "text": "The seed of heresy rests in the minds of reasonable men.",
    "citation": "Warhammer 40000(4th edition)",
    "topics": [
      "REASON"
    ]
  },
  {
    "text": "The traitors hand lies closer than you think.",
    "citation": "The Traitor's Hand(novel)",
    "topics": [
      "TREACHERY"
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
    "text": "Surliness is next to Godliness",
    "citation": "The Traitor's Hand(novel)",
    "topics": [
      "IAN QUOTES"
    ]
  },
  {
    "text": "Magnus did nothing wrong.",
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
    "text": "WE ARE GOING TO THE MOON, WHAT WILL YOU BRING!?",
    "citation": "The Traitor's Hand(novel)",
    "topics": [
      "GROUP SHAME"
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
    "text": "The wage of negligence is utter destruction.",
    "citation": "Codex: Armageddon(3rd edition)",
    "topics": [
      "NEGLIGENCE"
    ]
  },
  {
    "text": "The wise man learns from the deaths of others.",
    "citation": "Warhammer 40000(3rd edition)",
    "topics": [
      "WISDOM"
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
    "text": "I am not <looks around suspiciously> ... a Cylon?",
    "citation": "Warhammer 40000(4th edition)",
    "topics": [
      "ARI DEFINITELY BEING A CYLON"
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
    "text": "Trying to understand weakens the will to act.",
    "citation": "Codex: Black Templars(4th edition)",
    "topics": [
      "HOW TO ANNOY CHRIS DURING A BOARDGAME"
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
    "text": "Vigilance is the brother of truth.",
    "citation": "Codex: Necrons(3rd edition)",
    "topics": [
      "VIGILANCE",
      "TRUTH"
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
    "text": "You are not required to think, only to act.",
    "citation": "Warhammer 40000(4th edition)",
    "topics": [
      "THOUGHT"
    ]
  },
  {
    "text": "A broad mind lacks focus.",
    "citation": "Warhammer 40000(4th edition)",
    "topics": [
      "OPEN MIND"
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
    "text": "A questioning servant is more dangerous than an ignorant heretic.",
    "citation": "Warhammer 40000(4th edition)",
    "topics": [
      "QUESTION"
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
    "text": "An empty mind is a loyal mind.",
    "citation": "Codex: Craftworld Eldar(3rd edition)",
    "topics": [
      "INTELLIGENCE",
      "LOYALTY"
    ]
  },
  {
    "text": "Knowledge is power, hide it well. Perhaps too well",
    "citation": "Warhammer 40000(3rd edition)",
    "topics": [
      "KNOWLEDGE"
    ]
  },
  {
    "text": "Not even the dead know the end of war.",
    "citation": "Codex: Craftworld Eldar(3rd edition)",
    "topics": [
      "WAR"
    ]
  },
  {
    "text": "Only in death does duty end. Only in group shame does we're going to the moon end.",
    "citation": "Warhammer 40000(3rd edition)",
    "topics": [
      "DUTY"
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
    "text": "Peace is Hell.",
    "citation": "Warhammer 40000: Rogue Trader",
    "topics": [
      "PEACE"
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
    "text": "True happiness stems only from duty or winning at Viticulture.",
    "citation": "Warhammer 40000(6th edition)",
    "topics": [
      "HAPPINESS",
      "DUTY"
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
    "text": "Viticulture is a good game.",
    "citation": "Warhammer 40000(6th edition)",
    "topics": [
      "THINGS JACK SAID A MILLION TIMES"
    ]
  },
  {
    "text": "To search for answers is to beat a path to damnation.",
    "citation": "Warhammer 40000(6th edition)",
    "topics": [
      "KNOWLEDGE"
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
    "text": "Knowledge is power; Power corrupts.",
    "citation": "Warhammer 40000(6th edition)",
    "topics": [
      "KNOWLEDGE"
    ]
  },
  {
    "text": "Better crippled in body than corrupt in mind.",
    "citation": "Warhammer 40000(6th edition)",
    "topics": [
      "CORRUPTION"
    ]
  },
  {
    "text": "To relinquish contempt is capitulation.",
    "citation": "Warhammer 40000(6th edition)",
    "topics": [
      "CONTEMPT"
    ]
  },
  {
    "text": "Do not let fear conquer hate!",
    "citation": "Warhammer 40000(6th edition)",
    "topics": [
      "FEAR",
      "HATE"
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
  }
]



def get_quote():
    quote = random.choice(quotes)
    return quote