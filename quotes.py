import random

quotes = [{
  "text": "There is no such thing as innocence - only varying degrees of guilt.",
  "citation": "Codex: Black Templars(4th edition)",
  "topics": ["innocence", "guilt"]
},
{
  "text": "Reason begets doubt; doubt begets heresy.",
  "citation": "Warhammer 40000(5th edition)",
  "topics": ["reason", "doubt"]
},
{
  "text": "Only the awkward question; only the foolish ask twice.",
  "citation": "Codex: Space Marines(4th edition)",
  "topics": ["awkward", "question"]
},
{
  "text": "Success is measured in blood; yours or your enemy's.",
  "citation": "Codex: Space Marines(4th edition)",
  "topics": ["success"]
},
{
  "text": "The reward for treachery is retribution.",
  "citation": "Warhammer 40000(5th edition)",
  "topics": ["treachery"]
},
{
  "text": "Hope is the beginning of unhappiness.",
  "citation": "Warhammer 40000(3rd edition)",
  "topics": ["hope"]
},
{
  "text": "Even a man who has nothing can still offer his life.",
  "citation": "Warhammer 40000(5th edition)",
  "topics": ["sacrifice"]
},
{
  "text": "Inspiration grows from the barrel of a gun.",
  "citation": "Warhammer 400000: Compendium",
  "topics": ["inspiration", "gun"]
},
{
  "text": "Walk softly and carry a big gun.",
  "citation": "Codex: Space Marines(4th edition)",
  "topics": ["caution", "gun"]
},
{
  "text": "A mind without purpose will wander in dark places.",
  "citation": "Warhammer 40000(3rd edition)",
  "topics": ["purposelessness"]
},
{
  "text": "A moment of laxity spawns a lifetime of heresy.",
  "citation": "Codex: Dark Angels(3rd edition)",
  "topics": ["laxity"]
},
{
  "text": "A small mind is a tidy mind.",
  "citation": "Warhammer 40000(3rd edition)",
  "topics": ["small mind"]
},
{
  "text": "A suspicious mind is a healthy mind.",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["suspicion"]
},
{
  "text": "An open mind is like a fortress with its gates unbarred and unguarded.",
  "citation": "Warhammer 40000(3rd edition)",
  "topics": ["open mind"]
},
{
  "text": "Call no man happy until he is dead.",
  "citation": "Codex: Imperial Guard(3rd edition)",
  "topics": ["happiness"]
},
{
  "text": "Death is the servant of the righteous.",
  "citation": "Codex: Chaos Space Marines(4th edition)",
  "topics": ["death"]
},
{
  "text": "Doubt is a sign of weakness.",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["doubt"]
},
{
  "text": "Excuses are the refuge of the weak.",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["excuses"]
},
{
  "text": "Foolish are those who fear nothing, yet claim to know everything.",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["knowledge"]
},
{
  "text": "For a warrior the only crime is cowardice.",
  "citation": "Warhammer 40000: Rogue Trader",
  "topics": ["cowardice"]
},
{
  "text": "Happiness is a delusion of the weak.",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["happiness"]
},
{
  "text": "Hate enriches.",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["hatred"]
},
{
  "text": "Heresy grows from idleness.",
  "citation": "Codex: Black Templars(4th edition)",
  "topics": ["idleness"]
},
{
  "text": "Success is commemorated. Failure merely remembered.",
  "citation": "Warhammer 40000(3rd edition)",
  "topics": ["success", "failure"]
},
{
  "text": "The rewards of tolerance are treachery and betrayal.",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["tolerance"]
},
{
  "text": "The truly wise are always afraid.",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["wisdom"]
},
{
  "text": "Through the destruction of our enemies we earn our salvation.",
  "citation": "Warhammer 40000(3rd edition)",
  "topics": ["victory"]
},
{
  "text": "Prayer cleanses the soul, but pain cleanses the body.",
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
  "text": "Sorrow awaits the foolhardy.",
  "citation": "Codex: Armageddon(3rd edition)",
  "topics": ["fool"]
},
{
  "text": "The burden of failure is the most terrible punishment of all.",
  "citation": "Warhammer 40000 4th edition",
  "topics": ["failure"]
},
{
  "text": "The common man is like a worm in the gut of a corpse, trapped inside a prison of cold flesh, helpless and uncaring, unaware even of the inevitability of its own doom.",
  "citation": "Codex: Imperialis",
  "topics": ["doom"]
},
{
  "text": "The difference between heresy and treachery is ignorance.",
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
  "topics": ["hate"]
},
{
  "text": "To Know Ian is to Know Hate.",
  "citation": "The Traitor's Hand(novel)",
  "topics": ["hate"]
},
{
  "text": "To Know Ian is to Know Hate.",
  "citation": "The Traitor's Hand(novel)",
  "topics": ["hate"]
},
{
  "text": "To Know Ian is to Know Hate.",
  "citation": "The Traitor's Hand(novel)",
  "topics": ["hate"]
},
{
  "text": "To Know Ian is to Know Hate.",
  "citation": "The Traitor's Hand(novel)",
  "topics": ["hate"]
},
{
  "text": "To Know Ian is to Know Hate.",
  "citation": "The Traitor's Hand(novel)",
  "topics": ["hate"]
},
{
  "text": "The universe is a big place and, whatever happens, you will not be missed...",
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
  "text": "There are no answers. Only death.",
  "citation": "Warhammer 40000: Rogue Trader",
  "topics": ["answers", "death"]
},
{
  "text": "They who feast today do so in ignorance of their mortality. Tomorrow they must die or change.",
  "citation": "Warhammer 40000(5th edition)",
  "topics": ["death"]
},
{
  "text": "Timidity begets indecision; indecision begets treachery.",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["timidity", "indecision"]
},
{
  "text": "To compromise is to err.",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["compromise"]
},
{
  "text": "To err is to invite retribution.",
  "citation": "Warhammer 40000: Rogue Trader",
  "topics": ["error"]
},
{
  "text": "To withdraw in disgust is not apathy.",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["disgust", "apathy"]
},
{
  "text": "Truth begets hatred.",
  "citation": "Codex: Black Templars(4th edition)",
  "topics": ["truth", "hatred"]
},
{
  "text": "Trying to understand weakens the will to act.",
  "citation": "Codex: Black Templars(4th edition)",
  "topics": ["understanding"]
},
{
  "text": "Victory needs no explanation, defeat allows none.",
  "citation": "Warhammer 40000(3rd edition)",
  "topics": ["victory", "defeat"]
},
{
  "text": "Vigilance is the brother of truth.",
  "citation": "Codex: Necrons(3rd edition)",
  "topics": ["vigilance", "truth"]
},
{
  "text": "Vigilance is your shield.",
  "citation": "Codex: Necrons(3rd edition)",
  "topics": ["vigilance"]
},
{
  "text": "You are not required to think, only to act.",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["thought"]
},
{
  "text": "Zeal is its own excuse.",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["zeal"]
},
{
  "text": "A broad mind lacks focus.",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["open mind"]
},
{
  "text": "A coward always seeks compromise.",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["cowardice", "compromise"]
},
{
  "text": "A logical argument must be dismissed with absolute conviction!",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["logic"]
},
{
  "text": "A questioning servant is more dangerous than an ignorant heretic.",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["question"]
},
{
  "text": "Accept your lot!",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["fortune"]
},
{
  "text": "An empty mind is a loyal mind.",
  "citation": "Codex: Craftworld Eldar(3rd edition)",
  "topics": ["intelligence", "loyalty"]
},
{
  "text": "Analysis is the bane of conviction.",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["analysis"]
},
{
  "text": "Appeasement is a curse.",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["appeasement"]
},
{
  "text": "Be strong in your ignorance.",
  "citation": "Codex: Imperial Guard(3rd edition)",
  "topics": ["ignorance"]
},
{
  "text": "Blessed is the mind too small for doubt.",
  "citation": "Warhammer 40000(3rd edition)",
  "topics": ["doubt"]
},
{
  "text": "Burn the Heretic. Kill the Mutant. Purge the Unclean.",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["heresy", "mutation", "unclean"]
},
{
  "text": "Compromise is akin to treachery.",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["compromise"]
},
{
  "text": "Contemplation is the womb of treachery.",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["Contemplation"]
},
{
  "text": "Death brings its own reward.",
  "citation": "Warhammer 40000: Rogue Trader",
  "topics": ["death"]
},
{
  "text": "Death is the only answer.",
  "citation": "Warhammer 40000: Rogue Trader",
  "topics": ["death"]
},
{
  "text": "Every man is a spark in the darkness. By the time he is noticed he is gone forever. A retinal after-image that fades and is obscured by newer, brighter lights.",
  "citation": "Warhammer 40000: Rogue Trader",
  "topics": ["life"]
},
{
  "text": "Facts are chains that bind perception and fetter truth. For a man can remake the world if he has a dream and no facts to cloud his mind.",
  "citation": "Warhammer 40000(3rd edition)",
  "topics": ["facts"]
},
{
  "text": "For those who seek perfection there can be no rest this side of the grave.",
  "citation": "Warhammer 40000(3rd edition)",
  "topics": ["perfection"]
},
{
  "text": "Forgiveness is a sign of weakness.",
  "citation": "Codex: Space Marines(4th edition)",
  "topics": ["forgiveness"]
},
{
  "text": "In an hour of darkness a blind man is the best guide. In an age of insanity look to the madman to show the way.",
  "citation": "Warhammer 40000(3rd edition)",
  "topics": ["insanity"]
},
{
  "text": "Intellect is a mask for traitors.",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["intellect"]
},
{
  "text": "Intolerance is a blessing.",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["intolerance", "tolerance"]
},
{
  "text": "Knowledge is power, hide it well.",
  "citation": "Warhammer 40000(3rd edition)",
  "topics": ["knowledge"]
},
{
  "text": "Knowledge is to be feared!",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["knowledge"]
},
{
  "text": "Leniency is a sign of weakness!",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["Leniency"]
},
{
  "text": "Life is a prison, death a release.",
  "citation": "Codex: Black Templars(4th edition)",
  "topics": ["life", "death"]
},
{
  "text": "Mercy is a sign of weakness.",
  "citation": "Codex: Space Marines(4th edition)",
  "topics": ["mercy"]
},
{
  "text": "Negotiation is surrender.",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["Negotiation"]
},
{
  "text": "Never forget, never forgive.",
  "citation": "Codex: Dark Angels(3rd edition)",
  "topics": ["forgiveness"]
},
{
  "text": "Not even the dead know the end of war.",
  "citation": "Codex: Craftworld Eldar(3rd edition)",
  "topics": ["war"]
},
{
  "text": "Only in death does duty end.",
  "citation": "Warhammer 40000(3rd edition)",
  "topics": ["duty"]
},
{
  "text": "Only the insane have strength enough to prosper.",
  "citation": "Codex: Space Marines(4th edition)",
  "topics": ["insanity"]
},
{
  "text": "Peace is Hell.",
  "citation": "Warhammer 40000: Rogue Trader",
  "topics": ["peace"]
},
{
  "text": "Perseverance and silence are the highest virtues.",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["perseverance"]
},
{
  "text": "Only the weak question.",
  "citation": "Imperial Armour IV",
  "topics": ["question"]
},
{
  "text": "All souls cry out for salvation.",
  "citation": "Codex: Dark Angels(3rd Edition)",
  "topics": ["salvation"]
},
{
  "text": "All mortal life is folly that does not feed the spirit.",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["faith"]
},
{
  "text": "As the mind to the body so the soul to the spirit, as death to the mortal man so failure to the immortal, such is the price of all ambition.",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["ambition"]
},
{
  "text": "Blessed are the gun makers.",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["gun"]
},
{
  "text": "Blind faith is a just cause.",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["faith"]
},
{
  "text": "Curse now the death in vain.",
  "citation": "Codex: Space Marines(4th edition)",
  "topics": ["death"]
},
{
  "text": "Damnation is eternal.",
  "citation": "Codex: Dark Angels(3rd Edition)",
  "topics": ["damnation"]
},
{
  "text": "Dark dreams lie upon the heart.",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["dreams"]
},
{
  "text": "Heresy must be met with hatred.",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["heresy"]
},
{
  "text": "Know thine enemy.",
  "citation": "Codex: Dark Eldar (3rd Edition)",
  "topics": ["enemy"]
},
{
  "text": "Sins hidden in the heart turn all into decay.",
  "citation": "Warhammer 40000(4th edition)",
  "topics": ["sin"]
},
{
  "text": "Claims of innocence mean nothing; they serve only to prove a foolish lack of caution.",
  "citation": "Codex Imperialis",
  "topics": ["innocence"]
},
{
  "text": "The tools of salvation are faith and bullets.",
  "citation": "Warhammer 40000(6th edition)",
  "topics": ["salvtion", "faith"]
},
{
  "text": "A treacherous thought is as dangerous as a hundred bullets.",
  "citation": "Warhammer 40000(6th edition)",
  "topics": ["treachery"]
},
{
  "text": "Doubt is the fatal flaw in any armour.",
  "citation": "Warhammer 40000(6th edition)",
  "topics": ["doubt"]
},
{
  "text": "To punish the traitor is reward in itself.",
  "citation": "Warhammer 40000(6th edition)",
  "topics": ["betrayal"]
},
{
  "text": "Enlightenment is a myth; we do not need to understand in order to hate.",
  "citation": "Warhammer 40000(6th edition)",
  "topics": ["enlightenment"]
},
{
  "text": "Death and duty are all we must give.",
  "citation": "Warhammer 40000(6th edition)",
  "topics": ["death", "duty"]
},
{
  "text": "Betrayal's tithe is the hangman's noose.",
  "citation": "Warhammer 40000(6th edition)",
  "topics": ["betrayal"]
},
{
  "text": "True happiness stems only from duty.",
  "citation": "Warhammer 40000(6th edition)",
  "topics": ["happiness", "duty"]
},
{
  "text": "It is better for a man to be afraid than happy.",
  "citation": "Warhammer 40000(6th edition)",
  "topics": ["fear", "happiness"]
},
{
  "text": "To search for answers is to beat a path to damnation.",
  "citation": "Warhammer 40000(6th edition)",
  "topics": ["knowledge"]
},
{
  "text": "To err is human; To err again is treachery.",
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