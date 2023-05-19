import random

quotes = [{
  "text": "There is no such thing as innocence - only varying degrees of guilt.",
  "citation": "Codex: Black Templars(4th edition)",
  "topics": ["innocence", "guilt"]
},
{
  "text": "Prayer cleanses the soul, pain cleanses the body, 18 hours of TI cleanses the Sanity.",
  "citation": "Warhammer 40000(3rd edition)",
  "topics": ["prayer", "pain"]
},
{
  "text": "Innocence proves nothing.",
  "citation": "Codex: Black Templars(4th edition)",
  "topics": ["innocence"]
},
{
  "text": "There is nothing to fear but failure.",
  "citation": "Codex: Black Templars(4th edition)",
  "topics": ["failure"]
},
{
  "text": "To question is to doubt.",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["question"]
},
{
  "text": "Reason is the cloak of traitors.",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["reason"]
},
{
  "text": "Ruthlessness is the kindness of the wise.",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["ruthlessness"]
},
{
  "text": "Sorrow awaits the foolhardy. John awaits the minor offenders",
  "citation": "Codex: Armageddon(3rd edition)",
  "topics": ["foolishness"]
},
{
  "text": "The common man is like a worm in the gut of a corpse, trapped inside a prison of cold flesh, helpless and uncaring, unaware even of the inevitability of its own doom.",
  "citation": "Codex: Imperialis",
  "topics": ["doom"]
},
{
  "text": "The difference between heresy and treachery is ignorance. For Aaron, the difference between fun and treachery is boardgames",
  "citation": "Warhammer 40000(3rd edition)",
  "topics": ["treachery"]
},
{
  "text": "The dissident invites only retribution.",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["dissidence"]
},
{
  "text": "The justice of your action is measured by the strength of your conviction.",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["justice", "conviction"]
},
{
  "text": "The keenest blade is righteous hatred.",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["hatred"]
},
{
  "text": "The most deviant mind is often concealed in an unblemished body.",
  "citation": "Warhammer 40000(5th edition)",
  "topics": ["deviance"]
},
{
  "text": "The mutant bears his heresy on the outside, the traitor hides it in his soul.",
  "citation": "Warhammer 40000(3rd edition)",
  "topics": ["treachery"]
},
{
  "text": "The only reaction to treachery is vengeance.",
  "citation": "Warhammer 40000(3rd edition)",
  "topics": ["treachery"]
},
{
  "text": "The road to purity is drenched in the blood of the martyred.",
  "citation": "Codex: Imperial Guard(3rd edition)",
  "topics": ["purity"]
},
{
  "text": "The seed of heresy rests in the minds of reasonable men.",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["reason"]
},
{
  "text": "The traitorʹs hand lies closer than you think.",
  "citation": "The Traitor's Hand(novel)",
  "topics": ["treachery"]
},
{
  "text": "To Know Ian is to Know Hate.",
  "citation": "The Traitor's Hand(novel)",
  "topics": ["Ian"]
},
{
  "text": "By the manner of their art we shall hate them.",
  "citation": "The Traitor's Hand(novel)",
  "topics": ["Ian Quotes"]
},
{
  "text": "Surelyness is next to Godliness",
  "citation": "The Traitor's Hand(novel)",
  "topics": ["Ian Quotes"]
},
{
  "text": "Russ rules, Magnus drools.",
  "citation": "The Traitor's Hand(novel)",
  "topics": ["Ian Quotes"]
},
{
  "text": "Break a deal spin the wheel",
  "citation": "The Traitor's Hand(novel)",
  "topics": ["Ian Quotes"]
},
{
  "text": "To Know Ian is to Know Hate.",
  "citation": "The Traitor's Hand(novel)",
  "topics": ["Ian"]
},
{
  "text": "Pedantry ALWAYS wins.",
  "citation": "The Traitor's Hand(novel)",
  "topics": ["Luke Quotes"]
},
{
  "text": "Never listen to Aaron while playing a board game.",
  "citation": "The Traitor's Hand(novel)",
  "topics": ["Universal Truth"]
},
{
  "text": "Who needs super, I'm building a retirement fund with Jetskis",
  "citation": "The Traitor's Hand(novel)",
  "topics": ["Jack will never retire"]
},
{
  "text": "WE ARE GOING TO THE MOON, WHAT WILL YOU BRING!?",
  "citation": "The Traitor's Hand(novel)",
  "topics": ["Group Shame"]
},
{
  "text": "Only the dead know the end of Pendragons Spite lazer.",
  "citation": "The Traitor's Hand(novel)",
  "topics": ["spite"]
},
{
  "text": "The universe is a big place and, whatever happens, you will not be missed... Except for Tom Nurse, Hes wholesome",
  "citation": "Warhammer 40000(5th edition)",
  "topics": ["memories"]
},
{
  "text": "The wage of negligence is utter destruction.",
  "citation": "Codex: Armageddon(3rd edition)",
  "topics": ["negligence"]
},
{
  "text": "The wise man learns from the deaths of others.",
  "citation": "Warhammer 40000(3rd edition)",
  "topics": ["wisdom"]
},
{
  "text": "There are no answers. Only death and Ian.",
  "citation": "Warhammer 40000: Rogue Trader",
  "topics": ["answers", "death"]
},
{
  "text": "EXTREMELY LOUD EXHALE",
  "citation": "Warhammer 40000(5th edition)",
  "topics": ["Chris informing you of a poor choice"]
},
{
  "text": "I am not *suspicious look* ........ a Cylon?",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["Ari Definately Being a Cylon"]
},
{
  "text": "To err is to invite Luke to correct you.",
  "citation": "Warhammer 40000: Rogue Trader",
  "topics": ["Universal Truth"]
},
{
  "text": "To withdraw in disgust is not apathy, its a natural reaction to Art.",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["Ian Quotes"]
},
{
  "text": "I Declare myself Space Bureaucrat, prepare for new taxes",
  "citation": "Codex: Black Templars(4th edition)",
  "topics": ["Pendragon playing TI"]
},
{
  "text": "Trying to understand weakens the will to act.",
  "citation": "Codex: Black Templars(4th edition)",
  "topics": ["How to annoy Chris during a boardgame"]
},
{
  "text": "Let Me inform you, in detail, about why that was a bad move.",
  "citation": "Codex: Black Templars(4th edition)",
  "topics": ["Pendragon Quotes"]
},
{
  "text": "Vigilance is the brother of truth.",
  "citation": "Codex: Necrons(3rd edition)",
  "topics": ["vigilance", "truth"]
},
{
  "text": "Vigilance is my shield, Simpsons Quotes are my sword.",
  "citation": "Codex: Necrons(3rd edition)",
  "topics": ["Tims mantra"]
},
{
  "text": "You are not required to think, only to act.",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["thought"]
},
{
  "text": "Surliness is next to Godliness.",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["zeal"]
},
{
  "text": "A broad mind lacks focus.",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["open mind"]
},
{
  "text": "A coward always seeks compromise. A fool trusts Aaron",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["boardgames"]
},
{
  "text": "A logical argument must be dismissed with absolute conviction!",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["Luke Logic"]
},
{
  "text": "A questioning servant is more dangerous than an ignorant heretic.",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["question"]
},
{
  "text": "Accept your lot! Don't accept Aarons advice during a boardgame!",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["Wisdom"]
},
{
  "text": "An empty mind is a loyal mind.",
  "citation": "Codex: Craftworld Eldar(3rd edition)",
  "topics": ["intelligence", "loyalty"]
},
{
  "text": "Knowledge is power, hide it well.",
  "citation": "Warhammer 40000(3rd edition)",
  "topics": ["knowledge"]
},
{
  "text": "Not even the dead know the end of war.",
  "citation": "Codex: Craftworld Eldar(3rd edition)",
  "topics": ["war"]
},
{
  "text": "Only in death does duty end. Only in group shame does we're going to the moon end",
  "citation": "Warhammer 40000(3rd edition)",
  "topics": ["duty"]
},
{
  "text": "Only the insane have strength enough to prosper or win against Aaron in a game of drinking chess",
  "citation": "Codex: Space Marines(4th edition)",
  "topics": ["insanity"]
},
{
  "text": "Peace is Hell.",
  "citation": "Warhammer 40000: Rogue Trader",
  "topics": ["peace"]
},
{
  "text": "I hate my life, why would anyone enjoy this game.",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["what sane people say after playing Warhammer Fantasy"]
},
{
  "text": "Only the weak question. Real strength comes from Pedantry",
  "citation": "Imperial Armour IV",
  "topics": ["question"]
},
{
  "text": "True happiness stems only from duty or winning at Viticulture.",
  "citation": "Warhammer 40000(6th edition)",
  "topics": ["happiness", "duty"]
},
{
  "text": "It is better for a man to be afraid than happy.",
  "citation": "Warhammer 40000(6th edition)",
  "topics": ["fear", "happiness"]
},
{
  "text": "Viticulture is a good game.",
  "citation": "Warhammer 40000(6th edition)",
  "topics": ["things Jack said a million times"]
},
{
  "text": "To search for answers is to beat a path to damnation.",
  "citation": "Warhammer 40000(6th edition)",
  "topics": ["knowledge"]
},
{
  "text": "To err is human; To err again is treachery",
  "citation": "Warhammer 40000(6th edition)",
  "topics": ["err"]
},
{
  "text": "A closed mind is defence against sedition.",
  "citation": "Warhammer 40000(6th edition)",
  "topics": ["closed mind", "sedition"]
},
{
  "text": "Knowledge is power; Power corrupts.",
  "citation": "Warhammer 40000(6th edition)",
  "topics": ["knowledge"]
},
{
  "text": "Better crippled in body than corrupt in mind.",
  "citation": "Warhammer 40000(6th edition)",
  "topics": ["corruption"]
},
{
  "text": "To relinquish contempt is capitulation.",
  "citation": "Warhammer 40000(6th edition)",
  "topics": ["contempt"]
},
{
  "text": "Do not let fear conquer hate!",
  "citation": "Warhammer 40000(6th edition)",
  "topics": ["fear", "hate"]
}
]


def get_quote():
    quote = random.choice(quotes)
    return quote